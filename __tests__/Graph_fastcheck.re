open BsMocha.Mocha;
open BsFastCheck.Arbitrary;
open BsFastCheck.Property.Sync;
open BsFastCheck.Arbitrary.Combinators;

module M = Graph.T;
module I = Identity;
module ID = I.FocusId;
module CID = I.ChildId;
module PID = I.ParentId;
module P = Path.T;

module IDs = ID_fastcheck.Arbitrary;
module Paths = Path_fastcheck.Arbitrary;

module Arbitrary = {
  type data = {
    a: int,
    b: string,
    c: bool,
  };
  let data =
    tuple3(integer(), string(), boolean())
    ->Derive.map(((a, b, c)) => {a, b, c});
  /* let depthN = n => */
  /*   list(arrayWithLength(IDs.id, 1, n)) */
  /*   ->Derive.chain(ls => {ls->List.reduce(M.empty(), (g, arrPath))}); */
};
