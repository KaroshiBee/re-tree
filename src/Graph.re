module I = Identity;
module ID = I.FocusId;
module PID = I.ParentId;
module CID = I.ChildId;
module P = Path.T;
module IDTree = IDTree.T;

module type GRAPH = {
  type t('a);
  type dataWithPath('a);
  let empty: unit => t('a);
  let toString: (t('a), 'a => string) => string;
  let size: t('a) => int;
  let hasChildren: t('a) => bool;
  let numberChildren: t('a) => int;
  let containsId: (t('a), ID.t) => bool;
  let pathFromNode: (t('a), ID.t) => option(P.t);
  let parentId: (t('a), ID.t) => option(PID.t);
  let dataForNode: (t('a), ID.t) => option('a);
  let depth: (t('a), ID.t) => int;
  let maxDepth: t('a) => int;
  // 'a => 'a because only modifying one node
  let setDataForNode: (t('a), ID.t, 'a => 'a) => t('a);
  let subGraphForNode: (t('a), ID.t) => option(t('a));
  let childIdsOfRoot: t('a) => list(ID.t);
  let childrenOfRoot: t('a) => list(t('a));
  let childIds: (t('a), ID.t) => list(ID.t);
  let children: (t('a), ID.t) => list(t('a));
  let childData: (t('a), ID.t) => list('a);
  let addNode: (t('a), ID.t, 'a) => t('a);
  let addNodeAtPath: (t('a), ID.t, 'a, P.t) => t('a);
  let addNodeUnder: (t('a), ID.t, 'a, PID.t) => t('a);
  let removeNode: (t('a), ID.t) => Result.t(t('a), string);
  let moveChild: (t('a), CID.t, PID.t) => Result.t(t('a), string);
  let removeSubtree: (t('a), ID.t) => Result.t(t('a), string);
  let setSubGraphForNode: (t('a), PID.t, t('a)) => Result.t(t('a), string);
  let setSubGraphForRoot: (t('a), t('a)) => Result.t(t('a), string);
  let trimPaths: (t('a), option(P.t)) => t('a);
  let moveSubtree: (t('a), CID.t, PID.t) => Result.t(t('a), string);
  let map: (t('a), 'a => 'b) => t('b);
  // 'a => 'a because only modifying one node
  let updateChildren: (t('a), ID.t, 'a => 'a) => t('a);
  let forEach: (t('a), (ID.t, 'a) => unit) => unit;
  let keep: (t('a), (ID.t, 'a) => bool) => t('a);
  let toKeyValueArrayWithPaths: t('a) => array((ID.t, P.t, 'a));
  let toKeyValueArray: t('a) => array((ID.t, 'a));
  let toArray: t('a) => array('a);
  let fromArray: (array('a), 'a => ID.t, 'a => option(PID.t)) => t('a);

  let eq: (t('a), t('a)) => bool;
};

module T: GRAPH with type dataWithPath('a) = Graph_immutable.dataWithPath('a) = Graph_immutable;
