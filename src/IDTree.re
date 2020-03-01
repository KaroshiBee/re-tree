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

  let rec aux = (subtree: t, path: list(CID.t)): t => {
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
      ret;
    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      let childtree =
        switch (subtree->children->Map.get(cid)) {
        | Some(c) => c->aux(cids)
        | None => emptySubtree(cid->I.convertChildToFocus)->aux(cids)
        };
      let ret = {
        ...subtree,
        children: subtree->children->Map.set(cid, childtree),
      };
      /* %log.debug */
      /* "returning: " ++ ret->toSummaryString; */
      ret;
    };
  };
  aux(tree, pathFromRoot);
};

let removeChild = (tree: t, path: P.t, child: CID.t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let rec aux = (subtree: t, path: list(CID.t)): t => {
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
      ret;

    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      let childtree =
        switch (subtree->children->Map.get(cid)) {
        | Some(c) => c->aux(cids)
        | None => subtree
        };
      let ret = {
        ...subtree,
        children: subtree->children->Map.set(cid, childtree),
      };
      /* %log.debug */
      /* "returning: " ++ ret->toSummaryString; */
      ret;
    };
  };
  aux(tree, pathFromRoot);
};

let rec _getSubtreeAtPath = (subtree: t, path: list(CID.t)): option(t) => {
  /* %log.debug */
  /* "current subtree: " ++ subtree->toSummaryString; */
  /* %log.debug */
  /* "rest of path: " ++ (path->List.map(CID.toString) |> String.concat(",")); */
  switch (path) {
  | [] => Some(subtree)
  | [cid, ...cids] =>
    /* %log.debug */
    /* "getting children for: " ++ cid->CID.toString; */
    /* %log.debug */
    /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
    switch (subtree->children->Map.get(cid)) {
    | Some(c) => c->_getSubtreeAtPath(cids)
    | None => None
    }
  };
};

let rec _get =
        (subtree: t, path: P.t, cids: ref(list((CID.t, P.t))), first: bool) => {
  let tip = subtree->myId->I.convertFocusToChild;
  // if it is the root then recurse with the root children
  // but dont include the root in the final list
  let tippath =
    subtree->isRoot
      ? path : first ? path : path->P.append(tip->I.convertChildToParent);
  /* if (specialCase) { */
  /*   (); */
  /* } else { */
  /*   let p = tippath->P.moveUp; */
  /*   /\* [%log.debug *\/ */
  /*   /\*   "appending onto cids: " *\/ */
  /*   /\*   ++ tip->CID.toString *\/ */
  /*   /\*   ++ ", " *\/ */
  /*   /\*   ++ p->P.toString *\/ */
  /*   /\*   ++ ", " *\/ */
  /*   /\*   ++ tippath->P.toString *\/ */
  /*   /\*   ++ ", " *\/ */
  /*   /\*   ++ path->P.toString; *\/ */
  /*   /\*   ("", "") *\/ */
  /*   /\* ]; *\/ */

  /*   cids := [(tip, p), ...cids^]; */
  /* }; */
  let p = tippath->P.moveUp;
  cids := subtree->isRoot ? cids^ : [(tip, p), ...cids^];
  subtree
  ->children
  ->Map.forEach((_cid, childtree) => {
      _get(childtree, tippath, cids, false)
    });
};

let getChildPaths =
    (tree: t, path: P.t, inclusive: bool): array((CID.t, P.t)) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);
  switch (tree->_getSubtreeAtPath(pathFromRoot)) {
  | Some(subtree) =>
    //    [%log.debug subtree->toString; ("", "")];
    let cids = ref([]: list((CID.t, P.t)));
    let _ = _get(subtree, path, cids, true);
    let ret = (cids^)->List.toArray;
    let tip = subtree->myId->I.convertFocusToChild;
    inclusive ? ret : ret->Array.keep(d => {fst(d) != tip});
  | None => [||]
  };
};

let getAllPaths = (tree: t): array((CID.t, P.t)) => {
  tree->getChildPaths(P.empty(), true);
};

let getChildIds = (tree: t, path: P.t, inclusive: bool): array(CID.t) => {
  tree->getChildPaths(path, inclusive)->Array.map(pr => fst(pr));
};

let getAllIds = (tree: t): array(CID.t) => {
  tree->getChildIds(P.empty(), true);
};

let getSubtree = (tree: t, path: P.t, id: ID.t): option(t) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);
  switch (tree->_getSubtreeAtPath(pathFromRoot)) {
  | Some(parentTree) =>
    parentTree->children->Map.get(id->I.convertFocusToChild)
  | None => None
  };
};

let addSubtree = (tree: t, from: ID.t, under: P.t, subtreeToAdd: t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = under->P.pathFromRoot->List.map(I.convertParentToChild);
  // make sure that the tip of the subtree being added is not a root node
  // only wnat one root node per tree
  let subtreeToAdd =
    subtreeToAdd->isRoot
      ? {...subtreeToAdd, isRoot: false, me: from} : subtreeToAdd;
  let rec aux = (subtree: t, path: list(CID.t)): t => {
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
      let ret = {
        ...subtree,
        children:
          subtree
          ->children
          ->Map.set(from->I.convertFocusToChild, subtreeToAdd),
      };
      /* %log.debug */
      /* "returning: " ++ ret->toSummaryString; */
      ret;
    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      let childtree =
        switch (subtree->children->Map.get(cid)) {
        | Some(c) => c->aux(cids)
        | None => emptySubtree(cid->I.convertChildToFocus)->aux(cids)
        };
      let ret = {
        ...subtree,
        children: subtree->children->Map.set(cid, childtree),
      };
      /* %log.debug */
      /* "returning: " ++ ret->toSummaryString; */
      ret;
    };
  };
  aux(tree, pathFromRoot);
};

let removeSubtree = (tree: t, path: P.t, child: CID.t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let rec aux = (subtree: t, path: list(CID.t)): t => {
    /* %log.debug */
    /* "looking for " ++ child->CID.toString; */
    /* %log.debug */
    /* "current subtree: " ++ subtree->toSummaryString; */
    /* %log.debug */
    /* "rest of path: " ++ (path->List.map(CID.toString) |> String.concat(",")); */
    switch (path) {
    | [] => {...subtree, children: subtree->children->Map.remove(child)}
    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      let childtree =
        switch (subtree->children->Map.get(cid)) {
        | Some(c) => c->aux(cids)
        | None => subtree
        };
      let ret = {
        ...subtree,
        children: subtree->children->Map.set(cid, childtree),
      };
      /* %log.debug */
      /* "returning: " ++ ret->toSummaryString; */
      ret;
    };
  };
  aux(tree, pathFromRoot);
};
