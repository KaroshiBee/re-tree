module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module P = Path.T;

// phantom types
type root;
type subtree;

// realised types
type children = CID.Map.t(data)
and data = {
  me: ID.t,
  children,
  isRoot: bool,
}
and t('a) = data;

// NOTE remember root isn't actually in any maps
let _root = ID.create("root");
let empty = () => {
  {me: _root, children: CID.Map.make(), isRoot: true};
};

let emptySubtree = id => {
  {me: id, children: CID.Map.make(), isRoot: false};
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

let toString = (tree): string => {
  let rec _pprint = (tip, spacing: int): list(string) => {
    let fst = tip->toSummaryString ++ "\n";
    let rest =
      tip
      ->children
      ->Map.reduce(
          [],
          (acc, cid, child) => {
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

let _setChildtreeCont = (subtree, cid, childtree, k) => {
  let ret = {
    ...subtree,
    children: subtree->children->Map.set(cid, childtree),
  };
  k(ret);
};

let addChild = (tree, path, id) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let rec aux = (subtree, path, k) => {
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
          _setChildtreeCont(subtree, cid, childtree, k)
        })
      | None =>
        aux(emptySubtree(cid->I.convertChildToFocus), cids, childtree => {
          _setChildtreeCont(subtree, cid, childtree, k)
        })
      }
    };
  };
  aux(tree, pathFromRoot, x => {x});
};

let removeChild = (tree, path, child) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let rec aux = (subtree, path, k) => {
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
          _setChildtreeCont(subtree, cid, childtree, k)
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

let _getSubtreeAtPath = (subtree, path: list(CID.t)) => {
  /* %log.debug */
  /* "current subtree: " ++ subtree->toSummaryString; */
  /* %log.debug */
  /* "rest of path: " ++ (path->List.map(CID.toString) |> String.concat(",")); */
  let rec aux = (subtree, path, k) => {
    switch (path) {
    | [] => k(Some(subtree))
    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      switch (subtree->children->Map.get(cid)) {
      | Some(c) => aux(c, cids, k)
      | None => k(None)
      }
    };
  };
  aux(subtree, path, x => {x});
};

// helper function that returns ALL the nodes including the root
let _get = (subtree, path) => {
  let rec aux = (id, path, childList, k) => {
    /* [%log.debug "CONT aux called with : " ++ id->ID.toString; ("", "")]; */
    /* [%log.debug "CONT aux called with path: " ++ path->P.toString; ("", "")]; */
    switch (childList) {
    | [] =>
      //      let m = CID.Map.make();
      let ppath = path->P.moveUp;
      /* [%log.debug */
      /*   "CONT finished adding: " */
      /*   ++ ppath->P.toString */
      /*   ++ " to " */
      /*   ++ id->ID.toString; */
      /*   ("", "") */
      /* ]; */
      //    k(m->Map.set(id->I.convertFocusToChild, ppath));
      k([(id->I.convertFocusToChild, ppath)]);
    /* subtree->isRoot */
    /*   ? { */
    /*     [%log.debug "CONT found root"; ("", "")]; */
    /*     k(m); */
    /*   } */
    /*   : { */
    /*     [%log.debug */
    /*     "CONT finished not root"; ("","")]; */
    /*     k(m->Map.set(id->I.convertFocusToChild, path->P.moveUp)); */
    /*   }; */
    //base case
    | [(cid, newsubtree), ...rest] =>
      /* [%log.debug "CONT got cid: " ++ cid->CID.toString; ("", "")]; */
      aux(
        cid->I.convertChildToFocus,
        path->P.append(cid->I.convertChildToParent),
        newsubtree->children->Map.toList,
        ret => {
        /* [%log.debug "CONT recurse children list: "; ("", "")]; */
        /* [%log.debug */
        /*   "CONT ret map:" ++ ret->Map.size->string_of_int; */
        /*   ("", "") */
        /* ]; */
        aux(id, path, rest, siblings => {
          /* [%log.debug "CONT recurse sibling: "; ("", "")]; */
          /* [%log.debug */
          /*   "CONT sibling map:" ++ siblings->Map.size->string_of_int; */
          /*   ("", "") */
          /* ]; */
          k(
            List.concat(ret, siblings),
            //            ret->Map.mergeMany(siblings->Map.toArray),
          )
        })
      })
    //recurse over children
    };
  };
  aux(subtree->myId, path, subtree->children->Map.toList, x => {x});
};

let getChildPaths = (tree, path, inclusive) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);
  switch (tree->_getSubtreeAtPath(pathFromRoot)) {
  | Some(subtree) =>
    //    [%log.debug subtree->toString; ("", "")];
    let ret =
      _get(subtree, path)
      ->List.keep(tup => fst(tup) != _root->I.convertFocusToChild)
      ->List.toArray;
    /* _get(subtree, path) */
    /* ->Map.remove(_root->I.convertFocusToChild) */
    /* ->Map.toArray; */
    let tip = subtree->myId->I.convertFocusToChild;
    inclusive ? ret : ret->Array.keep(d => {fst(d) != tip});
  | None => [||]
  };
};

let getAllPaths = tree => {
  tree->getChildPaths(P.empty(), true);
};

let getChildIds = (tree, path, inclusive) => {
  tree->getChildPaths(path, inclusive)->Array.map(pr => fst(pr));
};

let getAllIds = tree => {
  tree->getChildIds(P.empty(), true);
};

let getSubtree = (tree, path, id) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);
  switch (tree->_getSubtreeAtPath(pathFromRoot)) {
  | Some(parentTree) =>
    parentTree->children->Map.get(id->I.convertFocusToChild)
  | None => None
  };
};

let addSubtree = (tree, from, under, subtreeToAdd) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = under->P.pathFromRoot->List.map(I.convertParentToChild);
  // make sure that the tip of the subtree being added is not a root node
  // only wnat one root node per tree
  let subtreeToAdd =
    subtreeToAdd->isRoot
      ? {...subtreeToAdd, isRoot: false, me: from} : subtreeToAdd;
  let rec aux = (subtree, path, k) => {
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
      k(ret);
    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      switch (subtree->children->Map.get(cid)) {
      | Some(c) =>
        aux(c, cids, childtree => {
          _setChildtreeCont(subtree, cid, childtree, k)
        })
      | None =>
        aux(emptySubtree(cid->I.convertChildToFocus), cids, childtree => {
          _setChildtreeCont(subtree, cid, childtree, k)
        })
      }
    };
  };
  aux(tree, pathFromRoot, x => {x});
};

let addRootAsSubtree = (tree, from, under, subtreeToAdd) => {
  tree;
};

let removeSubtree = (tree, path, child) => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let rec aux = (subtree, path, k) => {
    /* %log.debug */
    /* "looking for " ++ child->CID.toString; */
    /* %log.debug */
    /* "current subtree: " ++ subtree->toSummaryString; */
    /* %log.debug */
    /* "rest of path: " ++ (path->List.map(CID.toString) |> String.concat(",")); */
    switch (path) {
    | [] => k({...subtree, children: subtree->children->Map.remove(child)})
    | [cid, ...cids] =>
      /* %log.debug */
      /* "getting children for: " ++ cid->CID.toString; */
      /* %log.debug */
      /* "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(",")); */
      switch (subtree->children->Map.get(cid)) {
      | Some(c) =>
        aux(c, cids, childtree => {
          _setChildtreeCont(subtree, cid, childtree, k)
        })
      | None => k(subtree)
      }
    };
  };
  aux(tree, pathFromRoot, x => {x});
};

let eq = (expected, actual) => {
  let eIds =
    expected
    ->getAllPaths
    ->SortArray.stableSortBy((x, y) => {
        compare(x->fst->CID.toString, y->fst->CID.toString)
      });
  let aIds =
    actual
    ->getAllPaths
    ->SortArray.stableSortBy((x, y) => {
        compare(x->fst->CID.toString, y->fst->CID.toString)
      });
  eIds->Array.eq(aIds, (x, y) => {
    x->fst->CID.toString == y->fst->CID.toString && x->snd->P.eq(y->snd)
  });
};
