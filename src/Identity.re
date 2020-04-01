module Make = (()) => {
  module type Id_t = {
    type t;
    let create: string => t;
    let toString: t => string;
  };
  module Id: Id_t = {
    exception Empty_id;
    type t = string;

    let create = (id: string) =>
      id->String.length > 0
        ? id
        : {
          raise(Empty_id);
          id;
        };
    let toString = s => s;
  };

  type t = Id.t;
  let create = Id.create;
  let toString = Id.toString;

  module Comparable =
    Belt.Id.MakeComparable({
      type t = Id.t;
      let cmp = Pervasives.compare;
    });

  module Map = {
    type t('t) = Map.t(Id.t, 't, Comparable.identity);
    let make = () => Map.make(~id=(module Comparable));
  };

  module Set = {
    type t('t) = Set.t(Id.t, Comparable.identity);
    let make = () => Set.make(~id=(module Comparable));
    let fromArray = (vals: array('a)) =>
      Set.fromArray(vals, ~id=(module Comparable));
  };
};

module FocusId =
  Make({});

module ChildId =
  Make({});

module ParentId =
  Make({});

// looks like bucklescript converts all these to the id function
let convertChildToParent = (id: ChildId.t): ParentId.t => {
  id->ChildId.toString->ParentId.create;
};

let convertParentToChild = (id: ParentId.t): ChildId.t => {
  id->ParentId.toString->ChildId.create;
};

let convertFocusToParent = (id: FocusId.t): ParentId.t => {
  id->FocusId.toString->ParentId.create;
};

let convertFocusToChild = (id: FocusId.t): ChildId.t => {
  id->FocusId.toString->ChildId.create;
};

let convertParentToFocus = (id: ParentId.t): FocusId.t => {
  id->ParentId.toString->FocusId.create;
};

let convertChildToFocus = (id: ChildId.t): FocusId.t => {
  id->ChildId.toString->FocusId.create;
};
