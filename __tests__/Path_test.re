open Test_utils;
let _ = (); //weird bug in reason-mode reason-paren-level

describe("construction", () => {
  let p = P.empty();

  it("rootOfEmptyIsNone", () => {
    p->P.root |> Assert.equal(None)
  });

  it("parentOfEmptyIsNone", () => {
    p->P.parent |> Assert.equal(None)
  });

  let p = P.fromList(["parent", "root"]);
  it("canMakeFromList", () => {
    let id = Identity.ParentId.create("parent");
    p->P.parent->Option.getExn |> Assert.equal(id);
  });

  it("canMakeFromList1", () => {
    let id = Identity.ParentId.create("root");
    p->P.root->Option.getExn |> Assert.equal(id);
  });

  let p = P.fromList(["parent1", "parent2", "root"]);
  it("pathUpToRoot", () => {
    let ls = ["parent1", "parent2", "root"];
    let ps = ls->List.map(Identity.ParentId.create);
    let qs = p->P.pathToRoot;
    let deepEq = Pervasives.(===);
    List.eq(ps, qs, deepEq) |> Assert.equal(true);
  });

  it("pathFromRoot", () => {
    let ls = ["root", "parent2", "parent1"];
    let ps = ls->List.map(Identity.ParentId.create);
    let qs = p->P.pathFromRoot;
    let deepEq = Pervasives.(===);
    List.eq(ps, qs, deepEq) |> Assert.equal(true);
  });
});

describe("moving", () => {
  it("canMoveUp", () => {
    let p = P.fromList(["parent1", "parent2", "root"]);
    let pUp = P.fromList(["parent2", "root"]);
    p->P.moveUp->P.eq(pUp) |> Assert.equal(true);
  });

  it("canMoveUpEmpty", () => {
    let p = P.empty();
    let pUp = P.fromList([]);
    p->P.moveUp->P.eq(pUp) |> Assert.equal(true);
  });
  /* it("canMoveDown", () => { */
  /*   let p = P.fromList(["parent1", "parent2", "root"]); */
  /*   let pUp = P.fromList(["parent1", "parent2"]); */
  /*   (p->P.moveDown->P.eq(pUp)) |> Assert.equal(true); */
  /* }); */
  /* it("canMoveDownEmpty", () => { */
  /*   let p = P.empty(); */
  /*   let pUp = P.fromList([]); */
  /*   (p->P.moveDown->P.eq(pUp)) |> Assert.equal(true); */
  /* }); */
});

describe("equality", () => {
  it("samePath", () => {
    let p = P.fromList(["parent1", "parent2", "root"]);
    let p2 = P.fromList(["parent1", "parent2", "root"]);
    p->P.eq(p2) |> Assert.equal(true);
  });

  it("notSamePath", () => {
    let p = P.fromList(["parent1", "parent2", "root"]);
    let pUp = P.fromList(["parent3", "root"]);
    p->P.eq(pUp) |> Assert.equal(false);
  });
});

describe("append", () => {
  let p = P.fromList(["parent1", "parent2"]);
  let p1 = P.fromList(["child1", "parent1", "parent2"]);
  it("canAppend", () => {
    let q = p->P.append("child1"->Identity.ParentId.create);
    q->P.eq(p1) |> Assert.equal(true);
  });
});

describe("removeElement", () => {
  let p = P.fromList(["child1", "parent1", "parent2"]);
  let p1 = P.fromList(["child1", "parent2"]);
  it("canRemove", () => {
    let q = p->P.removeElement("parent1"->Identity.ParentId.create);
    q->P.eq(p1) |> Assert.equal(true);
  });
});

describe("concat", () => {
  let p = P.fromList(["child1", "parent1", "parent2"]);
  let p1 = P.fromList(["parent3", "parent4"]);
  let p2 = P.fromList(["child1", "parent1", "parent2", "parent3", "parent4"]);
  it("canConcat", () => {
    let q = p->P.concat(p1);
    q->P.eq(p2) |> Assert.equal(true);
  });
});
