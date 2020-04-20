// just a repo of generators for IDs

module I = Retree.Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module Uuid = {
  [@bs.module "uuid"] external v4: unit => string = "v4";
};

module Arbitrary = {
  open BsFastCheck.Arbitrary;
  let idString = string()->Derive.map(_ => Uuid.v4());
  let id = idString->Derive.map(ID.create);
  let cid = idString->Derive.map(CID.create);
  let pid = idString->Derive.map(PID.create);
};
