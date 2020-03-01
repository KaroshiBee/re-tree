open Jest;
module M = IDTree;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.Parents;

describe("canMakeEmpty", () => {
  open Expect;
  // open! Expect.Operators;
  let p = M.empty();

  test("hasNoChildren", () => {
    expect(p.children->Map.size) |> toBe(0)
  });

  test("emptyIsRootId", () => {
    expect(p.me === ID.create("root")) |> toBe(true)
  });

  test("emptyIsRootFlag", () => {
    expect(p.isRoot) |> toBe(true)
  });

  test("emptyIsRoot", () => {
    expect(p->M.rootId->Option.getExn == ID.create("root")) |> toBe(true)
  });
});

describe("addImmediateChildren", () => {
  open Expect;

  let t = M.empty();
  let path = P.fromList([]);
  let id = ID.create("child1");
  let t2 = t->M.addChild(path, id);

  test("oneChildAdded", () => {
    expect(t2.children->Map.size) |> toBe(1)
  });

  test("childIsInChildrenCollection", () => {
    expect(t2.children->Map.has(CID.create("child1"))) |> toBe(true)
  });

  test("childIsNotRoot", () => {
    let child1: M.t = t2.children->Map.getExn(CID.create("child1"));
    expect(child1.isRoot) |> toBe(false);
  });

  let id = ID.create("child2");
  let t3 = t2->M.addChild(path, id);
  test("secondChildIsAdded", () => {
    expect(t3.children->Map.size) |> toBe(2)
  });

  test("secondChildIsInChildrenCollection", () => {
    expect(t3.children->Map.has(id->I.convertFocusToChild)) |> toBe(true)
  });

  %log.debug
  t3
  ->M.getAllPaths
  ->Array.map(d =>
      "{" ++ fst(d)->CID.toString ++ "::" ++ snd(d)->P.toString ++ "}"
    )
  ->List.fromArray
  |> String.concat(",");
  test("secondChildIsNotRoot", () => {
    let child2: M.t = t3.children->Map.getExn(id->I.convertFocusToChild);
    expect(child2.isRoot) |> toBe(false);
  });
});

describe("addLowDownChildren", () => {
  open Expect;

  let t = M.empty();
  let path = P.fromList(["1", "2", "3"]);
  let id = ID.create("child1");
  let t2 = t->M.addChild(path, id);

  let t3 =
    t2.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  test("oneChildAdded", () => {
    expect(t3->M.children->Map.size) |> toBe(1)
  });

  test("childIsInChildrenCollection", () => {
    expect(t3->M.children->Map.has(CID.create("child1"))) |> toBe(true)
  });

  test("childIsNotRoot", () => {
    let child1: M.t = t3->M.children->Map.getExn(id->I.convertFocusToChild);
    expect(child1.isRoot) |> toBe(false);
  });

  let id2 = ID.create("child2");
  let t4 = t2->M.addChild(path, id2);

  let t5 =
    t4
    ->M.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  test("twoChildAdded", () => {
    expect(t5->M.children->Map.size) |> toBe(2)
  });

  test("secondChildIsInChildrenCollection", () => {
    expect(t5->M.children->Map.has(CID.create("child2"))) |> toBe(true)
  });

  test("secondChildIsNotRoot", () => {
    let child2: M.t = t5->M.children->Map.getExn(id2->I.convertFocusToChild);
    expect(child2.isRoot) |> toBe(false);
  });
});

describe("addInnerChild", () => {
  open Expect;

  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  let path4 = P.fromRootToPathList(["2", "d"]);
  let t2 = t->M.addChild(path4, ID.create("child4"));
  let t3 = t2->M.children->Map.getExn(CID.create("2"));

  test("dIsChild", () => {
    expect(t3->M.children->Map.has(CID.create("d"))) |> toBe(true)
  });

  let check2 = (p, c) => {
    expect(
      t3
      ->M.children
      ->Map.getExn(CID.create(p))
      ->M.children
      ->Map.has(CID.create(c)),
    )
    |> toBe(true);
  };
  test("dHasChild2", () => {
    check2("d", "child4")
  });
});

describe("removeImmediateChildren", () => {
  open Expect;

  let path = P.fromList([]);
  let id = ID.create("child1");
  let t = M.empty()->M.addChild(path, id);
  let t1 = t->M.removeChild(path, CID.create("child1"));

  test("oneChildRemoved", () => {
    expect(t1->M.children->Map.size) |> toBe(0)
  });

  test("childIsNotInChildrenCollection", () => {
    expect(t1->M.children->Map.has(CID.create("child1"))) |> toBe(false)
  });
});

describe("removeDeepChildren", () => {
  open Expect;

  let path = P.fromList(["1", "2", "3"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let t = M.empty()->M.addChild(path, id1)->M.addChild(path, id2);
  let t1 = t->M.removeChild(path, CID.create("child1"));
  let t2 =
    t1
    ->M.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  test("oneChildRemoved", () => {
    expect(t2.children->Map.size) |> toBe(1)
  });

  test("child1IsNotInChildrenCollection", () => {
    expect(t2.children->Map.has(id1->I.convertFocusToChild)) |> toBe(false)
  });

  test("child2IsStillInChildrenCollection", () => {
    expect(t2.children->Map.has(id2->I.convertFocusToChild)) |> toBe(true)
  });
});

describe("removeDeepChildren2", () => {
  open Expect;

  let path1 = P.fromList(["1", "2", "3"]);
  let path2 = P.fromList(["1", "2", "3", "4"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path1, id2)
    ->M.addChild(path2, id3);
  let t1 = t->M.removeChild(path1, CID.create("child2"));
  let t2 =
    t1
    ->M.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  test("oneChildRemoved", () => {
    expect(t2->M.children->Map.size) |> toBe(1)
  });

  test("child1IsStillInChildrenCollection", () => {
    expect(t2->M.children->Map.has(CID.create("child1"))) |> toBe(true)
  });

  test("child2IsNotInChildrenCollection", () => {
    expect(t2->M.children->Map.has(CID.create("child2"))) |> toBe(false)
  });

  let t3 =
    t1
    ->M.children
    ->Map.getExn(CID.create("4"))
    ->M.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  test("oneChildRemoved", () => {
    expect(t3->M.children->Map.size) |> toBe(1)
  });

  test("child1IsStillInChildrenCollection", () => {
    expect(t3->M.children->Map.has(CID.create("child3"))) |> toBe(true)
  });
});

describe("removeNonExistantChildren", () => {
  open Expect;

  let path1 = P.fromList(["1", "2", "3"]);
  let path2 = P.fromList(["1", "3", "4"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let t = M.empty()->M.addChild(path1, id1)->M.addChild(path1, id2);

  let t1 = t->M.removeChild(path1, CID.create("child3"));
  let t2 =
    t1
    ->M.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  test("noChildRemoved", () => {
    expect(t2.children->Map.size) |> toBe(2)
  });

  let t1 = t->M.removeChild(path2, CID.create("child1"));
  let t2 =
    t1
    ->M.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  test("noChildRemoved", () => {
    expect(t2->M.children->Map.size) |> toBe(2)
  });
});

describe("removeInnerChild", () => {
  open Expect;

  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  let t2 = t->M.removeChild(P.fromList(["2"]), CID.create("1"));
  let t3 = t2->M.children->Map.getExn(CID.create("2"));
  test("abMovedUp", () => {
    %log.debug
    t2->M.children->Map.getExn(CID.create("2"))->M.toString;
    expect(t3->M.children->Map.size) |> toBe(3);
  });

  let check = s => {
    expect(t3->M.children->Map.has(CID.create(s))) |> toBe(true);
  };
  test("aIsChild", () => {
    check("a")
  });
  test("bIsChild", () => {
    check("b")
  });
  test("cIsChild", () => {
    check("c")
  });

  let check2 = (p, c) => {
    expect(
      t3
      ->M.children
      ->Map.getExn(CID.create(p))
      ->M.children
      ->Map.has(CID.create(c)),
    )
    |> toBe(true);
  };
  test("aIsChild2", () => {
    check2("a", "child1")
  });
  test("bIsChild2", () => {
    check2("b", "child2")
  });
  test("cIsChild2", () => {
    check2("c", "child3")
  });
});

describe("getChildPaths", () => {
  open Expect;

  let path0 = P.fromRootToPathList(["2"]);
  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  [%log.debug "test tree: " ++ t->M.toString; ("", "")];
  test("gotAllChildren", () => {
    let paths = t->M.getChildPaths(path0, false); // should be all children of 2
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    expect(paths->Array.size) |> toBe(7);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2}
     */
  });

  test("gotFourChildren", () => {
    let paths = t->M.getChildPaths(P.fromRootToPathList(["2", "1"]), false);
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    expect(paths->Array.size) |> toBe(4);
    /*
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
     */
  });

  test("gotFourChildIds", () => {
    let paths = t->M.getChildIds(P.fromRootToPathList(["2", "1"]), false);
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    expect(paths->Array.size) |> toBe(4);
    /*
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
     */
  });

  let paths = t->M.getChildPaths(path3, false); // should be only one
  test("gotOnlyOne", () => {
    expect(paths->Array.size) |> toBe(1)
  });
  test("gotChild3", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->fst->CID.toString; ("", "")];
    [%log.debug "id3:" ++ id3->ID.toString; ("", "")];
    expect(pr->fst == id3->I.convertFocusToChild) |> toBe(true);
  });
  test("gotChild3Path", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->snd->P.toString; ("", "")];
    [%log.debug "id3:" ++ path3->P.toString; ("", "")];
    expect(pr->snd->P.eq(path3)) |> toBe(true);
  });

  test("gotNone", () => {
    let paths = t->M.getChildIds(P.fromRootToPathList(["20", "10"]), false);
    expect(paths->Array.size) |> toBe(0);
  });
});

describe("_getTests", () => {
  open Expect;
  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  test("_getFromRoot", () => {
    let cids = ref([]: list((CID.t, P.t)));

    let _ = t->M._get(P.empty(), cids, true);
    [%log.debug
      (cids^)
      ->List.map(pr =>
          "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}"
        )
      |> String.concat(",");
      ("", "")
    ];
    expect((cids^)->List.size) |> toBe(8);
  });

  test("_getFromLeaf", () => {
    let cids1 = ref([]: list((CID.t, P.t)));

    let _ =
      t
      ->M.getSubtree(path1, ID.create("child1"))
      ->Option.getExn
      ->M._get(path1, cids1, false);
    [%log.debug
      (cids1^)
      ->List.map(pr =>
          "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}"
        )
      |> String.concat(",");
      ("", "")
    ];
    expect((cids1^)->List.size) |> toBe(1);
  });
});

describe("getAllPaths", () => {
  open Expect;

  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  test("gotAllPaths", () => {
    let paths = t->M.getAllPaths; // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    expect(paths->Array.size) |> toBe(8);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},
       {2:},

     */
  });

  test("gotAllIds", () => {
    let paths = t->M.getAllIds; // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    expect(paths->Array.size) |> toBe(8);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},
       {2:},

     */
  });

  test("gotChildPAths", () => {
    let paths = t->M.getChildPaths(P.fromList(["2"]), false); // should not include 2
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    expect(paths->Array.size) |> toBe(7);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},

     */
  });

  test("gotChildPathsInclusive", () => {
    let paths = t->M.getChildPaths(P.fromList(["2"]), true); // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    expect(paths->Array.size) |> toBe(8);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},
       {2:},

     */
  });
});
describe("subtrees", () => {
  open Expect;

  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  let t1 = t->M.getSubtree(path1->P.moveUp, ID.create("a"))->Option.getExn;
  test("gotSubtree", () => {
    expect(t1->M.myId == ID.create("a")) |> toBe(true)
  });

  test("gotSubtreeIds", () => {
    [%log.debug "t1:" ++ t1->IDTree.toString; ("", "")];
    let cids = t1->IDTree.getAllIds;
    expect(cids->Array.size) |> toBe(2);
  });

  test("gotOneChildInSubtree", () => {
    expect(t1->M.children->Map.size) |> toBe(1)
  });

  test("gotChildInSubtree", () => {
    expect(t1->M.children->Map.has(CID.create("child1"))) |> toBe(true)
  });

  let t1 =
    t
    ->M.getSubtree(path1->P.moveUp->P.moveUp, ID.create("1"))
    ->Option.getExn;
  test("gotSubtree2", () => {
    expect(t1->M.myId == ID.create("1")) |> toBe(true)
  });

  test("gotTwoChildInSubtree", () => {
    expect(t1->M.children->Map.size) |> toBe(2)
  });

  test("gotChildInSubtree1", () => {
    expect(t1->M.children->Map.has(CID.create("a"))) |> toBe(true)
  });
  test("gotChildInSubtree2", () => {
    expect(t1->M.children->Map.has(CID.create("b"))) |> toBe(true)
  });
});

describe("addSubtree", () => {
  open Expect;

  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  let path4 = P.fromRootToPathList(["3", "a"]);
  let path5 = P.fromRootToPathList(["3", "b"]);
  let id4 = ID.create("child4");
  let id5 = ID.create("child5");
  let id6 = ID.create("child6");
  let t2 =
    M.empty()
    ->M.addChild(path4, id4)
    ->M.addChild(path4, id5)
    ->M.addChild(path5, id6);

  let t3 = t->M.addSubtree(ID.create("test"), path3, t2);
  [%log.debug "t3: " ++ t3->M.toString; ("", "")];
  let t4 =
    t3
    ->M.getSubtree(P.fromRootToPathList(["2", "c"]), ID.create("test"))
    ->Option.getExn;
  test("notAddedNewRootNode", () => {
    expect(t4->M.isRoot) |> toBe(false)
  });
  test("hasAddedNodeWithCorrectId", () => {
    expect(t4->M.myId == ID.create("test")) |> toBe(true)
  });
  let _get = (p1, p2) => {
    t4
    ->M.children
    ->Map.getExn(CID.create(p1))
    ->M.children
    ->Map.getExn(CID.create(p2))
    ->M.children;
  };

  test("3aHasTwoChildren", () => {
    expect(_get("3", "a")->Map.size) |> toBe(2)
  });

  test("3aHasChild4", () => {
    expect(_get("3", "a")->Map.has(CID.create("child4"))) |> toBe(true)
  });

  test("3aHasChild5", () => {
    expect(_get("3", "a")->Map.has(CID.create("child5"))) |> toBe(true)
  });

  test("3bHasOneChild", () => {
    expect(_get("3", "b")->Map.size) |> toBe(1)
  });

  test("3bHasChild6", () => {
    expect(_get("3", "b")->Map.has(CID.create("child6"))) |> toBe(true)
  });
});

describe("removeSubtree", () => {
  open Expect;

  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  let t1 = t->M.removeSubtree(path1->P.moveUp->P.moveUp, CID.create("1"));
  let t2 = t1->M.children->Map.getExn(CID.create("2"));
  test("oneSubtreeRemoved", () => {
    expect(t2->M.children->Map.size) |> toBe(1)
  });

  test("subtreeIsNotInChildrenCollection", () => {
    expect(t2->M.children->Map.has(ID.create("1")->I.convertFocusToChild))
    |> toBe(false)
  });

  test("subtree2IsStillInChildrenCollection", () => {
    expect(t2->M.children->Map.has(ID.create("c")->I.convertFocusToChild))
    |> toBe(true)
  });
});
