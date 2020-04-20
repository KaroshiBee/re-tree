open BsMocha.Mocha;
module Assert = BsMocha.Assert;

module I = Retree.Identity;
module PID = I.ParentId;
module M = Retree.Path.T;

describe("construction", () => {
  let p = M.empty();

  it("rootOfEmptyIsNone", () => {
    p->M.root |> Assert.equal(None)
  });

  it("parentOfEmptyIsNone", () => {
    p->M.parent |> Assert.equal(None)
  });

  let p = M.fromList(["parent", "root"]);
  it("canMakeFromList", () => {
    let id = PID.create("parent");
    p->M.parent->Option.getExn |> Assert.equal(id);
  });

  it("canMakeFromList1", () => {
    let id = PID.create("root");
    p->M.root->Option.getExn |> Assert.equal(id);
  });

  let p = M.fromList(["parent1", "parent2", "root"]);
  it("pathUpToRoot", () => {
    let ls = ["parent1", "parent2", "root"];
    let ps = ls->List.map(PID.create);
    let qs = p->M.pathToRoot;
    let deepEq = Pervasives.(===);
    List.eq(ps, qs, deepEq) |> Assert.equal(true);
  });

  it("pathFromRoot", () => {
    let ls = ["root", "parent2", "parent1"];
    let ps = ls->List.map(PID.create);
    let qs = p->M.pathFromRoot;
    let deepEq = Pervasives.(===);
    List.eq(ps, qs, deepEq) |> Assert.equal(true);
  });
});

describe("moving", () => {
  it("canMoveUp", () => {
    let p = M.fromList(["parent1", "parent2", "root"]);
    let pUp = M.fromList(["parent2", "root"]);
    p->M.moveUp->M.eq(pUp) |> Assert.equal(true);
  });

  it("canMoveUpEmpty", () => {
    let p = M.empty();
    let pUp = M.fromList([]);
    p->M.moveUp->M.eq(pUp) |> Assert.equal(true);
  });
  /* it("canMoveDown", () => { */
  /*   let p = M.fromList(["parent1", "parent2", "root"]); */
  /*   let pUp = M.fromList(["parent1", "parent2"]); */
  /*   (p->M.moveDown->M.eq(pUp)) |> Assert.equal(true); */
  /* }); */
  /* it("canMoveDownEmpty", () => { */
  /*   let p = M.empty(); */
  /*   let pUp = M.fromList([]); */
  /*   (p->M.moveDown->M.eq(pUp)) |> Assert.equal(true); */
  /* }); */
});

describe("equality", () => {
  it("samePath", () => {
    let p = M.fromList(["parent1", "parent2", "root"]);
    let p2 = M.fromList(["parent1", "parent2", "root"]);
    p->M.eq(p2) |> Assert.equal(true);
  });

  it("notSamePath", () => {
    let p = M.fromList(["parent1", "parent2", "root"]);
    let pUp = M.fromList(["parent3", "root"]);
    p->M.eq(pUp) |> Assert.equal(false);
  });
});

describe("append", () => {
  let p = M.fromList(["parent1", "parent2"]);
  let p1 = M.fromList(["child1", "parent1", "parent2"]);
  it("canAppend", () => {
    let q = p->M.append("child1"->PID.create);
    q->M.eq(p1) |> Assert.equal(true);
  });
});

describe("removeElement", () => {
  let p = M.fromList(["child1", "parent1", "parent2"]);
  let p1 = M.fromList(["child1", "parent2"]);
  it("canRemove", () => {
    let q = p->M.removeElement("parent1"->PID.create);
    q->M.eq(p1) |> Assert.equal(true);
  });
});

describe("concat", () => {
  let p = M.fromList(["child1", "parent1", "parent2"]);
  let p1 = M.fromList(["parent3", "parent4"]);
  let p2 = M.fromList(["child1", "parent1", "parent2", "parent3", "parent4"]);
  it("canConcat", () => {
    let q = p->M.concat(p1);
    q->M.eq(p2) |> Assert.equal(true);
  });
});
