open Jest;
module M = Graphs.Graph;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.Parents;

type data = {
  one: int,
  two: string,
};

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

/* describe("canMakeEmpty", () => { */
/*   open Expect; */
/*   // open! Expect.Operators; */
/*   let g = M.empty(); */

/*   test("hasNoLookup", () => { */
/*     expect(g->M.size) |> toBe(0) */
/*   }); */

/*   test("hasNoTree", () => { */
/*     expect(g->M.hasChildren) |> toBe(false) */
/*   }); */

/*   test("containsNothing", () => { */
/*     expect(g->M.containsId(ID.create("asd"))) |> toBe(false) */
/*   }); */
/* }); */

/* describe("addImmediateChildren", () => { */
/*   open Expect; */

/*   let g = M.empty()->M.addNode(ID.create("1"), {one: 4, two: "four"}); */

/*   test("oneChildAdded", () => { */
/*     expect(g->M.size) |> toBe(1) */
/*   }); */

/*   test("childIsInChildrenCollection", () => { */
/*     expect(g->M.containsId(ID.create("1"))) |> toBe(true) */
/*   }); */

/*   test("childIsInMasterLookup", () => { */
/*     expect(g->M.containsId(ID.create("1"))) |> toBe(true) */
/*   }); */

/*   let data = g->M.dataForNode(ID.create("1"))->Option.getExn; */
/*   test("masterLookupHasCorrectData", () => { */
/*     expect(data.one) |> toBe(4) */
/*   }); */
/*   test("masterLookupHasCorrectData2", () => { */
/*     expect(data.two) |> toBe("four") */
/*   }); */

/*   let path = g->M.pathFromNode(ID.create("1"))->Option.getExn; */
/*   test("masterLookupHasPathUp", () => { */
/*     expect(path->P.eq(P.fromList([]))) |> toBe(true) */
/*   }); */

/*   let g1 = g->M.addNode(ID.create("2"), {one: 8, two: "eight"}); */
/*   test("twoChildAdded", () => { */
/*     expect(g1->M.size) |> toBe(2) */
/*   }); */

/*   test("childIsInChildrenCollection", () => { */
/*     expect(g1->M.containsId(ID.create("2"))) |> toBe(true) */
/*   }); */

/*   test("childIsInMasterLookup", () => { */
/*     expect(g1->M.containsId(ID.create("2"))) |> toBe(true) */
/*   }); */
/* }); */

/* describe("addParentChild", () => { */
/*   open Expect; */

/*   let id = ID.create("1"); */
/*   let g = */
/*     M.empty() */
/*     ->M.addNode(id, {one: 4, two: "four"}) */
/*     ->M.addNodeUnder(ID.create("2"), {one: 2, two: "two"}, PID.create("1")) */
/*     ->M.addNodeUnder( */
/*         ID.create("3"), */
/*         {one: 1, two: "one"}, */
/*         PID.create("2"), */
/*       ); */

/*   test("childAdded2", () => { */
/*     expect(g->M.containsId(ID.create("2"))) |> toBe(true) */
/*   }); */

/*   test("childAdded3", () => { */
/*     expect(g->M.containsId(ID.create("3"))) |> toBe(true) */
/*   }); */

/*   let data = g->M.dataForNode(ID.create("2"))->Option.getExn; */
/*   test("masterLookupHasCorrectData", () => { */
/*     expect(data.one) |> toBe(2) */
/*   }); */

/*   test("masterLookupHasCorrectData2", () => { */
/*     expect(data.two) |> toBe("two") */
/*   }); */

/*   let data = g->M.dataForNode(ID.create("3"))->Option.getExn; */
/*   test("masterLookupHasCorrectData3", () => { */
/*     expect(data.one) |> toBe(1) */
/*   }); */

/*   test("masterLookupHasCorrectData4", () => { */
/*     expect(data.two) |> toBe("one") */
/*   }); */

/*   let path = g->M.pathFromNode(ID.create("2"))->Option.getExn; */
/*   test("masterLookupHasPathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */
/*   let path = g->M.pathFromNode(ID.create("3"))->Option.getExn; */
/*   test("masterLookupHasPathUp", () => { */
/*     expect(path->P.eq(P.fromList(["2", "1"]))) |> toBe(true) */
/*   }); */

/*   let t = g->M.subGraphForNode(ID.create("2"))->Option.getExn; */
/*   [%log.debug "original: " ++ g->M.toString(d => d.two); ("", "")]; */
/*   [%log.debug "subgraph: " ++ t->M.toString(d => d.two); ("", "")]; */
/*   test("subtreeHasChild", () => { */
/*     expect(t->M.size) |> toBe(2) */
/*   }); */
/*   test("subtreeHasChild1", () => { */
/*     expect(t->M.containsId(ID.create("3"))) |> toBe(true) */
/*   }); */
/* }); */

/* describe("moveChild", () => { */
/*   open Expect; */
/*   let g = makeGraph(); */
/*   let _test = (g, s) => { */
/*     test("_test", () => { */
/*       expect(g->M.containsId(ID.create(s))) |> toBe(true) */
/*     }); */
/*   }; */
/*   _test(g, "1"); */
/*   _test(g, "2"); */
/*   _test(g, "3"); */
/*   _test(g, "4"); */

/*   let path = g->M.pathFromNode(id4)->Option.getExn; */
/*   test("4PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["3", "1"]))) |> toBe(true) */
/*   }); */
/*   let path = g->M.pathFromNode(id3)->Option.getExn; */
/*   test("3PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */
/*   let path = g->M.pathFromNode(id2)->Option.getExn; */
/*   test("2PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */

/*   let g1 = */
/*     g->M.moveChild(id3->I.convertFocusToChild, id2->I.convertFocusToParent); */

/*   test("notErrored", () => { */
/*     expect(g1->Result.isOk) |> toBe(true) */
/*   }); */

/*   let g1 = g1->Result.getExn; */
/*   _test(g1, "1"); */
/*   _test(g1, "2"); */
/*   _test(g1, "3"); */
/*   _test(g1, "4"); */
/*   let path = g1->M.pathFromNode(id4)->Option.getExn; */
/*   test("4PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */
/*   let path = g1->M.pathFromNode(id3)->Option.getExn; */
/*   test("3PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["2", "1"]))) |> toBe(true) */
/*   }); */
/*   let path = g->M.pathFromNode(id2)->Option.getExn; */
/*   test("2PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */
/* }); */

/* describe("removeSubtree", () => { */
/*   open Expect; */

/*   let g = makeGraph(); */

/*   let _test = (g, s, e) => { */
/*     test("_test", () => { */
/*       expect(g->M.containsId(ID.create(s))) |> toBe(e) */
/*     }); */
/*   }; */
/*   _test(g, "1", true); */
/*   _test(g, "2", true); */
/*   _test(g, "3", true); */
/*   _test(g, "4", true); */

/*   %log.debug */
/*   g->M.pathFromNode(id3)->Option.getExn->P.toString; */
/*   let g1 = g->M.removeSubtree(id3); */
/*   test("notErrored", () => { */
/*     expect(g1->Result.isOk) |> toBe(true) */
/*   }); */

/*   let g1 = g1->Result.getExn; */
/*   _test(g1, "1", true); */
/*   _test(g1, "2", true); */
/*   _test(g1, "3", false); */
/*   _test(g1, "4", false); */
/* }); */

/* describe("moveSubtree", () => { */
/*   open Expect; */

/*   let g = makeGraph(); */

/*   let _test = (g, s) => { */
/*     test("_test", () => { */
/*       expect(g->M.containsId(ID.create(s))) |> toBe(true) */
/*     }); */
/*   }; */
/*   _test(g, "1"); */
/*   _test(g, "2"); */
/*   _test(g, "3"); */
/*   _test(g, "4"); */

/*   let path = g->M.pathFromNode(id4)->Option.getExn; */
/*   test("4PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["3", "1"]))) |> toBe(true) */
/*   }); */
/*   let path = g->M.pathFromNode(id3)->Option.getExn; */
/*   test("3PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */
/*   let path = g->M.pathFromNode(id2)->Option.getExn; */
/*   test("2PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */

/*   let g1 = */
/*     g->M.moveSubtree(id3->I.convertFocusToChild, id2->I.convertFocusToParent); */

/*   test("notErrored", () => { */
/*     expect(g1->Result.isOk) |> toBe(true) */
/*   }); */

/*   let g1 = g1->Result.getExn; */
/*   _test(g1, "1"); */
/*   _test(g1, "2"); */
/*   _test(g1, "3"); */
/*   _test(g1, "4"); */
/*   let path = g1->M.pathFromNode(id4)->Option.getExn; */
/*   test("4PathUp_", () => { */
/*     expect(path->P.eq(P.fromList(["3", "2", "1"]))) |> toBe(true) */
/*   }); */
/*   let path = g1->M.pathFromNode(id3)->Option.getExn; */
/*   test("3PathUp_", () => { */
/*     expect(path->P.eq(P.fromList(["2", "1"]))) |> toBe(true) */
/*   }); */
/*   let path = g->M.pathFromNode(id2)->Option.getExn; */
/*   test("2PathUp_", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */
/* }); */

/* describe("mapping", () => { */
/*   open Expect; */

/*   let g = makeGraph(); */

/*   let g1 = g->M.map(d => d.one->string_of_int ++ ":" ++ d.two); */

/*   let _test = (s, ss) => { */
/*     let data = g1->M.dataForNode(ID.create(s))->Option.getExn; */
/*     test("hasCorrectData1", () => { */
/*       expect(data) |> toBe(ss) */
/*     }); */
/*   }; */

/*   _test("1", "1:one"); */
/*   _test("2", "2:two"); */
/*   _test("3", "3:three"); */
/*   _test("4", "4:four"); */
/* }); */

/* describe("foreach", () => { */
/*   open Expect; */

/*   let g = makeGraph(); */

/*   let i = ref(0); */

/*   let _ = g->M.forEach((_id, _d) => {incr(i)}); */

/*   test("inc", () => { */
/*     expect(i^) |> toBe(4) */
/*   }); */
/* }); */

/* describe("keep", () => { */
/*   open Expect; */

/*   let g = makeGraph(); */
/*   let g1 = g->M.keep((id, d) => d.one < 2 || id == id3); */

/*   let _test = (g, s, e) => { */
/*     test("_test", () => { */
/*       expect(g->M.containsId(ID.create(s))) |> toBe(e) */
/*     }); */
/*   }; */
/*   _test(g1, "1", true); */
/*   _test(g1, "2", false); */
/*   _test(g1, "3", true); */
/*   _test(g1, "4", false); */
/*   let path = g1->M.pathFromNode(id3)->Option.getExn; */
/*   test("3PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */

/*   let g2 = g->M.keep((id, d) => d.one < 2 || id == id4); */
/*   _test(g2, "1", true); */
/*   _test(g2, "2", false); */
/*   _test(g2, "3", false); */
/*   _test(g2, "4", true); */
/*   let path = g2->M.pathFromNode(id4)->Option.getExn; */
/*   test("4PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */

/*   let g3 = g->M.keep((_id, d) => d.one < 4); */
/*   _test(g3, "1", true); */
/*   _test(g3, "2", true); */
/*   _test(g3, "3", true); */
/*   _test(g3, "4", false); */
/*   let path = g3->M.pathFromNode(id2)->Option.getExn; */
/*   test("2PathUp", () => { */
/*     expect(path->P.eq(P.fromList(["1"]))) |> toBe(true) */
/*   }); */
/* }); */

/* describe("makeFromOtherArray", () => { */
/*   open Expect; */

/*   let chartData = */
/*     {j| */
       /*        { */
       /*            "name": "Root", */
       /*            "imageUrl": "./general.jpg", */
       /*            "area": "root", */
       /*            "profileUrl": "http://example.com/employee/profile", */
       /*            "office": "root", */
       /*            "tags": "root", */
       /*            "isLoggedUser": false, */
       /*            "unit": { */
       /*                "type": "business", */
       /*                "value": "Business first" */
       /*            }, */
       /*            "positionName": "root", */
       /*            "children": [ */
       /*                { */
       /*                    "name": "Bin", */
       /*                    "imageUrl": "./bin.jpg", */
       /*                    "area": "bin", */
       /*                    "profileUrl": "http://example.com/employee/profile", */
       /*                    "office": "bin", */
       /*                    "tags": "bin", */
       /*                    "isLoggedUser": false, */
       /*                    "unit": { */
       /*                        "type": "util", */
       /*                        "value": "bin" */
       /*                    }, */
       /*                    "positionName": "bin" */
       /*                }, */
       /*                { */
       /*                    "name": "Ian Devling", */
       /*                    "imageUrl": "./general.jpg", */
       /*                    "area": "Corporate", */
       /*                    "profileUrl": "http://example.com/employee/profile", */
       /*                    "office": "CTO office", */
       /*                    "tags": "Ceo,tag1,manager,cto", */
       /*                    "isLoggedUser": false, */
       /*                    "unit": { */
       /*                        "type": "business", */
       /*                        "value": "Business first" */
       /*                    }, */
       /*                    "positionName": "Chief Executive Officer", */
       /*              "children": [ */
       /*                        { */
       /*                            "name": "Davolio Nancy", */
       /*                            "imageUrl": "./general.jpg", */
       /*                            "area": "Corporate", */
       /*                            "profileUrl": "http://example.com/employee/profile", */
       /*                            "office": "CEO office", */
       /*                            "tags": "Ceo,tag1, tag2", */
       /*                            "isLoggedUser": false, */
       /*                            "unit": { */
       /*                                "type": "business", */
       /*                                "value": "Business one" */
       /*                            }, */
       /*                            "positionName": "CTO", */
       /*                "children": [] */
       /*              }, */
       /*                                { */
       /*                                    "name": " Leverling Janet", */
       /*                                    "imageUrl": "./general.jpg", */
       /*                                    "area": "Corporate", */
       /*                                    "profileUrl": "http://example.com/employee/profile", */
       /*                                    "office": "CEO office", */
       /*                                    "tags": "Ceo,tag1, tag2", */
       /*                                    "isLoggedUser": false, */
       /*                                    "unit": { */
       /*                                        "type": "department", */
       /*                                        "value": " Finance Department", */
       /*                                        "desc": "Finance Dept description" */
       /*                                    }, */
       /*                                    "positionName": "CFO", */
       /*                "children": [] */
       /*                  } */

       /*                ] */
       /*                }, */
       /*                { */
       /*                    "name": "Bench", */
       /*                    "imageUrl": "./bench.png", */
       /*                    "area": "bench", */
       /*                    "profileUrl": "http://example.com/employee/profile", */
       /*                    "office": "bench", */
       /*                    "tags": "bench", */
       /*                    "isLoggedUser": false, */
       /*                    "unit": { */
       /*                        "type": "util", */
       /*                        "value": "bench" */
       /*                    }, */
       /*                    "positionName": "bench" */
       /*                } */
       /*            ] */
       /*        } */
       /*             |j} */
/*     |> Json.parseOrRaise; //Serialisers.Json.decode; */

/*   let otherData: array(Other.t) = chartData |> Data.prepData; */
/*   let otherDataMap = */
/*     otherData->Array.reduce(Map.String.empty, (m, d) => { */
/*       m->Map.String.set(d.templateType.positionName, d) */
/*     }); */

/*   let g: M.t(Other.t) = Data.makeGraph(otherData); */
/*   test("hasElements", () => { */
/*     expect(g->M.size) |> toBe(6) */
/*   }); */

/*   let ids = otherData->Array.map(d => d.nodeId->ID.create); */
/*   ids->Array.forEach(id => { */
/*     test("allPresent", () => { */
/*       expect(g->M.containsId(id)) |> toBe(true) */
/*     }) */
/*   }); */

/*   [%log.debug */
/*     otherDataMap->Map.String.keysToArray->List.fromArray |> String.concat(","); */
/*     ("", "") */
/*   ]; */
/*   let _testPositionName = (g: M.t(Other.t), s) => { */
/*     test("hasPositionName", () => { */
/*       [%log.debug s; ("", "")]; */
/*       let data = otherDataMap->Map.String.getExn(s); */
/*       let node = g->M.dataForNode(data.nodeId->ID.create)->Option.getExn; */
/*       expect(node.templateType.positionName) |> toBe(s); */
/*     }); */
/*   }; */

/*   _testPositionName(g, "root"); */
/*   _testPositionName(g, "bin"); */
/*   _testPositionName(g, "bench"); */
/*   _testPositionName(g, "Chief Executive Officer"); */
/*   _testPositionName(g, "CTO"); */
/*   _testPositionName(g, "CFO"); */

/*   let _testHasChildren = (g: M.t(Other.t), s, b) => { */
/*     test("hasChildren", () => { */
/*       let data = otherDataMap->Map.String.getExn(s); */
/*       let node = g->M.dataForNode(data.nodeId->ID.create)->Option.getExn; */
/*       expect(node.hasChildren) |> toBe(b); */
/*     }); */
/*   }; */
/*   _testHasChildren(g, "root", true); */
/*   _testHasChildren(g, "bin", false); */
/*   _testHasChildren(g, "bench", false); */
/*   _testHasChildren(g, "Chief Executive Officer", true); */
/*   _testHasChildren(g, "CTO", false); */
/*   _testHasChildren(g, "CFO", false); */

/*   let g1 = g->M.keep((_id, d) => d.visible); */
/*   test("hasFourVisibleToStart", () => { */
/*     expect(g1->M.size) |> toBe(4) */
/*   }); */

/*   _testPositionName(g1, "root"); */
/*   _testPositionName(g1, "bin"); */
/*   _testPositionName(g1, "bench"); */
/*   _testPositionName(g1, "Chief Executive Officer"); */

/*   let _testVisible = (g: M.t(Other.t), s, b) => { */
/*     test("isVisible", () => { */
/*       let data = otherDataMap->Map.String.getExn(s); */
/*       let node = g->M.dataForNode(data.nodeId->ID.create)->Option.getExn; */
/*       expect(node.visible) |> toBe(b); */
/*     }); */
/*   }; */

/*   let ceo = */
/*     otherDataMap->Map.String.getExn("Chief Executive Officer").nodeId */
/*     ->ID.create; */

/*   _testVisible(g, "CFO", false); */
/*   _testVisible(g, "CTO", false); */

/*   let g2 = */
/*     g */
/*     ->M.subGraphForNode(ceo) */
/*     ->Option.map(g_ => {g_->M.map(d => {...d, visible: true})}); */

/*   let gResult = */
/*     switch (g2) { */
/*     | Some(gChildren) => */
/*       [%log.debug */
/*         "gChildren " */
/*         ++ gChildren->M.toString(d => { */
/*              d.templateType.positionName ++ " - " ++ d.visible->string_of_bool */
/*            }); */
/*         ("", "") */
/*       ]; */
/*       test("subtreeHasThree", () => { */
/*         expect(gChildren->M.size) |> toBe(3) */
/*       }); */
/*       _testPositionName(gChildren, "CTO"); */
/*       _testPositionName(gChildren, "CFO"); */
/*       _testVisible(gChildren, "CFO", true); */
/*       _testVisible(gChildren, "CTO", true); */
/*       let gg = g->M.setSubGraphForNode(ceo, gChildren); */
/*       _testPositionName(gg->Result.getExn, "CTO"); */
/*       _testPositionName(gg->Result.getExn, "CFO"); */
/*       _testVisible(gg->Result.getExn, "CFO", true); */
/*       _testVisible(gg->Result.getExn, "CTO", true); */
/*       gg; */

/*     | None => */
/*       let err = "couldn't find child subtree at " ++ ceo->ID.toString; */
/*       [%log.error err; ("", "")]; */
/*       Result.Error(err); */
/*     }; */

/*   switch (gResult) { */
/*   | Ok(g3) => */
/*     test("hasSixVisibleNow1", () => { */
/*       [%log.debug */
/*         "g3: " */
/*         ++ g3->M.toString(d => { */
/*              d.templateType.positionName ++ " - " ++ d.visible->string_of_bool */
/*            }); */
/*         ("", "") */
/*       ]; */
/*       expect(g3->M.size) |> toBe(6); */
/*     }) */
/*   /\* let g4 = g3->M.keep((_id, d) => d.visible); *\/ */
/*   /\* test("hasSixVisibleNow2", () => { *\/ */
/*   /\*   expect(g4->M.size) |> toBe(6) *\/ */
/*   /\* }); *\/ */

/*   /\* _testPositionName(g4, "root"); *\/ */
/*   /\* _testPositionName(g4, "bin"); *\/ */
/*   /\* _testPositionName(g4, "bench"); *\/ */
/*   /\* _testPositionName(g4, "Chief Executive Officer"); *\/ */
/*   /\* _testPositionName(g4, "CTO"); *\/ */
/*   /\* _testPositionName(g4, "CFO"); *\/ */
/*   | Error(s) => test("errored", () => { */
/*                   expect(s == "wrong") |> toBe(true) */
/*                 }) */
/*   }; */
/* }); */

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
