module I = Identity;
module PID = I.ParentId;

module type PATH = {
  type el;
  type t;
  let empty: unit => t;
  let fromList: list(string) => t;
  let fromPathToRootList: list(string) => t;
  let fromRootToPathList: list(string) => t;
  let moveUp: t => t;
  let moveDown: t => t;
  let parent: t => option(el);
  let root: t => option(el);
  let pathToRoot: t => list(el);
  let pathFromRoot: t => list(el);
  let eq: (t, t) => bool;
  let append: (t, el) => t;
  let toString: t => string;
  let removeElement: (t, el) => t;
  let concat: (t, t) => t;
};

module Parents: PATH with type el = PID.t = {
  type el = PID.t;
  type t = {pathUp: list(el)};

  let empty = () => {pathUp: []};
  let fromList = path => {pathUp: path->List.map(s => PID.create(s))};
  let fromPathToRootList = fromList;
  let fromRootToPathList = path => path->List.reverse->fromList;
  let moveUp = parents => {
    {
      pathUp:
        switch (parents.pathUp) {
        | [_hd, ...tl] => tl
        | _ => []
        },
    };
  };
  let moveDown = parents => {
    let n = parents.pathUp->List.size;
    {pathUp: parents.pathUp->List.take(n - 1)->Option.getWithDefault([])};
  };
  let parent = parents =>
    switch (parents.pathUp) {
    | [hd, ..._tl] => Some(hd)
    | _ => None
    };
  let root = parents => {
    let n = List.size(parents.pathUp);
    parents.pathUp->List.get(n - 1);
  };

  let pathToRoot = (parents: t) => {
    parents.pathUp;
  };

  let pathFromRoot = (parents: t) => {
    parents->pathToRoot->List.reverse;
  };

  let eq = (p1, p2) => {
    List.eq(p1.pathUp, p2.pathUp, (id1, id2) => id1 == id2);
  };

  let append = (parents, el) => {
    {pathUp: [el, ...parents.pathUp]};
  };

  let toString = parents =>
    parents.pathUp->List.map(p => p->PID.toString) |> String.concat(",");

  let removeElement = (parents, el) => {
    {pathUp: parents.pathUp->List.keep(pid => pid != el)};
  };

  let concat = (parents, other) => {
    {pathUp: parents.pathUp->List.concat(other.pathUp)};
  };
};
