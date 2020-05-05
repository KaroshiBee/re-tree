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
    setWithLength(IDs.id, 2, maxSize, ~comparator=(a, b) => {
      String.equal(a->ID.toString, b->ID.toString)
    })
    ->Derive.map(arr =>
        arr->Array.reduce(
          MutableStack.make(),
          (st, el) => {
            st->MutableStack.push(el);
            st;
          },
        )
      );
  };

  let _randGraph = dst => {
    let n = dst->MutableStack.size;
    [%log.debug "_randGraph: size: " ++ n->string_of_int; ("", "")];
    n == 0
      ? constant(M.empty())
      : {
        let g = M.empty()->ref;
        let src = [|dst->MutableStack.pop->Option.getExn|]->ref;
        dst->MutableStack.dynamicPopIter(b => {
          let a = (src^)->Array.shuffle->Array.getExn(0);
          (g^)->M.containsId(a)
            ? g := (g^)->M.addNodeUnder(b, None, a->I.convertFocusToParent)
            : g :=
                (g^)
                ->M.addNode(a, None)
                ->M.addNodeUnder(b, None, a->I.convertFocusToParent);
          src := (src^)->Array.concat([|b|]);
        });
        let m = (g^)->M.size;
        [%log.debug "_randGraph: size after: " ++ m->string_of_int; ("", "")];
        m == 0
          ? M.empty()->constant
          : {
            let arr = (g^)->M.toKeyValueArrayWithPaths;
            data->Derive.map(d => {
              arr->Array.reduce(
                M.empty(),
                (gg, (nodeId, pth, _o)) => {
                  let parentNodeId = pth->P.parent;
                  gg->M.addNodeAtPath(
                    nodeId,
                    {nodeId, parentNodeId, data: d},
                    pth,
                  );
                },
              )
            });
          };
      };
  };

  let randomGraph = maxSize => {
    uniqueIds(maxSize)->Derive.chain(_randGraph);
  };

  let randomGraph2 = maxSize => {
    uniqueIds(2 * maxSize)
    ->Derive.chain(ids1 => {
        let n = ids1->MutableStack.size;
        let ids2 = MutableStack.make();
        let rec aux = m => {
          m > 0
            ? {
              ids1
              ->MutableStack.pop
              ->Option.map(ids2->MutableStack.push)
              ->ignore;
              aux(m - 1);
            }
            : ();
        };
        aux(n / 2);
        [%log.debug
          "randomGraphs2: ids1 " ++ ids1->MutableStack.size->string_of_int;
          ("", "")
        ];
        [%log.debug
          "randomGraphs2: ids2 " ++ ids2->MutableStack.size->string_of_int;
          ("", "")
        ];
        tuple2(_randGraph(ids1), _randGraph(ids2));
      });
  };
};

let eq = (expectedG: M.t(Arbitrary.other), actualG: M.t(Arbitrary.other)) => {
  let n = expectedG->M.size;
  let m = actualG->M.size;
  n != m
    ? false
    : {
      n == 0
        ? true
        : {
          let expected =
            expectedG
            ->M.toArray
            ->SortArray.stableSortBy((x, y) => {
                Pervasives.compare(x.nodeId, y.nodeId)
              });
          let actual =
            actualG
            ->M.toArray
            ->SortArray.stableSortBy((x, y) => {
                Pervasives.compare(x.nodeId, y.nodeId)
              });
          expected->Array.eq(actual, (x, y) => {
            x.nodeId->ID.toString >= y.nodeId->ID.toString
            && x.parentNodeId
               ->Option.eq(y.parentNodeId, (xx, yy) => {
                   xx->PID.toString == yy->PID.toString
                 })
            && x.data.a == y.data.a
            && x.data.b == y.data.b
            && x.data.c == y.data.c
          });
        };
    };
};

describe("Graph: construction", () => {
  it("toArray -> fromArray -> toArray gives same data", () => {
    assertProperty1(
      Arbitrary.randomGraph(1000),
      g => {
        let arr1 = g->M.toArray;
        let actual = arr1->M.fromArray(o => o.nodeId, o => o.parentNodeId);
        eq(g, actual);
      },
    )
  })
});

describe("Graph: add/move/remove nodes", () => {
  it("add -> move -> remove should give same data", () => {
    assertProperty2(
      Arbitrary.randomGraph(100),
      Arbitrary.data,
      (g, d) => {
        let expected =
          g
          ->M.toArray
          ->SortArray.stableSortBy((x, y) => {
              Pervasives.compare(x.nodeId, y.nodeId)
            });

        let nodeId =
          (expected->Array.getExn(0).nodeId->ID.toString ++ "UNIQUE")
          ->ID.create;

        let parentNodeId =
          expected->Array.shuffle->Array.getExn(0).parentNodeId;
        let newParentNodeId =
          expected->Array.shuffle->Array.getExn(0).parentNodeId;
        [%log.debug
          "ids: "
          ++ nodeId->ID.toString
          ++ ", "
          ++ parentNodeId
             ->Option.map(PID.toString)
             ->Option.getWithDefault("no parent")
          ++ ", "
          ++ newParentNodeId
             ->Option.map(PID.toString)
             ->Option.getWithDefault("no parent");
          ("", "")
        ];
        let o: Arbitrary.other = {nodeId, parentNodeId, data: d};
        let gg =
          switch (parentNodeId, newParentNodeId) {
          | (Some(pid1), Some(pid2)) =>
            g
            ->M.addNodeUnder(nodeId, o, pid1)
            ->M.moveChild(nodeId->I.convertFocusToChild, pid2)
            ->Result.flatMap(ggg => ggg->M.removeNode(nodeId))
          | (Some(pid1), None) =>
            g->M.addNodeUnder(nodeId, o, pid1)->M.removeNode(nodeId)
          | (None, Some(pid2)) =>
            g
            ->M.addNode(nodeId, o)
            ->M.moveChild(nodeId->I.convertFocusToChild, pid2)
            ->Result.flatMap(ggg => ggg->M.removeNode(nodeId))
          | (None, None) => g->M.addNode(nodeId, o)->M.removeNode(nodeId)
          };
        switch (gg) {
        | Result.Ok(gg) => eq(g, gg)
        | Result.Error(err) =>
          [%log.error err; ("", "")];
          false;
        };
      },
    )
  });

  it("add -> move -> remove subtrees should give same data", () => {
    assertProperty1(
      Arbitrary.randomGraph2(500),
      gg => {
        let (expected, g2) = gg;
        let n = expected->M.size;
        // need to take the IDs at the root of input
        let nodeIds = g2->M.childIdsOfRoot;

        let parentNodeId =
          n == 0
            ? None
            : expected->M.toArray->Array.shuffle->Array.getExn(0).parentNodeId;
        let newParentNodeId =
          n == 0
            ? None
            : expected->M.toArray->Array.shuffle->Array.getExn(0).parentNodeId;
        let r =
          switch (parentNodeId, newParentNodeId) {
          | (Some(pid1), Some(pid2)) =>
            [%log.debug "got pid1, got pid2"; ("", "")];
            expected
            ->M.setSubGraphForNode(pid1, g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg =>
                    ggg->M.moveSubtree(i->I.convertFocusToChild, pid2)
                  )
                })
              })
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->M.removeSubtree(i))
                })
              });
          | (Some(pid1), None) =>
            [%log.debug "got pid1, no pid2"; ("", "")];
            expected
            ->M.setSubGraphForNode(pid1, g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->M.removeSubtree(i))
                })
              });
          | (None, Some(pid2)) =>
            [%log.debug "no pid1, got pid2"; ("", "")];
            expected
            ->M.setSubGraphForRoot(g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg =>
                    ggg->M.moveSubtree(i->I.convertFocusToChild, pid2)
                  )
                })
              })
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->M.removeSubtree(i))
                })
              });
          | (None, None) =>
            [%log.debug "no pid1, no pid2"; ("", "")];
            expected
            ->M.setSubGraphForRoot(g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->M.removeSubtree(i))
                })
              });
          };
        switch (r) {
        | Result.Ok(actual) => eq(expected, actual)
        | Result.Error(err) =>
          [%log.error err; ("", "")];
          false;
        };
      },
    )
  });
});
