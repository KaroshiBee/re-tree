open Test_utils;
let _ = (); //weird bug in reason-mode reason-paren-level

describe("canMakeEmpty", () => {
  let p = T.empty();

  it("hasNoChildren", () => {
    p->T.children->Map.size |> Assert.equal(0)
  });

  it("emptyIsRootId", () => {
    p->T.myId === ID.create("root") |> Assert.equal(true)
  });

  it("emptyIsRootFlag", () => {
    p->T.isRoot |> Assert.equal(true)
  });

  it("emptyIsRoot", () => {
    p->T.rootId->Option.getExn == ID.create("root") |> Assert.equal(true)
  });
});

describe("addImmediateChildren", () => {
  let t = T.empty();
  let path = P.fromList([]);
  let id = ID.create("child1");
  let t2 = t->T.addChild(path, id);

  it("oneChildAdded", () => {
    t2->T.children->Map.size |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    t2->T.children->Map.has(CID.create("child1")) |> Assert.equal(true)
  });

  it("childIsNotRoot", () => {
    let child1: T.t = t2->T.children->Map.getExn(CID.create("child1"));
    child1->T.isRoot |> Assert.equal(false);
  });

  let id = ID.create("child2");
  let t3 = t2->T.addChild(path, id);
  it("secondChildIsAdded", () => {
    t3->T.children->Map.size |> Assert.equal(2)
  });

  it("secondChildIsInChildrenCollection", () => {
    t3->T.children->Map.has(id->I.convertFocusToChild) |> Assert.equal(true)
  });

  it("secondChildIsNotRoot", () => {
    let child2: T.t = t3->T.children->Map.getExn(id->I.convertFocusToChild);
    child2->T.isRoot |> Assert.equal(false);
  });
});

describe("addLowDownChildren", () => {
  let t = T.empty();
  let path = P.fromList(["1", "2", "3"]);
  let id = ID.create("child1");
  let t2 = t->T.addChild(path, id);

  let t3 =
    t2
    ->T.children
    ->Map.getExn(CID.create("3"))
    ->T.children
    ->Map.getExn(CID.create("2"))
    ->T.children
    ->Map.getExn(CID.create("1"));

  it("oneChildAdded", () => {
    t3->T.children->Map.size |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    t3->T.children->Map.has(CID.create("child1")) |> Assert.equal(true)
  });

  it("childIsNotRoot", () => {
    let child1: T.t = t3->T.children->Map.getExn(id->I.convertFocusToChild);
    child1->T.isRoot |> Assert.equal(false);
  });

  let id2 = ID.create("child2");
  let t4 = t2->T.addChild(path, id2);

  let t5 =
    t4
    ->T.children
    ->Map.getExn(CID.create("3"))
    ->T.children
    ->Map.getExn(CID.create("2"))
    ->T.children
    ->Map.getExn(CID.create("1"));

  it("twoChildAdded", () => {
    t5->T.children->Map.size |> Assert.equal(2)
  });

  it("secondChildIsInChildrenCollection", () => {
    t5->T.children->Map.has(CID.create("child2")) |> Assert.equal(true)
  });

  it("secondChildIsNotRoot", () => {
    let child2: T.t = t5->T.children->Map.getExn(id2->I.convertFocusToChild);
    child2->T.isRoot |> Assert.equal(false);
  });
});

describe("addInnerChild", () => {
  let t = StandardTree.t;
  let path4 = P.fromRootToPathList(["2", "d"]);
  let t2 = t->T.addChild(path4, ID.create("child4"));
  let t3 = t2->T.children->Map.getExn(CID.create("2"));

  it("dIsChild", () => {
    t3->T.children->Map.has(CID.create("d")) |> Assert.equal(true)
  });

  let check2 = (p, c) => {
    t3
    ->T.children
    ->Map.getExn(CID.create(p))
    ->T.children
    ->Map.has(CID.create(c))
    |> Assert.equal(true);
  };
  it("dHasChild2", () => {
    check2("d", "child4")
  });
});

describe("removeImmediateChildren", () => {
  let path = P.fromList([]);
  let id = ID.create("child1");
  let t = T.empty()->T.addChild(path, id);
  let t1 = t->T.removeChild(path, CID.create("child1"));

  it("oneChildRemoved", () => {
    t1->T.children->Map.size |> Assert.equal(0)
  });

  it("childIsNotInChildrenCollection", () => {
    t1->T.children->Map.has(CID.create("child1")) |> Assert.equal(false)
  });
});

describe("removeDeepChildren", () => {
  let path = P.fromList(["1", "2", "3"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let t = T.empty()->T.addChild(path, id1)->T.addChild(path, id2);
  let t1 = t->T.removeChild(path, CID.create("child1"));
  let t2 =
    t1
    ->T.children
    ->Map.getExn(CID.create("3"))
    ->T.children
    ->Map.getExn(CID.create("2"))
    ->T.children
    ->Map.getExn(CID.create("1"));

  it("oneChildRemoved", () => {
    t2->T.children->Map.size |> Assert.equal(1)
  });

  it("child1IsNotInChildrenCollection", () => {
    t2->T.children->Map.has(id1->I.convertFocusToChild)
    |> Assert.equal(false)
  });

  it("child2IsStillInChildrenCollection", () => {
    t2->T.children->Map.has(id2->I.convertFocusToChild) |> Assert.equal(true)
  });
});

describe("removeDeepChildren2", () => {
  let path1 = P.fromList(["1", "2", "3"]);
  let path2 = P.fromList(["1", "2", "3", "4"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    T.empty()
    ->T.addChild(path1, id1)
    ->T.addChild(path1, id2)
    ->T.addChild(path2, id3);
  let t1 = t->T.removeChild(path1, CID.create("child2"));
  let t2 =
    t1
    ->T.children
    ->Map.getExn(CID.create("3"))
    ->T.children
    ->Map.getExn(CID.create("2"))
    ->T.children
    ->Map.getExn(CID.create("1"));

  it("oneChildRemoved", () => {
    t2->T.children->Map.size |> Assert.equal(1)
  });

  it("child1IsStillInChildrenCollection", () => {
    t2->T.children->Map.has(CID.create("child1")) |> Assert.equal(true)
  });

  it("child2IsNotInChildrenCollection", () => {
    t2->T.children->Map.has(CID.create("child2")) |> Assert.equal(false)
  });

  let t3 =
    t1
    ->T.children
    ->Map.getExn(CID.create("4"))
    ->T.children
    ->Map.getExn(CID.create("3"))
    ->T.children
    ->Map.getExn(CID.create("2"))
    ->T.children
    ->Map.getExn(CID.create("1"));

  it("oneChildRemoved", () => {
    t3->T.children->Map.size |> Assert.equal(1)
  });

  it("child1IsStillInChildrenCollection", () => {
    t3->T.children->Map.has(CID.create("child3")) |> Assert.equal(true)
  });
});

describe("removeNonExistantChildren", () => {
  let path1 = P.fromList(["1", "2", "3"]);
  let path2 = P.fromList(["1", "3", "4"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let t = T.empty()->T.addChild(path1, id1)->T.addChild(path1, id2);

  let t1 = t->T.removeChild(path1, CID.create("child3"));
  let t2 =
    t1
    ->T.children
    ->Map.getExn(CID.create("3"))
    ->T.children
    ->Map.getExn(CID.create("2"))
    ->T.children
    ->Map.getExn(CID.create("1"));

  it("noChildRemoved", () => {
    t2->T.children->Map.size |> Assert.equal(2)
  });

  let t1 = t->T.removeChild(path2, CID.create("child1"));
  let t2 =
    t1
    ->T.children
    ->Map.getExn(CID.create("3"))
    ->T.children
    ->Map.getExn(CID.create("2"))
    ->T.children
    ->Map.getExn(CID.create("1"));

  it("noChildRemoved", () => {
    t2->T.children->Map.size |> Assert.equal(2)
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
    T.empty()
    ->T.addChild(path1, id1)
    ->T.addChild(path2, id2)
    ->T.addChild(path3, id3);

  let t2 = t->T.removeChild(P.fromList(["2"]), CID.create("1"));
  let t3 = t2->T.children->Map.getExn(CID.create("2"));
  it("abMovedUp", () => {
    %log.debug
    t2->T.children->Map.getExn(CID.create("2"))->T.toString;
    t3->T.children->Map.size |> Assert.equal(3);
  });

  let check = s => {
    t3->T.children->Map.has(CID.create(s)) |> Assert.equal(true);
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
    t3
    ->T.children
    ->Map.getExn(CID.create(p))
    ->T.children
    ->Map.has(CID.create(c))
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
