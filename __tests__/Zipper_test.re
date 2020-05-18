open Test_utils;
module Z = Zipper.Make(G);

let _ = (); //weird bug in reason-mode reason-paren-level

describe("can make and move around", () => {
  //  1
  // 2 3 5
  //   4
  let id5 = ID.create("5");
  let g =
    StandardGraph.(
      makeGraph()
      ->G.addNodeUnder(
          id5,
          {one: 5, two: "five"},
          id1->I.convertFocusToParent,
        )
    );

  it("can make", () => {
    let z = Z.create(g, StandardGraph.id1);
    [%log.debug z->Option.mapWithDefault("", Z.toString); ("", "")];
    z->Option.map(zz => zz->Z.focus->ID.toString) |> Assert.equal("1"->Some);
  });

  it("can make in middle and move", () => {
    let z = Z.create(g, StandardGraph.id3)->Option.flatMap(Z.right);
    [%log.debug z->Option.mapWithDefault("", Z.toString); ("", "")];
    z->Option.map(zz => zz->Z.focus->ID.toString) |> Assert.equal("5"->Some);
  });

  it("can move right", () => {
    let z1 = Z.create(g, StandardGraph.id2)->Option.flatMap(Z.right);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(Some("3"));
  });

  it("can move right off end", () => {
    let z1 =
      Z.create(g, StandardGraph.id3)
      ->Option.flatMap(Z.right)
      ->Option.flatMap(Z.right)
      ->Option.flatMap(Z.right)
      ->Option.flatMap(Z.right);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(Some("5"));
  });

  it("can move left", () => {
    let z1 = Z.create(g, id5)->Option.flatMap(Z.left);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(Some("3"));
  });

  it("can move left off end", () => {
    let z1 =
      Z.create(g, id5)
      ->Option.flatMap(Z.left)
      ->Option.flatMap(Z.left)
      ->Option.flatMap(Z.left)
      ->Option.flatMap(Z.left)
      ->Option.flatMap(Z.left);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(Some("2"));
  });

  it("can move up", () => {
    let z1 = Z.create(g, StandardGraph.id4)->Option.flatMap(Z.up);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(Some("3"));
  });

  it("can move up off top", () => {
    let z1 =
      Z.create(g, StandardGraph.id4)
      ->Option.flatMap(Z.up)
      ->Option.flatMap(Z.up)
      ->Option.flatMap(Z.up)
      ->Option.flatMap(Z.up)
      ->Option.flatMap(Z.up);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(None);
  });

  it("can move down", () => {
    let z1 = Z.create(g, StandardGraph.id3)->Option.flatMap(Z.down);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(Some("4"));
  });

  it("can move down off bottom", () => {
    let z1 =
      Z.create(g, StandardGraph.id4)
      ->Option.flatMap(Z.down)
      ->Option.flatMap(Z.down)
      ->Option.flatMap(Z.down)
      ->Option.flatMap(Z.down)
      ->Option.flatMap(Z.down);
    [%log.debug z1->Option.mapWithDefault("", Z.toString); ("", "")];
    z1->Option.map(d => d->Z.focus->ID.toString) |> Assert.equal(Some("4"));
  });
});
