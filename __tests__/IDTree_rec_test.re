open BsMocha.Mocha;
module Assert = BsMocha.Assert

module M = IDTree_rec;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

describe("canMakeEmpty", () => {

  // open! Expect.Operators;
  let p = M.empty();

  it("hasNoChildren", () => {
    (p.children->Map.size) |> Assert.equal(0)
  });

  it("emptyIsRootId", () => {
    (p.me === ID.create("root")) |> Assert.equal(true)
  });

  it("emptyIsRootFlag", () => {
    (p.isRoot) |> Assert.equal(true)
  });

  it("emptyIsRoot", () => {
    (p->M.rootId->Option.getExn == ID.create("root")) |> Assert.equal(true)
  });
});

describe("addImmediateChildren", () => {

  let t = M.empty();
  let path = P.fromList([]);
  let id = ID.create("child1");
  let t2 = t->M.addChild(path, id);

  it("oneChildAdded", () => {
    (t2.children->Map.size) |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    (t2.children->Map.has(CID.create("child1"))) |> Assert.equal(true)
  });

  it("childIsNotRoot", () => {
    let child1: M.t = t2.children->Map.getExn(CID.create("child1"));
    (child1.isRoot) |> Assert.equal(false);
  });

  let id = ID.create("child2");
  let t3 = t2->M.addChild(path, id);
  it("secondChildIsAdded", () => {
    (t3.children->Map.size) |> Assert.equal(2)
  });

  it("secondChildIsInChildrenCollection", () => {
    (t3.children->Map.has(id->I.convertFocusToChild)) |> Assert.equal(true)
  });

  %log.debug
  t3
  ->M.getAllPaths
  ->Array.map(d =>
      "{" ++ fst(d)->CID.toString ++ "::" ++ snd(d)->P.toString ++ "}"
    )
  ->List.fromArray
  |> String.concat(",");
  it("secondChildIsNotRoot", () => {
    let child2: M.t = t3.children->Map.getExn(id->I.convertFocusToChild);
    (child2.isRoot) |> Assert.equal(false);
  });
});

describe("addLowDownChildren", () => {

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

  it("oneChildAdded", () => {
    (t3->M.children->Map.size) |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    (t3->M.children->Map.has(CID.create("child1"))) |> Assert.equal(true)
  });

  it("childIsNotRoot", () => {
    let child1: M.t = t3->M.children->Map.getExn(id->I.convertFocusToChild);
    (child1.isRoot) |> Assert.equal(false);
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

  it("twoChildAdded", () => {
    (t5->M.children->Map.size) |> Assert.equal(2)
  });

  it("secondChildIsInChildrenCollection", () => {
    (t5->M.children->Map.has(CID.create("child2"))) |> Assert.equal(true)
  });

  it("secondChildIsNotRoot", () => {
    let child2: M.t = t5->M.children->Map.getExn(id2->I.convertFocusToChild);
    (child2.isRoot) |> Assert.equal(false);
  });
});

describe("addInnerChild", () => {

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

  it("dIsChild", () => {
    (t3->M.children->Map.has(CID.create("d"))) |> Assert.equal(true)
  });

  let check2 = (p, c) => {
    (
      t3
      ->M.children
      ->Map.getExn(CID.create(p))
      ->M.children
      ->Map.has(CID.create(c)),
    )
    |> Assert.equal(true);
  };
  it("dHasChild2", () => {
    check2("d", "child4")
  });
});

describe("removeImmediateChildren", () => {

  let path = P.fromList([]);
  let id = ID.create("child1");
  let t = M.empty()->M.addChild(path, id);
  let t1 = t->M.removeChild(path, CID.create("child1"));

  it("oneChildRemoved", () => {
    (t1->M.children->Map.size) |> Assert.equal(0)
  });

  it("childIsNotInChildrenCollection", () => {
    (t1->M.children->Map.has(CID.create("child1"))) |> Assert.equal(false)
  });
});

describe("removeDeepChildren", () => {

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

  it("oneChildRemoved", () => {
    (t2.children->Map.size) |> Assert.equal(1)
  });

  it("child1IsNotInChildrenCollection", () => {
    (t2.children->Map.has(id1->I.convertFocusToChild)) |> Assert.equal(false)
  });

  it("child2IsStillInChildrenCollection", () => {
    (t2.children->Map.has(id2->I.convertFocusToChild)) |> Assert.equal(true)
  });
});

describe("removeDeepChildren2", () => {

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

  it("oneChildRemoved", () => {
    (t2->M.children->Map.size) |> Assert.equal(1)
  });

  it("child1IsStillInChildrenCollection", () => {
    (t2->M.children->Map.has(CID.create("child1"))) |> Assert.equal(true)
  });

  it("child2IsNotInChildrenCollection", () => {
    (t2->M.children->Map.has(CID.create("child2"))) |> Assert.equal(false)
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

  it("oneChildRemoved", () => {
    (t3->M.children->Map.size) |> Assert.equal(1)
  });

  it("child1IsStillInChildrenCollection", () => {
    (t3->M.children->Map.has(CID.create("child3"))) |> Assert.equal(true)
  });
});

describe("removeNonExistantChildren", () => {

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

  it("noChildRemoved", () => {
    (t2.children->Map.size) |> Assert.equal(2)
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

  it("noChildRemoved", () => {
    (t2->M.children->Map.size) |> Assert.equal(2)
  });
});

describe("removeInnerChild", () => {

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
  it("abMovedUp", () => {
    %log.debug
    t2->M.children->Map.getExn(CID.create("2"))->M.toString;
    (t3->M.children->Map.size) |> Assert.equal(3);
  });

  let check = s => {
    (t3->M.children->Map.has(CID.create(s))) |> Assert.equal(true);
  };
  it("aIsChild", () => {
    check("a")
  });
  it("bIsChild", () => {
    check("b")
  });
  it("cIsChild", () => {
    check("c")
  });

  let check2 = (p, c) => {
    (
      t3
      ->M.children
      ->Map.getExn(CID.create(p))
      ->M.children
      ->Map.has(CID.create(c)),
    )
    |> Assert.equal(true);
  };
  it("aIsChild2", () => {
    check2("a", "child1")
  });
  it("bIsChild2", () => {
    check2("b", "child2")
  });
  it("cIsChild2", () => {
    check2("c", "child3")
  });
});

describe("getChildPaths", () => {

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
  it("gotAllChildren", () => {
    let paths = t->M.getChildPaths(path0, false); // should be all children of 2
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    (paths->Array.size) |> Assert.equal(7);
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

  it("gotFourChildren", () => {
    let paths = t->M.getChildPaths(P.fromRootToPathList(["2", "1"]), false);
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    (paths->Array.size) |> Assert.equal(4);
    /*
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
     */
  });

  it("gotFourChildIds", () => {
    let paths = t->M.getChildIds(P.fromRootToPathList(["2", "1"]), false);
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    (paths->Array.size) |> Assert.equal(4);
    /*
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
     */
  });

  let paths = t->M.getChildPaths(path3, false); // should be only one
  it("gotOnlyOne", () => {
    (paths->Array.size) |> Assert.equal(1)
  });
  it("gotChild3", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->fst->CID.toString; ("", "")];
    [%log.debug "id3:" ++ id3->ID.toString; ("", "")];
    (pr->fst == id3->I.convertFocusToChild) |> Assert.equal(true);
  });
  it("gotChild3Path", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->snd->P.toString; ("", "")];
    [%log.debug "id3:" ++ path3->P.toString; ("", "")];
    (pr->snd->P.eq(path3)) |> Assert.equal(true);
  });

  it("gotNone", () => {
    let paths = t->M.getChildIds(P.fromRootToPathList(["20", "10"]), false);
    (paths->Array.size) |> Assert.equal(0);
  });
});

describe("_getTests", () => {

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

  it("_getFromRoot", () => {
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
    ((cids^)->List.size) |> Assert.equal(8);
  });

  it("_getFromLeaf", () => {
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
    ((cids1^)->List.size) |> Assert.equal(1);
  });
});

describe("getAllPaths", () => {

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

  it("gotAllPaths", () => {
    let paths = t->M.getAllPaths; // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    (paths->Array.size) |> Assert.equal(8);
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

  it("gotAllIds", () => {
    let paths = t->M.getAllIds; // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    (paths->Array.size) |> Assert.equal(8);
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

  it("gotChildPAths", () => {
    let paths = t->M.getChildPaths(P.fromList(["2"]), false); // should not include 2
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    (paths->Array.size) |> Assert.equal(7);
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

  it("gotChildPathsInclusive", () => {
    let paths = t->M.getChildPaths(P.fromList(["2"]), true); // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    (paths->Array.size) |> Assert.equal(8);
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
  it("gotSubtree", () => {
    (t1->M.myId == ID.create("a")) |> Assert.equal(true)
  });

  it("gotSubtreeIds", () => {
    [%log.debug "t1:" ++ t1->M.toString; ("", "")];
    let cids = t1->M.getAllIds;
    (cids->Array.size) |> Assert.equal(2);
  });

  it("gotOneChildInSubtree", () => {
    (t1->M.children->Map.size) |> Assert.equal(1)
  });

  it("gotChildInSubtree", () => {
    (t1->M.children->Map.has(CID.create("child1"))) |> Assert.equal(true)
  });

  let t1 =
    t
    ->M.getSubtree(path1->P.moveUp->P.moveUp, ID.create("1"))
    ->Option.getExn;
  it("gotSubtree2", () => {
    (t1->M.myId == ID.create("1")) |> Assert.equal(true)
  });

  it("gotTwoChildInSubtree", () => {
    (t1->M.children->Map.size) |> Assert.equal(2)
  });

  it("gotChildInSubtree1", () => {
    (t1->M.children->Map.has(CID.create("a"))) |> Assert.equal(true)
  });
  it("gotChildInSubtree2", () => {
    (t1->M.children->Map.has(CID.create("b"))) |> Assert.equal(true)
  });
});

describe("addSubtree", () => {

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
  it("notAddedNewRootNode", () => {
    (t4->M.isRoot) |> Assert.equal(false)
  });
  it("hasAddedNodeWithCorrectId", () => {
    (t4->M.myId == ID.create("test")) |> Assert.equal(true)
  });
  let _get = (p1, p2) => {
    t4
    ->M.children
    ->Map.getExn(CID.create(p1))
    ->M.children
    ->Map.getExn(CID.create(p2))
    ->M.children;
  };

  it("3aHasTwoChildren", () => {
    (_get("3", "a")->Map.size) |> Assert.equal(2)
  });

  it("3aHasChild4", () => {
    (_get("3", "a")->Map.has(CID.create("child4"))) |> Assert.equal(true)
  });

  it("3aHasChild5", () => {
    (_get("3", "a")->Map.has(CID.create("child5"))) |> Assert.equal(true)
  });

  it("3bHasOneChild", () => {
    (_get("3", "b")->Map.size) |> Assert.equal(1)
  });

  it("3bHasChild6", () => {
    (_get("3", "b")->Map.has(CID.create("child6"))) |> Assert.equal(true)
  });
});

describe("removeSubtree", () => {

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
  it("oneSubtreeRemoved", () => {
    (t2->M.children->Map.size) |> Assert.equal(1)
  });

  it("subtreeIsNotInChildrenCollection", () => {
    (t2->M.children->Map.has(ID.create("1")->I.convertFocusToChild))
    |> Assert.equal(false)
  });

  it("subtree2IsStillInChildrenCollection", () => {
    (t2->M.children->Map.has(ID.create("c")->I.convertFocusToChild))
    |> Assert.equal(true)
  });
});
