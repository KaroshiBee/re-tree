open Test_utils;
let _ = (); //weird bug in reason-mode reason-paren-level

describe("canMakeEmpty", () => {
  let g = GF.empty();

  it("has no lookup", () => {
    g->GF.size |> Assert.equal(0)
  });

  it("hasNoTree", () => {
    g->GF.hasChildren |> Assert.equal(false)
  });

  it("containsNothing", () => {
    g->GF.containsId(ID.create("asd")) |> Assert.equal(false)
  });

  it("hasZeroDepth", () => {
    g->GF.maxDepth |> Assert.equal(0)
  });
});

describe("addImmediateChildren", () => {
  let g = GF.empty()->GF.addNode(ID.create("1"), {one: 4, two: "four"});

  it("oneChildAdded", () => {
    g->GF.size |> Assert.equal(1)
  });

  it("childIsInChildrenCollection", () => {
    g->GF.containsId(ID.create("1")) |> Assert.equal(true)
  });

  it("hasDepthZero", () => {
    g->GF.maxDepth |> Assert.equal(0)
  });

  let data = g->GF.dataForNode(ID.create("1"))->Option.getExn;
  it("masterLookupHasCorrectData", () => {
    data.one |> Assert.equal(4)
  });
  it("masterLookupHasCorrectData2", () => {
    data.two |> Assert.equal("four")
  });

  let path = g->GF.pathFromNode(ID.create("1"))->Option.getExn;
  it("masterLookupHasPathUp", () => {
    path->P.eq(P.fromList([])) |> Assert.equal(true)
  });

  let g1 = g->GF.addNode(ID.create("2"), {one: 8, two: "eight"});
  it("twoChildAdded", () => {
    g1->GF.size |> Assert.equal(2)
  });

  it("childIsInChildrenCollection", () => {
    g1->GF.containsId(ID.create("2")) |> Assert.equal(true)
  });

  it("childIsInMasterLookup", () => {
    g1->GF.containsId(ID.create("2")) |> Assert.equal(true)
  });
});

describe("addParentChild", () => {
  let id = ID.create("1");
  let g =
    GF.empty()
    ->GF.addNode(id, {one: 4, two: "four"})
    ->GF.addNodeUnder(
        ID.create("2"),
        {one: 2, two: "two"},
        PID.create("1"),
      )
    ->GF.addNodeUnder(
        ID.create("3"),
        {one: 1, two: "one"},
        PID.create("2"),
      );

  it("hasDepthTwo", () => {
    g->GF.maxDepth |> Assert.equal(2)
  });

  it("childAdded2", () => {
    g->GF.containsId(ID.create("2")) |> Assert.equal(true)
  });

  it("childAdded3", () => {
    g->GF.containsId(ID.create("3")) |> Assert.equal(true)
  });

  let data = g->GF.dataForNode(ID.create("2"))->Option.getExn;
  it("masterLookupHasCorrectData", () => {
    data.one |> Assert.equal(2)
  });

  it("masterLookupHasCorrectData2", () => {
    data.two |> Assert.equal("two")
  });

  let data = g->GF.dataForNode(ID.create("3"))->Option.getExn;
  it("masterLookupHasCorrectData3", () => {
    data.one |> Assert.equal(1)
  });

  it("masterLookupHasCorrectData4", () => {
    data.two |> Assert.equal("one")
  });

  let path = g->GF.pathFromNode(ID.create("2"))->Option.getExn;
  it("masterLookupHasPathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g->GF.pathFromNode(ID.create("3"))->Option.getExn;
  it("masterLookupHasPathUp", () => {
    path->P.eq(P.fromList(["2", "1"])) |> Assert.equal(true)
  });

  let t = g->GF.subGraphForNode(ID.create("2"))->Option.getExn;
  [%log.debug "original: " ++ g->GF.toString; ("", "")];
  [%log.debug "subgraph: " ++ t->GF.toString; ("", "")];
  it("subtreeHasChild", () => {
    t->GF.size |> Assert.equal(2)
  });
  it("subtreeHasChild1", () => {
    t->GF.containsId(ID.create("3")) |> Assert.equal(true)
  });
});

describe("moveChild", () => {
  let g = FancyGraph.makeGraph();
  let _test = (g, s) => {
    it("_test", () => {
      g->GF.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let path = g->GF.pathFromNode(FancyGraph.id4)->Option.getExn;
  it("4PathUp", () => {
    path->P.eq(P.fromList(["3", "1"])) |> Assert.equal(true)
  });
  let path = g->GF.pathFromNode(FancyGraph.id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g->GF.pathFromNode(FancyGraph.id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });

  let g1 =
    g->GF.moveChild(
      FancyGraph.id3->I.convertFocusToChild,
      FancyGraph.id2->I.convertFocusToParent,
    );

  it("notErrored", () => {
    g1->Result.isOk |> Assert.equal(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1");
  _test(g1, "2");
  _test(g1, "3");
  _test(g1, "4");
  let path = g1->GF.pathFromNode(FancyGraph.id4)->Option.getExn;
  it("4PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g1->GF.pathFromNode(FancyGraph.id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["2", "1"])) |> Assert.equal(true)
  });
  let path = g->GF.pathFromNode(FancyGraph.id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
});

describe("removeSubtree", () => {
  let g = FancyGraph.makeGraph();

  let _test = (g, s, e) => {
    it("_test", () => {
      g->GF.containsId(ID.create(s)) |> Assert.equal(e)
    });
  };
  _test(g, "1", true);
  _test(g, "2", true);
  _test(g, "3", true);
  _test(g, "4", true);

  %log.debug
  g->GF.pathFromNode(FancyGraph.id3)->Option.getExn->P.toString;
  let g1 = g->GF.removeSubtree(FancyGraph.id3);
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
  let g = FancyGraph.makeGraph();

  let _test = (g, s) => {
    it("_test", () => {
      g->GF.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let path = g->GF.pathFromNode(FancyGraph.id4)->Option.getExn;
  it("4PathUp", () => {
    path->P.eq(P.fromList(["3", "1"])) |> Assert.equal(true)
  });
  let path = g->GF.pathFromNode(FancyGraph.id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
  let path = g->GF.pathFromNode(FancyGraph.id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });

  let g1 =
    g->GF.moveSubtree(
      FancyGraph.id3->I.convertFocusToChild,
      FancyGraph.id2->I.convertFocusToParent,
    );

  it("notErrored", () => {
    g1->Result.isOk |> Assert.equal(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1");
  _test(g1, "2");
  _test(g1, "3");
  _test(g1, "4");
  let path = g1->GF.pathFromNode(FancyGraph.id4)->Option.getExn;
  it("4PathUp_", () => {
    path->P.eq(P.fromList(["3", "2", "1"])) |> Assert.equal(true)
  });
  let path = g1->GF.pathFromNode(FancyGraph.id3)->Option.getExn;
  it("3PathUp_", () => {
    path->P.eq(P.fromList(["2", "1"])) |> Assert.equal(true)
  });
  let path = g->GF.pathFromNode(FancyGraph.id2)->Option.getExn;
  it("2PathUp_", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
});

/* describe("mapping", () => { */
/*   let g = FancyGraph.makeGraph(); */

/*   let g1 = g->GF.map(d => d.one->string_of_int ++ ":" ++ d.two); */

/*   let _test = (s, ss) => { */
/*     let data = g1->GF.dataForNode(ID.create(s))->Option.getExn; */
/*     it("hasCorrectData1", () => { */
/*       data |> Assert.equal(ss) */
/*     }); */
/*   }; */

/*   _test("1", "1:one"); */
/*   _test("2", "2:two"); */
/*   _test("3", "3:three"); */
/*   _test("4", "4:four"); */
/* }); */

describe("foreach", () => {
  let g = FancyGraph.makeGraph();

  let i = ref(0);

  let _ = g->GF.forEach((_id, _d) => {incr(i)});

  it("inc", () => {
    i^ |> Assert.equal(4)
  });
});

describe("keep", () => {
  let g = FancyGraph.makeGraph();
  let g1 = g->GF.keep((id, d) => d.one < 2 || id == FancyGraph.id3);

  let _test = (g, s, e) => {
    it("_test", () => {
      g->GF.containsId(ID.create(s)) |> Assert.equal(e)
    });
  };
  _test(g1, "1", true);
  _test(g1, "2", false);
  _test(g1, "3", true);
  _test(g1, "4", false);
  let path = g1->GF.pathFromNode(FancyGraph.id3)->Option.getExn;
  it("3PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });

  let g2 = g->GF.keep((id, d) => d.one <= 2 || id == FancyGraph.id4);
  // this should remove 4 because it is no longer reachable
  _test(g2, "1", true);
  _test(g2, "2", true);
  _test(g2, "3", false);
  _test(g2, "4", false);

  let g3 = g->GF.keep((_id, d) => d.one < 4);
  _test(g3, "1", true);
  _test(g3, "2", true);
  _test(g3, "3", true);
  _test(g3, "4", false);
  let path = g3->GF.pathFromNode(FancyGraph.id2)->Option.getExn;
  it("2PathUp", () => {
    path->P.eq(P.fromList(["1"])) |> Assert.equal(true)
  });
});

describe("setSubGraphForNode-should-set-subgraph", () => {
  let g = FancyGraph.makeGraph();
  let _test = (g, s) => {
    it("_test", () => {
      g->GF.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let id5 = ID.create("5");
  let id6 = ID.create("6");
  let gChild =
    GF.empty()
    ->GF.addNode(FancyGraph.id2, {one: 22222, two: "ASdasdasda"})
    ->GF.addNodeUnder(
        id5,
        {one: 5, two: "five"},
        FancyGraph.id2->I.convertFocusToParent,
      )
    ->GF.addNodeUnder(
        id6,
        {one: 6, two: "six"},
        FancyGraph.id2->I.convertFocusToParent,
      );
  _test(gChild, "5");
  _test(gChild, "6");
  [%log.debug "about to set new subgraph"; ("", "")];
  switch (
    g->GF.setSubGraphForNode(FancyGraph.id2->I.convertFocusToParent, gChild)
  ) {
  | Ok(g1) =>
    _test(g1, "5");
    _test(g1, "6");
  | Error(_) => it("fail", () => {
                  true |> Assert.equal(false)
                })
  };
});

describe("setSubGraphForNode-should-set-subgraph that has been extracted", () => {
  let g = FancyGraph.makeGraph();
  let _test = (g, s) => {
    it("_test", () => {
      g->GF.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  [%log.debug "get subgraph"; ("", "")];
  let gChild = g->GF.subGraphForNode(FancyGraph.id3)->Option.getExn;
  [%log.debug "about to set new subgraph"; ("", "")];
  switch (
    g->GF.setSubGraphForNode(FancyGraph.id3->I.convertFocusToParent, gChild)
  ) {
  | Ok(g1) => it("ok", () => {
                g->GF.eq(g1) |> Assert.equal(true)
              })
  | Error(_) => it("fail", () => {
                  true |> Assert.equal(false)
                })
  };
});

describe(
  "setSubGraphForRoot-should on extracted subgraph and new empty graph", () => {
  let g = FancyGraph.makeGraph();
  let _test = (g, s) => {
    it("_test", () => {
      g->GF.containsId(ID.create(s)) |> Assert.equal(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  [%log.debug "get subgraph"; ("", "")];
  let gChild = g->GF.subGraphForNode(FancyGraph.id3)->Option.getExn;
  [%log.debug "RAAAA got subgraph: " ++ gChild->GF.toString; ("", "")];
  [%log.debug "about to set new subgraph"; ("", "")];
  let pth = P.fromPathToRootList(["1"])->Some;
  switch (GF.empty()->GF.setSubGraphForRoot(gChild->GF.trimPaths(pth))) {
  | Ok(g1) =>
    it("ok", () => {
      gChild->GF.eq(g1)
      |> Assert.equal(false) // different paths
    })
  | Error(_) => it("fail", () => {
                  true |> Assert.equal(false)
                })
  };
});

describe("updteChildren-should-update-only-children", () => {
  let _test = (g, n, vl) => {
    let data = g->GF.dataForNode(ID.create(n))->Option.getExn;
    it("masterLookupHasCorrectData", () => {
      data.one |> Assert.equal(vl)
    });
  };

  let g = FancyGraph.makeGraph();
  _test(g, "1", 1);
  _test(g, "2", 2);
  _test(g, "3", 3);
  _test(g, "4", 4);

  let g1 = g->GF.updateChildren(ID.create("1"), d => {...d, one: 200});

  _test(g1, "1", 1);
  _test(g1, "2", 200);
  _test(g1, "3", 200);
  _test(g1, "4", 4);

  let g2 =
    g->GF.updateChildren(ID.create("not_there"), d => {...d, one: 200});

  _test(g2, "1", 1);
  _test(g2, "2", 2);
  _test(g2, "3", 3);
  _test(g2, "4", 4);

  let g3 = g->GF.updateChildren(ID.create("3"), d => {...d, one: 200});

  _test(g3, "1", 1);
  _test(g3, "2", 2);
  _test(g3, "3", 3);
  _test(g3, "4", 200);
});
