open Jest;
module M = Path.T;

describe("construction", () => {
  open Expect;
  open! Expect.Operators;

  let p = M.empty();

  test("rootOfEmptyIsNone", () => {
    expect(p->M.root) === None
  });

  test("parentOfEmptyIsNone", () => {
    expect(p->M.parent) === None
  });

  let p = M.fromList(["parent", "root"]);
  test("canMakeFromList", () => {
    let id = Identity.ParentId.create("parent");
    expect(p->M.parent->Option.getExn) === id;
  });

  test("canMakeFromList1", () => {
    let id = Identity.ParentId.create("root");
    expect(p->M.root->Option.getExn) === id;
  });

  let p = M.fromList(["parent1", "parent2", "root"]);
  test("pathUpToRoot", () => {
    let ls = ["parent1", "parent2", "root"];
    let ps = ls->List.map(Identity.ParentId.create);
    let qs = p->M.pathToRoot;
    let deepEq = Pervasives.(===);
    expect(List.eq(ps, qs, deepEq)) |> toBe(true);
  });

  test("pathFromRoot", () => {
    let ls = ["root", "parent2", "parent1"];
    let ps = ls->List.map(Identity.ParentId.create);
    let qs = p->M.pathFromRoot;
    let deepEq = Pervasives.(===);
    expect(List.eq(ps, qs, deepEq)) |> toBe(true);
  });
});

describe("moving", () => {
  open Expect;
  open! Expect.Operators;

  test("canMoveUp", () => {
    let p = M.fromList(["parent1", "parent2", "root"]);
    let pUp = M.fromList(["parent2", "root"]);
    expect(p->M.moveUp->M.eq(pUp)) |> toBe(true);
  });

  test("canMoveUpEmpty", () => {
    let p = M.empty();
    let pUp = M.fromList([]);
    expect(p->M.moveUp->M.eq(pUp)) |> toBe(true);
  });

  test("canMoveDown", () => {
    let p = M.fromList(["parent1", "parent2", "root"]);
    let pUp = M.fromList(["parent1", "parent2"]);
    expect(p->M.moveDown->M.eq(pUp)) |> toBe(true);
  });

  test("canMoveDownEmpty", () => {
    let p = M.empty();
    let pUp = M.fromList([]);
    expect(p->M.moveDown->M.eq(pUp)) |> toBe(true);
  });
});

describe("equality", () => {
  open Expect;
  open! Expect.Operators;

  test("samePath", () => {
    let p = M.fromList(["parent1", "parent2", "root"]);
    let p2 = M.fromList(["parent1", "parent2", "root"]);
    expect(p->M.eq(p2)) |> toBe(true);
  });

  test("notSamePath", () => {
    let p = M.fromList(["parent1", "parent2", "root"]);
    let pUp = M.fromList(["parent3", "root"]);
    expect(p->M.eq(pUp)) |> toBe(false);
  });
});

describe("append", () => {
  open Expect;

  let p = M.fromList(["parent1", "parent2"]);
  let p1 = M.fromList(["child1", "parent1", "parent2"]);
  test("canAppend", () => {
    let q = p->M.append("child1"->Identity.ParentId.create);
    expect(q->M.eq(p1)) |> toBe(true);
  });
});

describe("removeElement", () => {
  open Expect;

  let p = M.fromList(["child1", "parent1", "parent2"]);
  let p1 = M.fromList(["child1", "parent2"]);
  test("canRemove", () => {
    let q = p->M.removeElement("parent1"->Identity.ParentId.create);
    expect(q->M.eq(p1)) |> toBe(true);
  });
});

describe("concat", () => {
  open Expect;

  let p = M.fromList(["child1", "parent1", "parent2"]);
  let p1 = M.fromList(["parent3", "parent4"]);
  let p2 = M.fromList(["child1", "parent1", "parent2", "parent3", "parent4"]);
  test("canConcat", () => {
    let q = p->M.concat(p1);
    expect(q->M.eq(p2)) |> toBe(true);
  });
});
