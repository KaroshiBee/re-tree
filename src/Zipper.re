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
  let createAt: (graph, focus) => option(t);
  let create: graph => option(t);
  let toString: t => string;

  let focus: t => focus;
  let up: t => option(t);
  let down: t => option(t);
  let left: t => option(t);
  let right: t => option(t);
  /* let current: t => option(Graph.T.t); */
  /* let context: t => Graph.T.t; */

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

  let _siblings = (up, g) =>
    up
    ->Option.map(pid => g->G.childIds(pid->I.convertParentToFocus))
    ->Option.getWithDefault([])
    ->List.sort(Pervasives.compare);

  let createAt = (g, focus) => {
    g->G.containsId(focus)
      ? {
        let up_ = g->G.parentId(focus);
        let down_ = g->G.childIds(focus)->List.sort(Pervasives.compare);
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
    switch (g->G.childIdsOfRoot->List.sort(Pervasives.compare)) {
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
        down_: t.background_->G.childIds(hd)->List.sort(Pervasives.compare),
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
