open Test_utils;

describe("subtrees", () => {
  let t = StandardTree.t;
  let t1 =
    t
    ->T.getSubtree(StandardTree.path1->P.moveUp, ID.create("a"))
    ->Option.getExn;
  it("gotSubtree", () => {
    t1->T.myId == ID.create("a") |> Assert.equal(true)
  });

  it("gotSubtreeIds", () => {
    [%log.debug "t1 subtree:" ++ t1->T.toString; ("", "")];
    let cids = t1->T.getAllIds;
    cids->Array.size |> Assert.equal(2);
  });

  it("gotOneChildInSubtree", () => {
    t1->T.children->Map.size |> Assert.equal(1)
  });

  it("gotChildInSubtree", () => {
    t1->T.children->Map.has(CID.create("child1")) |> Assert.equal(true)
  });

  let t1 =
    t
    ->T.getSubtree(StandardTree.path1->P.moveUp->P.moveUp, ID.create("1"))
    ->Option.getExn;
  /* | . 1:{ me: 1, #children: 2, isRoot: false} */
  /* | . . . b:{ me: b, #children: 1, isRoot: false} */
  /* | . . . . . child2:{ me: child2, #children: 0, isRoot: false} */
  /* | . . . a:{ me: a, #children: 1, isRoot: false} */
  /* | . . . . . child1:{ me: child1, #children: 0, isRoot: false} */
  it("gotSubtree2", () => {
    t1->T.myId == ID.create("1") |> Assert.equal(true)
  });

  it("gotTwoChildInSubtree", () => {
    t1->T.children->Map.size |> Assert.equal(2)
  });

  it("gotChildInSubtree1", () => {
    t1->T.children->Map.has(CID.create("a")) |> Assert.equal(true)
  });
  it("gotChildInSubtree2", () => {
    t1->T.children->Map.has(CID.create("b")) |> Assert.equal(true)
  });

  it("is not rooted yet", () => {
    t1->T.isRoot |> Assert.equal(false)
  });

  let t2 = t1->T.makeIntoRootedSubtree;
  /* { me: root, #children: 1, isRoot: true} */
  /* | . 1:{ me: 1, #children: 2, isRoot: false} */
  /* | . . . b:{ me: b, #children: 1, isRoot: false} */
  /* | . . . . . child2:{ me: child2, #children: 0, isRoot: false} */
  /* | . . . a:{ me: a, #children: 1, isRoot: false} */
  /* | . . . . . child1:{ me: child1, #children: 0, isRoot: false} */
  it("can make rooted subtree", () => {
    [%log.debug t2->T.toString; ("", "")];
    t2->T.isRoot |> Assert.equal(true);
  });
  it("gotSubtree3", () => {
    t2->T.myId == ID.create("root") |> Assert.equal(true)
  });

  it("gotOntChildInSubtree now", () => {
    t2->T.children->Map.size |> Assert.equal(1)
  });

  it("gotChildInSubtree2", () => {
    t2->T.children->Map.has(CID.create("1")) |> Assert.equal(true)
  });

  it("original is rooted", () => {
    t->T.isRoot |> Assert.ok
  });

  it("original can be made rooted but is noop", () => {
    t->T.makeIntoRootedSubtree->T.eq(t)->Assert.ok
  });
});

describe("addSubtree", () => {
  let t = StandardTree.t;
  let t2 = StandardTree.t2;

  [%log.debug "t2: " ++ t2->T.toString; ("", "")];

  let t3 = t->T.addSubtree(ID.create("test"), StandardTree.path3, t2);
  [%log.debug "t3: " ++ t3->T.toString; ("", "")];
  let t4 =
    t3
    ->T.getSubtree(P.fromRootToPathList(["2", "c"]), ID.create("test"))
    ->Option.getExn;
  it("notAddedNewRootNode", () => {
    t4->T.isRoot |> Assert.equal(false)
  });
  it("hasAddedNodeWithCorrectId", () => {
    t4->T.myId == ID.create("test") |> Assert.equal(true)
  });
  let _get = (p1, p2) => {
    t4
    ->T.children
    ->Map.getExn(CID.create(p1))
    ->T.children
    ->Map.getExn(CID.create(p2))
    ->T.children;
  };

  it("3aHasTwoChildren", () => {
    _get("3", "a")->Map.size |> Assert.equal(2)
  });

  it("3aHasChild4", () => {
    _get("3", "a")->Map.has(CID.create("child4")) |> Assert.equal(true)
  });

  it("3aHasChild5", () => {
    _get("3", "a")->Map.has(CID.create("child5")) |> Assert.equal(true)
  });

  it("3bHasOneChild", () => {
    _get("3", "b")->Map.size |> Assert.equal(1)
  });

  it("3bHasChild6", () => {
    _get("3", "b")->Map.has(CID.create("child6")) |> Assert.equal(true)
  });
});

describe("removeSubtree", () => {
  let t = StandardTree.t;

  let t1 =
    t->T.removeSubtree(
      StandardTree.path1->P.moveUp->P.moveUp,
      CID.create("1"),
    );
  let t2 = t1->T.children->Map.getExn(CID.create("2"));
  it("oneSubtreeRemoved", () => {
    t2->T.children->Map.size |> Assert.equal(1)
  });

  it("subtreeIsNotInChildrenCollection", () => {
    t2->T.children->Map.has(ID.create("1")->I.convertFocusToChild)
    |> Assert.equal(false)
  });

  it("subtree2IsStillInChildrenCollection", () => {
    t2->T.children->Map.has(ID.create("c")->I.convertFocusToChild)
    |> Assert.equal(true)
  });
});
