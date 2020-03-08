__all__ = ['mynum']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(require, module, exports, this, arguments, var=var):
    var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
    var.registers(['module', 'require', 'exports', 'uniq', 'nums'])
    var.put('uniq', var.get('require')(Js('uniq')))
    var.put('nums', Js([Js(5.0), Js(2.0), Js(1.0), Js(3.0), Js(2.0), Js(5.0), Js(4.0), Js(2.0), Js(0.0), Js(1.0)]))
    var.get('console').callprop('log', var.get('uniq')(var.get('nums')))
PyJs_anonymous_0_._set_name('anonymous')
@Js
def PyJs_anonymous_1_(require, module, exports, this, arguments, var=var):
    var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
    var.registers(['unique', 'module', 'require', 'unique_eq', 'exports', 'unique_pred'])
    @Js
    def PyJsHoisted_unique_pred_(list, compare, this, arguments, var=var):
        var = Scope({'list':list, 'compare':compare, 'this':this, 'arguments':arguments}, var)
        var.registers(['compare', 'a', 'len', 'b', 'list', 'i', 'ptr'])
        var.put('ptr', Js(1.0))
        var.put('len', var.get('list').get('length'))
        var.put('a', var.get('list').get('0'))
        var.put('b', var.get('list').get('0'))
        #for JS loop
        var.put('i', Js(1.0))
        while (var.get('i')<var.get('len')):
            try:
                var.put('b', var.get('a'))
                var.put('a', var.get('list').get(var.get('i')))
                if var.get('compare')(var.get('a'), var.get('b')):
                    if PyJsStrictEq(var.get('i'),var.get('ptr')):
                        (var.put('ptr',Js(var.get('ptr').to_number())+Js(1))-Js(1))
                        continue
                    var.get('list').put((var.put('ptr',Js(var.get('ptr').to_number())+Js(1))-Js(1)), var.get('a'))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('list').put('length', var.get('ptr'))
        return var.get('list')
    PyJsHoisted_unique_pred_.func_name = 'unique_pred'
    var.put('unique_pred', PyJsHoisted_unique_pred_)
    @Js
    def PyJsHoisted_unique_eq_(list, this, arguments, var=var):
        var = Scope({'list':list, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'len', 'b', 'list', 'i', 'ptr'])
        var.put('ptr', Js(1.0))
        var.put('len', var.get('list').get('length'))
        var.put('a', var.get('list').get('0'))
        var.put('b', var.get('list').get('0'))
        #for JS loop
        var.put('i', Js(1.0))
        while (var.get('i')<var.get('len')):
            try:
                var.put('b', var.get('a'))
                var.put('a', var.get('list').get(var.get('i')))
                if PyJsStrictNeq(var.get('a'),var.get('b')):
                    if PyJsStrictEq(var.get('i'),var.get('ptr')):
                        (var.put('ptr',Js(var.get('ptr').to_number())+Js(1))-Js(1))
                        continue
                    var.get('list').put((var.put('ptr',Js(var.get('ptr').to_number())+Js(1))-Js(1)), var.get('a'))
            finally:
                    PyJsComma(var.put('i',Js(var.get('i').to_number())+Js(1)),var.put('b', var.get('a')))
        var.get('list').put('length', var.get('ptr'))
        return var.get('list')
    PyJsHoisted_unique_eq_.func_name = 'unique_eq'
    var.put('unique_eq', PyJsHoisted_unique_eq_)
    @Js
    def PyJsHoisted_unique_(list, compare, sorted, this, arguments, var=var):
        var = Scope({'list':list, 'compare':compare, 'sorted':sorted, 'this':this, 'arguments':arguments}, var)
        var.registers(['compare', 'sorted', 'list'])
        if PyJsStrictEq(var.get('list').get('length'),Js(0.0)):
            return var.get('list')
        if var.get('compare'):
            if var.get('sorted').neg():
                var.get('list').callprop('sort', var.get('compare'))
            return var.get('unique_pred')(var.get('list'), var.get('compare'))
        if var.get('sorted').neg():
            var.get('list').callprop('sort')
        return var.get('unique_eq')(var.get('list'))
    PyJsHoisted_unique_.func_name = 'unique'
    var.put('unique', PyJsHoisted_unique_)
    Js('use strict')
    pass
    pass
    pass
    var.get('module').put('exports', var.get('unique'))
PyJs_anonymous_1_._set_name('anonymous')
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['r'])
    @Js
    def PyJsHoisted_r_(e, n, t, this, arguments, var=var):
        var = Scope({'e':e, 'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['u', 't', 'i', 'e', 'n', 'o'])
        @Js
        def PyJsHoisted_o_(i, f, this, arguments, var=var):
            var = Scope({'i':i, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'f', 'i', 'a', 'c'])
            if var.get('n').get(var.get('i')).neg():
                if var.get('e').get(var.get('i')).neg():
                    var.put('c', ((Js('function')==var.get('require',throw=False).typeof()) and var.get('require')))
                    if (var.get('f').neg() and var.get('c')):
                        return var.get('c')(var.get('i'), Js(0.0).neg())
                    if var.get('u'):
                        return var.get('u')(var.get('i'), Js(0.0).neg())
                    var.put('a', var.get('Error').create(((Js("Cannot find module '")+var.get('i'))+Js("'"))))
                    PyJsTempException = JsToPyException(PyJsComma(var.get('a').put('code', Js('MODULE_NOT_FOUND')),var.get('a')))
                    raise PyJsTempException
                var.put('p', var.get('n').put(var.get('i'), Js({'exports':Js({})})))
                @Js
                def PyJs_anonymous_3_(r, this, arguments, var=var):
                    var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                    var.registers(['n', 'r'])
                    var.put('n', var.get('e').get(var.get('i')).get('1').get(var.get('r')))
                    return var.get('o')((var.get('n') or var.get('r')))
                PyJs_anonymous_3_._set_name('anonymous')
                var.get('e').get(var.get('i')).get('0').callprop('call', var.get('p').get('exports'), PyJs_anonymous_3_, var.get('p'), var.get('p').get('exports'), var.get('r'), var.get('e'), var.get('n'), var.get('t'))
            return var.get('n').get(var.get('i')).get('exports')
        PyJsHoisted_o_.func_name = 'o'
        var.put('o', PyJsHoisted_o_)
        pass
        #for JS loop
        var.put('u', ((Js('function')==var.get('require',throw=False).typeof()) and var.get('require')))
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('t').get('length')):
            try:
                var.get('o')(var.get('t').get(var.get('i')))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('o')
    PyJsHoisted_r_.func_name = 'r'
    var.put('r', PyJsHoisted_r_)
    pass
    return var.get('r')
PyJs_anonymous_2_._set_name('anonymous')
PyJs_anonymous_2_()(Js({'1':Js([PyJs_anonymous_0_, Js({'uniq':Js(2.0)})]),'2':Js([PyJs_anonymous_1_, Js({})])}), Js({}), Js([Js(1.0)]))
pass


# Add lib to the module scope
mynum = var.to_python()