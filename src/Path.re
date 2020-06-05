module PID = Identity.ParentId;

module type PATH = {
  type el;
  type t;
  let empty: unit => t;
  let size: t => int;
  let fromList: list(string) => t;
  let fromPathToRootList: list(string) => t;
  let fromRootToPathList: list(string) => t;
  let moveUp: t => t;
  let parent: t => option(el);
  let root: t => option(el);
  let pathToRoot: t => list(el);
  let pathFromRoot: t => list(el);
  let eq: (t, t) => bool;
  let append: (t, el) => t;
  let toString: t => string;
  let removeElement: (t, el) => t;
  let concat: (t, t) => t;
  let trim: (t, t) => t;
};

module T: PATH with type el = Path_immutable.el = Path_immutable;
