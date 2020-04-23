open BsMocha.Mocha;
open BsFastCheck.Arbitrary;
open BsFastCheck.Property.Sync;
open BsFastCheck.Arbitrary.Combinators;

module M = Graph.T;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

module IDs = ID_fastcheck.Arbitrary;
module Paths = Path_fastcheck.Arbitrary;

module Arbitrary = {
  type data = {
    a: int,
    b: string,
    c: bool,
  };
  let data =
    tuple3(integer(), string(), boolean())
    ->Derive.map(((a, b, c)) => {a, b, c});

  type other = {
    nodeId: ID.t,
    parentNodeId: option(PID.t),
    data,
  };

  // a non-empty set of unique ID which will be the nodes
  let uniqueIds = maxSize => {
    arrayWithLength(IDs.id, 2, maxSize)
    ->Derive.map(s => s->ID.Set.fromArray->Set.toArray);
  };

  let _genParentChildrenPairs = (parent: int, first, last) => {
    let children = Array.range(first, last - 1);
    let ps = Array.make(children->Array.size, Some(parent));
    Array.zip(children, ps)->constant;
  };

  let genParentChildrenPairs = (maxChildren, layers) => {
    let rec _aux = (newStart, count) => {
      count < 1
        ? [[|(0, None)|]]->constant
        : {
          integerRange(1, maxChildren)
          ->Derive.chain(n => {
              _genParentChildrenPairs(
                newStart,
                newStart + 1,
                newStart + 1 + n,
              )
            })
          ->Derive.chain(arr => {
              let n = arr->Array.size;
              _aux(n, count - 1)->Derive.map(rest => {[arr, ...rest]});
            });
        };
    };
    _aux(0, layers)->Derive.map(l => l->List.toArray->Array.concatMany);
  };

  let graphData =
    genParentChildrenPairs(4, 10)
    ->Derive.chain(idParents => {
        let n = idParents->Array.size;
        data
        ->arrayWithLength(n, n)
        ->Derive.map(ds =>
            ds->Array.zipBy(
              idParents,
              (d, idParent) => {
                let (id, pid) = idParent;
                [%log.debug
                  "graphData: "
                  ++ id->string_of_int
                  ++ ", "
                  ++ pid
                     ->Option.map(string_of_int)
                     ->Option.getWithDefault("");
                  ("", "")
                ];
                {
                  nodeId: id->string_of_int->ID.create,
                  parentNodeId:
                    pid->Option.map(string_of_int)->Option.map(PID.create),
                  data: d,
                };
              },
            )
          );
      });
};

describe("Graph: construction", () => {
  it("fromArray -> toArray gives same data", () => {
    assertProperty1(
      Arbitrary.graphData,
      arr => {
        //        [%log.debug "tree: " ++ t->M.toString; ("", "")];
        let g = arr->M.fromArray(o => o.nodeId, o => o.parentNodeId);
        let arr2 = g->M.toArray;
        let expected =
          arr->SortArray.stableSortBy((x, y) => {
            Pervasives.compare(x.nodeId, y.nodeId)
          });
        let actual =
          arr2->SortArray.stableSortBy((x, y) => {
            Pervasives.compare(x.nodeId, y.nodeId)
          });
        expected->Array.eq(actual, (x, y) => {
          x.nodeId->ID.toString == y.nodeId->ID.toString
          && x.parentNodeId
             ->Option.eq(y.parentNodeId, (xx, yy) => {
                 xx->PID.toString == yy->PID.toString
               })
          && x.data.a == y.data.a
          && x.data.b == y.data.b
          && x.data.c == y.data.c
        });
      },
    )
  })
});

/* let counterexample = [ */
/*   [ */
/*   {"nodeId":"53d096b5-cab5-487e-8f17-2e3a0dbf39dd", */
/*    "parentNodeId":undefined, */
/*    "data":{"a":0,"b":"","c":false}}, */
/*   {"nodeId":"ae58854a-3256-478b-8029-dae2ebf3bfec", */
/*    "parentNodeId":"ae58854a-3256-478b-8029-dae2ebf3bfec", */
/*    "data":{"a":-2008096949,"b":"M","c":false}}, */
/*   {"nodeId":"a7908541-04bd-4e26-993a-6aba6a7e7de8", */
/*    "parentNodeId":"ae58854a-3256-478b-8029-dae2ebf3bfec", */
/*    "data":{"a":858015518,"b":"%","c":false}}] */
/* ] */

/* Counterexample: [[{"nodeId":"5efb98dd-01f9-4bac-a7bf-e9e557c39419", */
/*                    "parentNodeId":undefined, */
/*                    "data":{"a":0,"b":"","c":false}}, */
/*                   {"nodeId":"975c725f-1139-434b-9bad-0c080cdf9f02", */
/*                    "parentNodeId":"975c725f-1139-434b-9bad-0c080cdf9f02", */
/*                    "data":{"a":13,"b":"$3#","c":false}}, */
/*                   {"nodeId":"eef91312-8b76-4483-9fe1-ee5a20397705", */
/*                    "parentNodeId":"5efb98dd-01f9-4bac-a7bf-e9e557c39419", */
/*                    "data":{"a":-1746299436,"b":"w'O%z/eo>5","c":true}}]] */

/* Counterexample: [[{"nodeId":"2b298e57-fb97-439d-9158-c10bb1b73204", */
/*                    "parentNodeId":undefined, */
/*                    "data":{"a":0,"b":"","c":false}}, */
/*                   {"nodeId":"5ad510c7-d71d-4c8e-b818-f491b530cef9", */
/*                    "parentNodeId":"9092f443-361d-4882-9172-e5072c35c581", */
/*                    "data":{"a":-1727639346,"b":"];y,","c":true}}, */
/*                   {"nodeId":"9092f443-361d-4882-9172-e5072c35c581", */
/*                    "parentNodeId":"5ad510c7-d71d-4c8e-b818-f491b530cef9", */
/*                    "data":{"a":-2042665511,"b":"","c":true}}, */
/*                   {"nodeId":"aebbbe54-56a6-4b8a-a1bf-6704ccd21f18", */
/*                    "parentNodeId":"2b298e57-fb97-439d-9158-c10bb1b73204", */
/*                    "data":{"a":480790877,"b":"cB^h","c":true}}]] */
