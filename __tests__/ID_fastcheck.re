// just a repo of generators for IDs

module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;

module Arbitrary = {
  open BsFastCheck.Arbitrary;
  let idString = stringWithLength(1, 10);
  let id = idString->Derive.map(ID.create);
  let cid = idString->Derive.map(CID.create);
  let pid = idString->Derive.map(PID.create);
};
