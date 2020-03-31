module I = Identity;
module ID = I.FocusId;
module PID = I.ParentId;
module CID = I.ChildId;
module P = Path.T;
module IDTree = IDTree.T;

module type GRAPH = {
  type el;
  type t;
  type err;

  let empty: unit => t;
  let toString: t => string;
  let size: t => int;
  let hasChildren: t => bool;
  let numberChildren: t => int;
  let containsId: (t, ID.t) => bool;
  let pathFromNode: (t, ID.t) => option(P.t);
  let dataForNode: (t, ID.t) => option(el)
  let depth: (t, ID.t) => int;
  let maxDepth: (t, ID.t) => int;
  let setDataForNode: (t, ID.t, el => el) => t;
  let subGraphForNode: (t, ID.t) => option(t);
  let addNodeAtPath: (t, ID.t, el, P.t) => t;
  let addNode: (t, ID.t, el) => t;
  let addNodeUnder: (t, ID.t, el, PID.t) => t;
  let removeNode: (t, ID.t) => Result.t(t, err);
  let moveChild: (t, CID.t, PID.t) => Result.t(t, err);
  let removeSubtree: (t, ID.t) => Result.t(t, err);
  let setSubGraphForNode: (t, ID.t, t) => Result.t(t, err);
  let moveSubtree: (t, CID.t, PID.t) => Result.t(t, err);
  let map: (t, el => el) => t;
  let updateChildren: (t, ID.t, el => el) => t;
  let forEach: (t, (ID.t, el) => unit) => unit;
  let keep: (t, (ID.t, el) => bool) => t;
  let toArray: t => array(el);
  let toKeyValueArray: t => array((ID.t, el));
};


module Make(S:Data.STRINGLY) : (GRAPH with type el := S.t and type err := string) = {
  include Graph_immutable_.Make(S);
}

