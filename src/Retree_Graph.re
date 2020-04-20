module I = Retree_Identity;
module ID = I.FocusId;
module PID = I.ParentId;
module CID = I.ChildId;
module P = Retree_Path.T;
module IDTree = Retree_IDTree.T;

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
  let maxDepth: (t('a), ID.t) => int;
  let setDataForNode: (t('a), ID.t, 'a => 'a) => t('a);
  let subGraphForNode: (t('a), ID.t) => option(t('a));
  let childIdsOfRoot: t('a) => list(ID.t);
  let childrenOfRoot: t('a) => list(t('a));
  let addNodeAtPath: (t('a), ID.t, 'a, P.t) => t('a);
  let addNode: (t('a), ID.t, 'a) => t('a);
  let addNodeUnder: (t('a), ID.t, 'a, PID.t) => t('a);
  let removeNode: (t('a), ID.t) => Result.t(t('a), string);
  let moveChild: (t('a), CID.t, PID.t) => Result.t(t('a), string);
  let removeSubtree: (t('a), ID.t) => Result.t(t('a), string);
  let setSubGraphForNode:
    (t('a), PID.t, ID.t, t('a)) => Result.t(t('a), string);
  let setSubGraphForRoot: (t('a), ID.t, t('a)) => Result.t(t('a), string);
  let moveSubtree: (t('a), CID.t, PID.t) => Result.t(t('a), string);
  let map: (t('a), 'a => 'b) => t('b);
  let updateChildren: (t('a), ID.t, 'a => 'a) => t('a);
  let forEach: (t('a), (ID.t, 'a) => unit) => unit;
  let keep: (t('a), (ID.t, 'a) => bool) => t('a);
  let toKeyValueArrayWithPaths: t('a) => array((ID.t, P.t, 'a));
  let toKeyValueArray: t('a) => array((ID.t, 'a));
  let toArray: t('a) => array('a);
  let fromArray: (array('a), 'a => ID.t, 'a => option(PID.t)) => t('a);
};

module T: GRAPH = {
  include Graph_immutable;
};