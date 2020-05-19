module I = Identity;
module ID = I.FocusId;
module PID = I.ParentId;
module CID = I.ChildId;
module P = Path.T;
module IDTree = IDTree.T;

module type HASHABLE = {
  type t;
  let hash: t => int;
  let eq: (t, t) => bool;
  let toString: t => string;
};

module type GRAPH_ELEMENT = {
  type el;
  type t;
  let create: (el, P.t) => t;
  let pathUp: t => P.t;
  let setPathUp: (t, P.t) => t;
  let value: t => el;
  let setValue: (t, el) => t;

  let hash: t => int;
  let eq: (t, t) => bool;
  let toString: t => string;
};

module MakeElement = (H: HASHABLE) : (GRAPH_ELEMENT with type el = H.t) => {
  type el = H.t;
  type t = {
    pathUp_: P.t,
    value_: el,
  };
  let create = (el, pth) => {value_: el, pathUp_: pth};
  let pathUp = t => t.pathUp_;
  let setPathUp = (t, pth) => {...t, pathUp_: pth};
  let value = t => t.value_;
  let setValue = (t, el) => {...t, value_: el};

  let hash = t => t.value_->H.hash + Hashtbl.hash(t.pathUp_->P.toString);
  let eq = (x, y) => x->hash == y->hash;
  let toString = t =>
    "{ value: "
    ++ t.value_->H.toString
    ++ ", path-up: "
    ++ t.pathUp_->P.toString
    ++ "}";
};

module type GRAPH = {
  type el;
  type node;
  type t;
  let empty: unit => t;
  let toString: t => string;
  let size: t => int;
  let hasChildren: t => bool;
  let numberChildren: t => int;
  let containsId: (t, ID.t) => bool;
  let pathFromNode: (t, ID.t) => option(P.t);
  let parentId: (t, ID.t) => option(PID.t);
  let dataForNode: (t, ID.t) => option(el);
  let depth: (t, ID.t) => int;
  let maxDepth: t => int;
  // el => el because only modifying one node
  let setDataForNode: (t, ID.t, el => el) => t;
  let subGraphForNode: (t, ID.t) => option(t);
  let childIdsOfRoot: t => list(ID.t);
  let childrenOfRoot: t => list(t);
  let childIds: (t, ID.t) => list(ID.t);
  let children: (t, ID.t) => list(t);
  let childData: (t, ID.t) => list(el);
  let addNode: (t, ID.t, el) => t;
  let addNodeAtPath: (t, ID.t, el, P.t) => t;
  let addNodeUnder: (t, ID.t, el, PID.t) => t;
  let removeNode: (t, ID.t) => Result.t(t, string);
  let moveChild: (t, CID.t, PID.t) => Result.t(t, string);
  let removeSubtree: (t, ID.t) => Result.t(t, string);
  let setSubGraphForNode: (t, PID.t, t) => Result.t(t, string);
  let setSubGraphForRoot: (t, t) => Result.t(t, string);
  let trimPaths: (t, option(P.t)) => t;
  let moveSubtree: (t, CID.t, PID.t) => Result.t(t, string);
  let map: (t, el => el) => t;
  // el => el because only modifying one node
  let updateChildren: (t, ID.t, el => el) => t;
  let forEach: (t, (ID.t, el) => unit) => unit;
  let keep: (t, (ID.t, el) => bool) => t;
  let toKeyValueArrayWithPaths: t => array((ID.t, P.t, el));
  let toKeyValueArray: t => array((ID.t, el));
  let toArray: t => array(el);
  let fromArray: (array(el), el => ID.t, el => option(PID.t)) => t;
  let eq: (t, t) => bool;
};

module T =
       (EL: GRAPH_ELEMENT)
       : (GRAPH with type el = EL.el and type node = EL.t) => {
  type el = EL.el;
  type node = EL.t;
  type t = {
    masterLookup: ID.Map.t(EL.t),
    tree: IDTree.t,
  };

  let empty = () => {
    let tree = IDTree.empty();
    let masterLookup = ID.Map.make();
    {masterLookup, tree};
  };

  let toString = graph => {
    let treeS = graph.tree->IDTree.toString;
    let dataS =
      graph.masterLookup
      ->Map.reduce(
          [],
          (acc, ky, d) => {
            let s =
              ky->ID.toString
              ++ ": { "
              ++ "value: "
              ++ d->EL.toString
              ++ ", "
              ++ "pathUp: "
              ++ d->EL.pathUp->P.toString
              ++ " }";
            [s, ...acc];
          },
        )
      |> String.concat("\n");
    "{tree:\n" ++ treeS ++ "\n masterLookup:\n" ++ dataS ++ "\n}";
  };

  let size = graph => {
    graph.masterLookup->Map.size;
  };

  let hasChildren = graph => {
    graph.tree->IDTree.hasChildren;
  };

  let numberChildren = graph => {
    graph.tree->IDTree.children->Map.keysToArray->Array.size;
  };

  let containsId = (graph, id) => {
    graph.masterLookup->Map.has(id);
  };

  let fullDataFromNode = (graph, id) =>
    if (graph->containsId(id)) {
      let dataWithPath = graph.masterLookup->Map.getExn(id);
      Some(dataWithPath);
    } else {
      None;
    };

  let pathFromNode = (graph, id) => {
    graph->fullDataFromNode(id)->Option.map(d => d->EL.pathUp);
  };

  let parentId = (graph, id) => {
    graph->pathFromNode(id)->Option.flatMap(d => d->P.parent);
  };

  let dataForNode = (graph, id) =>
    graph->fullDataFromNode(id)->Option.map(d => d->EL.value);

  let depth = (graph, id) => {
    graph->pathFromNode(id)->Option.map(P.size)->Option.getWithDefault(0);
  };

  let maxDepth = graph => {
    graph.masterLookup
    ->Map.reduce(0, (acc, _ky, dataWithPath) => {
        max(acc, dataWithPath->EL.pathUp->P.size)
      });
  };

  let setDataForNode = (graph, id, f) =>
    switch (graph->fullDataFromNode(id)) {
    | Some(olddata) =>
      let masterLookup =
        graph.masterLookup
        ->Map.set(id, olddata->EL.setValue(f(olddata->EL.value)));
      {...graph, masterLookup};
    | None => graph
    };

  let subGraphForNode = (graph, id) => {
    switch (graph->pathFromNode(id)) {
    | Some(path) =>
      switch (graph.tree->IDTree.getSubtree(path, id)) {
      | Some(tree) =>
        /* [%log.debug */
        /*   "subgraphfornode tree: " ++ tree->IDTree.toString; */
        /*   ("", "") */
        /* ]; */
        let allIds = graph.masterLookup->Map.keysToArray; //;
        /* [%log.debug */
        /*   "all ids: " */
        /*   ++ ( */
        /*     allIds->Array.map(cid => cid->ID.toString)->List.fromArray */
        /*     |> String.concat(",") */
        /*   ); */
        /*   ("", "") */
        /* ]; */
        let ids = tree->IDTree.getAllIds;
        /* [%log.debug */
        /*   "to keep: " */
        /*   ++ ( */
        /*     ids->Array.map(cid => cid->CID.toString)->List.fromArray */
        /*     |> String.concat(",") */
        /*   ); */
        /*   ("", "") */
        /* ]; */
        let toKeep = ids->Array.map(I.convertChildToFocus)->ID.Set.fromArray;
        let cids = allIds->ID.Set.fromArray->Set.diff(toKeep)->Set.toArray;
        /* [%log.debug */
        /*   "to remove: " */
        /*   ++ ( */
        /*     cids->Array.map(cid => cid->ID.toString)->List.fromArray */
        /*     |> String.concat(",") */
        /*   ); */
        /*   ("", "") */
        /* ]; */
        // remove these from graph
        let masterLookup = graph.masterLookup->Map.removeMany(cids);
        let ret = {masterLookup, tree};
        /* [%log.debug "subGraphForNode returning: " ++ ret->toString; ("", "")]; */
        ret->Some;
      | None =>
        [%log.error
          "subGraphForNode: cannot find IDTree: path - "
          ++ path->P.toString
          ++ ", id - "
          ++ id->ID.toString;
          ("", "")
        ];
        None;
      }

    | None =>
      [%log.error
        "subGraphForNode: cannot find path at id: " ++ id->ID.toString;
        ("", "")
      ];
      None;
    };
  };

  let childIdsOfRoot = graph => {
    [%log.debug "childIdsOfRoot"; ("", "")];
    let ret =
      graph.tree
      ->IDTree.makeIntoRootedSubtree
      ->IDTree.children
      ->Map.keysToArray
      ->List.fromArray
      ->List.map(I.convertChildToFocus);
    [%log.debug
      "ret: " ++ (ret->List.map(ID.toString) |> String.concat(","));
      ("", "")
    ];
    ret;
  };

  let childrenOfRoot = graph => {
    [%log.debug "childrenOfRoot"; ("", "")];
    graph
    ->childIdsOfRoot
    ->List.reduce([], (trees, id) => {
        switch (graph->subGraphForNode(id)) {
        | Some(t) => [t, ...trees]
        | None => trees
        }
      });
  };

  let childIds = (graph, id) => {
    switch (graph->subGraphForNode(id)) {
    | Some(g) =>
      g.tree
      ->IDTree.children
      ->Map.keysToArray
      ->List.fromArray
      ->List.map(I.convertChildToFocus)
    | None => []
    };
  };

  let children = (graph, id) => {
    graph
    ->childIds(id)
    ->List.reduce([], (trees, id) => {
        switch (graph->subGraphForNode(id)) {
        | Some(t) => [t, ...trees]
        | None => trees
        }
      });
  };

  let childData = (graph, id) => {
    graph
    ->childIds(id)
    ->List.reduce([], (data, id) => {
        switch (graph->dataForNode(id)) {
        | Some(d) => [d, ...data]
        | None => data
        }
      });
  };

  let addNodeAtPath = (graph, id, data, path) => {
    let tree = graph.tree->IDTree.addChild(path, id);
    let node = EL.create(data, path);
    let masterLookup = graph.masterLookup->Map.set(id, node);
    {masterLookup, tree};
  };

  let addNode = (graph, id, data) => {
    let path = P.empty();
    graph->addNodeAtPath(id, data, path);
  };

  let addNodeUnder = (graph, id, data, under) => {
    switch (graph->pathFromNode(under->I.convertParentToFocus)) {
    | Some(path) =>
      let path = path->P.append(under);
      graph->addNodeAtPath(id, data, path);
    | None => graph
    };
  };

  let removeNode = (graph, id) =>
    // if id exists then remove it from masterLookup and tree
    if (graph->containsId(id)) {
      // first need to find its path in the tree
      switch (graph->pathFromNode(id)) {
      | Some(path) =>
        /* %log.debug */
        /* "removeNode:" ++ id->ID.toString; */
        /* %log.debug */
        /* "removeNode - pathUp:" ++ path->P.toString; */
        let pid = id->I.convertFocusToParent;
        let masterLookup =
          graph.masterLookup
          ->Map.remove(id) // have to remove the node
          ->Map.map(dataWithPath => {
              dataWithPath->EL.setPathUp(
                dataWithPath->EL.pathUp->P.removeElement(pid),
              )
            });
        let tree =
          graph.tree->IDTree.removeChild(path, id->I.convertFocusToChild);
        Result.Ok({masterLookup, tree});
      // can now remove from master list and tree
      | None => Result.Error("removeNode failed to get parent path")
      };
    } else {
      Result.Ok(graph);
    };

  let moveChild = (graph, from, under) => {
    let pid = under->I.convertParentToFocus;
    if (graph->containsId(pid)) {
      let id = from->I.convertChildToFocus;
      switch (graph->dataForNode(id)) {
      | Some(data) =>
        // remove old child node first as it might edit the graph
        // then can calculate new paths properly
        graph
        ->removeNode(id)
        ->Result.flatMap(graph => {
            // know pid already exist
            switch (graph->pathFromNode(pid)) {
            | Some(parentPathUp) =>
              // NOTE remember to append the new "under" id
              let pidPathUp = parentPathUp->P.append(under);
              /* %log.debug */
              /* "moveChild:" ++ pidPathUp->P.toString; */
              let masterLookup =
                graph.masterLookup->Map.set(id, EL.create(data, pidPathUp));

              let tree = graph.tree->IDTree.addChild(pidPathUp, id);
              Result.Ok({masterLookup, tree});
            | None => Result.Error("moveChild failed to get parent path")
            }
          })
      | None => Result.Error("moveChild failed to get data")
      };
    } else {
      /* %log.debug */
      /* "passthrough"; */
      Result.Ok(graph);
    };
  };

  let removeSubtree = (graph, id) =>
    // if id exists then remove it from masterLookup and tree
    if (graph->containsId(id)) {
      // first need to find its path in the tree
      switch (graph->pathFromNode(id)) {
      | Some(path) =>
        /* %log.debug */
        /* "found path: " ++ path->P.toString; */
        // NOTE remember to append id because do not want to delete siblings of id
        let idPath = path->P.append(id->I.convertFocusToParent);
        // can now remove id and all children from master list and tree
        let ids =
          graph.tree
          ->IDTree.getChildIds(idPath, false) // childIds doesnt include id
          ->Array.map(I.convertChildToFocus)
          ->Array.concat([|id|]); // so add it on explicitly
        /* %log.debug */
        /* ids->Array.map(ID.toString)->List.fromArray |> String.concat(","); */
        let masterLookup = graph.masterLookup->Map.removeMany(ids);
        // remove the subtree tipped by id found at path
        let tree =
          graph.tree->IDTree.removeSubtree(path, id->I.convertFocusToChild);
        Result.Ok({masterLookup, tree});
      | None => Result.Error("removeSubtree failed to get parent path")
      };
    } else {
      Result.Ok(graph);
    };

  let _setSubGraphForNode = (graph, pid, id, subgraph) => {
    /* [%log.debug "setSubGraphForNode: " ++ id->ID.toString; ("", "")]; */
    /* [%log.debug "input graph:" ++ graph->toString; ("", "")]; */
    /* [%log.debug "adding subgraph:" ++ subgraph->toString; ("", "")]; */
    /* [%log.debug "under:" ++ pid->PID.toString; ("", "")]; */
    subgraph->size == 0
      ? graph->Result.Ok
      : {
        let masterLookup = graph.masterLookup;
        switch (graph->pathFromNode(pid->I.convertParentToFocus)) {
        | Some(pathUp) =>
          let pathUp = pathUp->P.append(pid);
          /* [%log.debug "got pathUp: " ++ pathUp->P.toString; ("", "")]; */
          let g =
            graph->containsId(id)
              ? graph->removeSubtree(id) : graph->Result.Ok;
          g->Result.flatMap(graph => {
            /* [%log.debug "removed subtree at: " ++ id->ID.toString; ("", "")]; */
            /* [%log.debug graph->toString; ("", "")]; */

            let tree =
              graph.tree->IDTree.addSubtree(id, pathUp, subgraph.tree);
            /* [%log.debug "got tree: " ++ tree->IDTree.toString; ("", "")]; */

            // know pid already exist
            let pidPathUp = pathUp; //->P.append(id->I.convertFocusToParent);
            /* [%log.debug */
            /*   "got pid pathUp: " ++ pidPathUp->P.toString; */
            /*   ("", "") */
            /* ]; */

            let toMerge =
              tree
              ->IDTree.getChildPaths(pidPathUp, true) // include the original parent ID in this
              ->Array.map(d => {
                  let i = fst(d)->I.convertChildToFocus;
                  let pth = snd(d);
                  /* [%log.debug */
                  /*   "got i: " ++ i->ID.toString ++ " - " ++ pth->P.toString; */
                  /*   ("", "") */
                  /* ]; */
                  // if the subgraph lookup doesnt have the dataForNode
                  // then hope it is on the original lookup
                  switch (subgraph.masterLookup->Map.get(i)) {
                  | Some(dataWithPath) => (
                      i,
                      dataWithPath->EL.setPathUp(pth),
                    )
                  | None =>
                    let dataWithPath = masterLookup->Map.getExn(i);
                    (i, dataWithPath->EL.setPathUp(pth));
                  };
                });

            let ret = {
              masterLookup: graph.masterLookup->Map.mergeMany(toMerge),
              tree,
            };
            /* [%log.debug */
            /*   "setSubGraphForNode returning: " ++ ret->toString; */
            /*   ("", "") */
            /* ]; */
            Result.Ok(ret);
          });
        | None =>
          [%log.debug
            "didn't get pathUp for id: " ++ id->ID.toString;
            ("", "")
          ];
          Result.Ok(graph);
        };
      };
  };

  let setSubGraphForNode = (graph, pid, subgraph) => {
    subgraph
    ->childIdsOfRoot
    ->List.reduce(graph->Result.Ok, (g, i) => {
        g->Result.flatMap(gg =>
          switch (subgraph->subGraphForNode(i)) {
          | Some(sg) => gg->_setSubGraphForNode(pid, i, sg)
          | None =>
            [%log.error
              "setSubGraphForNode: cannot find childID " ++ i->ID.toString;
              ("", "")
            ];
            gg->Result.Ok;
          }
        ) //should be present cos of reduce
      });
  };

  let _setSubGraphForRoot = (graph, id, subgraph) => {
    /* [%log.debug "setSubGraphForRoot: " ++ id->ID.toString; ("", "")]; */
    /* [%log.debug "input graph:" ++ graph->toString; ("", "")]; */
    /* [%log.debug "adding subgraph:" ++ subgraph->toString; ("", "")]; */
    subgraph->size == 0
      ? graph->Result.Ok
      : {
        let masterLookup = graph.masterLookup;
        let pathUp = P.empty();
        let tree = graph.tree->IDTree.addSubtree(id, pathUp, subgraph.tree);
        /* [%log.debug "got tree: " ++ tree->IDTree.toString; ("", "")]; */

        // know pid already exist
        let pidPathUp = pathUp->P.append(id->I.convertFocusToParent);
        /* [%log.debug "got pid pathUp: " ++ pidPathUp->P.toString; ("", "")]; */

        let toMerge =
          tree
          ->IDTree.getChildPaths(pidPathUp, true) // include the original parent ID in this
          ->Array.map(d => {
              let i = fst(d)->I.convertChildToFocus;
              let pth = snd(d);
              /* [%log.debug */
              /*   "got i: " ++ i->ID.toString ++ " - " ++ pth->P.toString; */
              /*   ("", "") */
              /* ]; */
              // if the subgraph lookup doesnt have the dataForNode
              // then hope it is on the original lookup
              switch (subgraph.masterLookup->Map.get(i)) {
              | Some(dataWithPath) => (i, dataWithPath->EL.setPathUp(pth))
              | None =>
                let dataWithPath = masterLookup->Map.getExn(i);
                (i, dataWithPath->EL.setPathUp(pth));
              };
            });

        let ret = {
          masterLookup: graph.masterLookup->Map.mergeMany(toMerge),
          tree,
        };

        /* [%log.debug */
        /*   "setSubGraphForRoot returning: " ++ ret->toString; */
        /*   ("", "") */
        /* ]; */
        Result.Ok(ret);
      };
  };

  let setSubGraphForRoot = (graph, subgraph) => {
    // TODO should be able to fastcheck this property:
    // for any subgraph of any graph, _setSubgraph(getSubgraph)
    subgraph
    ->childIdsOfRoot
    ->List.reduce(graph->Result.Ok, (g, i) => {
        g->Result.flatMap(gg =>
          gg->_setSubGraphForRoot(
            i,
            subgraph->subGraphForNode(i)->Option.getExn,
          )
        ) //should be present cos of reduce
      });
  };

  let trimPaths = (graph, pathToTrimOff) => {
    switch (pathToTrimOff) {
    | Some(pth) =>
      let masterLookup =
        graph.masterLookup
        ->Map.map(d => d->EL.setPathUp(d->EL.pathUp->P.trim(pth)));
      {...graph, masterLookup};
    | None => graph
    };
  };

  let moveSubtree = (graph, from, under) => {
    let id = from->Identity.convertChildToFocus;
    let pid = under->I.convertParentToFocus;
    let masterLookup = graph.masterLookup;
    switch (graph->containsId(id), graph->containsId(pid)) {
    | (true, true) =>
      /* %log.debug */
      /* "pidPath In: " ++ graph->pathFromNode(pid)->Option.getExn->P.toString; */
      switch (graph->subGraphForNode(id)) {
      | Some(subtree) =>
        graph
        ->removeSubtree(id)
        ->Result.flatMap(graph => {
            // know pid already exist
            switch (graph->pathFromNode(pid)) {
            | Some(parentPathUp) =>
              let pidPathUp = parentPathUp->P.append(under);
              let tree =
                graph.tree->IDTree.addSubtree(id, pidPathUp, subtree.tree);
              let recalculatedPaths =
                tree
                ->IDTree.getChildPaths(pidPathUp, false) // dont want parent ID here
                ->Array.map(d => {
                    let i = fst(d)->I.convertChildToFocus;
                    let pth = snd(d);
                    /* %log.debug */
                    /* "got i: " ++ i->ID.toString ++ " - " ++ pth->P.toString; */
                    let dataWithPath = masterLookup->Map.getExn(i);
                    (i, dataWithPath->EL.setPathUp(pth));
                  });

              Result.Ok({
                masterLookup: masterLookup->Map.mergeMany(recalculatedPaths),
                tree,
              });
            | None => Result.Error("moveSubtree failed to get parent path")
            }
          })
      | None => Result.Error("moveSubtree failed to get subtree")
      }
    | (false, _)
    | (_, false) => Result.Ok(graph)
    };
  };

  let map = (graph, f) => {
    {
      ...graph,
      masterLookup:
        graph.masterLookup->Map.map(d => d->EL.setValue(f(d->EL.value))),
    };
  };

  let updateChildren = (graph, id, f) => {
    switch (graph->subGraphForNode(id)) {
    | Some(subgraph) =>
      let idsToUpdate =
        subgraph.tree
        ->IDTree.children
        ->Map.keysToArray
        ->Array.map(I.convertChildToFocus)
        ->Array.map(id => {
            let d = subgraph.masterLookup->Map.getExn(id);
            /* [%log.debug "got id: " ++ id->ID.toString; ("", "")]; */
            (id, d->EL.setValue(f(d->EL.value)));
          });

      let masterLookup = graph.masterLookup->Map.mergeMany(idsToUpdate);
      {...graph, masterLookup};
    | None => graph
    };
  };

  let forEach = (graph, f) => {
    graph.masterLookup->Map.forEach((k, v) => {f(k, v->EL.value)});
  };

  let keep = (graph, f) => {
    // partition masterLookup into (keeping, discarding)
    // then remove from tree whats in the discard pile
    // but making sure that remaining nodes are all reachable from the root
    // then reform smaller master lookup by getting new paths
    let (willKeep, willDiscard) =
      graph.masterLookup
      ->Map.toArray
      ->Array.partition(kv => {f(fst(kv), snd(kv)->EL.value)});

    let lookup = ID.Map.make()->Map.mergeMany(willKeep);

    let tree =
      willDiscard->Array.reduce(
        graph.tree,
        (tree, idAndPath) => {
          let id = fst(idAndPath);
          let dataWithPath = snd(idAndPath);
          tree->IDTree.removeSubtree(
            dataWithPath->EL.pathUp,
            id->I.convertFocusToChild,
          );
        },
      );

    let newChildPaths =
      tree
      ->IDTree.getAllPaths
      ->Array.map(d => {
          let i = fst(d)->I.convertChildToFocus;
          let pth = snd(d);
          let dataWithPath = lookup->Map.getExn(i);
          (i, dataWithPath->EL.setPathUp(pth));
        });

    let newGraph = empty();
    let masterLookup = newGraph.masterLookup->Map.mergeMany(newChildPaths);
    {masterLookup, tree};
  };

  let toKeyValueArrayWithPaths = graph => {
    graph.masterLookup
    ->Map.toArray
    ->Array.map(((id, d)) => {(id, d->EL.pathUp, d->EL.value)});
  };

  let toKeyValueArray = graph => {
    graph->toKeyValueArrayWithPaths->Array.map(((id, _pth, d)) => (id, d));
  };

  let toArray = graph => {
    graph->toKeyValueArray->Array.map(d => snd(d));
  };

  let rec _auxTopoSort = (root, unsorted, nodeId, parentNodeId) => {
    switch (unsorted) {
    | [] =>
      /* [%log.debug "last one: " ++ root->nodeId->ID.toString; ("", "")]; */
      []
    | _ as unsorted =>
      let pid = root->nodeId->I.convertFocusToParent;
      let (children, unsorted_) =
        unsorted->List.partition(d =>
          d
          ->parentNodeId
          ->Option.eq(Some(pid), (a, b) =>
              a->PID.toString == b->PID.toString
            )
        );
      /* [%log.debug */
      /*   root->nodeId->ID.toString */
      /*   ++ " children: " */
      /*   ++ ( */
      /*     children->List.map(d => d->nodeId->ID.toString) */
      /*     |> String.concat(",") */
      /*   ); */
      /*   ("", "") */
      /* ]; */
      children->List.concat(
        children
        ->List.map(c => c->_auxTopoSort(unsorted_, nodeId, parentNodeId))
        ->List.toArray
        ->List.concatMany,
      );
    };
  };

  let topoSort = (data, nodeId, parentNodeId) => {
    let sortedData =
      // NOTE sort by parentNodeId so that the root node with id="" is first
      data
      ->SortArray.stableSortBy((d1, d2) => {
          compare(
            d1
            ->parentNodeId
            ->Option.map(PID.toString)
            ->Option.getWithDefault(""),
            d2
            ->parentNodeId
            ->Option.map(PID.toString)
            ->Option.getWithDefault(""),
          )
        })
      ->List.fromArray;
    /* [%log.debug */
    /*   "INPUT:\n" */
    /*   ++ ( */
    /*     sortedData->List.map(d => */
    /*       d->nodeId->ID.toString */
    /*       ++ ": " */
    /*       ++ d */
    /*          ->parentNodeId */
    /*          ->Option.map(PID.toString) */
    /*          ->Option.getWithDefault("ROOT") */
    /*     ) */
    /*     |> String.concat("\n") */
    /*   ); */
    /*   ("", "") */
    /* ]; */
    switch (sortedData) {
    | [root, ...unsorted] =>
      let ret =
        [root, ..._auxTopoSort(root, unsorted, nodeId, parentNodeId)]
        ->List.toArray;
      /* [%log.debug */
      /*   "OUTPUT:\n" */
      /*   ++ ( */
      /*     ret */
      /*     ->List.fromArray */
      /*     ->List.map(d => */
      /*         d->nodeId->ID.toString */
      /*         ++ ": " */
      /*         ++ d */
      /*            ->parentNodeId */
      /*            ->Option.map(PID.toString) */
      /*            ->Option.getWithDefault("ROOT") */
      /*       ) */
      /*     |> String.concat("\n") */
      /*   ); */
      /*   ("", "") */
      /* ]; */

      ret;
    | [] => [||]
    };
  };

  let fromArray = (data, nodeId, parentNodeId) => {
    data->Array.size == 0
      ? empty()
      : topoSort(data, nodeId, parentNodeId)
        ->Array.reduceWithIndex(empty(), (graph, d, i)
            /* [%log.debug */
            /*   "adding node [" */
            /*   ++ d->nodeId->ID.toString */
            /*   ++ "] with parent [" */
            /*   ++ d */
            /*      ->parentNodeId */
            /*      ->Option.map(PID.toString) */
            /*      ->Option.getWithDefault("") */
            /*   ++ "]"; */
            /*   ("", "") */
            /* ]; */
            =>
              if (i == 0) {
                graph->addNode(d->nodeId, d);
              } else {
                graph->addNodeUnder(
                  d->nodeId,
                  d,
                  d->parentNodeId->Option.getExn,
                );
              }
            );
  };

  let eq = (g, h) => {
    let gMap = g.masterLookup;
    let hMap = h.masterLookup;
    gMap->Map.eq(hMap, (el1, el2) => {el1->EL.eq(el2)});
  };
};
