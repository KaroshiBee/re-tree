module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

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

let _setChildtreeCont = (subtree, cid, childtree, k) => {
  let ret = {
    ...subtree,
    children: subtree->children->Map.set(cid, childtree),
  };
  k(ret);
};

let addChild = (tree: t, path: P.t, id: ID.t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

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

let removeChild = (tree: t, path: P.t, child: CID.t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

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

let _stitchOnRoot = (subtree: t): t => {
  subtree->isRoot
    ? subtree
    : {
      let t = empty();
      {
        ...t,
        children:
          t->children->Map.set(subtree->myId->I.convertFocusToChild, subtree),
      };
    };
    /* let children = */
    /*   subtree */
    /*   ->children */
    /*   ->Map.reduce(t->children, (acc, cid, subtree') => { */
    /*       acc->Map.set(cid, subtree') */
    /*     }); */
    /* {...t, children}; */
};

let _getSubtreeAtPath = (subtree: t, path: list(CID.t)): option(t) => {
  [%log.debug "current subtree: " ++ subtree->toString; ("", "")];
  [%log.debug
    "rest of path: " ++ (path->List.map(CID.toString) |> String.concat(","));
    ("", "")
  ];
  let rec aux = (subtree', path', k) => {
    switch (path') {
    | [cid, ...cids] =>
      [%log.debug "getting children for: " ++ cid->CID.toString; ("", "")];
      [%log.debug
        "otherids: " ++ (cids->List.map(CID.toString) |> String.concat(","));
        ("", "")
      ];
      switch (subtree'->children->Map.get(cid)) {
      | Some(c) => aux(c, cids, k)
      | None =>
        [%log.debug
          "not found: "
          ++ (path->List.map(CID.toString) |> String.concat(","));
          ("", "")
        ];
        k(None);
      };
    | [] =>
      [%log.debug
        "found: "
        ++ (path->List.map(CID.toString) |> String.concat(","))
        ++ ", "
        ++ subtree'->toString;
        ("", "")
      ];
      k(Some(subtree'));
    };
  };
  let ret = aux(subtree, path, x => {x})->Option.map(_stitchOnRoot);
  [%log.debug
    "ret: "
    ++ (path->List.map(CID.toString) |> String.concat(","))
    ++ ", "
    ++ ret->Option.map(toString)->Option.getWithDefault("none");
    ("", "")
  ];
  ret;
};

// helper function that returns ALL the nodes including the root
let _get = (subtree: t): list((CID.t, P.t)) => {
  let rec aux =
          (id: CID.t, childList: list((CID.t, t)), accumulatedPath: P.t, k) => {
    /* let (last, ppathIn) = pathIn->P.splitLast; */
    /* let ppathOut = */
    /*   switch (last) { */
    /*   | Some(el) => pathOut->P.append(el) */
    /*   | None => pathOut */
    /*   }; */
    /* [%log.debug "CONT aux called with : " ++ id->ID.toString; ("", "")]; */
    /* [%log.debug */
    /*   "CONT aux called with pathIn: " */
    /*   ++ pathIn->P.toString */
    /*   ++ "->" */
    /*   ++ ppathIn->P.toString; */
    /*   ("", "") */
    /* ]; */
    /* [%log.debug */
    /*   "CONT aux called with pathOut: " */
    /*   ++ pathOut->P.toString */
    /*   ++ "->" */
    /*   ++ ppathOut->P.toString; */
    /*   ("", "") */
    /* ]; */
    /* [%log.debug */
    /*   "CONT aux called with children: " */
    /*   ++ ( */
    /*     childList->List.map(((cid, _)) => cid->CID.toString) */
    /*     |> String.concat(",") */
    /*   ); */
    /*   ("", "") */
    /* ]; */
    switch (childList) {
    | [(cid, newsubtree), ...rest] =>
      /* [%log.debug */
      /*   "CONT got cid: " */
      /*   ++ cid->CID.toString */
      /*   ++ " with new subtree: " */
      /*   ++ newsubtree->toString; */
      /*   ("", "") */
      /* ]; */
      let id' = cid;
      let childList' = newsubtree->children->Map.toList;
      let accumulatedPath' =
        accumulatedPath->P.append(cid->I.convertChildToParent);
      aux(id', childList', accumulatedPath', ret => {
        aux(id, rest, accumulatedPath, siblings => {
          k(List.concat(ret, siblings))
        })
      });

    | [] =>
      /* [%log.debug */
      /*   "CONT finished: pathIn: " */
      /*   ++ ppathIn->P.toString */
      /*   ++ " pathOut: " */
      /*   ++ ppathOut->P.toString */
      /*   ++ " id " */
      /*   ++ id->ID.toString */
      /*   ++ ", original path: " */
      /*   ++ path->P.toString; */
      /*   ("", "") */
      /* ]; */

      k([(id, accumulatedPath->P.moveUp)])
    };
  };
  aux(
    _root->I.convertFocusToChild, subtree->children->Map.toList, P.empty(), x => {
    x
  });
};

let getChildPaths =
    (tree: t, path: P.t, inclusive: bool): array((CID.t, P.t)) => {
  // switch the path so that it goes from root -> node
  [%log.debug "getChildPaths path: " ++ path->P.toString; ("", "")];
  [%log.debug
    "getChildPaths moveUp: " ++ path->P.moveUp->P.toString;
    ("", "")
  ];
  [%log.debug
    "getChildPaths parent: "
    ++ path->P.parent->Option.map(PID.toString)->Option.getWithDefault("");
    ("", "")
  ];
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);
  switch (tree->_getSubtreeAtPath(pathFromRoot)) {
  | Some(subtree) =>
    [%log.debug "getChildPaths subtree: " ++ subtree->toString; ("", "")];
    let ret =
      _get(subtree)
      ->List.keep(tup => fst(tup) != _root->I.convertFocusToChild)
      ->List.map(tup => {(tup->fst, tup->snd->P.concat(path->P.moveUp))})
      ->List.toArray;
    inclusive
      ? ret
      : {
        ret->Array.keep(((cid, _)) => {
          path
          ->P.parent
          ->Option.eq(
              Some(cid->I.convertChildToParent),
              (x, y) => {
                [%log.debug
                  "xy: " ++ x->PID.toString ++ "," ++ y->PID.toString;
                  ("", "")
                ];
                x->PID.toString != y->PID.toString;
              },
            )
        });
      };

  /* inclusive */
  /*   ? { */
  /*     switch (path->P.parent) { */
  /*     | Some(pid) => */
  /*       ret->Array.concat([| */
  /*         (pid->I.convertParentToChild, path->P.moveUp), */
  /*       |]) */
  /*     | None => ret */
  /*     }; */
  /*   } */
  /*   : ret; */
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
  let pathFromRoot =
    path
    ->P.append(id->I.convertFocusToParent)
    ->P.pathFromRoot
    ->List.map(I.convertParentToChild);
  let ret =
    switch (tree->_getSubtreeAtPath(pathFromRoot)) {
    | Some(parentTree) =>
      [%log.debug "getSubtree: parentTree" ++ parentTree->toString; ("", "")];
      parentTree->children->Map.get(id->I.convertFocusToChild);
    | None => None
    };
  ret->Option.map(_stitchOnRoot);
};

let addSubtree = (tree: t, from: ID.t, under: P.t, subtreeToAdd: t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = under->P.pathFromRoot->List.map(I.convertParentToChild);
  // make sure that the tip of the subtree being added is not a root node
  // only wnat one root node per tree
  let subtreeToAdd =
    subtreeToAdd->isRoot
      ? {...subtreeToAdd, isRoot: false, me: from} : subtreeToAdd;
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

let removeSubtree = (tree: t, path: P.t, child: CID.t): t => {
  // switch the path so that it goes from root -> node
  let pathFromRoot = path->P.pathFromRoot->List.map(I.convertParentToChild);

  let rec aux = (subtree: t, path: list(CID.t), k): t => {
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
