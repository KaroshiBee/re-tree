open Test_utils;

type data = {
  one: int,
  two: string,
};

let id1 = ID.create("1");
let id2 = ID.create("2");
let id3 = ID.create("3");
let id4 = ID.create("4");

let makeGraph = () => {
  G.empty()
  ->G.addNode(id1, {one: 1, two: "one"})
  ->G.addNodeUnder(
      id2,
      {one: 2, two: "two"},
      id1->Identity.convertFocusToParent,
    )
  ->G.addNodeUnder(
      id3,
      {one: 3, two: "three"},
      id1->Identity.convertFocusToParent,
    )
  ->G.addNodeUnder(
      id4,
      {one: 4, two: "four"},
      id3->Identity.convertFocusToParent,
    );
};

describe("canMakeEmpty", () => {
  let g = G.empty();

  it("has no lookup", () => {
    g->G.size |> Assert.equal(0)
  });

  it("hasNoTree", () => {
    g->G.hasChildren |> Assert.equal(false)
  });

  it("containsNothing", () => {
    g->G.containsId(ID.create("asd")) |> Assert.equal(false)
  });

  it("hasZeroDepth", () => {
    g->G.maxDepth |> Assert.equal(0)
  });
});

describe("addImmediateChildren", () => {
  let g = G.empty()->G.addNode(ID.create("1"), {one: 4, two: "four"});

  it("oneChildAdded", () => {
    g->G.size |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    g->G.containsId(ID.create("1")) |> Assert.equal(true)
  });

  it("hasDepthZero", () => {
    g->G.maxDepth |> Assert.equal(0)
  });

  let data = g->G.dataForNode(ID.create("1"))->Option.getExn;
  it("masterLookupHasCorrectData", () => {
    data.one |> Assert.equal(4)
  });
  it("masterLookupHasCorrectData2", () => {
    data.two |> Assert.equal("four")
  });

  let path = g->G.pathFromNode(ID.create("1"))->Option.getExn;
  it("masterLookupHasPathUp", () => {
    path->P.eq(P.fromList([])) |> Assert.equal(true)
  });

  let g1 = g->G.addNode(ID.create("2"), {one: 8, two: "eight"});
  it("twoChildAdded", () => {
    g1->G.size |> Assert.equal(2)
  });

  it("childIsInChildrenCollection", () => {
    g1->G.containsId(ID.create("2")) |> Assert.equal(true)
  });

  it("childIsInMasterLookup", () => {
    g1->G.containsId(ID.create("2")) |> Assert.equal(true)
  });
});

describe("addParentChild", () => {
  let id = ID.create("1");
  let g =
    G.empty()
    ->G.addNode(id, {one: 4, two: "four"})
    ->G.addNodeUnder(ID.create("2"), {one: 2, two: "two"}, PID.create("1"))
    ->G.addNodeUnder(
        ID.create("3"),
        {one: 1, two: "one"},
        PID.create("2"),
      );

  it("hasDepthTwo", () => {
    g->G.maxDepth |> Assert.equal(2)
  });

  it("childAdded2", () => {
    g->G.containsId(ID.create("2")) |> Assert.equal(true)
  });

  it("childAdded3", () => {
    g->G.containsId(ID.create("3")) |> Assert.equal(true)
  });

  let data = g->G.dataForNode(ID.create("2"))->Option.getExn;
  it("masterLookupHasCorrectData", () => {
    data.one |> Assert.equal(2)
  });

  it("masterLookupHasCorrectData2", () => {
    data.two |> Assert.equal("two")
  });

  let data = g->G.dataForNode(ID.create("3"))->Option.getExn;
  it("masterLookupHasCorrectData3", () => {
    data.one |> Assert.equal(1)
  });

  it("masterLookupHasCorrectData4", () => {
    data.two |> Assert.equal("one")
  });

  let path = g->G.pathFromNode(ID.create("2"))->Option.getExn;
  it("masterLookupHasPathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g->G.pathFromNode(ID.create("3"))->Option.getExn;
  it("masterLookupHasPathUp", () => {
    path->P.eq(P.fromList(["2", "1"])) |> Assert.equal(true)
  });

  let t = g->G.subGraphForNode(ID.create("2"))->Option.getExn;
  [%log.debug "original: " ++ g->G.toString(d => d.two); ("", "")];
  [%log.debug "subgraph: " ++ t->G.toString(d => d.two); ("", "")];
  it("subtreeHasChild", () => {
    t->G.size |> Assert.equal(2)
  });
  it("subtreeHasChild1", () => {
    t->G.containsId(ID.create("3")) |> Assert.equal(true)
  });
});

describe("moveChild", () => {
  let g = makeGraph();
  let _test = (g, s) => {
    it("_test", () => {
      g->G.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let path = g->G.pathFromNode(id4)->Option.getExn;
  it("4PathUp", () => {
    path->P.eq(P.fromList(["3", "1"])) |> Assert.equal(true)
  });
  let path = g->G.pathFromNode(id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g->G.pathFromNode(id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });

  let g1 =
    g->G.moveChild(id3->I.convertFocusToChild, id2->I.convertFocusToParent);

  it("notErrored", () => {
    g1->Result.isOk |> Assert.equal(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1");
  _test(g1, "2");
  _test(g1, "3");
  _test(g1, "4");
  let path = g1->G.pathFromNode(id4)->Option.getExn;
  it("4PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g1->G.pathFromNode(id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["2", "1"])) |> Assert.equal(true)
  });
  let path = g->G.pathFromNode(id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
});

describe("removeSubtree", () => {
  let g = makeGraph();

  let _test = (g, s, e) => {
    it("_test", () => {
      g->G.containsId(ID.create(s)) |> Assert.equal(e)
    });
  };
  _test(g, "1", true);
  _test(g, "2", true);
  _test(g, "3", true);
  _test(g, "4", true);

  %log.debug
  g->G.pathFromNode(id3)->Option.getExn->P.toString;
  let g1 = g->G.removeSubtree(id3);
  it("notErrored", () => {
    g1->Result.isOk |> Assert.equal(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1", true);
  _test(g1, "2", true);
  _test(g1, "3", false);
  _test(g1, "4", false);
});

describe("moveSubtree", () => {
  let g = makeGraph();

  let _test = (g, s) => {
    it("_test", () => {
      g->G.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let path = g->G.pathFromNode(id4)->Option.getExn;
  it("4PathUp", () => {
    path->P.eq(P.fromList(["3", "1"])) |> Assert.equal(true)
  });
  let path = g->G.pathFromNode(id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g->G.pathFromNode(id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });

  let g1 =
    g->G.moveSubtree(id3->I.convertFocusToChild, id2->I.convertFocusToParent);

  it("notErrored", () => {
    g1->Result.isOk |> Assert.equal(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1");
  _test(g1, "2");
  _test(g1, "3");
  _test(g1, "4");
  let path = g1->G.pathFromNode(id4)->Option.getExn;
  it("4PathUp_", () => {
    path->P.eq(P.fromList(["3", "2", "1"])) |> Assert.equal(true)
  });
  let path = g1->G.pathFromNode(id3)->Option.getExn;
  it("3PathUp_", () => {
    path->P.eq(P.fromList(["2", "1"])) |> Assert.equal(true)
  });
  let path = g->G.pathFromNode(id2)->Option.getExn;
  it("2PathUp_", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
});

describe("mapping", () => {
  let g = makeGraph();

  let g1 = g->G.map(d => d.one->string_of_int ++ ":" ++ d.two);

  let _test = (s, ss) => {
    let data = g1->G.dataForNode(ID.create(s))->Option.getExn;
    it("hasCorrectData1", () => {
      data |> Assert.equal(ss)
    });
  };

  _test("1", "1:one");
  _test("2", "2:two");
  _test("3", "3:three");
  _test("4", "4:four");
});

describe("foreach", () => {
  let g = makeGraph();

  let i = ref(0);

  let _ = g->G.forEach((_id, _d) => {incr(i)});

  it("inc", () => {
    i^ |> Assert.equal(4)
  });
});

describe("keep", () => {
  let g = makeGraph();
  let g1 = g->G.keep((id, d) => d.one < 2 || id == id3);

  let _test = (g, s, e) => {
    it("_test", () => {
      g->G.containsId(ID.create(s)) |> Assert.equal(e)
    });
  };
  _test(g1, "1", true);
  _test(g1, "2", false);
  _test(g1, "3", true);
  _test(g1, "4", false);
  let path = g1->G.pathFromNode(id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });

  let g2 = g->G.keep((id, d) => d.one <= 2 || id == id4);
  // this should remove 4 because it is no longer reachable
  _test(g2, "1", true);
  _test(g2, "2", true);
  _test(g2, "3", false);
  _test(g2, "4", false);

  let g3 = g->G.keep((_id, d) => d.one < 4);
  _test(g3, "1", true);
  _test(g3, "2", true);
  _test(g3, "3", true);
  _test(g3, "4", false);
  let path = g3->G.pathFromNode(id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
});

describe("setSubGraphForNode-should-set-subgraph", () => {
  let g = makeGraph();
  let _test = (g, s) => {
    it("_test", () => {
      g->G.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let id5 = ID.create("5");
  let id6 = ID.create("6");
  let gChild =
    G.empty()
    ->G.addNode(id2, {one: 22222, two: "ASdasdasda"})
    ->G.addNodeUnder(id5, {one: 5, two: "five"}, id2->I.convertFocusToParent)
    ->G.addNodeUnder(id6, {one: 6, two: "six"}, id2->I.convertFocusToParent);
  _test(gChild, "5");
  _test(gChild, "6");
  [%log.debug "about to set new subgraph"; ("", "")];
  switch (g->G.setSubGraphForNode(id2->I.convertFocusToParent, gChild)) {
  | Ok(g1) =>
    _test(g1, "5");
    _test(g1, "6");
  | Error(_) => it("fail", () => {
                  true |> Assert.equal(false)
                })
  };
});

describe("updteChildren-should-update-only-children", () => {
  let _test = (g, n, vl) => {
    let data = g->G.dataForNode(ID.create(n))->Option.getExn;
    it("masterLookupHasCorrectData", () => {
      data.one |> Assert.equal(vl)
    });
  };

  let g = makeGraph();
  _test(g, "1", 1);
  _test(g, "2", 2);
  _test(g, "3", 3);
  _test(g, "4", 4);

  let g1 = g->G.updateChildren(ID.create("1"), d => {...d, one: 200});

  _test(g1, "1", 1);
  _test(g1, "2", 200);
  _test(g1, "3", 200);
  _test(g1, "4", 4);

  let g2 =
    g->G.updateChildren(ID.create("not_there"), d => {...d, one: 200});

  _test(g2, "1", 1);
  _test(g2, "2", 2);
  _test(g2, "3", 3);
  _test(g2, "4", 4);

  let g3 = g->G.updateChildren(ID.create("3"), d => {...d, one: 200});

  _test(g3, "1", 1);
  _test(g3, "2", 2);
  _test(g3, "3", 3);
  _test(g3, "4", 200);
});
