module type STRINGLY = {
  type t;
  let toString: t => string;
}

