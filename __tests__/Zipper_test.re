open Test_utils;
module Z = Zipper.Make(G);

let _ = (); //weird bug in reason-mode reason-paren-level

//  1
// 2 3 5
//   4
let id5 = ID.create("5");
let g =
  StandardGraph.(
    makeGraph()
    ->G.addNodeUnder(id5, {one: 5, two: "five"}, id1->I.convertFocusToParent)
  );

describe("can make and move around", () => {
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

describe("Can split and reform", () => {
  open StandardGraph;

  it("can split", () => {
    let z = Z.create(g, id3)->Option.getExn;
    switch (z->Z.split) {
    | Result.Ok(g) =>
      (
        g->G.size == 2
        && g->G.containsId(id3)
        && g->G.containsId(id4)
        && g
           ->G.parentId(id4)
           ->Option.getExn
           ->I.convertParentToFocus
           ->ID.toString
        == id3->ID.toString
      )
      |> Assert.ok
    | Result.Error(_) => Assert.ok(false)
    };
  });

  it("can reform when unchanged", () => {
    let z = Z.create(g, id3)->Option.getExn;
    switch (
      z
      ->Z.split
      ->Result.flatMap(g => z->Z.reform(g))
      ->Result.flatMap(Z.split)
    ) {
    | Result.Ok(gg) =>
      g->G.subGraphForNode(id3)->Option.map(ggg => ggg->G.eq(gg))
      |> Assert.equal(true->Some)
    | Result.Error(_) => Assert.ok(false)
    };
  });

  it("can reform when changed", () => {
    let z = Z.create(g, id3)->Option.getExn;
    [%log.debug
      "hashing: "
      ++ Hashtbl.hash(StandardGraph.{one: 1, two: "one"})->string_of_int;
      ("", "")
    ];
    [%log.debug
      "hashing: "
      ++ Hashtbl.hash(StandardGraph.{one: 21, two: "one"})->string_of_int;
      ("", "")
    ];
    switch (
      z
      ->Z.split
      ->Result.flatMap(g => {
          let gg =
            g->G.setDataForNode(id4, _d =>
              StandardGraph.{one: 100, two: "asdasd"}
            );
          z->Z.reform(gg);
        })
      ->Result.flatMap(zz => {
          [%log.debug zz->Z.toString; ("", "")];
          zz->Z.split;
        })
    ) {
    | Result.Ok(gg) =>
      g->G.subGraphForNode(id3)->Option.map(ggg => ggg->G.eq(gg))
      |> Assert.equal(false->Some)
    | Result.Error(err) => Assert.equal(~message=err, false, true)
    };
  });
});
