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

module type IDTREE2 = {
  type root;
  type subtree;
  type t('a);

  /* makes an empty IDTree with root, root is never included in the IDTree */
  let empty: unit => t(root);
  /* makes an empty IDTree with ID as (non-root) parent, ID is included in the IDTree */
  let emptySubtree: ID.t => t(subtree);
  let isRoot: t('a) => bool;
  let rootId: t('a) => option(ID.t);
  let myId: t('a) => ID.t;
  let children: t('a) => CID.Map.t(t('a));
  let hasChildren: t('a) => bool;
  let toSummaryString: t('a) => string;
  let toString: t('a) => string;
  /* add ID into t under path P */
  let addChild: (t('a), P.t, ID.t) => t('a);
  let removeChild: (t('a), P.t, CID.t) => t('a);
  let getChildPaths: (t('a), P.t, bool) => array((CID.t, P.t));
  let getAllPaths: t('a) => array((CID.t, P.t));
  let getChildIds: (t('a), P.t, bool) => array(CID.t);
  let getAllIds: t('a) => array(CID.t);
  let getSubtree: (t('a), P.t, ID.t) => option(t(subtree));
  /* add subtree from ID into t under new Path P
       ID is needed in case you are adding an empty subtree with a proper root node
     */
  let addSubtree: (t('a), ID.t, P.t, t(subtree)) => t('a);
  let addRootAsSubtree: (t('a), ID.t, P.t, t(root)) => t('a);
  let removeSubtree: (t('a), P.t, CID.t) => t('a);
  let eq: (t('a), t('a)) => bool;
};

module T2: IDTREE2 = {
  include IDTree_cont2;
};
