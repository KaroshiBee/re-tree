open BsMocha.Mocha;
module Assert = BsMocha.Assert;

module M = IDTree.T;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

describe("getChildPaths", () => {
  let path0 = P.fromRootToPathList(["2"]);
  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  [%log.debug "test tree: " ++ t->M.toString; ("", "")];
  it("gotAllChildren", () => {
    let paths = t->M.getChildPaths(path0, false); // should be all children of 2
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
    paths->Array.size |> Assert.equal(7);
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
    let paths = t->M.getChildPaths(P.fromRootToPathList(["2", "1"]), false);
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
  it("gotFourChildIds", () => {
    let paths = t->M.getChildIds(P.fromRootToPathList(["2", "1"]), false);
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
  let paths = t->M.getChildPaths(path3, false); // should be only one
  it("gotOnlyOne", () => {
    paths->Array.size |> Assert.equal(1)
  });
  it("gotChild3", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->fst->CID.toString; ("", "")];
    [%log.debug "id3:" ++ id3->ID.toString; ("", "")];
    pr->fst == id3->I.convertFocusToChild |> Assert.equal(true);
  });
  it("gotChild3Path", () => {
    let pr = paths->Array.getExn(0);
    [%log.debug "pr:" ++ pr->snd->P.toString; ("", "")];
    [%log.debug "id3:" ++ path3->P.toString; ("", "")];
    pr->snd->P.eq(path3) |> Assert.equal(true);
  });
  it("gotNone", () => {
    let paths = t->M.getChildIds(P.fromRootToPathList(["20", "10"]), false);
    paths->Array.size |> Assert.equal(0);
  });
});

describe("getAllPaths", () => {
  let path1 = P.fromRootToPathList(["2", "1", "a"]);
  let path2 = P.fromRootToPathList(["2", "1", "b"]);
  let path3 = P.fromRootToPathList(["2", "c"]);
  let id1 = ID.create("child1");
  let id2 = ID.create("child2");
  let id3 = ID.create("child3");
  let t =
    M.empty()
    ->M.addChild(path1, id1)
    ->M.addChild(path2, id2)
    ->M.addChild(path3, id3);

  it("gotAllPaths", () => {
    let paths = t->M.getAllPaths; // should be all of them
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

  it("gotAllIds", () => {
    let paths = t->M.getAllIds; // should be all of them
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
    let paths = t->M.getChildPaths(P.fromList(["2"]), false); // should not include 2
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
    let paths = t->M.getChildPaths(P.fromList(["2"]), true); // should be all of them
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
