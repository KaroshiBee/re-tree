open BsMocha.Mocha;
module Assert = BsMocha.Assert

module I = Identity;

describe("construction", () => {

  it("canMakeFromString", () => {
    module Id1 =
      I.Make({});
    let id1 = Id1.create("hello");
    (id1->Id1.toString) |> Assert.equal("hello");
  });

  it("canMakeMap", () => {
    module Id =
      I.Make({});
    let key = Id.create("key");
    let mp = Id.Map.make()->Map.set(key, 1);
    (mp->Map.get(key)) |> Assert.equal(Some(1));
  });

  it("canMakeMap2", () => {
    module Id =
      I.Make({});
    let key = Id.create("key");
    let mp = Id.Map.make()->Map.set(key, 1);
    (mp->Map.get(Id.create("notthere"))) |> Assert.equal(None);
  });
  // this doesnt compile - which is what we want
  /* it("canMakeMap2", () => { */
  /*   module Id = */
  /*     I.Make({}); */
  /*   let key = Id.create("key"); */
  /*   module Id2 = */
  /*     I.Make({}); */
  /*   let mp = Id.Map.make()->Map.set(key, 1); */
  /*   (mp->Map.get(Id2.create("key"))) |> Assert.equal(Some(1)); */
  /* }); */
});

describe("conversion", () => {

  it("childToParent", () => {
    let id1 = I.ChildId.create("child");
    (id1->I.convertChildToParent->I.ParentId.toString)
    |> Assert.equal("child");
  });

  it("parentToChild", () => {
    let id1 = I.ParentId.create("parent");
    (id1->I.convertParentToChild->I.ChildId.toString)
    |> Assert.equal("parent");
  });

  it("focusToParent", () => {
    let id1 = I.FocusId.create("id");
    (id1->I.convertFocusToParent->I.ParentId.toString) |> Assert.equal("id");
  });

  it("focusToChild", () => {
    let id1 = I.FocusId.create("id");
    (id1->I.convertFocusToChild->I.ChildId.toString) |> Assert.equal("id");
  });

  it("childToFocus", () => {
    let id1 = I.ChildId.create("child");
    (id1->I.convertChildToFocus->I.FocusId.toString)
    |> Assert.equal("child");
  });

  it("parentToFocus", () => {
    let id1 = I.ParentId.create("parent");
    (id1->I.convertParentToFocus->I.FocusId.toString)
    |> Assert.equal("parent");
  });

  it("canInsertChildIntoParentMap", () => {
    let key = I.ParentId.create("key1");
    let mp = I.ParentId.Map.make()->Map.set(key, 1);
    let childKey = I.ChildId.create("key2");
    let mp2 = mp->Map.set(I.convertChildToParent(childKey), 2);
    (mp2->Map.get(I.ParentId.create("key2"))) |> Assert.equal(Some(2));
  });
});
