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
        let pid = t->M.myId->Identity.FocusId.toString;
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
        let pth = P.fromPathToRootList([pid->Identity.FocusId.toString]);
        list(depth1)
        ->Derive.map(children =>
            children->List.reduce(t, (tree, childtree) =>
              tree->M.addSubtree(childtree->M.myId, pth, childtree)
            )
          );
      });

  // generate fingery trees - lots of straight down deep branches
  // NOTE i dont mean finger-trees
  let fingersN = n =>
    tuple2(
      IDs.id,
      Paths.paths(n, 10)
    )
    ->Derive.map(tup => {
        let id = tup->fst;
        let ls = tup->snd;
        ls->List.reduce(
          M.empty(),
          (t, pth) => {
            t->M.addChild(pth, id);
          },
        );
      });
};

describe("construction", () => {
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

describe("removing nodes", () => {
  let remove = (n, remover) => assertProperty1(
      Arbitrary.fingersN(n),
      t => {
//        [%log.debug "before: " ++ t->M.toString; ("", "")];
        let ids = M.getAllPaths(t);
        let t1 = ids->Array.reduce(t, (tree, cpath) => {
          let cid = cpath->fst;
          let pth = cpath->snd;
//          [%log.debug cid->CID.toString ++ ": " ++ pth->P.toString; ("","")];
          tree->remover(pth, cid);
        });
//        [%log.debug "after: " ++ t1->M.toString; ("", "")];
        t1->M.getAllIds->Array.size == 0;
      });

  it("removing all children (small trees) in order should leave empty tree", () => {
    remove(2, M.removeChild);
  })

  it("removing all children (big trees) in order should leave empty tree", () => {
    remove(10, M.removeChild);
  })

  it("removing all subtrees (small trees) in order should leave empty tree", () => {
    remove(2, M.removeSubtree);
  })

  it("removing all subtrees (big trees) in order should leave empty tree", () => {
    remove(10, M.removeSubtree);
  })

})
