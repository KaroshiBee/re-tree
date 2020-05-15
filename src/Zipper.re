module I = Identity;
module ID = I.FocusId;
module PID = I.ParentId;
module CID = I.ChildId;
module P = Path.T;
module type GRAPH = Graph.GRAPH;

module type ZIPPER = {
  type focus;
  type graph('a);
  type t('a);
  let create: (graph('a), focus) => t('a);
  let focus: t('a) => option(focus);
  let up: t('a) => option(t('a));
  let down: t('a) => option(t('a));
  let left: t('a) => option(t('a));
  let right: t('a) => option(t('a));
  /* let current: t('a) => option(Graph.T.t('a)); */
  /* let context: t('a) => Graph.T.t('a); */
};

module Make =
       (G: GRAPH)
       : (ZIPPER with type focus = ID.t and type graph('a) = G.t('a)) => {
  type focus = ID.t;
  type graph('a) = G.t('a);
  type t('a) = {
    focus: option(ID.t),
    up: option(PID.t),
    down: list(ID.t),
    left: list(ID.t),
    right: list(ID.t),
    background: G.t('a),
  };
  let create = (g, id) => {
    let up = g->G.parentId(id);
    let down = g->G.childIds(id);
    let siblings =
      up
      ->Option.map(pid => g->G.childIds(pid->I.convertParentToFocus))
      ->Option.getWithDefault([]);
    let index = siblings->List.toArray->Array.getIndexBy(i => i == id);
    let lr = index->Option.flatMap(i => {siblings->List.splitAt(i)});
    let (left, right) =
      lr->Option.mapWithDefault(([], []), ((l, r)) => (l, r));
    let focus = g->G.containsId(id) ? Some(id) : None;
    {focus, up, down, left, right, background: g};
  };

  let focus = t => t.focus;
  let up = t =>
    t.up
    ->Option.map(pid => t.background->create(pid->I.convertParentToFocus));
  let down = t => t.down;
  let left = t => t.left;
  let right = t => t.right;
};
