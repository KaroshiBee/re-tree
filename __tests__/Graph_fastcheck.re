open Test_utils;
open BsFastCheck.Arbitrary;
open BsFastCheck.Property.Sync;
open BsFastCheck.Arbitrary.Combinators;

module IDs = ID_fastcheck.Arbitrary;
module Paths = Path_fastcheck.Arbitrary;

type data = {
  a: int,
  b: string,
  c: bool,
};

module Other = {
  type t = {
    nodeId: ID.t,
    parentNodeId: option(PID.t),
    data,
  };

  let hash = t =>
    Hashtbl.(
      hash(t.nodeId->ID.toString)
      + t.parentNodeId
        ->Option.mapWithDefault(0, pid => pid->PID.toString->hash)
      + hash(t.data.a)
      + hash(t.data.b)
      + hash(t.data.c)
    );

  let eq = (x, y) =>
    x.nodeId->ID.toString == y.nodeId->ID.toString
    && x.parentNodeId
       ->Option.eq(y.parentNodeId, (xx, yy) =>
           xx->PID.toString == yy->PID.toString
         )
    && x.data.a == y.data.a
    && x.data.b == y.data.b
    && x.data.c == y.data.c;
  let toString = t =>
    "{"
    ++ t.nodeId->ID.toString
    ++ ": ("
    ++ t.parentNodeId->Option.mapWithDefault("None", pid => pid->PID.toString)
    ++ ")}";
};

module E = GraphF.MakeElement(Other);
module GF2 = GraphF.Make(E);

module Arbitrary = {
  let data =
    tuple3(integer(), string(), boolean())
    ->Derive.map(((a, b, c)) => {a, b, c});

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
    // [%log.debug "_randGraph: size: " ++ n->string_of_int; ("", "")];
    n == 0
      ? constant(GF2.empty())
      : {
        let g = GF2.empty()->ref;
        let src = [|dst->MutableStack.pop->Option.getExn|]->ref;
        dst->MutableStack.dynamicPopIter(b => {
          let a = (src^)->Array.shuffle->Array.getExn(0);
          // NOTE make with fake data to start
          let withParent =
            Other.{
              nodeId: a,
              parentNodeId: a->I.convertFocusToParent->Some,
              data: {
                a: 1,
                b: "",
                c: false,
              },
            };

          let withoutParent =
            Other.{
              nodeId: a,
              parentNodeId: None,
              data: {
                a: 1,
                b: "",
                c: false,
              },
            };

          (g^)->GF2.containsId(a)
            ? g :=
                (g^)
                ->GF2.addNodeUnder(b, withParent, a->I.convertFocusToParent)
            : g :=
                (g^)
                ->GF2.addNode(a, withoutParent)
                ->GF2.addNodeUnder(b, withParent, a->I.convertFocusToParent);
          src := (src^)->Array.concat([|b|]);
        });
        let m = (g^)->GF2.size;
        // [%log.debug "_randGraph: size after: " ++ m->string_of_int; ("", "")];
        m == 0
          ? GF2.empty()->constant
          : {
            let arr = (g^)->GF2.toKeyValueArrayWithPaths;
            data->Derive.map(d => {
              arr->Array.reduce(
                GF2.empty(),
                (gg, (nodeId, pth, _o)) => {
                  let parentNodeId = pth->P.parent;
                  gg->GF2.addNodeAtPath(
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
        /* [%log.debug */
        /*   "randomGraphs2: ids1 " ++ ids1->MutableStack.size->string_of_int; */
        /*   ("", "") */
        /* ]; */
        /* [%log.debug */
        /*   "randomGraphs2: ids2 " ++ ids2->MutableStack.size->string_of_int; */
        /*   ("", "") */
        /* ]; */
        tuple2(_randGraph(ids1), _randGraph(ids2));
      });
  };
};

let eq = (expectedG, actualG) => expectedG->GF2.eq(actualG);
/*   { */
/*   let n = expectedG->GF2.size; */
/*   let m = actualG->GF2.size; */
/*   n != m */
/*     ? false */
/*     : { */
/*       n == 0 */
/*         ? true */
/*         : { */
/*           let expected = */
/*             expectedG */
/*             ->GF2.toArray */
/*             ->SortArray.stableSortBy((x, y) => { */
/*                 Pervasives.compare(x.nodeId, y.nodeId) */
/*               }); */
/*           let actual = */
/*             actualG */
/*             ->GF2.toArray */
/*             ->SortArray.stableSortBy((x, y) => { */
/*                 Pervasives.compare(x.nodeId, y.nodeId) */
/*               }); */
/*           expected->Array.eq(actual, (x, y) => { */
/*             x.nodeId->ID.toString >= y.nodeId->ID.toString */
/*             && x.parentNodeId */
/*                ->Option.eq(y.parentNodeId, (xx, yy) => { */
/*                    xx->PID.toString == yy->PID.toString */
/*                  }) */
/*             && x.data.a == y.data.a */
/*             && x.data.b == y.data.b */
/*             && x.data.c == y.data.c */
/*           }); */
/*         }; */
/*     }; */
/* }; */

describe("Graph: construction", () => {
  it("toArray -> fromArray -> toArray gives same data", () => {
    assertProperty1(
      Arbitrary.randomGraph(1000),
      g => {
        let arr1 = g->GF2.toArray;
        let actual = arr1->GF2.fromArray(o => o.nodeId, o => o.parentNodeId);
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
          ->GF2.toArray
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
        /* [%log.debug */
        /*   "ids: " */
        /*   ++ nodeId->ID.toString */
        /*   ++ ", " */
        /*   ++ parentNodeId */
        /*      ->Option.map(PID.toString) */
        /*      ->Option.getWithDefault("no parent") */
        /*   ++ ", " */
        /*   ++ newParentNodeId */
        /*      ->Option.map(PID.toString) */
        /*      ->Option.getWithDefault("no parent"); */
        /*   ("", "") */
        /* ]; */
        let o: Other.t = {nodeId, parentNodeId, data: d};
        let gg =
          switch (parentNodeId, newParentNodeId) {
          | (Some(pid1), Some(pid2)) =>
            g
            ->GF2.addNodeUnder(nodeId, o, pid1)
            ->GF2.moveChild(nodeId->I.convertFocusToChild, pid2)
            ->Result.flatMap(ggg => ggg->GF2.removeNode(nodeId))
          | (Some(pid1), None) =>
            g->GF2.addNodeUnder(nodeId, o, pid1)->GF2.removeNode(nodeId)
          | (None, Some(pid2)) =>
            g
            ->GF2.addNode(nodeId, o)
            ->GF2.moveChild(nodeId->I.convertFocusToChild, pid2)
            ->Result.flatMap(ggg => ggg->GF2.removeNode(nodeId))
          | (None, None) =>
            g->GF2.addNode(nodeId, o)->GF2.removeNode(nodeId)
          };
        switch (gg) {
        | Result.Ok(gg) => eq(g, gg)
        | Result.Error(_err) =>
          [%log.error _err; ("", "")];
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
        let n = expected->GF2.size;
        // need to take the IDs at the root of input
        let nodeIds = g2->GF2.childIdsOfRoot;

        let parentNodeId =
          n == 0
            ? None
            : expected->GF2.toArray->Array.shuffle->Array.getExn(0).
                parentNodeId;
        let newParentNodeId =
          n == 0
            ? None
            : expected->GF2.toArray->Array.shuffle->Array.getExn(0).
                parentNodeId;
        let r =
          switch (parentNodeId, newParentNodeId) {
          | (Some(pid1), Some(pid2)) =>
            /* [%log.debug "got pid1, got pid2"; ("", "")]; */
            expected
            ->GF2.setSubGraphForNode(pid1, g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg =>
                    ggg->GF2.moveSubtree(i->I.convertFocusToChild, pid2)
                  )
                })
              })
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->GF2.removeSubtree(i))
                })
              })
          | (Some(pid1), None) =>
            /* [%log.debug "got pid1, no pid2"; ("", "")]; */
            expected
            ->GF2.setSubGraphForNode(pid1, g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->GF2.removeSubtree(i))
                })
              })
          | (None, Some(pid2)) =>
            /* [%log.debug "no pid1, got pid2"; ("", "")]; */
            expected
            ->GF2.setSubGraphForRoot(g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg =>
                    ggg->GF2.moveSubtree(i->I.convertFocusToChild, pid2)
                  )
                })
              })
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->GF2.removeSubtree(i))
                })
              })
          | (None, None) =>
            /* [%log.debug "no pid1, no pid2"; ("", "")]; */
            expected
            ->GF2.setSubGraphForRoot(g2)
            ->Result.flatMap(g => {
                nodeIds->List.reduce(g->Result.Ok, (gg, i) => {
                  gg->Result.flatMap(ggg => ggg->GF2.removeSubtree(i))
                })
              })
          };
        switch (r) {
        | Result.Ok(actual) => eq(expected, actual)
        | Result.Error(_err) =>
          [%log.error _err; ("", "")];
          false;
        };
      },
    )
  });
});
