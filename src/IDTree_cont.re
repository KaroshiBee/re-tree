module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module P = Path.Parents;

type children = CID.Map.t(t)
and t = {
  me: ID.t,
  children,
  isRoot: bool,
};

// NOTE remember root isn't actually in any maps
let _root = ID.create("root");
let empty = () => {
  {me: _root, children: CID.Map.make(), isRoot: true};
};

let emptySubtree = id => {
  {me: id, children: CID.Map.make(), isRoot: false};
};

let isRoot = t => t.isRoot;
let rootId = t => t->isRoot ? Some(t.me) : None;

let myId = t => t.me;

let children = t => t.children;

let hasChildren = t => t->children->Map.size > 0;

let toSummaryString = t => {
  "{ me: "
  ++ t->myId->ID.toString
  ++ ", #children: "
  ++ t->children->Map.size->string_of_int
  ++ ", isRoot: "
  ++ t.isRoot->string_of_bool
  ++ "}";
};

let toString = (tree: t): string => {
  let rec _pprint = (tip: t, spacing: int): list(string) => {
    let fst = tip->toSummaryString ++ "\n";
    let rest =
      tip
      ->children
      ->Map.reduce(
          [],
          (acc, cid, child: t) => {
            let s =
              "|"
              ++ String.concat(".", List.make(spacing, " "))
              ++ cid->CID.toString
              ++ ":";
            /* ++ child->toSummaryString; */
            let sRest = _pprint(child, spacing + 2);
            [s, ...sRest->List.concat(acc)];
          },
        );
    [fst, ...rest];
  };
  "\n" ++ (_pprint(tree, 2) |> String.concat(""));
};

let addChild = (tree: t, path: P.t, id: ID.t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let childtree_cont = (subtree, cid, childtree, k) => {
    let ret = {
      ...subtree,
      children: subtree->children->Map.set(cid, childtree),
    };
    k(ret);
  };

  let rec aux = (subtree: t, path: list(CID.t), k): t => {
    /* %log.debug */
    /* "looking for home for " ++ id->ID.toString; */
    /* %log.debug */
    /* "current subtree: " ++ subtree->toSummaryString; */
    /* %log.debug */
    /* "rest of path: " ++ (path->List.map(CID.toString) |> String.concat(",")); */
    switch (path) {
    | [] =>
      /* %log.debug */
      /* "found home for " */
      /* ++ id->ID.toString */
      /* ++ " under " */
      /* ++ subtree->myId->ID.toString; */
      let childtree = emptySubtree(id);
      let ret = {
        ...subtree,
        children:
          subtree->children->Map.set(id->I.convertFocusToChild, childtree),
      };
      /* %log.debug */
      /* "returning: " ++ ret->toSummaryString; */
      k(ret);
    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      switch (subtree->children->Map.get(cid)) {
      | Some(c) =>
        aux(c, cids, childtree => {
          childtree_cont(subtree, cid, childtree, k)
        })
      | None =>
        aux(emptySubtree(cid->I.convertChildToFocus), cids, childtree => {
          childtree_cont(subtree, cid, childtree, k)
        })
      }
    };
  };
  aux(tree, pathFromRoot, x => {x});
};

let removeChild = (tree: t, path: P.t, child: CID.t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let childtree_cont = (subtree, cid, childtree, k) => {
    let ret = {
      ...subtree,
      children: subtree->children->Map.set(cid, childtree),
    };
    k(ret);
  };

  let rec aux = (subtree: t, path: list(CID.t), k): t => {
    /* %log.debug */
    /* "looking for " ++ child->CID.toString; */
    /* %log.debug */
    /* "current subtree: " ++ subtree->toSummaryString; */
    /* %log.debug */
    /* "rest of path: " ++ (path->List.map(CID.toString) |> String.concat(",")); */
    switch (path) {
    | [] =>
      let ret =
        switch (subtree->children->Map.get(child)) {
        | Some(childTreeWithChildToRemove) =>
          /* %log.debug */
          /* "got child, removing and merging its children: " */
          /* ++ childTreeWithChildToRemove->children->Map.size->string_of_int; */
          if (childTreeWithChildToRemove->hasChildren) {
            {
              /* %log.debug */
              /* childTreeWithChildToRemove */
              /* ->children */
              /* ->Map.keysToArray */
              /* ->Array.map(CID.toString) */
              /* ->List.fromArray */
              /* |> String.concat(","); */

              ...subtree,
              children:
                subtree
                ->children
                ->Map.remove(child)
                ->Map.mergeMany(
                    childTreeWithChildToRemove->children->Map.toArray,
                  ),
            };
          } else {
            {
              /* %log.debug */
              /* "no children so just removing child"; */
              ...subtree,
              children: subtree->children->Map.remove(child),
            };
          }
        | None => subtree
        };
      /* %log.debug */
      /* "returning: " ++ ret->toSummaryString; */
      k(ret);

    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      switch (subtree->children->Map.get(cid)) {
      | Some(c) =>
        aux(c, cids, childtree => {
          childtree_cont(subtree, cid, childtree, k)
        })
      | None =>
        let ret = subtree;
        /* %log.debug */
        /* "returning: " ++ ret->toSummaryString; */
        k(ret);
      }
    };
  };
  aux(tree, pathFromRoot, x => {x});
};
