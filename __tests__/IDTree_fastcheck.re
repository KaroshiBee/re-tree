open Test_utils;
open BsFastCheck.Arbitrary;
open BsFastCheck.Property.Sync;
open BsFastCheck.Arbitrary.Combinators;

module IDs = ID_fastcheck.Arbitrary;
module Paths = Path_fastcheck.Arbitrary;

module Arbitrary = {
  let depth1 =
    IDs.id
    ->Derive.map(T.emptySubtree)
    ->Derive.chain(t => {
        let pid = t->T.myId->ID.toString;
        let pth = P.fromPathToRootList([pid]);
        list(IDs.id)
        ->Derive.map(ids =>
            ids->List.reduce(t, (tree, i) => tree->T.addChild(pth, i))
          );
      });

  let depth2 =
    IDs.id
    ->Derive.map(T.emptySubtree)
    ->Derive.chain(t => {
        let pid = t->T.myId;
        let pth = P.fromPathToRootList([pid->ID.toString]);
        list(depth1)
        ->Derive.map(children =>
            children->List.reduce(t, (tree, childtree) =>
              tree->T.addSubtree(childtree->T.myId, pth, childtree)
            )
          );
      });

  // generate fingery trees - lots of straight down deep branches
  // NOTE i dont mean finger-trees
  let fingersN_ = (n, empty) =>
    tuple2(IDs.id, Paths.paths(n, 10))
    ->Derive.map(tup => {
        let id = tup->fst;
        let ls = tup->snd;
        ls->List.reduce(empty, (t, pth) => {t->T.addChild(pth, id)});
      });

  let fingersN = n => fingersN_(n, T.empty());
  let fingersN_subtree = (n, name) =>
    fingersN_(n, T.emptySubtree(name->ID.create));
};

module Utils = {
  let equalMaps = (expected, actual) => {
    expected->Map.eq(actual, (x, y) => {x->T.toString == y->T.toString});
  };
};

describe("IDTree: construction", () => {
  it("constructs", () => {
    assertProperty1(Arbitrary.fingersN(4), t => {
      //        [%log.debug "tree: " ++ t->T.toString; ("", "")];
      t->T.getAllIds->Array.size > 0
    })
  })
});

describe("IDTree: removing nodes", () => {
  let remove = (n, remover) =>
    assertProperty1(
      Arbitrary.fingersN(n),
      t => {
        /* [%log.debug "before: " ++ t->T.toString; ("", "")]; */
        let ids = T.getAllPaths(t);
        let t1 =
          ids->Array.reduce(
            t,
            (tree, cpath) => {
              let cid = cpath->fst;
              let pth = cpath->snd;
              /* [%log.debug cid->CID.toString ++ ": " ++ pth->P.toString; ("","")]; */
              tree->remover(pth, cid);
            },
          );
        /* [%log.debug "after: " ++ t1->T.toString; ("", "")]; */
        t1->T.getAllIds->Array.size == 0;
      },
    );

  it("removing all children (small trees) should leave empty tree", () => {
    remove(2, T.removeChild)
  });

  it("removing all children (big trees) should leave empty tree", () => {
    remove(10, T.removeChild)
  });

  it("removing all subtrees (small trees) should leave empty tree", () => {
    remove(2, T.removeSubtree)
  });

  it("removing all subtrees (big trees) should leave empty tree", () => {
    remove(10, T.removeSubtree)
  });

  let removeSubtree = (n, s1) =>
    assertProperty1(
      Arbitrary.fingersN_subtree(n, s1),
      t => {
        let expected = t->T.children;
        let id = s1->ID.create;
        let cid = s1->CID.create;
        let tt = T.empty()->T.addSubtree(id, P.empty(), t);
        // [%log.debug "before: " ++ tt->T.toString; ("", "")];
        let ttt = tt->T.removeChild(P.empty(), cid);
        // [%log.debug "after: " ++ ttt->T.toString; ("", "")];
        let actual = ttt->T.children;
        Utils.equalMaps(expected, actual);
      },
    );

  it("removing child should bring subtree up a level (small)", () => {
    removeSubtree(2, "test1")
  });

  it("removing child should bring subtree up a level (large)", () => {
    removeSubtree(10, "test1")
  });
});

describe("IDTree: removing then adding nodes/subtrees & vice versa", () => {
  let removeThenAdd = gen => {
    gen
    ->Derive.chain(t => {
        /* [%log.debug "before: " ++ t->T.toString; ("", "")]; */
        let i = integerRange(1, t->T.getAllIds->Array.size - 1);
        tuple2(constant(t), i);
      })
    ->Derive.chain(((t, i)) => {
        let (id, pth) = T.getAllPaths(t)->Array.getExn(i);
        let sub = t->T.getSubtree(pth, id->I.convertChildToFocus)->constant;
        let tt = t->T.removeSubtree(pth, id)->constant;
        tuple5(t->constant, id->constant, pth->constant, sub, tt);
      })
    ->Derive.chain(((t, cid, pth, sub, tt)) => {
        /*[%log.debug "before: " ++ t->T.toString; ("", "")]; */
        let id = cid->I.convertChildToFocus;
        tuple2(
          t->constant,
          tt
          ->T.addSubtree(
              id,
              pth,
              sub->Option.getWithDefault(T.emptySubtree(id)),
            )
          ->constant,
        );
      });
  };

  it("IDTree: remove then add back gives same as start", () => {
    assertProperty1(
      Arbitrary.fingersN(10)->removeThenAdd, ((expected, actual)) => {
      /* [%log.debug "expected: " ++ expected->T.toString; ("", "")]; */
      /* [%log.debug "actual: " ++ actual->T.toString; ("", "")]; */
      expected->T.eq(actual)
    })
  });

  it("IDTree: remove then add back gives same as start (small)", () => {
    assertProperty1(
      Arbitrary.fingersN(2)->removeThenAdd, ((expected, actual)) => {
      /* [%log.debug "expected: " ++ expected->T.toString; ("", "")]; */
      /* [%log.debug "actual: " ++ actual->T.toString; ("", "")]; */
      expected->T.eq(actual)
    })
  });

  // NOTE remove then add child is not same as start as children of child get moved up

  let addThenRemove = (gen, n) => {
    gen
    ->Derive.chain(t => {
        /* [%log.debug "before: " ++ t->T.toString; ("", "")]; */
        let i = integerRange(1, t->T.getAllIds->Array.size - 1);
        tuple2(t->constant, i);
      })
    ->Derive.chain(((t, i)) => {
        let (_id, pth) = T.getAllPaths(t)->Array.getExn(i);
        tuple3(t->constant, IDs.id, pth->constant);
      })
    ->Derive.chain(((t, id, pth)) => {
        let tt = Arbitrary.fingersN_subtree(n, id->ID.toString);
        tuple4(t->constant, id->constant, pth->constant, tt);
      })
    ->Derive.chain(((t, id, pth, tt)) => {
        let ttt = t->T.addSubtree(id, pth, tt);
        tuple4(t->constant, id->constant, pth->constant, ttt->constant);
      })
    ->Derive.chain(((t, id, pth, _tt)) => {
        let tt = t->T.removeSubtree(pth, id->I.convertFocusToChild);
        tuple2(t->constant, tt->constant);
      });
  };
  it("IDTree: add then remove subtree gives same as start", () => {
    assertProperty1(
      Arbitrary.fingersN(10)->addThenRemove(10), ((expected, actual)) => {
      /* [%log.debug "expected: " ++ expected->T.toString; ("", "")]; */
      /* [%log.debug "actual: " ++ actual->T.toString; ("", "")]; */
      expected->T.eq(actual)
    })
  });

  it("IDTree: add then remove subtree gives same as start (small)", () => {
    assertProperty1(
      Arbitrary.fingersN(2)->addThenRemove(2), ((expected, actual)) => {
      /* [%log.debug "expected: " ++ expected->T.toString; ("", "")]; */
      /* [%log.debug "actual: " ++ actual->T.toString; ("", "")]; */
      expected->T.eq(actual)
    })
  });
});
