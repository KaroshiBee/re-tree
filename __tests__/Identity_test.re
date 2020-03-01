open Jest;
module I = Identity;

describe("construction", () => {
  open Expect;

  test("canMakeFromString", () => {
    module Id1 =
      I.Make({});
    let id1 = Id1.create("hello");
    expect(id1->Id1.toString) |> toEqual("hello");
  });

  test("canMakeMap", () => {
    module Id =
      I.Make({});
    let key = Id.create("key");
    let mp = Id.Map.make()->Map.set(key, 1);
    expect(mp->Map.get(key)) |> toEqual(Some(1));
  });

  test("canMakeMap2", () => {
    module Id =
      I.Make({});
    let key = Id.create("key");
    let mp = Id.Map.make()->Map.set(key, 1);
    expect(mp->Map.get(Id.create("notthere"))) |> toEqual(None);
  });
  // this doesnt compile - which is what we want
  /* test("canMakeMap2", () => { */
  /*   module Id = */
  /*     I.Make({}); */
  /*   let key = Id.create("key"); */
  /*   module Id2 = */
  /*     I.Make({}); */
  /*   let mp = Id.Map.make()->Map.set(key, 1); */
  /*   expect(mp->Map.get(Id2.create("key"))) |> toEqual(Some(1)); */
  /* }); */
});

describe("conversion", () => {
  open Expect;

  test("childToParent", () => {
    let id1 = I.ChildId.create("child");
    expect(id1->I.convertChildToParent->I.ParentId.toString)
    |> toEqual("child");
  });

  test("parentToChild", () => {
    let id1 = I.ParentId.create("parent");
    expect(id1->I.convertParentToChild->I.ChildId.toString)
    |> toEqual("parent");
  });

  test("focusToParent", () => {
    let id1 = I.FocusId.create("id");
    expect(id1->I.convertFocusToParent->I.ParentId.toString) |> toEqual("id");
  });

  test("focusToChild", () => {
    let id1 = I.FocusId.create("id");
    expect(id1->I.convertFocusToChild->I.ChildId.toString) |> toEqual("id");
  });

  test("childToFocus", () => {
    let id1 = I.ChildId.create("child");
    expect(id1->I.convertChildToFocus->I.FocusId.toString)
    |> toEqual("child");
  });

  test("parentToFocus", () => {
    let id1 = I.ParentId.create("parent");
    expect(id1->I.convertParentToFocus->I.FocusId.toString)
    |> toEqual("parent");
  });

  test("canInsertChildIntoParentMap", () => {
    let key = I.ParentId.create("key1");
    let mp = I.ParentId.Map.make()->Map.set(key, 1);
    let childKey = I.ChildId.create("key2");
    let mp2 = mp->Map.set(I.convertChildToParent(childKey), 2);
    expect(mp2->Map.get(I.ParentId.create("key2"))) |> toEqual(Some(2));
  });
});
