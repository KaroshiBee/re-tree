type r('d) = {
  x: int,
  y: string,
  z: 'd,
};

module Example = {
  type readonly;
  type readwrite;

  module type AccessRW = {
    type t('a, 'el);
    let create: (int, string, 'el) => t(readwrite, 'el);
    let getX: t('a, 'el) => int;
    let getY: t('a, 'el) => string;
    let setX: (t(readwrite, 'el), int) => t(readwrite, 'el);
    let setY: (t(readwrite, 'el), string) => t(readwrite, 'el);
    let readonlyView: t('a, 'el) => t(readonly, 'el);
  };

  module M: AccessRW = {
    type t('a, 'd) = r('d);
    let create = (i, s, el) => {x: i, y: s, z: el};
    let getX = t => t.x;
    let getY = t => t.y;

    let setX = (t, i) => {...t, x: i};
    let setY = (t, s) => {...t, y: s};
    let readonlyView = a => a;
  };
};

open BsMocha.Mocha;
module Assert = BsMocha.Assert;

describe("stuff", () => {
  Example.
    /* module A: AccessRO = M; */
    /* module B: AccessRW = M; */
    (
      it("doesstuff", () => {
        let b = M.create(2, "a", 0.3);
        let a = M.readonlyView(b);
        Assert.equal(a->M.getX, b->M.getX);
        let b = b->M.setY("x");
        Assert.not_equal(a->M.getY, b->M.getY);
        //let a = a->M.setX(3);
        //        Assert.ok(false);
      })
    )
});
