open BsMocha.Mocha;
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
      arrayWithLength(arrayWithLength(IDs.idString, 1, 10), 1, 10),
    )
    ->Derive.map(tup => {
        let id = tup->fst;
        let ls = tup->snd;
        ls->Array.reduce(
          M.empty(),
          (t, arrPath) => {
            let pth = P.fromRootToPathList(arrPath->List.fromArray);
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
        [%log.debug t->M.toString; ("", "")];
        t->M.getAllIds->Array.size > 0;
      },
    )
  })
});
