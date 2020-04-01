open BsMocha.Mocha;
open BsFastCheck.Arbitrary;
open BsFastCheck.Property.Sync;
open BsFastCheck.Arbitrary.Combinators;

module M = Path.T;

describe("PathToRootIsReverseRootToPath", () => {
  it("is", () => {
    let ap =
      assertProperty1(
        list(string()),
        ls => {
          let pth1 = M.fromPathToRootList(ls);
          let pth2 = M.fromRootToPathList(ls->List.reverse);
          M.eq(pth1, pth2);
        },
      );
    ();
  })
});
