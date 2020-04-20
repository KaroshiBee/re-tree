open BsMocha.Mocha;
open BsFastCheck.Arbitrary;
open BsFastCheck.Property.Sync;
open BsFastCheck.Arbitrary.Combinators;

module I = Retree.Identity;
module PID = I.ParentId;
module M = Retree.Path.T;

module IDs = ID_fastcheck.Arbitrary;

let idString = IDs.idString;

describe("Path: construction", () => {
  it("fromPathToRoot is reverse fromRootToPath", () => {
    assertProperty1(
      list(idString),
      ls => {
        let pth1 = M.fromPathToRootList(ls);
        let pth2 = M.fromRootToPathList(ls->List.reverse);
        M.eq(pth1, pth2);
      },
    )
  });

  it("path is same size as input list", () => {
    assertProperty1(
      list(idString),
      ls => {
        let n = M.fromList(ls)->M.size;
        let m = List.size(ls);
        n == m;
      },
    )
  });

  it("concat two path is same as making from concat lists", () => {
    assertProperty2(
      list(idString),
      list(idString),
      (ls1, ls2) => {
        let pth1 = M.fromList(ls1);
        let pth2 = M.fromList(ls2);
        let pth3 = M.fromList(List.concat(ls1, ls2));
        M.eq(pth3, M.concat(pth1, pth2));
      },
    )
  });
});

describe("Path: append-remove", () => {
  it("append-remove same as starting", () => {
    assertProperty2(
      IDs.pid,
      list(idString),
      (pid, ls_) => {
        let s = pid->PID.toString;
        let ls = ls_->List.keep(l => l != s);
        //        [%log.debug pid->PID.toString; ("", "")];
        let pth1 = M.fromList(ls)->M.append(pid)->M.removeElement(pid);
        //        [%log.debug pth1->M.toString; ("", "")];
        let pth2 = M.fromList(ls);
        //        [%log.debug pth2->M.toString; ("", "")];
        let e = M.eq(pth1, pth2);
        /* [%log.debug */
        /*   "s: " */
        /*   ++ s */
        /*   ++ ", ls: [" */
        /*   ++ (ls |> String.concat(",")) */
        /*   ++ "] is ok: " */
        /*   ++ e->string_of_bool; */
        /*   ("", "") */
        /* ]; */
        e;
      },
    )
  });

  it("remove-append same as starting", () => {
    assertProperty2(
      IDs.pid,
      list(idString),
      (pid, ls_) => {
        let s = pid->PID.toString;
        let ls = ls_->List.keep(l => l != s);
        //        [%log.debug pid->PID.toString; ("", "")];
        let pth1 =
          M.fromList([s, ...ls])->M.removeElement(pid)->M.append(pid);
        //        [%log.debug pth1->M.toString; ("", "")];
        let pth2 = M.fromList([s, ...ls]);
        //        [%log.debug pth2->M.toString; ("", "")];
        let e = M.eq(pth1, pth2);
        /* [%log.debug */
        /*   "s: " */
        /*   ++ s */
        /*   ++ ", ls: [" */
        /*   ++ (ls |> String.concat(",")) */
        /*   ++ "] is ok: " */
        /*   ++ e->string_of_bool; */
        /*   ("", "") */
        /* ]; */
        e;
      },
    )
  });

  it("remove removes all occurances", () => {
    assertProperty4(
      IDs.pid,
      list(idString),
      list(idString),
      list(idString),
      (pid, ls1, ls2, ls3) => {
        let s = pid->PID.toString;
        let ls1 = ls1->List.keep(l => l != s);
        let ls2 = ls2->List.keep(l => l != s);
        let ls3 = ls3->List.keep(l => l != s);
        //        [%log.debug pid->PID.toString; ("", "")];
        let pth1 =
          M.fromList(List.concatMany([|ls1, [s], ls2, [s], ls3|]))
          ->M.removeElement(pid);
        //        [%log.debug pth1->M.toString; ("", "")];
        let pth2 = M.fromList(List.concatMany([|ls1, ls2, ls3|]));
        //        [%log.debug pth2->M.toString; ("", "")];
        let e = M.eq(pth1, pth2);
        e;
      },
    )
  });
});

describe("Path: root/parent/moveup", () => {
  it("root of non empty is always the same", () => {
    assertProperty2(
      idString,
      list(idString),
      (s, ls) => {
        // NOTE root to path  here
        let pth = M.fromRootToPathList([s, ...ls]);
        let root = pth->M.root->Option.getExn;
        root->PID.toString == s;
      },
    )
  });

  it("parent of non empty is always next one", () => {
    assertProperty2(
      idString,
      list(idString),
      (s, ls) => {
        // NOTE path to root here
        let pth = M.fromPathToRootList([s, ...ls]);
        let parent = pth->M.parent->Option.getExn;
        let e = parent->PID.toString == s;
        /* [%log.debug */
        /*   pth->M.toString */
        /*   ++ " with parent: " */
        /*   ++ parent->PID.toString */
        /*   ++ " is ok " */
        /*   ++ e->string_of_bool; */
        /*   ("", "") */
        /* ]; */
        e;
      },
    )
  });

  it("moveUp of non empty is always rest of path", () => {
    assertProperty2(
      idString,
      list(idString),
      (s, ls) => {
        // NOTE path to root here
        let pth = M.fromPathToRootList([s, ...ls]);
        let pth1 = M.fromPathToRootList(ls);
        let pathUp = pth->M.moveUp;
        let e = M.eq(pth1, pathUp);
        /* [%log.debug */
        /*   pth->M.toString */
        /*   ++ " with parent: " */
        /*   ++ parent->PID.toString */
        /*   ++ " is ok " */
        /*   ++ e->string_of_bool; */
        /*   ("", "") */
        /* ]; */
        e;
      },
    )
  });
});

module Arbitrary = {
  // at most n length path
  let path = n =>
    setWithLength(IDs.idString, 1, n, ~comparator=(==))
    ->Derive.map(s => s->List.fromArray->M.fromList);
  // at most m paths of length at least n
  let paths = (n, m) =>
    setWithLength(path(n), 1, m, ~comparator=M.eq)
    ->Derive.map(s => s->List.fromArray);
};
