module type HASHABLE = {
  type t;
  let toHash: t => int;
  let eq: (t, t) => bool;
};

module HashablePath: HASHABLE with type t = Path.T.t = {
  include Path.T;
  let toHash = pth => pth->toString->Hashtbl.hash;
};

module HashableIDTree: HASHABLE with type t = IDTree.T.t = {
  include IDTree.T;
  let toHash = tree => tree->getAllPaths;
};
