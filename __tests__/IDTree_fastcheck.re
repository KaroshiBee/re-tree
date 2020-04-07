open BsMocha.Mocha;
module Assert = BsMocha.Assert;
open BsFastCheck.Arbitrary;
open BsFastCheck.Property.Sync;
open BsFastCheck.Arbitrary.Combinators;

module M = IDTree.T;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

module IDs = ID_fastcheck.Arbitrary;
module Paths = Path_fastcheck.Arbitrary;

module Arbitrary = {
  let depth1 =
    IDs.id
    ->Derive.map(M.emptySubtree)
    ->Derive.chain(t => {
        let pid = t->M.myId->ID.toString;
        let pth = P.fromPathToRootList([pid]);
        list(IDs.id)
        ->Derive.map(ids =>
            ids->List.reduce(t, (tree, i) => tree->M.addChild(pth, i))
          );
      });

  let depth2 =
    IDs.id
    ->Derive.map(M.emptySubtree)
    ->Derive.chain(t => {
        let pid = t->M.myId;
        let pth = P.fromPathToRootList([pid->ID.toString]);
        list(depth1)
        ->Derive.map(children =>
            children->List.reduce(t, (tree, childtree) =>
              tree->M.addSubtree(childtree->M.myId, pth, childtree)
            )
          );
      });

  // generate fingery trees - lots of straight down deep branches
  // NOTE i dont mean finger-trees
  let fingersN_ = (n, empty) =>
    tuple2(
      IDs.id,
      Paths.paths(n, 10)
    )
    ->Derive.map(tup => {
        let id = tup->fst;
        let ls = tup->snd;
        ls->List.reduce(
          empty,
          (t, pth) => {
            t->M.addChild(pth, id);
          },
        );
      });

  let fingersN = n => fingersN_(n, M.empty());
  let fingersN_subtree = (n, name) => fingersN_(n, M.emptySubtree(name->ID.create));
};

module Utils = {
  let equalMaps = (expected, actual) => {
    expected->Map.eq(actual, (x, y) => {
      x->M.toString == y->M.toString
    });
  };
}

describe("IDTree: construction", () => {
  it("constructs", () => {
    assertProperty1(
      Arbitrary.fingersN(4),
      t => {
//        [%log.debug "tree: " ++ t->M.toString; ("", "")];
        t->M.getAllIds->Array.size > 0;
      },
    )
  })
});

describe("IDTree: removing nodes", () => {
  let remove = (n, remover)  => assertProperty1(
      Arbitrary.fingersN(n),
      t => {
        /* [%log.debug "before: " ++ t->M.toString; ("", "")]; */
        let ids = M.getAllPaths(t);
        let t1 = ids->Array.reduce(t, (tree, cpath) => {
          let cid = cpath->fst;
          let pth = cpath->snd;
          /* [%log.debug cid->CID.toString ++ ": " ++ pth->P.toString; ("","")]; */
          tree->remover(pth, cid);
        });
        /* [%log.debug "after: " ++ t1->M.toString; ("", "")]; */
        t1->M.getAllIds->Array.size == 0;
      });

  it("removing all children (small trees) should leave empty tree", () => {
    remove(2, M.removeChild);
  });

  it("removing all children (big trees) should leave empty tree", () => {
    remove(10, M.removeChild);
  });

  it("removing all subtrees (small trees) should leave empty tree", () => {
    remove(2, M.removeSubtree);
  });

  it("removing all subtrees (big trees) should leave empty tree", () => {
    remove(10, M.removeSubtree);
  });

  let removeSubtree = (n, s1) => assertProperty1(
      Arbitrary.fingersN_subtree(n, s1),
      t => {
        let expected = t->M.children;
        let id = s1->ID.create;
        let cid = s1->CID.create;
        let tt = M.empty()->M.addSubtree(id, P.empty(), t);
        // [%log.debug "before: " ++ tt->M.toString; ("", "")];
        let ttt = tt->M.removeChild(P.empty(), cid);
        // [%log.debug "after: " ++ ttt->M.toString; ("", "")];
        let actual = ttt->M.children;
        Utils.equalMaps(expected, actual);
      }
  );

  it("removing child should bring subtree up a level (small)", () => {
    removeSubtree(2, "test1");
  });

  it("removing child should bring subtree up a level (large)", () => {
    removeSubtree(10, "test1");
  });

})

describe("IDTree: removing then adding nodes/subtrees & vice versa", () => {
  let remove = (gen)  => {
      gen->Derive.chain(t => {
        /* [%log.debug "before: " ++ t->M.toString; ("", "")]; */
        let i = integerRange(1, t->M.getAllIds->Array.size-1);
        tuple2(constant(t), i)
      })->Derive.chain( ((t, i)) => {
        let (id, pth) = M.getAllPaths(t)->Array.getExn(i);
        let sub = t->M.getSubtree(pth, id->I.convertChildToFocus)->constant;
        let tt = t->M.removeSubtree(pth, id)->constant;
        tuple5(t->constant, id->constant, pth->constant, sub, tt);
      });
  };

  let add = (gen)  => {
      gen->Derive.chain( ((t, cid, pth, sub, tt)) => {
        /*[%log.debug "before: " ++ t->M.toString; ("", "")]; */
        let id = cid->I.convertChildToFocus;
        tuple2(t->constant, tt->M.addSubtree(id, pth, sub->Option.getWithDefault(M.emptySubtree(id)))->constant);
      })
  }

    it("IDTree: remove then add back gives same as start", () => {
      assertProperty1(
        Arbitrary.fingersN(2)->remove->add,
        ((expected, actual)) => {
          /* [%log.debug "expected: " ++ expected->M.toString; ("", "")]; */
          /* [%log.debug "actual: " ++ actual->M.toString; ("", "")]; */
          expected->M.eq(actual);
        }
      )
    });

  // NOTE remove then add child is not same as start as children of child get moved up

})
