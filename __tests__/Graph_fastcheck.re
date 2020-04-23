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

  let randomGraph = maxSize => {
    uniqueIds(maxSize)
    ->Derive.chain(dst => {
        [%log.debug
          "size: " ++ dst->MutableStack.size->string_of_int;
          ("", "")
        ];
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
        [%log.debug "size: " ++ (g^)->M.size->string_of_int; ("", "")];
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
      });
  };
};

describe("Graph: construction", () => {
  it("toArray -> fromArray -> toArray gives same data", () => {
    assertProperty1(
      Arbitrary.randomGraph(1000),
      g => {
        let arr1 = g->M.toArray;
        let expected =
          arr1->SortArray.stableSortBy((x, y) => {
            Pervasives.compare(x.nodeId, y.nodeId)
          });
        let actual =
          arr1
          ->M.fromArray(o => o.nodeId, o => o.parentNodeId)
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
      },
    )
  })
});
