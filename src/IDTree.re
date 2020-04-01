module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module P = Path.T;

/*
 for confusion with addSubtree and ID.t:
  could have type subtree = | Inner(t) | Full(t, ID.t) ?
  */
module type IDTREE = {
  type t;

  /* makes an empty IDTree with root, root is never included in the IDTree */
  let empty: unit => t;
  /* makes an empty IDTree with ID as (non-root) parent, ID is included in the IDTree */
  let emptySubtree: ID.t => t;
  let isRoot: t => bool;
  let rootId: t => option(ID.t);
  let myId: t => ID.t;
  let children: t => CID.Map.t(t);
  let hasChildren: t => bool;
  let toSummaryString: t => string;
  let toString: t => string;
  /* add ID into t under path P */
  let addChild: (t, P.t, ID.t) => t;
  let removeChild: (t, P.t, CID.t) => t;
  let getChildPaths: (t, P.t, bool) => array((CID.t, P.t));
  let getAllPaths: t => array((CID.t, P.t));
  let getChildIds: (t, P.t, bool) => array(CID.t);
  let getAllIds: t => array(CID.t);
  let getSubtree: (t, P.t, ID.t) => option(t);
  /* add subtree from ID into t under new Path P
       ID is needed in case you are adding an empty subtree with a proper root node
     */
  let addSubtree: (t, ID.t, P.t, t) => t;
  let removeSubtree: (t, P.t, CID.t) => t;
  let eq: (t, t) => bool;
};

module T: IDTREE = {
  include IDTree_cont;
};
