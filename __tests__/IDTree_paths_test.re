open Test_utils;

describe("getChildPaths", () => {
  let t = StandardTree.t;

  [%log.debug "test tree: " ++ t->T.toString; ("", "")];
  it("gotAllChildren", () => {
    let paths = t->T.getChildPaths(StandardTree.path0, false); // should be all children of 2
    [%log.debug
      "gotAllChildren CONT"
      ++ (
        paths
        ->Array.map(pr =>
            "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}"
          )
        ->List.fromArray
        |> String.concat(",")
      );
      ("", "")
    ];
    Path_utils.(comparePathLists(expected, paths))->Assert.ok;
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2}
     */
  });
  it("gotFourChildren", () => {
    let paths = t->T.getChildPaths(P.fromRootToPathList(["2", "1"]), false);
    [%log.debug
      "gotFourChildren paths: "
      ++ (
        paths
        ->Array.map(pr =>
            "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}"
          )
        ->List.fromArray
        |> String.concat(",")
      );
      ("", "")
    ];
    let expected = [|
      ("child2"->CID.create, StandardTree.path2),
      ("b"->CID.create, StandardTree.path2->P.moveUp),
      ("child1"->CID.create, StandardTree.path1),
      ("a"->CID.create, StandardTree.path2->P.moveUp),
    |];

    Path_utils.comparePathLists(expected, paths)->Assert.ok;
    /*
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
     */
  });
  it("gotFourChildIds", () => {
    let paths = t->T.getChildIds(P.fromRootToPathList(["2", "1"]), false);
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    paths->Array.size |> Assert.equal(4);
    /*
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
     */
  });
  let paths = t->T.getChildPaths(StandardTree.path3, false); // should be only one
  it("gotOnlyOne", () => {
    paths->Array.size |> Assert.equal(1)
  });
  it("gotChild3", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->fst->CID.toString; ("", "")];
    [%log.debug "id3:" ++ StandardTree.id3->ID.toString; ("", "")];
    pr->fst == StandardTree.id3->I.convertFocusToChild |> Assert.equal(true);
  });
  it("gotChild3Path", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->snd->P.toString; ("", "")];
    [%log.debug "id3:" ++ StandardTree.path3->P.toString; ("", "")];
    pr->snd->P.eq(StandardTree.path3) |> Assert.equal(true);
  });
  it("gotNone", () => {
    let paths = t->T.getChildIds(P.fromRootToPathList(["20", "10"]), false);
    paths->Array.size |> Assert.equal(0);
  });
});

describe("getAllPaths", () => {
  let t = StandardTree.t;
  it("gotAllPaths", () => {
    let paths = t->T.getAllPaths; // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    Path_utils.(
      comparePathLists(
        expected->Array.concat([|("2"->CID.create, P.empty())|]),
        paths,
      )
    )
    ->Assert.ok;
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},
       {2:},

     */
  });

  it("gotAllIds", () => {
    let paths = t->T.getAllIds; // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    paths->Array.size |> Assert.equal(8);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},
       {2:},

     */
  });

  it("gotChildPAths", () => {
    let paths = t->T.getChildPaths(P.fromList(["2"]), false); // should not include 2
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    paths->Array.size |> Assert.equal(7);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},

     */
  });

  it("gotChildPathsInclusive", () => {
    let paths = t->T.getChildPaths(P.fromList(["2"]), true); // should be all of them
    /* %log.debug */
    /* paths */
    /* ->Array.map(pr => */
    /*     "{" ++ pr->fst->CID.toString ++ ":" ++ pr->snd->P.toString ++ "}" */
    /*   ) */
    /* ->List.fromArray */
    /* |> String.concat(","); */
    paths->Array.size |> Assert.equal(8);
    /*
       {child3:c,2},
       {c:2},
       {child2:b,1,2},
       {b:1,2},
       {child1:a,1,2},
       {a:1,2},
       {1:2},
       {2:},

     */
  });
});
