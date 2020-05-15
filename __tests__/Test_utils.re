module M = IDTree.T;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

let path0 = P.fromRootToPathList(["2"]);
let path1 = P.fromRootToPathList(["2", "1", "a"]);
let path2 = P.fromRootToPathList(["2", "1", "b"]);
let path3 = P.fromRootToPathList(["2", "c"]);
let id1 = ID.create("child1");
let id2 = ID.create("child2");
let id3 = ID.create("child3");

let standardTree =
  M.empty()
  ->M.addChild(path1, id1)
  ->M.addChild(path2, id2)
  ->M.addChild(path3, id3);

let sort = paths => {
  paths->SortArray.stableSortBy((x, y) =>
    String.compare(fst(x)->CID.toString, fst(y)->CID.toString)
  );
};

let expected = [|
  ("child3"->CID.create, path3),
  ("c"->CID.create, path0),
  ("child2"->CID.create, path2),
  ("b"->CID.create, path2->P.moveUp),
  ("child1"->CID.create, path1),
  ("a"->CID.create, path2->P.moveUp),
  ("1"->CID.create, path0),
|];

let printDebug = (guff, pathList) => {
  [%log.debug
    guff
    ++ (
      pathList
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
      fst(x)->CID.toString == fst(y)->CID.toString && snd(x)->P.eq(snd(y))
    });
};
