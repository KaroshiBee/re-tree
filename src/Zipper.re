module I = Identity;
module ID = I.FocusId;
module PID = I.ParentId;
module CID = I.ChildId;
module P = Path.T;
module type GRAPH = GraphF.GRAPH;

module type ZIPPER = {
  type focus;
  type graph;
  type t;
  type m('a);
  let createAt: (graph, focus) => m(t);
  let create: graph => m(t);
  let toString: t => string;

  //  monad / functor interface
  let flatMap: (m('a), 'a => m('b)) => m('b);
  let map: (m('a), 'a => 'b) => m('b);
  let mapWithDefault: (m('a), 'b, 'a => 'b) => 'b;
  let getExn: m('a) => 'a;
  let getOpt: m('a) => option('a);
  let getResult: m('a) => Result.t('a, string);

  // zipper
  let focus: t => focus;
  let up: t => m(t);
  let down: t => m(t);
  let left: t => m(t);
  let right: t => m(t);

  let split: t => Result.t(graph, string);
  let reform: (t, graph) => Result.t(t, string);
};

module Make =
       (G: GRAPH)
       : (ZIPPER with type focus = ID.t and type graph = G.t) => {
  type focus = ID.t;
  type graph = G.t;
  type t = {
    focus_: ID.t,
    up_: option(PID.t),
    down_: list(ID.t),
    left_: list(ID.t),
    right_: list(ID.t),
    background_: G.t,
  };
  type m('a) = option('a);

  let _sortedIds = ids => ids->List.sort(Pervasives.compare);

  let _siblings = (up, g) =>
    up
    ->Option.map(pid => g->G.childIds(pid->I.convertParentToFocus))
    ->Option.getWithDefault([])
    ->List.sort(Pervasives.compare);

  let createAt = (g, focus) => {
    g->G.containsId(focus)
      ? {
        let up_ = g->G.parentId(focus);
        let down_ = g->G.childIds(focus)->_sortedIds;
        let siblings = _siblings(up_, g);
        let index = siblings->List.toArray->Array.getIndexBy(i => i == focus);
        let lr = index->Option.flatMap(i => {siblings->List.splitAt(i)});
        let (left_, right_) =
          lr->Option.mapWithDefault(([], []), ((l, r)) =>
            (l->List.reverse, r->List.tail->Option.getWithDefault([]))
          );
        {focus_: focus, up_, down_, left_, right_, background_: g}->Some;
      }
      : None;
  };

  let create = g =>
    switch (g->G.childIdsOfRoot->_sortedIds) {
    | [hd, ..._tl] => g->createAt(hd)
    | [] => None
    };

  let toString = t =>
    "Focus: "
    ++ t.focus_->ID.toString
    ++ ", up: "
    ++ t.up_->Option.mapWithDefault("None", PID.toString)
    ++ ", down: ["
    ++ (t.down_->List.map(ID.toString) |> String.concat(","))
    ++ "]"
    ++ ", left: ["
    ++ (t.left_->List.map(ID.toString) |> String.concat(","))
    ++ "]"
    ++ ", right: ["
    ++ (t.right_->List.map(ID.toString) |> String.concat(","))
    ++ "]";

  let flatMap = Option.flatMap;
  let map = Option.map;
  let mapWithDefault = Option.mapWithDefault;
  let getExn = Option.getExn;
  let getOpt = t => t;
  let getResult = t =>
    switch (t->getOpt) {
    | Some(tt) => Result.Ok(tt)
    | None => Result.Error("Zipper is none")
    };

  let focus = t => t.focus_;

  // TODO can reform without the second childIds call
  let up = t =>
    t.up_
    ->Option.flatMap(pid =>
        t.background_->createAt(pid->I.convertParentToFocus)
      );

  let down = t =>
    switch (t.down_) {
    | [hd, ...tl] =>
      {
        ...t,
        focus_: hd,
        left_: [],
        right_: tl,
        up_: t.focus_->I.convertFocusToParent->Some,
        down_: t.background_->G.childIds(hd)->_sortedIds,
      }
      ->Some
    | [] => t->Some
    };

  let left = t => {
    let (focus_, left_, right_, down_) =
      switch (t.left_) {
      | [hd, ...tl] => (
          hd,
          tl,
          t.right_->List.add(t.focus_),
          t.background_->G.childIds(hd),
        )
      | [] => (t.focus_, t.left_, t.right_, t.down_)
      };
    {...t, focus_, left_, right_, down_}->Some;
  };
  let right = t => {
    let (focus_, left_, right_, down_) =
      switch (t.right_) {
      | [hd, ...tl] => (
          hd,
          t.left_->List.add(t.focus_),
          tl,
          t.background_->G.childIds(hd),
        )
      | [] => (t.focus_, t.left_, t.right_, t.down_)
      };
    {...t, focus_, left_, right_, down_}->Some;
  };

  let split = t => {
    let res =
      switch (t.background_->G.subGraphForNode(t.focus_)) {
      | Some(g) =>
        [%log.debug "adding to empty"; ("", "")];
        G.empty()->G.setSubGraphForRoot(g);
      | None =>
        Result.Error("Split: cannot find subgraph: " ++ t.focus_->ID.toString)
      };
    switch (res) {
    | Result.Ok(g) => [%log.debug "SPLIT: " ++ g->G.toString; ("", "")]
    | Result.Error(err) => [%log.error "SPLIT: " ++ err; ("", "")]
    };
    res;
  };

  let reform = (t, inner) => {
    switch (
      t.background_->G.subGraphForNode(t.focus_),
      inner->G.subGraphForNode(t.focus_),
    ) {
    | (Some(g), Some(g1)) =>
      g->G.eq(g1)
        ? {
          [%log.debug "reform equal"; ("", "")];
          t->Result.Ok;
        }
        : {
          [%log.debug "reform not equal"; ("", "")];
          let res =
            switch (t.up_) {
            | Some(pid) => t.background_->G.setSubGraphForNode(pid, g1)
            | None => t.background_->G.setSubGraphForRoot(g1)
            };
          res->Result.map(r => {...t, background_: r});
        }
    | (_, _) =>
      Result.Error("Reform: cannot find subgraph: " ++ t.focus_->ID.toString)
    };
  };
};
