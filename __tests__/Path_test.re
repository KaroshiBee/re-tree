open Jest;
module M = Path;

describe("construction", () => {
  open Expect;
  open! Expect.Operators;

  let p = M.Parents.empty();

  test("rootOfEmptyIsNone", () => {
    expect(p->M.Parents.root) === None
  });

  test("parentOfEmptyIsNone", () => {
    expect(p->M.Parents.parent) === None
  });

  let p = M.Parents.fromList(["parent", "root"]);
  test("canMakeFromList", () => {
    let id = Identity.ParentId.create("parent");
    expect(p->M.Parents.parent->Option.getExn) === id;
  });

  test("canMakeFromList1", () => {
    let id = Identity.ParentId.create("root");
    expect(p->M.Parents.root->Option.getExn) === id;
  });

  let p = M.Parents.fromList(["parent1", "parent2", "root"]);
  test("pathUpToRoot", () => {
    let ls = ["parent1", "parent2", "root"];
    let ps = ls->List.map(Identity.ParentId.create);
    let qs = p->M.Parents.pathToRoot;
    let deepEq = Pervasives.(===);
    expect(List.eq(ps, qs, deepEq)) |> toBe(true);
  });

  test("pathFromRoot", () => {
    let ls = ["root", "parent2", "parent1"];
    let ps = ls->List.map(Identity.ParentId.create);
    let qs = p->M.Parents.pathFromRoot;
    let deepEq = Pervasives.(===);
    expect(List.eq(ps, qs, deepEq)) |> toBe(true);
  });
});

describe("moving", () => {
  open Expect;
  open! Expect.Operators;

  test("canMoveUp", () => {
    let p = M.Parents.fromList(["parent1", "parent2", "root"]);
    let pUp = M.Parents.fromList(["parent2", "root"]);
    expect(p->M.Parents.moveUp->M.Parents.eq(pUp)) |> toBe(true);
  });

  test("canMoveUpEmpty", () => {
    let p = M.Parents.empty();
    let pUp = M.Parents.fromList([]);
    expect(p->M.Parents.moveUp->M.Parents.eq(pUp)) |> toBe(true);
  });

  test("canMoveDown", () => {
    let p = M.Parents.fromList(["parent1", "parent2", "root"]);
    let pUp = M.Parents.fromList(["parent1", "parent2"]);
    expect(p->M.Parents.moveDown->M.Parents.eq(pUp)) |> toBe(true);
  });

  test("canMoveDownEmpty", () => {
    let p = M.Parents.empty();
    let pUp = M.Parents.fromList([]);
    expect(p->M.Parents.moveDown->M.Parents.eq(pUp)) |> toBe(true);
  });
});

describe("equality", () => {
  open Expect;
  open! Expect.Operators;

  test("samePath", () => {
    let p = M.Parents.fromList(["parent1", "parent2", "root"]);
    let p2 = M.Parents.fromList(["parent1", "parent2", "root"]);
    expect(p->M.Parents.eq(p2)) |> toBe(true);
  });

  test("notSamePath", () => {
    let p = M.Parents.fromList(["parent1", "parent2", "root"]);
    let pUp = M.Parents.fromList(["parent3", "root"]);
    expect(p->M.Parents.eq(pUp)) |> toBe(false);
  });
});

describe("append", () => {
  open Expect;

  let p = M.Parents.fromList(["parent1", "parent2"]);
  let p1 = M.Parents.fromList(["child1", "parent1", "parent2"]);
  test("canAppend", () => {
    let q = p->M.Parents.append("child1"->Identity.ParentId.create);
    expect(q->M.Parents.eq(p1)) |> toBe(true);
  });
});

describe("removeElement", () => {
  open Expect;

  let p = M.Parents.fromList(["child1", "parent1", "parent2"]);
  let p1 = M.Parents.fromList(["child1", "parent2"]);
  test("canRemove", () => {
    let q = p->M.Parents.removeElement("parent1"->Identity.ParentId.create);
    expect(q->M.Parents.eq(p1)) |> toBe(true);
  });
});

describe("concat", () => {
  open Expect;

  let p = M.Parents.fromList(["child1", "parent1", "parent2"]);
  let p1 = M.Parents.fromList(["parent3", "parent4"]);
  let p2 =
    M.Parents.fromList([
      "child1",
      "parent1",
      "parent2",
      "parent3",
      "parent4",
    ]);
  test("canConcat", () => {
    let q = p->M.Parents.concat(p1);
    expect(q->M.Parents.eq(p2)) |> toBe(true);
  });
});
