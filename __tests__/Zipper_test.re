open Test_utils;
module Z = Zipper.Make(GF);

let _ = (); //weird bug in reason-mode reason-paren-level

//  1
// 2 3 5
//   4
let id5 = ID.create("5");
let g =
  FancyGraph.(
    makeGraph()
    ->GF.addNodeUnder(
        id5,
        {one: 5, two: "five"},
        id1->I.convertFocusToParent,
      )
  );

describe("can make and move around", () => {
  it("can make", () => {
    let z = Z.createAt(g, FancyGraph.id1);
    [%log.debug z->Z.mapWithDefault("", Z.toString); ("", "")];
    z->Z.map(zz => zz->Z.focus->ID.toString)->Z.getExn |> Assert.equal("1");
  });
  it("can make at root", () => {
    let z = Z.create(g);
    [%log.debug z->Z.mapWithDefault("FAILED TO MAKE", Z.toString); ("", "")];
    z->Z.map(zz => zz->Z.focus->ID.toString)->Z.getExn |> Assert.equal("1");
  });
  it("can make in middle and move", () => {
    let z = Z.createAt(g, FancyGraph.id3)->Z.flatMap(Z.right);
    [%log.debug z->Z.mapWithDefault("", Z.toString); ("", "")];
    z->Z.map(zz => zz->Z.focus->ID.toString)->Z.getExn |> Assert.equal("5");
  });
  it("can move right", () => {
    let z1 = Z.createAt(g, FancyGraph.id2)->Z.flatMap(Z.right);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getExn |> Assert.equal("3");
  });
  it("can move right off end", () => {
    let z1 =
      Z.createAt(g, FancyGraph.id3)
      ->Z.flatMap(Z.right)
      ->Z.flatMap(Z.right)
      ->Z.flatMap(Z.right)
      ->Z.flatMap(Z.right);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getExn |> Assert.equal("5");
  });
  it("can move left", () => {
    let z1 = Z.createAt(g, id5)->Z.flatMap(Z.left);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getExn |> Assert.equal("3");
  });
  it("can move left off end", () => {
    let z1 =
      Z.createAt(g, id5)
      ->Z.flatMap(Z.left)
      ->Z.flatMap(Z.left)
      ->Z.flatMap(Z.left)
      ->Z.flatMap(Z.left)
      ->Z.flatMap(Z.left);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getExn |> Assert.equal("2");
  });
  it("can move up", () => {
    let z1 = Z.createAt(g, FancyGraph.id4)->Z.flatMap(Z.up);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getExn |> Assert.equal("3");
  });
  it("can move up off top", () => {
    let z1 =
      Z.createAt(g, FancyGraph.id4)
      ->Z.flatMap(Z.up)
      ->Z.flatMap(Z.up)
      ->Z.flatMap(Z.up)
      ->Z.flatMap(Z.up)
      ->Z.flatMap(Z.up);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getOpt |> Assert.equal(None);
  });
  it("can move down", () => {
    let z1 = Z.createAt(g, FancyGraph.id3)->Z.flatMap(Z.down);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getExn |> Assert.equal("4");
  });
  it("can move down off bottom", () => {
    let z1 =
      Z.createAt(g, FancyGraph.id4)
      ->Z.flatMap(Z.down)
      ->Z.flatMap(Z.down)
      ->Z.flatMap(Z.down)
      ->Z.flatMap(Z.down)
      ->Z.flatMap(Z.down);
    [%log.debug z1->Z.mapWithDefault("", Z.toString); ("", "")];
    z1->Z.map(d => d->Z.focus->ID.toString)->Z.getExn |> Assert.equal("4");
  });
});

describe("Can split and reform", () => {
  open FancyGraph;
  it("can split", () => {
    [%log.debug "HEREE"; ("", "")];
    let z = Z.createAt(g, id3)->Z.getExn;
    [%log.debug "AFTERRR"; ("", "")];
    switch (z->Z.split) {
    | Result.Ok(g) =>
      (
        g->GF.size == 2
        && g->GF.containsId(id3)
        && g->GF.containsId(id4)
        && g
           ->GF.parentId(id4)
           ->Option.getExn
           ->I.convertParentToFocus
           ->ID.toString
        == id3->ID.toString
      )
      |> Assert.ok
    | Result.Error(err) => Assert.equal(~message=err, 1, 0)
    };
  });
  it("can reform when unchanged", () => {
    let z = Z.createAt(g, id3)->Z.getExn;
    switch (
      z
      ->Z.split
      ->Result.flatMap(g => z->Z.reform(g))
      ->Result.flatMap(Z.split)
    ) {
    | Result.Ok(gg) =>
      g->GF.subGraphForNode(id3)->Option.map(ggg => ggg->GF.eq(gg))
      |> Assert.equal(true->Some)
    | Result.Error(_) => Assert.ok(false)
    };
  });
  it("can reform when changed", () => {
    let z = Z.createAt(g, id3)->Z.getExn;
    switch (
      z
      ->Z.split
      ->Result.flatMap(g => {
          [%log.debug "after split: " ++ g->GF.toString; ("", "")];
          let gg = g->GF.setDataForNode(id4, _d => {one: 100, two: "asdasd"});
          [%log.debug "after set data: " ++ gg->GF.toString; ("", "")];
          z->Z.reform(gg);
        })
      ->Result.flatMap(zz => {
          [%log.debug "after reform: " ++ zz->Z.toString; ("", "")];
          zz->Z.split;
        })
    ) {
    | Result.Ok(gg) =>
      g
      ->GF.subGraphForNode(id3)
      ->Option.map(ggg => {
          [%log.debug "original subgraph: " ++ ggg->GF.toString; ("", "")];
          [%log.debug "new subgraph: " ++ gg->GF.toString; ("", "")];
          ggg->GF.eq(gg);
        })
      |> Assert.equal(false->Some)
    | Result.Error(err) => Assert.equal(~message=err, false, true)
    };
  });
});
