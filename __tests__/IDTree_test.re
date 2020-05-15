open BsMocha.Mocha;
module Assert = BsMocha.Assert;

open Test_utils;

describe("canMakeEmpty", () => {
  let p = M.empty();

  it("hasNoChildren", () => {
    p->M.children->Map.size |> Assert.equal(0)
  });

  it("emptyIsRootId", () => {
    p->M.myId === ID.create("root") |> Assert.equal(true)
  });

  it("emptyIsRootFlag", () => {
    p->M.isRoot |> Assert.equal(true)
  });

  it("emptyIsRoot", () => {
    p->M.rootId->Option.getExn == ID.create("root") |> Assert.equal(true)
  });
});

describe("addImmediateChildren", () => {
  let t = M.empty();
  let path = P.fromList([]);
  let id = ID.create("child1");
  let t2 = t->M.addChild(path, id);

  it("oneChildAdded", () => {
    t2->M.children->Map.size |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    t2->M.children->Map.has(CID.create("child1")) |> Assert.equal(true)
  });

  it("childIsNotRoot", () => {
    let child1: M.t = t2->M.children->Map.getExn(CID.create("child1"));
    child1->M.isRoot |> Assert.equal(false);
  });

  let id = ID.create("child2");
  let t3 = t2->M.addChild(path, id);
  it("secondChildIsAdded", () => {
    t3->M.children->Map.size |> Assert.equal(2)
  });

  it("secondChildIsInChildrenCollection", () => {
    t3->M.children->Map.has(id->I.convertFocusToChild) |> Assert.equal(true)
  });

  it("secondChildIsNotRoot", () => {
    let child2: M.t = t3->M.children->Map.getExn(id->I.convertFocusToChild);
    child2->M.isRoot |> Assert.equal(false);
  });
});

describe("addLowDownChildren", () => {
  let t = M.empty();
  let path = P.fromList(["1", "2", "3"]);
  let id = ID.create("child1");
  let t2 = t->M.addChild(path, id);

  let t3 =
    t2
    ->M.children
    ->Map.getExn(CID.create("3"))
    ->M.children
    ->Map.getExn(CID.create("2"))
    ->M.children
    ->Map.getExn(CID.create("1"));

  it("oneChildAdded", () => {
    t3->M.children->Map.size |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    t3->M.children->Map.has(CID.create("child1")) |> Assert.equal(true)
  });

  it("childIsNotRoot", () => {
    let child1: M.t = t3->M.children->Map.getExn(id->I.convertFocusToChild);
    child1->M.isRoot |> Assert.equal(false);
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
    t5->M.children->Map.size |> Assert.equal(2)
  });

  it("secondChildIsInChildrenCollection", () => {
    t5->M.children->Map.has(CID.create("child2")) |> Assert.equal(true)
  });

  it("secondChildIsNotRoot", () => {
    let child2: M.t = t5->M.children->Map.getExn(id2->I.convertFocusToChild);
    child2->M.isRoot |> Assert.equal(false);
  });
});

describe("addInnerChild", () => {
  let t = StandardTree.t;
  let path4 = P.fromRootToPathList(["2", "d"]);
  let t2 = t->M.addChild(path4, ID.create("child4"));
  let t3 = t2->M.children->Map.getExn(CID.create("2"));

  it("dIsChild", () => {
    t3->M.children->Map.has(CID.create("d")) |> Assert.equal(true)
  });

  let check2 = (p, c) => {
    t3
    ->M.children
    ->Map.getExn(CID.create(p))
    ->M.children
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
  let t = M.empty()->M.addChild(path, id);
  let t1 = t->M.removeChild(path, CID.create("child1"));

  it("oneChildRemoved", () => {
    t1->M.children->Map.size |> Assert.equal(0)
  });

  it("childIsNotInChildrenCollection", () => {
    t1->M.children->Map.has(CID.create("child1")) |> Assert.equal(false)
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
    t2->M.children->Map.size |> Assert.equal(1)
  });

  it("child1IsNotInChildrenCollection", () => {
    t2->M.children->Map.has(id1->I.convertFocusToChild)
    |> Assert.equal(false)
  });

  it("child2IsStillInChildrenCollection", () => {
    t2->M.children->Map.has(id2->I.convertFocusToChild) |> Assert.equal(true)
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
    t2->M.children->Map.size |> Assert.equal(1)
  });

  it("child1IsStillInChildrenCollection", () => {
    t2->M.children->Map.has(CID.create("child1")) |> Assert.equal(true)
  });

  it("child2IsNotInChildrenCollection", () => {
    t2->M.children->Map.has(CID.create("child2")) |> Assert.equal(false)
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
    t3->M.children->Map.size |> Assert.equal(1)
  });

  it("child1IsStillInChildrenCollection", () => {
    t3->M.children->Map.has(CID.create("child3")) |> Assert.equal(true)
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
    t2->M.children->Map.size |> Assert.equal(2)
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
    t2->M.children->Map.size |> Assert.equal(2)
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
    t3->M.children->Map.size |> Assert.equal(3);
  });

  let check = s => {
    t3->M.children->Map.has(CID.create(s)) |> Assert.equal(true);
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
    ->M.children
    ->Map.getExn(CID.create(p))
    ->M.children
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
