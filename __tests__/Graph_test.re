open Jest;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

module Data = {
type t = {
  one: int,
  two: string,
};
let toString = t => {
  "{ one: " ++ t.one->string_of_int ++ ", two: " ++ t.two ++ " }";
}
}

module M = Graph.Make(Data);

let id1 = ID.create("1");
let id2 = ID.create("2");
let id3 = ID.create("3");
let id4 = ID.create("4");

let makeGraph = () => {
  M.empty()
  ->M.addNode(id1, {one: 1, two: "one"})
  ->M.addNodeUnder(
      id2,
      {one: 2, two: "two"},
      id1->Identity.convertFocusToParent,
    )
  ->M.addNodeUnder(
      id3,
      {one: 3, two: "three"},
      id1->Identity.convertFocusToParent,
    )
  ->M.addNodeUnder(
      id4,
      {one: 4, two: "four"},
      id3->Identity.convertFocusToParent,
    );
};

describe("canMakeEmpty", () => {
  open Expect;
  // open! Expect.Operators;
  let g = M.empty();

  test("hasNoLookup", () => {
    expect(g->M.size) |> toBe(0)
  });

  test("hasNoTree", () => {
    expect(g->M.hasChildren) |> toBe(false)
  });

  test("containsNothing", () => {
    expect(g->M.containsId(ID.create("asd"))) |> toBe(false)
  });
});

describe("addImmediateChildren", () => {
  open Expect;

  let g = M.empty()->M.addNode(ID.create("1"), {one: 4, two: "four"});

  test("oneChildAdded", () => {
    expect(g->M.size) |> toBe(1)
  });

  test("childIsInChildrenCollection", () => {
    expect(g->M.containsId(ID.create("1"))) |> toBe(true)
  });

  test("childIsInMasterLookup", () => {
    expect(g->M.containsId(ID.create("1"))) |> toBe(true)
  });

  let data = g->M.dataForNode(ID.create("1"))->Option.getExn;
  test("masterLookupHasCorrectData", () => {
    expect(data.one) |> toBe(4)
  });
  test("masterLookupHasCorrectData2", () => {
    expect(data.two) |> toBe("four")
  });

  let path = g->M.pathFromNode(ID.create("1"))->Option.getExn;
  test("masterLookupHasPathUp", () => {
    expect(path->P.eq(P.fromList([]))) |> toBe(true)
  });

  let g1 = g->M.addNode(ID.create("2"), {one: 8, two: "eight"});
  test("twoChildAdded", () => {
    expect(g1->M.size) |> toBe(2)
  });

  test("childIsInChildrenCollection", () => {
    expect(g1->M.containsId(ID.create("2"))) |> toBe(true)
  });

  test("childIsInMasterLookup", () => {
    expect(g1->M.containsId(ID.create("2"))) |> toBe(true)
  });
});

describe("addParentChild", () => {
  open Expect;

  let id = ID.create("1");
  let g =
    M.empty()
    ->M.addNode(id, {one: 4, two: "four"})
    ->M.addNodeUnder(ID.create("2"), {one: 2, two: "two"}, PID.create("1"))
    ->M.addNodeUnder(
        ID.create("3"),
        {one: 1, two: "one"},
        PID.create("2"),
      );

  test("childAdded2", () => {
    expect(g->M.containsId(ID.create("2"))) |> toBe(true)
  });

  test("childAdded3", () => {
    expect(g->M.containsId(ID.create("3"))) |> toBe(true)
  });

  let data = g->M.dataForNode(ID.create("2"))->Option.getExn;
  test("masterLookupHasCorrectData", () => {
    expect(data.one) |> toBe(2)
  });

  test("masterLookupHasCorrectData2", () => {
    expect(data.two) |> toBe("two")
  });

  let data = g->M.dataForNode(ID.create("3"))->Option.getExn;
  test("masterLookupHasCorrectData3", () => {
    expect(data.one) |> toBe(1)
  });

  test("masterLookupHasCorrectData4", () => {
    expect(data.two) |> toBe("one")
  });

  let path = g->M.pathFromNode(ID.create("2"))->Option.getExn;
  test("masterLookupHasPathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });
  let path = g->M.pathFromNode(ID.create("3"))->Option.getExn;
  test("masterLookupHasPathUp", () => {
    expect(path->P.eq(P.fromList(["2", "1"]))) |> toBe(true)
  });

  let t = g->M.subGraphForNode(ID.create("2"))->Option.getExn;
  [%log.debug "original: " ++ g->M.toString; ("", "")];
  [%log.debug "subgraph: " ++ t->M.toString; ("", "")];
  test("subtreeHasChild", () => {
    expect(t->M.size) |> toBe(2)
  });
  test("subtreeHasChild1", () => {
    expect(t->M.containsId(ID.create("3"))) |> toBe(true)
  });
});

describe("moveChild", () => {
  open Expect;
  let g = makeGraph();
  let _test = (g, s) => {
    test("_test", () => {
      expect(g->M.containsId(ID.create(s))) |> toBe(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let path = g->M.pathFromNode(id4)->Option.getExn;
  test("4PathUp", () => {
    expect(path->P.eq(P.fromList(["3", "1"]))) |> toBe(true)
  });
  let path = g->M.pathFromNode(id3)->Option.getExn;
  test("3PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });
  let path = g->M.pathFromNode(id2)->Option.getExn;
  test("2PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });

  let g1 =
    g->M.moveChild(id3->I.convertFocusToChild, id2->I.convertFocusToParent);

  test("notErrored", () => {
    expect(g1->Result.isOk) |> toBe(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1");
  _test(g1, "2");
  _test(g1, "3");
  _test(g1, "4");
  let path = g1->M.pathFromNode(id4)->Option.getExn;
  test("4PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });
  let path = g1->M.pathFromNode(id3)->Option.getExn;
  test("3PathUp", () => {
    expect(path->P.eq(P.fromList(["2", "1"]))) |> toBe(true)
  });
  let path = g->M.pathFromNode(id2)->Option.getExn;
  test("2PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });
});

describe("removeSubtree", () => {
  open Expect;

  let g = makeGraph();

  let _test = (g, s, e) => {
    test("_test", () => {
      expect(g->M.containsId(ID.create(s))) |> toBe(e)
    });
  };
  _test(g, "1", true);
  _test(g, "2", true);
  _test(g, "3", true);
  _test(g, "4", true);

  %log.debug
  g->M.pathFromNode(id3)->Option.getExn->P.toString;
  let g1 = g->M.removeSubtree(id3);
  test("notErrored", () => {
    expect(g1->Result.isOk) |> toBe(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1", true);
  _test(g1, "2", true);
  _test(g1, "3", false);
  _test(g1, "4", false);
});

describe("moveSubtree", () => {
  open Expect;

  let g = makeGraph();

  let _test = (g, s) => {
    test("_test", () => {
      expect(g->M.containsId(ID.create(s))) |> toBe(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let path = g->M.pathFromNode(id4)->Option.getExn;
  test("4PathUp", () => {
    expect(path->P.eq(P.fromList(["3", "1"]))) |> toBe(true)
  });
  let path = g->M.pathFromNode(id3)->Option.getExn;
  test("3PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });
  let path = g->M.pathFromNode(id2)->Option.getExn;
  test("2PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });

  let g1 =
    g->M.moveSubtree(id3->I.convertFocusToChild, id2->I.convertFocusToParent);

  test("notErrored", () => {
    expect(g1->Result.isOk) |> toBe(true)
  });

  let g1 = g1->Result.getExn;
  _test(g1, "1");
  _test(g1, "2");
  _test(g1, "3");
  _test(g1, "4");
  let path = g1->M.pathFromNode(id4)->Option.getExn;
  test("4PathUp_", () => {
    expect(path->P.eq(P.fromList(["3", "2", "1"]))) |> toBe(true)
  });
  let path = g1->M.pathFromNode(id3)->Option.getExn;
  test("3PathUp_", () => {
    expect(path->P.eq(P.fromList(["2", "1"]))) |> toBe(true)
  });
  let path = g->M.pathFromNode(id2)->Option.getExn;
  test("2PathUp_", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });
});

describe("mapping", () => {
  open Expect;

  let g = makeGraph();

  let _test = (s, ss) => {
    let data = g->M.dataForNode(ID.create(s))->Option.getExn;
    test("hasCorrectData1", () => {
      expect(data->Data.toString) |> toBe(ss)
    });
  };

  _test("1", "{ one: 1, two: one }");
  _test("2", "{ one: 2, two: two }");
  _test("3", "{ one: 3, two: three }");
  _test("4", "{ one: 4, two: four }");
});

describe("foreach", () => {
  open Expect;

  let g = makeGraph();

  let i = ref(0);

  let _ = g->M.forEach((_id, _d) => {incr(i)});

  test("inc", () => {
    expect(i^) |> toBe(4)
  });
});

describe("keep", () => {
  open Expect;

  let g = makeGraph();
  let g1 = g->M.keep((id, d) => d.one < 2 || id == id3);

  let _test = (g, s, e) => {
    test("_test", () => {
      expect(g->M.containsId(ID.create(s))) |> toBe(e)
    });
  };
  _test(g1, "1", true);
  _test(g1, "2", false);
  _test(g1, "3", true);
  _test(g1, "4", false);
  let path = g1->M.pathFromNode(id3)->Option.getExn;
  test("3PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });

  let g2 = g->M.keep((id, d) => d.one <= 2 || id == id4);
  // this should remove 4 because it is no longer reachable
  _test(g2, "1", true);
  _test(g2, "2", true);
  _test(g2, "3", false);
  _test(g2, "4", false);

  let g3 = g->M.keep((_id, d) => d.one < 4);
  _test(g3, "1", true);
  _test(g3, "2", true);
  _test(g3, "3", true);
  _test(g3, "4", false);
  let path = g3->M.pathFromNode(id2)->Option.getExn;
  test("2PathUp", () => {
    expect(path->P.eq(P.fromList(["1"]))) |> toBe(true)
  });
});

describe("setSubGraphForNode-should-set-subgraph", () => {
  open Expect;
  let g = makeGraph();
  let _test = (g, s) => {
    test("_test", () => {
      expect(g->M.containsId(ID.create(s))) |> toBe(true)
    });
  };
  _test(g, "1");
  _test(g, "2");
  _test(g, "3");
  _test(g, "4");

  let id5 = ID.create("5");
  let id6 = ID.create("6");
  let gChild =
    M.empty()
    ->M.addNode(id5, {one: 5, two: "five"})
    ->M.addNode(id6, {one: 6, two: "six"});
  _test(gChild, "5");
  _test(gChild, "6");
  [%log.debug "about to set new subgraph"; ("", "")];
  switch (g->M.setSubGraphForNode(id2, gChild)) {
  | Ok(g1) =>
    _test(g1, "5");
    _test(g1, "6");
  | Error(_) => test("fail", () => {
                  expect(true) |> toBe(false)
                })
  };
});

describe("updteChildren-should-update-only-children", () => {
  open Expect;

  let _test = (g, n, vl) => {
    let data = g->M.dataForNode(ID.create(n))->Option.getExn;
    test("masterLookupHasCorrectData", () => {
      expect(data.one) |> toBe(vl)
    });
  };

  let g = makeGraph();
  _test(g, "1", 1);
  _test(g, "2", 2);
  _test(g, "3", 3);
  _test(g, "4", 4);

  let g1 = g->M.updateChildren(ID.create("1"), d => {...d, one: 200});

  _test(g1, "1", 1);
  _test(g1, "2", 200);
  _test(g1, "3", 200);
  _test(g1, "4", 4);

  let g2 =
    g->M.updateChildren(ID.create("not_there"), d => {...d, one: 200});

  _test(g2, "1", 1);
  _test(g2, "2", 2);
  _test(g2, "3", 3);
  _test(g2, "4", 4);

  let g3 = g->M.updateChildren(ID.create("3"), d => {...d, one: 200});

  _test(g3, "1", 1);
  _test(g3, "2", 2);
  _test(g3, "3", 3);
  _test(g3, "4", 200);
});
