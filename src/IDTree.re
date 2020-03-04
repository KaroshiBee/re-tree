module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module P = Path.T;

module type IDTREE = {
  type t;

  let empty: unit => t;
  let emptySubtree: ID.t => t;
  let isRoot: t => bool;
  let rootId: t => option(ID.t);
  let myId: t => ID.t;
  let children: t => CID.Map.t(t);
  let hasChildren: t => bool;
  let toSummaryString: t => string;
  let toString: t => string;
  let addChild: (t, P.t, ID.t) => t;
  let removeChild: (t, P.t, CID.t) => t;
  let getChildPaths: (t, P.t, bool) => array((CID.t, P.t));
  let getAllPaths: t => array((CID.t, P.t));
  let getChildIds: (t, P.t, bool) => array(CID.t);
  let getAllIds: t => array(CID.t);
  let getSubtree: (t, P.t, ID.t) => option(t);
  let addSubtree: (t, ID.t, P.t, t) => t;
  let removeSubtree: (t, P.t, CID.t) => t;
};

module T: IDTREE = {
  include IDTree_cont;
};
