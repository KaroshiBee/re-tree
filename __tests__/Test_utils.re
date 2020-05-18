module M = BsMocha.Mocha;
module Assert = BsMocha.Assert;

let describe = M.describe;
let it = M.it;

module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;
module T = IDTree.T;
module G = Graph.T;

module StandardTree = {
  let path0 = P.fromRootToPathList(["2"]);
  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");

  let t =
    T.empty()
    ->T.addChild(path1, id1)
    ->T.addChild(path2, id2)
    ->T.addChild(path3, id3);

  let path4 = P.fromRootToPathList(["3", "a"]);
  let path5 = P.fromRootToPathList(["3", "b"]);
  let id4 = ID.create("child4");
  let id5 = ID.create("child5");
  let id6 = ID.create("child6");
  let t2 =
    T.empty()
    ->T.addChild(path4, id4)
    ->T.addChild(path4, id5)
    ->T.addChild(path5, id6);
};

module Path_utils = {
  let sort = paths => {
    paths->SortArray.stableSortBy((x, y) =>
      String.compare(fst(x)->CID.toString, fst(y)->CID.toString)
    );
  };

  let expected = [|
    ("child2"->CID.create, StandardTree.path2),
    ("b"->CID.create, StandardTree.path2->P.moveUp),
    ("child1"->CID.create, StandardTree.path1),
    ("a"->CID.create, StandardTree.path2->P.moveUp),
    ("child3"->CID.create, StandardTree.path3),
    ("c"->CID.create, StandardTree.path0),
    ("1"->CID.create, StandardTree.path0),
  |];

  let printDebug = (_guff, _pathList) => {
    [%log.debug
      _guff
      ++ (
        _pathList
        ->Array.map(x => {
            "\n{" ++ x->fst->CID.toString ++ ":" ++ x->snd->P.toString ++ "}"
          })
        ->List.fromArray
        |> String.concat("\n")
      );
      ("", "")
    ];
  };
  let comparePathLists = (expected, actual) => {
    printDebug("expected: ", expected->sort);
    printDebug("actual: ", actual->sort);
    expected
    ->sort
    ->Array.eq(actual->sort, (x, y) => {
        fst(x)->CID.toString == fst(y)->CID.toString
        && snd(x)->P.eq(snd(y))
      });
  };
};
