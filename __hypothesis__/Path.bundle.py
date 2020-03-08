__all__ = ['Path']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
def PyJs_LONG_84_(var=var):
    @Js
    def PyJs_anonymous_0_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['get', 'mapU', 'makeBy', 'getIndexByU', 'keepWithIndex', 'map', 'shuffleInPlace', 'exports', 'swapUnsafe', 'Caml_option', 'Caml_primitive', 'getBy', 'some2U', 'some2', 'some', 'setExn', 'zip', 'every', 'rangeBy', 'set', 'reverse', 'Js_math', 'reduceReverse2U', 'zipByU', 'forEachWithIndexU', 'reduceWithIndexU', 'everyU', 'module', 'getIndexBy', 'every2U', 'forEachWithIndex', 'fill', 'sliceToEnd', 'reduceWithIndex', 'blitUnsafe', 'keepMapU', 'reduceReverse', 'cmpU', 'eq', 'range', 'reverseInPlace', 'require', 'getExn', 'reduceReverseU', 'shuffle', 'cmp', 'Curry', 'make', 'keep', 'mapWithIndexU', 'partition', 'zipBy', 'every2', 'makeByU', 'reduceU', 'keepWithIndexU', 'mapWithIndex', 'forEach', 'someU', 'concat', 'keepMap', 'reduceReverse2', 'makeByAndShuffleU', 'blit', 'eqU', 'getByU', 'keepU', 'slice', 'partitionU', 'everyAux2', 'makeByAndShuffle', 'reduce', 'concatMany', 'unzip', 'forEachU'])
        @Js
        def PyJsHoisted_get_(arr, i, this, arguments, var=var):
            var = Scope({'arr':arr, 'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr', 'i'])
            if ((var.get('i')>=Js(0.0)) and (var.get('i')<var.get('arr').get('length'))):
                return var.get('Caml_option').callprop('some', var.get('arr').get(var.get('i')))
        PyJsHoisted_get_.func_name = 'get'
        var.put('get', PyJsHoisted_get_)
        @Js
        def PyJsHoisted_getExn_(arr, i, this, arguments, var=var):
            var = Scope({'arr':arr, 'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr', 'i'])
            if ((var.get('i')>=Js(0.0)) and (var.get('i')<var.get('arr').get('length'))).neg():
                PyJsTempException = JsToPyException(var.get('Error').create(Js('File "belt_Array.ml", line 25, characters 6-12')))
                raise PyJsTempException
            return var.get('arr').get(var.get('i'))
        PyJsHoisted_getExn_.func_name = 'getExn'
        var.put('getExn', PyJsHoisted_getExn_)
        @Js
        def PyJsHoisted_set_(arr, i, v, this, arguments, var=var):
            var = Scope({'arr':arr, 'i':i, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr', 'i', 'v'])
            if ((var.get('i')>=Js(0.0)) and (var.get('i')<var.get('arr').get('length'))):
                var.get('arr').put(var.get('i'), var.get('v'))
                return Js(True)
            else:
                return Js(False)
        PyJsHoisted_set_.func_name = 'set'
        var.put('set', PyJsHoisted_set_)
        @Js
        def PyJsHoisted_setExn_(arr, i, v, this, arguments, var=var):
            var = Scope({'arr':arr, 'i':i, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr', 'i', 'v'])
            if ((var.get('i')>=Js(0.0)) and (var.get('i')<var.get('arr').get('length'))).neg():
                PyJsTempException = JsToPyException(var.get('Error').create(Js('File "belt_Array.ml", line 31, characters 4-10')))
                raise PyJsTempException
            var.get('arr').put(var.get('i'), var.get('v'))
            return Js(0.0)
        PyJsHoisted_setExn_.func_name = 'setExn'
        var.put('setExn', PyJsHoisted_setExn_)
        @Js
        def PyJsHoisted_swapUnsafe_(xs, i, j, this, arguments, var=var):
            var = Scope({'xs':xs, 'i':i, 'j':j, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'tmp', 'i', 'j'])
            var.put('tmp', var.get('xs').get(var.get('i')))
            var.get('xs').put(var.get('i'), var.get('xs').get(var.get('j')))
            var.get('xs').put(var.get('j'), var.get('tmp'))
            return Js(0.0)
        PyJsHoisted_swapUnsafe_.func_name = 'swapUnsafe'
        var.put('swapUnsafe', PyJsHoisted_swapUnsafe_)
        @Js
        def PyJsHoisted_shuffleInPlace_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'i', 'i_finish'])
            var.put('len', var.get('xs').get('length'))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('swapUnsafe')(var.get('xs'), var.get('i'), var.get('Js_math').callprop('random_int', var.get('i'), var.get('len')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_shuffleInPlace_.func_name = 'shuffleInPlace'
        var.put('shuffleInPlace', PyJsHoisted_shuffleInPlace_)
        @Js
        def PyJsHoisted_shuffle_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'result'])
            var.put('result', var.get('xs').callprop('slice', Js(0.0)))
            var.get('shuffleInPlace')(var.get('result'))
            return var.get('result')
        PyJsHoisted_shuffle_.func_name = 'shuffle'
        var.put('shuffle', PyJsHoisted_shuffle_)
        @Js
        def PyJsHoisted_reverseInPlace_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'ofs', 'i_finish', 'len$1', 'xs$1', 'i'])
            var.put('len', var.get('xs').get('length'))
            var.put('xs$1', var.get('xs'))
            var.put('ofs', Js(0.0))
            var.put('len$1', var.get('len'))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((((var.get('len$1')/Js(2.0))|Js(0.0))-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('swapUnsafe')(var.get('xs$1'), ((var.get('ofs')+var.get('i'))|Js(0.0)), ((((((var.get('ofs')+var.get('len$1'))|Js(0.0))-var.get('i'))|Js(0.0))-Js(1.0))|Js(0.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_reverseInPlace_.func_name = 'reverseInPlace'
        var.put('reverseInPlace', PyJsHoisted_reverseInPlace_)
        @Js
        def PyJsHoisted_reverse_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'result', 'i_finish', 'i'])
            var.put('len', var.get('xs').get('length'))
            var.put('result', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('result').put(var.get('i'), var.get('xs').get(((((var.get('len')-Js(1.0))|Js(0.0))-var.get('i'))|Js(0.0))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('result')
        PyJsHoisted_reverse_.func_name = 'reverse'
        var.put('reverse', PyJsHoisted_reverse_)
        @Js
        def PyJsHoisted_make_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'res', 'i_finish', 'i', 'l'])
            if (var.get('l')<=Js(0.0)):
                return Js([])
            else:
                var.put('res', var.get('Array').create(var.get('l')))
                #for JS loop
                var.put('i', Js(0.0))
                var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.get('res').put(var.get('i'), var.get('f'))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('res')
        PyJsHoisted_make_.func_name = 'make'
        var.put('make', PyJsHoisted_make_)
        @Js
        def PyJsHoisted_makeByU_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'res', 'i_finish', 'i', 'l'])
            if (var.get('l')<=Js(0.0)):
                return Js([])
            else:
                var.put('res', var.get('Array').create(var.get('l')))
                #for JS loop
                var.put('i', Js(0.0))
                var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.get('res').put(var.get('i'), var.get('f')(var.get('i')))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('res')
        PyJsHoisted_makeByU_.func_name = 'makeByU'
        var.put('makeByU', PyJsHoisted_makeByU_)
        @Js
        def PyJsHoisted_makeBy_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l'])
            return var.get('makeByU')(var.get('l'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_makeBy_.func_name = 'makeBy'
        var.put('makeBy', PyJsHoisted_makeBy_)
        @Js
        def PyJsHoisted_makeByAndShuffleU_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['u', 'f', 'l'])
            var.put('u', var.get('makeByU')(var.get('l'), var.get('f')))
            var.get('shuffleInPlace')(var.get('u'))
            return var.get('u')
        PyJsHoisted_makeByAndShuffleU_.func_name = 'makeByAndShuffleU'
        var.put('makeByAndShuffleU', PyJsHoisted_makeByAndShuffleU_)
        @Js
        def PyJsHoisted_makeByAndShuffle_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l'])
            return var.get('makeByAndShuffleU')(var.get('l'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_makeByAndShuffle_.func_name = 'makeByAndShuffle'
        var.put('makeByAndShuffle', PyJsHoisted_makeByAndShuffle_)
        @Js
        def PyJsHoisted_range_(start, finish, this, arguments, var=var):
            var = Scope({'start':start, 'finish':finish, 'this':this, 'arguments':arguments}, var)
            var.registers(['cut', 'start', 'finish', 'arr', 'i'])
            var.put('cut', ((var.get('finish')-var.get('start'))|Js(0.0)))
            if (var.get('cut')<Js(0.0)):
                return Js([])
            else:
                var.put('arr', var.get('Array').create(((var.get('cut')+Js(1.0))|Js(0.0))))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<=var.get('cut')):
                    try:
                        var.get('arr').put(var.get('i'), ((var.get('start')+var.get('i'))|Js(0.0)))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('arr')
        PyJsHoisted_range_.func_name = 'range'
        var.put('range', PyJsHoisted_range_)
        @Js
        def PyJsHoisted_rangeBy_(start, finish, step, this, arguments, var=var):
            var = Scope({'start':start, 'finish':finish, 'step':step, 'this':this, 'arguments':arguments}, var)
            var.registers(['cut', 'i_finish', 'start', 'step', 'nb', 'cur', 'finish', 'arr', 'i'])
            var.put('cut', ((var.get('finish')-var.get('start'))|Js(0.0)))
            if ((var.get('cut')<Js(0.0)) or (var.get('step')<=Js(0.0))):
                return Js([])
            else:
                var.put('nb', ((((var.get('cut')/var.get('step'))|Js(0.0))+Js(1.0))|Js(0.0)))
                var.put('arr', var.get('Array').create(var.get('nb')))
                var.put('cur', var.get('start'))
                #for JS loop
                var.put('i', Js(0.0))
                var.put('i_finish', ((var.get('nb')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.get('arr').put(var.get('i'), var.get('cur'))
                        var.put('cur', ((var.get('cur')+var.get('step'))|Js(0.0)))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('arr')
        PyJsHoisted_rangeBy_.func_name = 'rangeBy'
        var.put('rangeBy', PyJsHoisted_rangeBy_)
        @Js
        def PyJsHoisted_zip_(xs, ys, this, arguments, var=var):
            var = Scope({'xs':xs, 'ys':ys, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'leny', 'i_finish', 'ys', 's', 'lenx', 'i'])
            var.put('lenx', var.get('xs').get('length'))
            var.put('leny', var.get('ys').get('length'))
            var.put('len', (var.get('lenx') if (var.get('lenx')<var.get('leny')) else var.get('leny')))
            var.put('s', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('s').put(var.get('i'), Js([var.get('xs').get(var.get('i')), var.get('ys').get(var.get('i'))]))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('s')
        PyJsHoisted_zip_.func_name = 'zip'
        var.put('zip', PyJsHoisted_zip_)
        @Js
        def PyJsHoisted_zipByU_(xs, ys, f, this, arguments, var=var):
            var = Scope({'xs':xs, 'ys':ys, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'f', 'leny', 'i_finish', 'ys', 's', 'lenx', 'i'])
            var.put('lenx', var.get('xs').get('length'))
            var.put('leny', var.get('ys').get('length'))
            var.put('len', (var.get('lenx') if (var.get('lenx')<var.get('leny')) else var.get('leny')))
            var.put('s', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('s').put(var.get('i'), var.get('f')(var.get('xs').get(var.get('i')), var.get('ys').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('s')
        PyJsHoisted_zipByU_.func_name = 'zipByU'
        var.put('zipByU', PyJsHoisted_zipByU_)
        @Js
        def PyJsHoisted_zipBy_(xs, ys, f, this, arguments, var=var):
            var = Scope({'xs':xs, 'ys':ys, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'f', 'ys'])
            return var.get('zipByU')(var.get('xs'), var.get('ys'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_zipBy_.func_name = 'zipBy'
        var.put('zipBy', PyJsHoisted_zipBy_)
        @Js
        def PyJsHoisted_concat_(a1, a2, this, arguments, var=var):
            var = Scope({'a1':a1, 'a2':a2, 'this':this, 'arguments':arguments}, var)
            var.registers(['i$1', 'i_finish$1', 'l2', 'a1', 'l1', 'a2', 'i_finish', 'a1a2', 'i'])
            var.put('l1', var.get('a1').get('length'))
            var.put('l2', var.get('a2').get('length'))
            var.put('a1a2', var.get('Array').create(((var.get('l1')+var.get('l2'))|Js(0.0))))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('l1')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('a1a2').put(var.get('i'), var.get('a1').get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            #for JS loop
            var.put('i$1', Js(0.0))
            var.put('i_finish$1', ((var.get('l2')-Js(1.0))|Js(0.0)))
            while (var.get('i$1')<=var.get('i_finish$1')):
                try:
                    var.get('a1a2').put(((var.get('l1')+var.get('i$1'))|Js(0.0)), var.get('a2').get(var.get('i$1')))
                finally:
                        var.put('i$1',Js(var.get('i$1').to_number())+Js(1))
            return var.get('a1a2')
        PyJsHoisted_concat_.func_name = 'concat'
        var.put('concat', PyJsHoisted_concat_)
        @Js
        def PyJsHoisted_concatMany_(arrs, this, arguments, var=var):
            var = Scope({'arrs':arrs, 'this':this, 'arguments':arguments}, var)
            var.registers(['arrs', 'j', 'result', 'i_finish', 'k_finish', 'cur', 'lenArrs', 'k', 'j_finish', 'i', 'totalLen'])
            var.put('lenArrs', var.get('arrs').get('length'))
            var.put('totalLen', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('lenArrs')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('totalLen', ((var.get('totalLen')+var.get('arrs').get(var.get('i')).get('length'))|Js(0.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.put('result', var.get('Array').create(var.get('totalLen')))
            var.put('totalLen', Js(0.0))
            #for JS loop
            var.put('j', Js(0.0))
            var.put('j_finish', ((var.get('lenArrs')-Js(1.0))|Js(0.0)))
            while (var.get('j')<=var.get('j_finish')):
                try:
                    var.put('cur', var.get('arrs').get(var.get('j')))
                    #for JS loop
                    var.put('k', Js(0.0))
                    var.put('k_finish', ((var.get('cur').get('length')-Js(1.0))|Js(0.0)))
                    while (var.get('k')<=var.get('k_finish')):
                        try:
                            var.get('result').put(var.get('totalLen'), var.get('cur').get(var.get('k')))
                            var.put('totalLen', ((var.get('totalLen')+Js(1.0))|Js(0.0)))
                        finally:
                                var.put('k',Js(var.get('k').to_number())+Js(1))
                finally:
                        var.put('j',Js(var.get('j').to_number())+Js(1))
            return var.get('result')
        PyJsHoisted_concatMany_.func_name = 'concatMany'
        var.put('concatMany', PyJsHoisted_concatMany_)
        @Js
        def PyJsHoisted_slice_(a, offset, len, this, arguments, var=var):
            var = Scope({'a':a, 'offset':offset, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'ofs', 'hasLen', 'a', 'result', 'i_finish', 'lena', 'offset', 'i', 'copyLength'])
            if (var.get('len')<=Js(0.0)):
                return Js([])
            else:
                var.put('lena', var.get('a').get('length'))
                var.put('ofs', (var.get('Caml_primitive').callprop('caml_int_max', ((var.get('lena')+var.get('offset'))|Js(0.0)), Js(0.0)) if (var.get('offset')<Js(0.0)) else var.get('offset')))
                var.put('hasLen', ((var.get('lena')-var.get('ofs'))|Js(0.0)))
                var.put('copyLength', (var.get('hasLen') if (var.get('hasLen')<var.get('len')) else var.get('len')))
                if (var.get('copyLength')<=Js(0.0)):
                    return Js([])
                else:
                    var.put('result', var.get('Array').create(var.get('copyLength')))
                    #for JS loop
                    var.put('i', Js(0.0))
                    var.put('i_finish', ((var.get('copyLength')-Js(1.0))|Js(0.0)))
                    while (var.get('i')<=var.get('i_finish')):
                        try:
                            var.get('result').put(var.get('i'), var.get('a').get(((var.get('ofs')+var.get('i'))|Js(0.0))))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    return var.get('result')
        PyJsHoisted_slice_.func_name = 'slice'
        var.put('slice', PyJsHoisted_slice_)
        @Js
        def PyJsHoisted_sliceToEnd_(a, offset, this, arguments, var=var):
            var = Scope({'a':a, 'offset':offset, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'ofs', 'a', 'result', 'i_finish', 'lena', 'offset', 'i'])
            var.put('lena', var.get('a').get('length'))
            var.put('ofs', (var.get('Caml_primitive').callprop('caml_int_max', ((var.get('lena')+var.get('offset'))|Js(0.0)), Js(0.0)) if (var.get('offset')<Js(0.0)) else var.get('offset')))
            var.put('len', ((var.get('lena')-var.get('ofs'))|Js(0.0)))
            var.put('result', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('result').put(var.get('i'), var.get('a').get(((var.get('ofs')+var.get('i'))|Js(0.0))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('result')
        PyJsHoisted_sliceToEnd_.func_name = 'sliceToEnd'
        var.put('sliceToEnd', PyJsHoisted_sliceToEnd_)
        @Js
        def PyJsHoisted_fill_(a, offset, len, v, this, arguments, var=var):
            var = Scope({'a':a, 'offset':offset, 'len':len, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'ofs', 'hasLen', 'a', 'i_finish', 'lena', 'v', 'fillLength', 'offset', 'i'])
            if (var.get('len')>Js(0.0)):
                var.put('lena', var.get('a').get('length'))
                var.put('ofs', (var.get('Caml_primitive').callprop('caml_int_max', ((var.get('lena')+var.get('offset'))|Js(0.0)), Js(0.0)) if (var.get('offset')<Js(0.0)) else var.get('offset')))
                var.put('hasLen', ((var.get('lena')-var.get('ofs'))|Js(0.0)))
                var.put('fillLength', (var.get('hasLen') if (var.get('hasLen')<var.get('len')) else var.get('len')))
                if (var.get('fillLength')>Js(0.0)):
                    #for JS loop
                    var.put('i', var.get('ofs'))
                    var.put('i_finish', ((((var.get('ofs')+var.get('fillLength'))|Js(0.0))-Js(1.0))|Js(0.0)))
                    while (var.get('i')<=var.get('i_finish')):
                        try:
                            var.get('a').put(var.get('i'), var.get('v'))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    return Js(0.0)
                else:
                    return Js(0.0)
            else:
                return Js(0.0)
        PyJsHoisted_fill_.func_name = 'fill'
        var.put('fill', PyJsHoisted_fill_)
        @Js
        def PyJsHoisted_blitUnsafe_(a1, srcofs1, a2, srcofs2, blitLength, this, arguments, var=var):
            var = Scope({'a1':a1, 'srcofs1':srcofs1, 'a2':a2, 'srcofs2':srcofs2, 'blitLength':blitLength, 'this':this, 'arguments':arguments}, var)
            var.registers(['a1', 'j', 'srcofs1', 'a2', 'blitLength', 'j$1', 'j_finish', 'srcofs2'])
            if (var.get('srcofs2')<=var.get('srcofs1')):
                #for JS loop
                var.put('j', Js(0.0))
                var.put('j_finish', ((var.get('blitLength')-Js(1.0))|Js(0.0)))
                while (var.get('j')<=var.get('j_finish')):
                    try:
                        var.get('a2').put(((var.get('j')+var.get('srcofs2'))|Js(0.0)), var.get('a1').get(((var.get('j')+var.get('srcofs1'))|Js(0.0))))
                    finally:
                            var.put('j',Js(var.get('j').to_number())+Js(1))
                return Js(0.0)
            else:
                #for JS loop
                var.put('j$1', ((var.get('blitLength')-Js(1.0))|Js(0.0)))
                while (var.get('j$1')>=Js(0.0)):
                    try:
                        var.get('a2').put(((var.get('j$1')+var.get('srcofs2'))|Js(0.0)), var.get('a1').get(((var.get('j$1')+var.get('srcofs1'))|Js(0.0))))
                    finally:
                            var.put('j$1',Js(var.get('j$1').to_number())-Js(1))
                return Js(0.0)
        PyJsHoisted_blitUnsafe_.func_name = 'blitUnsafe'
        var.put('blitUnsafe', PyJsHoisted_blitUnsafe_)
        @Js
        def PyJsHoisted_blit_(a1, ofs1, a2, ofs2, len, this, arguments, var=var):
            var = Scope({'a1':a1, 'ofs1':ofs1, 'a2':a2, 'ofs2':ofs2, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'j', 'a1', 'srcofs1', 'lena1', 'a2', 'blitLength', 'ofs2', 'j$1', 'lena2', 'j_finish', 'ofs1', 'srcofs2'])
            var.put('lena1', var.get('a1').get('length'))
            var.put('lena2', var.get('a2').get('length'))
            var.put('srcofs1', (var.get('Caml_primitive').callprop('caml_int_max', ((var.get('lena1')+var.get('ofs1'))|Js(0.0)), Js(0.0)) if (var.get('ofs1')<Js(0.0)) else var.get('ofs1')))
            var.put('srcofs2', (var.get('Caml_primitive').callprop('caml_int_max', ((var.get('lena2')+var.get('ofs2'))|Js(0.0)), Js(0.0)) if (var.get('ofs2')<Js(0.0)) else var.get('ofs2')))
            var.put('blitLength', var.get('Caml_primitive').callprop('caml_int_min', var.get('len'), var.get('Caml_primitive').callprop('caml_int_min', ((var.get('lena1')-var.get('srcofs1'))|Js(0.0)), ((var.get('lena2')-var.get('srcofs2'))|Js(0.0)))))
            if (var.get('srcofs2')<=var.get('srcofs1')):
                #for JS loop
                var.put('j', Js(0.0))
                var.put('j_finish', ((var.get('blitLength')-Js(1.0))|Js(0.0)))
                while (var.get('j')<=var.get('j_finish')):
                    try:
                        var.get('a2').put(((var.get('j')+var.get('srcofs2'))|Js(0.0)), var.get('a1').get(((var.get('j')+var.get('srcofs1'))|Js(0.0))))
                    finally:
                            var.put('j',Js(var.get('j').to_number())+Js(1))
                return Js(0.0)
            else:
                #for JS loop
                var.put('j$1', ((var.get('blitLength')-Js(1.0))|Js(0.0)))
                while (var.get('j$1')>=Js(0.0)):
                    try:
                        var.get('a2').put(((var.get('j$1')+var.get('srcofs2'))|Js(0.0)), var.get('a1').get(((var.get('j$1')+var.get('srcofs1'))|Js(0.0))))
                    finally:
                            var.put('j$1',Js(var.get('j$1').to_number())-Js(1))
                return Js(0.0)
        PyJsHoisted_blit_.func_name = 'blit'
        var.put('blit', PyJsHoisted_blit_)
        @Js
        def PyJsHoisted_forEachU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f', 'i', 'i_finish'])
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('f')(var.get('a').get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_forEachU_.func_name = 'forEachU'
        var.put('forEachU', PyJsHoisted_forEachU_)
        @Js
        def PyJsHoisted_forEach_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('forEachU')(var.get('a'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_forEach_.func_name = 'forEach'
        var.put('forEach', PyJsHoisted_forEach_)
        @Js
        def PyJsHoisted_mapU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'a', 'i_finish', 'r', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('r', var.get('Array').create(var.get('l')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('r').put(var.get('i'), var.get('f')(var.get('a').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('r')
        PyJsHoisted_mapU_.func_name = 'mapU'
        var.put('mapU', PyJsHoisted_mapU_)
        @Js
        def PyJsHoisted_map_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('mapU')(var.get('a'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_map_.func_name = 'map'
        var.put('map', PyJsHoisted_map_)
        @Js
        def PyJsHoisted_getByU_(a, p, this, arguments, var=var):
            var = Scope({'a':a, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'a', 'r', 'v', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('i', Js(0.0))
            var.put('r', var.get('undefined'))
            while (PyJsStrictEq(var.get('r'),var.get('undefined')) and (var.get('i')<var.get('l'))):
                var.put('v', var.get('a').get(var.get('i')))
                if var.get('p')(var.get('v')):
                    var.put('r', var.get('Caml_option').callprop('some', var.get('v')))
                var.put('i', ((var.get('i')+Js(1.0))|Js(0.0)))
            pass
            return var.get('r')
        PyJsHoisted_getByU_.func_name = 'getByU'
        var.put('getByU', PyJsHoisted_getByU_)
        @Js
        def PyJsHoisted_getBy_(a, p, this, arguments, var=var):
            var = Scope({'a':a, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'p'])
            return var.get('getByU')(var.get('a'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_getBy_.func_name = 'getBy'
        var.put('getBy', PyJsHoisted_getBy_)
        @Js
        def PyJsHoisted_getIndexByU_(a, p, this, arguments, var=var):
            var = Scope({'a':a, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'a', 'r', 'v', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('i', Js(0.0))
            var.put('r', var.get('undefined'))
            while (PyJsStrictEq(var.get('r'),var.get('undefined')) and (var.get('i')<var.get('l'))):
                var.put('v', var.get('a').get(var.get('i')))
                if var.get('p')(var.get('v')):
                    var.put('r', var.get('i'))
                var.put('i', ((var.get('i')+Js(1.0))|Js(0.0)))
            pass
            return var.get('r')
        PyJsHoisted_getIndexByU_.func_name = 'getIndexByU'
        var.put('getIndexByU', PyJsHoisted_getIndexByU_)
        @Js
        def PyJsHoisted_getIndexBy_(a, p, this, arguments, var=var):
            var = Scope({'a':a, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'p'])
            return var.get('getIndexByU')(var.get('a'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_getIndexBy_.func_name = 'getIndexBy'
        var.put('getIndexBy', PyJsHoisted_getIndexBy_)
        @Js
        def PyJsHoisted_keepU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'j', 'a', 'i_finish', 'r', 'v', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('r', var.get('Array').create(var.get('l')))
            var.put('j', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('v', var.get('a').get(var.get('i')))
                    if var.get('f')(var.get('v')):
                        var.get('r').put(var.get('j'), var.get('v'))
                        var.put('j', ((var.get('j')+Js(1.0))|Js(0.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('length', var.get('j'))
            return var.get('r')
        PyJsHoisted_keepU_.func_name = 'keepU'
        var.put('keepU', PyJsHoisted_keepU_)
        @Js
        def PyJsHoisted_keep_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('keepU')(var.get('a'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_keep_.func_name = 'keep'
        var.put('keep', PyJsHoisted_keep_)
        @Js
        def PyJsHoisted_keepWithIndexU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'j', 'a', 'i_finish', 'r', 'v', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('r', var.get('Array').create(var.get('l')))
            var.put('j', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('v', var.get('a').get(var.get('i')))
                    if var.get('f')(var.get('v'), var.get('i')):
                        var.get('r').put(var.get('j'), var.get('v'))
                        var.put('j', ((var.get('j')+Js(1.0))|Js(0.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('length', var.get('j'))
            return var.get('r')
        PyJsHoisted_keepWithIndexU_.func_name = 'keepWithIndexU'
        var.put('keepWithIndexU', PyJsHoisted_keepWithIndexU_)
        @Js
        def PyJsHoisted_keepWithIndex_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('keepWithIndexU')(var.get('a'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_keepWithIndex_.func_name = 'keepWithIndex'
        var.put('keepWithIndex', PyJsHoisted_keepWithIndex_)
        @Js
        def PyJsHoisted_keepMapU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'j', 'a', 'i_finish', 'r', 'v', 'match', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('r', var.get('Array').create(var.get('l')))
            var.put('j', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('v', var.get('a').get(var.get('i')))
                    var.put('match', var.get('f')(var.get('v')))
                    if PyJsStrictNeq(var.get('match'),var.get('undefined')):
                        var.get('r').put(var.get('j'), var.get('Caml_option').callprop('valFromOption', var.get('match')))
                        var.put('j', ((var.get('j')+Js(1.0))|Js(0.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('length', var.get('j'))
            return var.get('r')
        PyJsHoisted_keepMapU_.func_name = 'keepMapU'
        var.put('keepMapU', PyJsHoisted_keepMapU_)
        @Js
        def PyJsHoisted_keepMap_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('keepMapU')(var.get('a'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_keepMap_.func_name = 'keepMap'
        var.put('keepMap', PyJsHoisted_keepMap_)
        @Js
        def PyJsHoisted_forEachWithIndexU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f', 'i', 'i_finish'])
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('f')(var.get('i'), var.get('a').get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_forEachWithIndexU_.func_name = 'forEachWithIndexU'
        var.put('forEachWithIndexU', PyJsHoisted_forEachWithIndexU_)
        @Js
        def PyJsHoisted_forEachWithIndex_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('forEachWithIndexU')(var.get('a'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_forEachWithIndex_.func_name = 'forEachWithIndex'
        var.put('forEachWithIndex', PyJsHoisted_forEachWithIndex_)
        @Js
        def PyJsHoisted_mapWithIndexU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'a', 'i_finish', 'r', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('r', var.get('Array').create(var.get('l')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('r').put(var.get('i'), var.get('f')(var.get('i'), var.get('a').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('r')
        PyJsHoisted_mapWithIndexU_.func_name = 'mapWithIndexU'
        var.put('mapWithIndexU', PyJsHoisted_mapWithIndexU_)
        @Js
        def PyJsHoisted_mapWithIndex_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('mapWithIndexU')(var.get('a'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_mapWithIndex_.func_name = 'mapWithIndex'
        var.put('mapWithIndex', PyJsHoisted_mapWithIndex_)
        @Js
        def PyJsHoisted_reduceU_(a, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'a', 'r', 'i_finish', 'x', 'i'])
            var.put('r', var.get('x'))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('r', var.get('f')(var.get('r'), var.get('a').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('r')
        PyJsHoisted_reduceU_.func_name = 'reduceU'
        var.put('reduceU', PyJsHoisted_reduceU_)
        @Js
        def PyJsHoisted_reduce_(a, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f', 'x'])
            return var.get('reduceU')(var.get('a'), var.get('x'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_reduce_.func_name = 'reduce'
        var.put('reduce', PyJsHoisted_reduce_)
        @Js
        def PyJsHoisted_reduceReverseU_(a, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'a', 'r', 'x', 'i'])
            var.put('r', var.get('x'))
            #for JS loop
            var.put('i', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.put('r', var.get('f')(var.get('r'), var.get('a').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            return var.get('r')
        PyJsHoisted_reduceReverseU_.func_name = 'reduceReverseU'
        var.put('reduceReverseU', PyJsHoisted_reduceReverseU_)
        @Js
        def PyJsHoisted_reduceReverse_(a, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f', 'x'])
            return var.get('reduceReverseU')(var.get('a'), var.get('x'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_reduceReverse_.func_name = 'reduceReverse'
        var.put('reduceReverse', PyJsHoisted_reduceReverse_)
        @Js
        def PyJsHoisted_reduceReverse2U_(a, b, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'f', 'a', 'r', 'x', 'b', 'i'])
            var.put('r', var.get('x'))
            var.put('len', var.get('Caml_primitive').callprop('caml_int_min', var.get('a').get('length'), var.get('b').get('length')))
            #for JS loop
            var.put('i', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.put('r', var.get('f')(var.get('r'), var.get('a').get(var.get('i')), var.get('b').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            return var.get('r')
        PyJsHoisted_reduceReverse2U_.func_name = 'reduceReverse2U'
        var.put('reduceReverse2U', PyJsHoisted_reduceReverse2U_)
        @Js
        def PyJsHoisted_reduceReverse2_(a, b, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'f', 'x'])
            return var.get('reduceReverse2U')(var.get('a'), var.get('b'), var.get('x'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_reduceReverse2_.func_name = 'reduceReverse2'
        var.put('reduceReverse2', PyJsHoisted_reduceReverse2_)
        @Js
        def PyJsHoisted_reduceWithIndexU_(a, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'a', 'r', 'i_finish', 'x', 'i'])
            var.put('r', var.get('x'))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('r', var.get('f')(var.get('r'), var.get('a').get(var.get('i')), var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('r')
        PyJsHoisted_reduceWithIndexU_.func_name = 'reduceWithIndexU'
        var.put('reduceWithIndexU', PyJsHoisted_reduceWithIndexU_)
        @Js
        def PyJsHoisted_reduceWithIndex_(a, x, f, this, arguments, var=var):
            var = Scope({'a':a, 'x':x, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f', 'x'])
            return var.get('reduceWithIndexU')(var.get('a'), var.get('x'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_reduceWithIndex_.func_name = 'reduceWithIndex'
        var.put('reduceWithIndex', PyJsHoisted_reduceWithIndex_)
        @Js
        def PyJsHoisted_everyU_(arr, b, this, arguments, var=var):
            var = Scope({'arr':arr, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'b$1', 'len$1', '_i', 'arr$1', 'arr', 'b', 'i'])
            var.put('len', var.get('arr').get('length'))
            var.put('arr$1', var.get('arr'))
            var.put('_i', Js(0.0))
            var.put('b$1', var.get('b'))
            var.put('len$1', var.get('len'))
            while Js(True):
                var.put('i', var.get('_i'))
                if PyJsStrictEq(var.get('i'),var.get('len$1')):
                    return Js(True)
                else:
                    if var.get('b$1')(var.get('arr$1').get(var.get('i'))):
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        continue
                    else:
                        return Js(False)
            pass
        PyJsHoisted_everyU_.func_name = 'everyU'
        var.put('everyU', PyJsHoisted_everyU_)
        @Js
        def PyJsHoisted_every_(arr, f, this, arguments, var=var):
            var = Scope({'arr':arr, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr', 'f'])
            return var.get('everyU')(var.get('arr'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_every_.func_name = 'every'
        var.put('every', PyJsHoisted_every_)
        @Js
        def PyJsHoisted_someU_(arr, b, this, arguments, var=var):
            var = Scope({'arr':arr, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'b$1', 'len$1', '_i', 'arr$1', 'arr', 'b', 'i'])
            var.put('len', var.get('arr').get('length'))
            var.put('arr$1', var.get('arr'))
            var.put('_i', Js(0.0))
            var.put('b$1', var.get('b'))
            var.put('len$1', var.get('len'))
            while Js(True):
                var.put('i', var.get('_i'))
                if PyJsStrictEq(var.get('i'),var.get('len$1')):
                    return Js(False)
                else:
                    if var.get('b$1')(var.get('arr$1').get(var.get('i'))):
                        return Js(True)
                    else:
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        continue
            pass
        PyJsHoisted_someU_.func_name = 'someU'
        var.put('someU', PyJsHoisted_someU_)
        @Js
        def PyJsHoisted_some_(arr, f, this, arguments, var=var):
            var = Scope({'arr':arr, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr', 'f'])
            return var.get('someU')(var.get('arr'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_some_.func_name = 'some'
        var.put('some', PyJsHoisted_some_)
        @Js
        def PyJsHoisted_everyAux2_(arr1, arr2, _i, b, len, this, arguments, var=var):
            var = Scope({'arr1':arr1, 'arr2':arr2, '_i':_i, 'b':b, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'arr1', '_i', 'arr2', 'b', 'i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if PyJsStrictEq(var.get('i'),var.get('len')):
                    return Js(True)
                else:
                    if var.get('b')(var.get('arr1').get(var.get('i')), var.get('arr2').get(var.get('i'))):
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        continue
                    else:
                        return Js(False)
            pass
        PyJsHoisted_everyAux2_.func_name = 'everyAux2'
        var.put('everyAux2', PyJsHoisted_everyAux2_)
        @Js
        def PyJsHoisted_every2U_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'p'])
            return var.get('everyAux2')(var.get('a'), var.get('b'), Js(0.0), var.get('p'), var.get('Caml_primitive').callprop('caml_int_min', var.get('a').get('length'), var.get('b').get('length')))
        PyJsHoisted_every2U_.func_name = 'every2U'
        var.put('every2U', PyJsHoisted_every2U_)
        @Js
        def PyJsHoisted_every2_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'p'])
            return var.get('every2U')(var.get('a'), var.get('b'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_every2_.func_name = 'every2'
        var.put('every2', PyJsHoisted_every2_)
        @Js
        def PyJsHoisted_some2U_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'b$1', 'a', 'arr1', '_i', 'arr2', 'b', 'i', 'p'])
            var.put('arr1', var.get('a'))
            var.put('arr2', var.get('b'))
            var.put('_i', Js(0.0))
            var.put('b$1', var.get('p'))
            var.put('len', var.get('Caml_primitive').callprop('caml_int_min', var.get('a').get('length'), var.get('b').get('length')))
            while Js(True):
                var.put('i', var.get('_i'))
                if PyJsStrictEq(var.get('i'),var.get('len')):
                    return Js(False)
                else:
                    if var.get('b$1')(var.get('arr1').get(var.get('i')), var.get('arr2').get(var.get('i'))):
                        return Js(True)
                    else:
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        continue
            pass
        PyJsHoisted_some2U_.func_name = 'some2U'
        var.put('some2U', PyJsHoisted_some2U_)
        @Js
        def PyJsHoisted_some2_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'p'])
            return var.get('some2U')(var.get('a'), var.get('b'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_some2_.func_name = 'some2'
        var.put('some2', PyJsHoisted_some2_)
        @Js
        def PyJsHoisted_eqU_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'lena', 'lenb', 'b', 'p'])
            var.put('lena', var.get('a').get('length'))
            var.put('lenb', var.get('b').get('length'))
            if PyJsStrictEq(var.get('lena'),var.get('lenb')):
                return var.get('everyAux2')(var.get('a'), var.get('b'), Js(0.0), var.get('p'), var.get('lena'))
            else:
                return Js(False)
        PyJsHoisted_eqU_.func_name = 'eqU'
        var.put('eqU', PyJsHoisted_eqU_)
        @Js
        def PyJsHoisted_eq_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'p'])
            return var.get('eqU')(var.get('a'), var.get('b'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_cmpU_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'b$1', 'c', 'a', 'lena', 'lenb', 'arr1', '_i', 'arr2', 'b', 'i', 'p'])
            var.put('lena', var.get('a').get('length'))
            var.put('lenb', var.get('b').get('length'))
            if (var.get('lena')>var.get('lenb')):
                return Js(1.0)
            else:
                if (var.get('lena')<var.get('lenb')):
                    return (-Js(1.0))
                else:
                    var.put('arr1', var.get('a'))
                    var.put('arr2', var.get('b'))
                    var.put('_i', Js(0.0))
                    var.put('b$1', var.get('p'))
                    var.put('len', var.get('lena'))
                    while Js(True):
                        var.put('i', var.get('_i'))
                        if PyJsStrictEq(var.get('i'),var.get('len')):
                            return Js(0.0)
                        else:
                            var.put('c', var.get('b$1')(var.get('arr1').get(var.get('i')), var.get('arr2').get(var.get('i'))))
                            if PyJsStrictEq(var.get('c'),Js(0.0)):
                                var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                                continue
                            else:
                                return var.get('c')
                    pass
        PyJsHoisted_cmpU_.func_name = 'cmpU'
        var.put('cmpU', PyJsHoisted_cmpU_)
        @Js
        def PyJsHoisted_cmp_(a, b, p, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'p'])
            return var.get('cmpU')(var.get('a'), var.get('b'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_cmp_.func_name = 'cmp'
        var.put('cmp', PyJsHoisted_cmp_)
        @Js
        def PyJsHoisted_partitionU_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'ii_finish', 'a1', 'j', 'a', 'a2', 'v', 'ii', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('i', Js(0.0))
            var.put('j', Js(0.0))
            var.put('a1', var.get('Array').create(var.get('l')))
            var.put('a2', var.get('Array').create(var.get('l')))
            #for JS loop
            var.put('ii', Js(0.0))
            var.put('ii_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
            while (var.get('ii')<=var.get('ii_finish')):
                try:
                    var.put('v', var.get('a').get(var.get('ii')))
                    if var.get('f')(var.get('v')):
                        var.get('a1').put(var.get('i'), var.get('v'))
                        var.put('i', ((var.get('i')+Js(1.0))|Js(0.0)))
                    else:
                        var.get('a2').put(var.get('j'), var.get('v'))
                        var.put('j', ((var.get('j')+Js(1.0))|Js(0.0)))
                finally:
                        var.put('ii',Js(var.get('ii').to_number())+Js(1))
            var.get('a1').put('length', var.get('i'))
            var.get('a2').put('length', var.get('j'))
            return Js([var.get('a1'), var.get('a2')])
        PyJsHoisted_partitionU_.func_name = 'partitionU'
        var.put('partitionU', PyJsHoisted_partitionU_)
        @Js
        def PyJsHoisted_partition_(a, f, this, arguments, var=var):
            var = Scope({'a':a, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'f'])
            return var.get('partitionU')(var.get('a'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_partition_.func_name = 'partition'
        var.put('partition', PyJsHoisted_partition_)
        @Js
        def PyJsHoisted_unzip_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a1', 'a', 'a2', 'i_finish', 'match', 'i', 'l'])
            var.put('l', var.get('a').get('length'))
            var.put('a1', var.get('Array').create(var.get('l')))
            var.put('a2', var.get('Array').create(var.get('l')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('match', var.get('a').get(var.get('i')))
                    var.get('a1').put(var.get('i'), var.get('match').get('0'))
                    var.get('a2').put(var.get('i'), var.get('match').get('1'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js([var.get('a1'), var.get('a2')])
        PyJsHoisted_unzip_.func_name = 'unzip'
        var.put('unzip', PyJsHoisted_unzip_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Js_math', var.get('require')(Js('./js_math.js')))
        var.put('Caml_option', var.get('require')(Js('./caml_option.js')))
        var.put('Caml_primitive', var.get('require')(Js('./caml_primitive.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('set', var.get('set'))
        var.get('exports').put('setExn', var.get('setExn'))
        var.get('exports').put('shuffleInPlace', var.get('shuffleInPlace'))
        var.get('exports').put('shuffle', var.get('shuffle'))
        var.get('exports').put('reverseInPlace', var.get('reverseInPlace'))
        var.get('exports').put('reverse', var.get('reverse'))
        var.get('exports').put('make', var.get('make'))
        var.get('exports').put('range', var.get('range'))
        var.get('exports').put('rangeBy', var.get('rangeBy'))
        var.get('exports').put('makeByU', var.get('makeByU'))
        var.get('exports').put('makeBy', var.get('makeBy'))
        var.get('exports').put('makeByAndShuffleU', var.get('makeByAndShuffleU'))
        var.get('exports').put('makeByAndShuffle', var.get('makeByAndShuffle'))
        var.get('exports').put('zip', var.get('zip'))
        var.get('exports').put('zipByU', var.get('zipByU'))
        var.get('exports').put('zipBy', var.get('zipBy'))
        var.get('exports').put('unzip', var.get('unzip'))
        var.get('exports').put('concat', var.get('concat'))
        var.get('exports').put('concatMany', var.get('concatMany'))
        var.get('exports').put('slice', var.get('slice'))
        var.get('exports').put('sliceToEnd', var.get('sliceToEnd'))
        var.get('exports').put('fill', var.get('fill'))
        var.get('exports').put('blit', var.get('blit'))
        var.get('exports').put('blitUnsafe', var.get('blitUnsafe'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('mapU', var.get('mapU'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('getByU', var.get('getByU'))
        var.get('exports').put('getBy', var.get('getBy'))
        var.get('exports').put('getIndexByU', var.get('getIndexByU'))
        var.get('exports').put('getIndexBy', var.get('getIndexBy'))
        var.get('exports').put('keepU', var.get('keepU'))
        var.get('exports').put('keep', var.get('keep'))
        var.get('exports').put('keepWithIndexU', var.get('keepWithIndexU'))
        var.get('exports').put('keepWithIndex', var.get('keepWithIndex'))
        var.get('exports').put('keepMapU', var.get('keepMapU'))
        var.get('exports').put('keepMap', var.get('keepMap'))
        var.get('exports').put('forEachWithIndexU', var.get('forEachWithIndexU'))
        var.get('exports').put('forEachWithIndex', var.get('forEachWithIndex'))
        var.get('exports').put('mapWithIndexU', var.get('mapWithIndexU'))
        var.get('exports').put('mapWithIndex', var.get('mapWithIndex'))
        var.get('exports').put('partitionU', var.get('partitionU'))
        var.get('exports').put('partition', var.get('partition'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('reduceReverseU', var.get('reduceReverseU'))
        var.get('exports').put('reduceReverse', var.get('reduceReverse'))
        var.get('exports').put('reduceReverse2U', var.get('reduceReverse2U'))
        var.get('exports').put('reduceReverse2', var.get('reduceReverse2'))
        var.get('exports').put('reduceWithIndexU', var.get('reduceWithIndexU'))
        var.get('exports').put('reduceWithIndex', var.get('reduceWithIndex'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('every2U', var.get('every2U'))
        var.get('exports').put('every2', var.get('every2'))
        var.get('exports').put('some2U', var.get('some2U'))
        var.get('exports').put('some2', var.get('some2'))
        var.get('exports').put('cmpU', var.get('cmpU'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eqU', var.get('eqU'))
        var.get('exports').put('eq', var.get('eq'))
    PyJs_anonymous_0_._set_name('anonymous')
    @Js
    def PyJs_anonymous_1_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'MakeComparableU', 'MakeHashable', 'require', 'Curry', 'hashableU', 'module', 'MakeHashableU', 'MakeComparable', 'comparableU', 'comparable', 'hashable'])
        @Js
        def PyJsHoisted_MakeComparableU_(M, this, arguments, var=var):
            var = Scope({'M':M, 'this':this, 'arguments':arguments}, var)
            var.registers(['M'])
            return var.get('M')
        PyJsHoisted_MakeComparableU_.func_name = 'MakeComparableU'
        var.put('MakeComparableU', PyJsHoisted_MakeComparableU_)
        @Js
        def PyJsHoisted_MakeComparable_(M, this, arguments, var=var):
            var = Scope({'M':M, 'this':this, 'arguments':arguments}, var)
            var.registers(['M', 'cmp$1', 'cmp'])
            var.put('cmp', var.get('M').get('cmp'))
            var.put('cmp$1', var.get('Curry').callprop('__2', var.get('cmp')))
            return Js({'cmp':var.get('cmp$1')})
        PyJsHoisted_MakeComparable_.func_name = 'MakeComparable'
        var.put('MakeComparable', PyJsHoisted_MakeComparable_)
        @Js
        def PyJsHoisted_comparableU_(cmp, this, arguments, var=var):
            var = Scope({'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp'])
            return Js({'cmp':var.get('cmp')})
        PyJsHoisted_comparableU_.func_name = 'comparableU'
        var.put('comparableU', PyJsHoisted_comparableU_)
        @Js
        def PyJsHoisted_comparable_(cmp, this, arguments, var=var):
            var = Scope({'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp$1', 'cmp'])
            var.put('cmp$1', var.get('Curry').callprop('__2', var.get('cmp')))
            return Js({'cmp':var.get('cmp$1')})
        PyJsHoisted_comparable_.func_name = 'comparable'
        var.put('comparable', PyJsHoisted_comparable_)
        @Js
        def PyJsHoisted_MakeHashableU_(M, this, arguments, var=var):
            var = Scope({'M':M, 'this':this, 'arguments':arguments}, var)
            var.registers(['M'])
            return var.get('M')
        PyJsHoisted_MakeHashableU_.func_name = 'MakeHashableU'
        var.put('MakeHashableU', PyJsHoisted_MakeHashableU_)
        @Js
        def PyJsHoisted_MakeHashable_(M, this, arguments, var=var):
            var = Scope({'M':M, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'M', 'hash', 'eq$1', 'hash$1'])
            var.put('hash', var.get('M').get('hash'))
            var.put('hash$1', var.get('Curry').callprop('__1', var.get('hash')))
            var.put('eq', var.get('M').get('eq'))
            var.put('eq$1', var.get('Curry').callprop('__2', var.get('eq')))
            return Js({'hash':var.get('hash$1'),'eq':var.get('eq$1')})
        PyJsHoisted_MakeHashable_.func_name = 'MakeHashable'
        var.put('MakeHashable', PyJsHoisted_MakeHashable_)
        @Js
        def PyJsHoisted_hashableU_(hash, eq, this, arguments, var=var):
            var = Scope({'hash':hash, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'hash'])
            return Js({'hash':var.get('hash'),'eq':var.get('eq')})
        PyJsHoisted_hashableU_.func_name = 'hashableU'
        var.put('hashableU', PyJsHoisted_hashableU_)
        @Js
        def PyJsHoisted_hashable_(hash, eq, this, arguments, var=var):
            var = Scope({'hash':hash, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'hash', 'eq$1', 'hash$1'])
            var.put('hash$1', var.get('Curry').callprop('__1', var.get('hash')))
            var.put('eq$1', var.get('Curry').callprop('__2', var.get('eq')))
            return Js({'hash':var.get('hash$1'),'eq':var.get('eq$1')})
        PyJsHoisted_hashable_.func_name = 'hashable'
        var.put('hashable', PyJsHoisted_hashable_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('MakeComparableU', var.get('MakeComparableU'))
        var.get('exports').put('MakeComparable', var.get('MakeComparable'))
        var.get('exports').put('comparableU', var.get('comparableU'))
        var.get('exports').put('comparable', var.get('comparable'))
        var.get('exports').put('MakeHashableU', var.get('MakeHashableU'))
        var.get('exports').put('MakeHashable', var.get('MakeHashable'))
        var.get('exports').put('hashableU', var.get('hashableU'))
        var.get('exports').put('hashable', var.get('hashable'))
    PyJs_anonymous_1_._set_name('anonymous')
    @Js
    def PyJs_anonymous_2_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['setAssoc', 'hasAssocU', 'getAssoc', 'filter', 'mapReverse2U', 'reduceWithIndexU', 'forEachWithIndexU', 'mapReverse2', 'everyU', 'getAssocU', 'every2U', 'forEachWithIndex', 'eq', 'reduceReverseU', 'hasAssoc', 'shuffle', 'cmp', 'make', 'partitionAux', 'reduceU', 'mapWithIndex', 'mapReverse', 'forEach', 'keepMap', 'splitAtAux', 'reduce2U', 'hasU', 'get', 'makeBy', 'forEach2U', 'removeAssoc', 'some2', 'flatten', 'reverse', 'setAssocU', 'filterWithIndex', 'require', 'getExn', 'splitAt', 'flattenAux', 'drop', 'reduceReverseUnsafeU', 'keepWithIndexU', 'removeAssocAuxWithMap', 'someU', 'headExn', 'keepU', 'reduceWithIndex', 'take', 'reduce', 'concatMany', 'reduceReverse2UnsafeU', 'Belt_SortArray', 'takeAux', 'mapU', 'copyAuxWitFilter', 'sort', 'Caml_option', 'getBy', 'toArray', 'zip', 'every', 'reduceReverse2U', 'module', 'sortU', 'length', 'size', 'reduce2', 'cmpU', 'keepMapU', 'reverseConcat', 'Belt_Array', 'forEach2', 'keep', 'mapWithIndexU', 'partition', 'zipBy', 'every2', 'splitAux', 'makeByU', 'fillAux', 'mapReverseU', 'concat', 'reduceReverse2', 'eqU', 'copyAuxCont', 'partitionU', 'unzip', 'forEachU', 'head', 'exports', 'keepWithIndex', 'map', 'some2U', 'some', 'fromArray', 'cmpByLength', 'zipAux', 'tailExn', 'zipByU', 'reduceReverse', 'add', 'tail', 'setAssocAuxWithMap', 'copyAuxWithMapI', 'Curry', 'removeAssocU', 'copyAuxWithMap2', 'has', 'copyAuxWithFilterIndex', 'getByU', 'copyAuxWitFilterMap', 'copyAuxWithMap'])
        @Js
        def PyJsHoisted_head_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if var.get('x'):
                return var.get('Caml_option').callprop('some', var.get('x').get('0'))
        PyJsHoisted_head_.func_name = 'head'
        var.put('head', PyJsHoisted_head_)
        @Js
        def PyJsHoisted_headExn_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if var.get('x'):
                return var.get('x').get('0')
            else:
                PyJsTempException = JsToPyException(var.get('Error').create(Js('headExn')))
                raise PyJsTempException
        PyJsHoisted_headExn_.func_name = 'headExn'
        var.put('headExn', PyJsHoisted_headExn_)
        @Js
        def PyJsHoisted_tail_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if var.get('x'):
                return var.get('x').get('1')
        PyJsHoisted_tail_.func_name = 'tail'
        var.put('tail', PyJsHoisted_tail_)
        @Js
        def PyJsHoisted_tailExn_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if var.get('x'):
                return var.get('x').get('1')
            else:
                PyJsTempException = JsToPyException(var.get('Error').create(Js('tailExn')))
                raise PyJsTempException
        PyJsHoisted_tailExn_.func_name = 'tailExn'
        var.put('tailExn', PyJsHoisted_tailExn_)
        @Js
        def PyJsHoisted_add_(xs, x, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'x'])
            return Js([var.get('x'), var.get('xs')])
        PyJsHoisted_add_.func_name = 'add'
        var.put('add', PyJsHoisted_add_)
        @Js
        def PyJsHoisted_get_(x, n, this, arguments, var=var):
            var = Scope({'x':x, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['_x', 'n$1', 'x', 'n', '_n', 'x$1'])
            if (var.get('n')<Js(0.0)):
                return var.get('undefined')
            else:
                var.put('_x', var.get('x'))
                var.put('_n', var.get('n'))
                while Js(True):
                    var.put('n$1', var.get('_n'))
                    var.put('x$1', var.get('_x'))
                    if var.get('x$1'):
                        if PyJsStrictEq(var.get('n$1'),Js(0.0)):
                            return var.get('Caml_option').callprop('some', var.get('x$1').get('0'))
                        else:
                            var.put('_n', ((var.get('n$1')-Js(1.0))|Js(0.0)))
                            var.put('_x', var.get('x$1').get('1'))
                            continue
                    else:
                        return var.get('undefined')
                pass
        PyJsHoisted_get_.func_name = 'get'
        var.put('get', PyJsHoisted_get_)
        @Js
        def PyJsHoisted_getExn_(x, n, this, arguments, var=var):
            var = Scope({'x':x, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['_x', 'n$1', 'x', 'n', '_n', 'x$1'])
            if (var.get('n')<Js(0.0)):
                PyJsTempException = JsToPyException(var.get('Error').create(Js('getExn')))
                raise PyJsTempException
            var.put('_x', var.get('x'))
            var.put('_n', var.get('n'))
            while Js(True):
                var.put('n$1', var.get('_n'))
                var.put('x$1', var.get('_x'))
                if var.get('x$1'):
                    if PyJsStrictEq(var.get('n$1'),Js(0.0)):
                        return var.get('x$1').get('0')
                    else:
                        var.put('_n', ((var.get('n$1')-Js(1.0))|Js(0.0)))
                        var.put('_x', var.get('x$1').get('1'))
                        continue
                else:
                    PyJsTempException = JsToPyException(var.get('Error').create(Js('getExn')))
                    raise PyJsTempException
            pass
        PyJsHoisted_getExn_.func_name = 'getExn'
        var.put('getExn', PyJsHoisted_getExn_)
        @Js
        def PyJsHoisted_partitionAux_(p, _cell, _precX, _precY, this, arguments, var=var):
            var = Scope({'p':p, '_cell':_cell, '_precX':_precX, '_precY':_precY, 'this':this, 'arguments':arguments}, var)
            var.registers(['_precY', 't', '_precX', 'cell', 'precY', 'next', '_cell', 'h', 'precX', 'p'])
            while Js(True):
                var.put('precY', var.get('_precY'))
                var.put('precX', var.get('_precX'))
                var.put('cell', var.get('_cell'))
                if var.get('cell'):
                    var.put('t', var.get('cell').get('1'))
                    var.put('h', var.get('cell').get('0'))
                    var.put('next', Js([var.get('h'), Js(0.0)]))
                    if var.get('p')(var.get('h')):
                        var.get('precX').put('1', var.get('next'))
                        var.put('_precX', var.get('next'))
                        var.put('_cell', var.get('t'))
                        continue
                    else:
                        var.get('precY').put('1', var.get('next'))
                        var.put('_precY', var.get('next'))
                        var.put('_cell', var.get('t'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_partitionAux_.func_name = 'partitionAux'
        var.put('partitionAux', PyJsHoisted_partitionAux_)
        @Js
        def PyJsHoisted_splitAux_(_cell, _precX, _precY, this, arguments, var=var):
            var = Scope({'_cell':_cell, '_precX':_precX, '_precY':_precY, 'this':this, 'arguments':arguments}, var)
            var.registers(['_precY', 'precX', '_precX', 'cell', 'precY', 'match', 'nextB', 'nextA', '_cell'])
            while Js(True):
                var.put('precY', var.get('_precY'))
                var.put('precX', var.get('_precX'))
                var.put('cell', var.get('_cell'))
                if var.get('cell'):
                    var.put('match', var.get('cell').get('0'))
                    var.put('nextA', Js([var.get('match').get('0'), Js(0.0)]))
                    var.put('nextB', Js([var.get('match').get('1'), Js(0.0)]))
                    var.get('precX').put('1', var.get('nextA'))
                    var.get('precY').put('1', var.get('nextB'))
                    var.put('_precY', var.get('nextB'))
                    var.put('_precX', var.get('nextA'))
                    var.put('_cell', var.get('cell').get('1'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_splitAux_.func_name = 'splitAux'
        var.put('splitAux', PyJsHoisted_splitAux_)
        @Js
        def PyJsHoisted_copyAuxCont_(_cellX, _prec, this, arguments, var=var):
            var = Scope({'_cellX':_cellX, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['_cellX', 'next', '_prec', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                if var.get('cellX'):
                    var.put('next', Js([var.get('cellX').get('0'), Js(0.0)]))
                    var.get('prec').put('1', var.get('next'))
                    var.put('_prec', var.get('next'))
                    var.put('_cellX', var.get('cellX').get('1'))
                    continue
                else:
                    return var.get('prec')
            pass
        PyJsHoisted_copyAuxCont_.func_name = 'copyAuxCont'
        var.put('copyAuxCont', PyJsHoisted_copyAuxCont_)
        @Js
        def PyJsHoisted_copyAuxWitFilter_(f, _cellX, _prec, this, arguments, var=var):
            var = Scope({'f':f, '_cellX':_cellX, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 't', '_cellX', 'next', '_prec', 'h', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                if var.get('cellX'):
                    var.put('t', var.get('cellX').get('1'))
                    var.put('h', var.get('cellX').get('0'))
                    if var.get('f')(var.get('h')):
                        var.put('next', Js([var.get('h'), Js(0.0)]))
                        var.get('prec').put('1', var.get('next'))
                        var.put('_prec', var.get('next'))
                        var.put('_cellX', var.get('t'))
                        continue
                    else:
                        var.put('_cellX', var.get('t'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_copyAuxWitFilter_.func_name = 'copyAuxWitFilter'
        var.put('copyAuxWitFilter', PyJsHoisted_copyAuxWitFilter_)
        @Js
        def PyJsHoisted_copyAuxWithFilterIndex_(f, _cellX, _prec, _i, this, arguments, var=var):
            var = Scope({'f':f, '_cellX':_cellX, '_prec':_prec, '_i':_i, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 't', '_cellX', 'next', '_prec', '_i', 'h', 'prec', 'i', 'cellX'])
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                if var.get('cellX'):
                    var.put('t', var.get('cellX').get('1'))
                    var.put('h', var.get('cellX').get('0'))
                    if var.get('f')(var.get('h'), var.get('i')):
                        var.put('next', Js([var.get('h'), Js(0.0)]))
                        var.get('prec').put('1', var.get('next'))
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        var.put('_prec', var.get('next'))
                        var.put('_cellX', var.get('t'))
                        continue
                    else:
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        var.put('_cellX', var.get('t'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_copyAuxWithFilterIndex_.func_name = 'copyAuxWithFilterIndex'
        var.put('copyAuxWithFilterIndex', PyJsHoisted_copyAuxWithFilterIndex_)
        @Js
        def PyJsHoisted_copyAuxWitFilterMap_(f, _cellX, _prec, this, arguments, var=var):
            var = Scope({'f':f, '_cellX':_cellX, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 't', '_cellX', 'next', '_prec', 'match', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                if var.get('cellX'):
                    var.put('t', var.get('cellX').get('1'))
                    var.put('match', var.get('f')(var.get('cellX').get('0')))
                    if PyJsStrictNeq(var.get('match'),var.get('undefined')):
                        var.put('next', Js([var.get('Caml_option').callprop('valFromOption', var.get('match')), Js(0.0)]))
                        var.get('prec').put('1', var.get('next'))
                        var.put('_prec', var.get('next'))
                        var.put('_cellX', var.get('t'))
                        continue
                    else:
                        var.put('_cellX', var.get('t'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_copyAuxWitFilterMap_.func_name = 'copyAuxWitFilterMap'
        var.put('copyAuxWitFilterMap', PyJsHoisted_copyAuxWitFilterMap_)
        @Js
        def PyJsHoisted_removeAssocAuxWithMap_(_cellX, x, _prec, f, this, arguments, var=var):
            var = Scope({'_cellX':_cellX, 'x':x, '_prec':_prec, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 't', '_cellX', 'next', '_prec', 'x', 'h', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                if var.get('cellX'):
                    var.put('t', var.get('cellX').get('1'))
                    var.put('h', var.get('cellX').get('0'))
                    if var.get('f')(var.get('h').get('0'), var.get('x')):
                        var.get('prec').put('1', var.get('t'))
                        return Js(True)
                    else:
                        var.put('next', Js([var.get('h'), Js(0.0)]))
                        var.get('prec').put('1', var.get('next'))
                        var.put('_prec', var.get('next'))
                        var.put('_cellX', var.get('t'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_removeAssocAuxWithMap_.func_name = 'removeAssocAuxWithMap'
        var.put('removeAssocAuxWithMap', PyJsHoisted_removeAssocAuxWithMap_)
        @Js
        def PyJsHoisted_setAssocAuxWithMap_(_cellX, x, k, _prec, eq, this, arguments, var=var):
            var = Scope({'_cellX':_cellX, 'x':x, 'k':k, '_prec':_prec, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 't', '_cellX', 'next', '_prec', 'x', 'h', 'k', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                if var.get('cellX'):
                    var.put('t', var.get('cellX').get('1'))
                    var.put('h', var.get('cellX').get('0'))
                    if var.get('eq')(var.get('h').get('0'), var.get('x')):
                        var.get('prec').put('1', Js([Js([var.get('x'), var.get('k')]), var.get('t')]))
                        return Js(True)
                    else:
                        var.put('next', Js([var.get('h'), Js(0.0)]))
                        var.get('prec').put('1', var.get('next'))
                        var.put('_prec', var.get('next'))
                        var.put('_cellX', var.get('t'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_setAssocAuxWithMap_.func_name = 'setAssocAuxWithMap'
        var.put('setAssocAuxWithMap', PyJsHoisted_setAssocAuxWithMap_)
        @Js
        def PyJsHoisted_copyAuxWithMap_(_cellX, _prec, f, this, arguments, var=var):
            var = Scope({'_cellX':_cellX, '_prec':_prec, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', '_cellX', 'next', '_prec', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                if var.get('cellX'):
                    var.put('next', Js([var.get('f')(var.get('cellX').get('0')), Js(0.0)]))
                    var.get('prec').put('1', var.get('next'))
                    var.put('_prec', var.get('next'))
                    var.put('_cellX', var.get('cellX').get('1'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_copyAuxWithMap_.func_name = 'copyAuxWithMap'
        var.put('copyAuxWithMap', PyJsHoisted_copyAuxWithMap_)
        @Js
        def PyJsHoisted_zipAux_(_cellX, _cellY, _prec, this, arguments, var=var):
            var = Scope({'_cellX':_cellX, '_cellY':_cellY, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['_cellX', '_cellY', 'next', 'cellY', '_prec', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellY', var.get('_cellY'))
                var.put('cellX', var.get('_cellX'))
                if (var.get('cellX') and var.get('cellY')):
                    var.put('next', Js([Js([var.get('cellX').get('0'), var.get('cellY').get('0')]), Js(0.0)]))
                    var.get('prec').put('1', var.get('next'))
                    var.put('_prec', var.get('next'))
                    var.put('_cellY', var.get('cellY').get('1'))
                    var.put('_cellX', var.get('cellX').get('1'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_zipAux_.func_name = 'zipAux'
        var.put('zipAux', PyJsHoisted_zipAux_)
        @Js
        def PyJsHoisted_copyAuxWithMap2_(f, _cellX, _cellY, _prec, this, arguments, var=var):
            var = Scope({'f':f, '_cellX':_cellX, '_cellY':_cellY, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', '_cellX', '_cellY', 'next', 'cellY', '_prec', 'prec', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellY', var.get('_cellY'))
                var.put('cellX', var.get('_cellX'))
                if (var.get('cellX') and var.get('cellY')):
                    var.put('next', Js([var.get('f')(var.get('cellX').get('0'), var.get('cellY').get('0')), Js(0.0)]))
                    var.get('prec').put('1', var.get('next'))
                    var.put('_prec', var.get('next'))
                    var.put('_cellY', var.get('cellY').get('1'))
                    var.put('_cellX', var.get('cellX').get('1'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_copyAuxWithMap2_.func_name = 'copyAuxWithMap2'
        var.put('copyAuxWithMap2', PyJsHoisted_copyAuxWithMap2_)
        @Js
        def PyJsHoisted_copyAuxWithMapI_(f, _i, _cellX, _prec, this, arguments, var=var):
            var = Scope({'f':f, '_i':_i, '_cellX':_cellX, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', '_cellX', 'next', '_prec', '_i', 'prec', 'i', 'cellX'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cellX', var.get('_cellX'))
                var.put('i', var.get('_i'))
                if var.get('cellX'):
                    var.put('next', Js([var.get('f')(var.get('i'), var.get('cellX').get('0')), Js(0.0)]))
                    var.get('prec').put('1', var.get('next'))
                    var.put('_prec', var.get('next'))
                    var.put('_cellX', var.get('cellX').get('1'))
                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_copyAuxWithMapI_.func_name = 'copyAuxWithMapI'
        var.put('copyAuxWithMapI', PyJsHoisted_copyAuxWithMapI_)
        @Js
        def PyJsHoisted_takeAux_(_n, _cell, _prec, this, arguments, var=var):
            var = Scope({'_n':_n, '_cell':_cell, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['cell', '_prec', 'n', '_n', 'prec', 'cell$1', '_cell'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cell', var.get('_cell'))
                var.put('n', var.get('_n'))
                if PyJsStrictEq(var.get('n'),Js(0.0)):
                    return Js(True)
                else:
                    if var.get('cell'):
                        var.put('cell$1', Js([var.get('cell').get('0'), Js(0.0)]))
                        var.get('prec').put('1', var.get('cell$1'))
                        var.put('_prec', var.get('cell$1'))
                        var.put('_cell', var.get('cell').get('1'))
                        var.put('_n', ((var.get('n')-Js(1.0))|Js(0.0)))
                        continue
                    else:
                        return Js(False)
            pass
        PyJsHoisted_takeAux_.func_name = 'takeAux'
        var.put('takeAux', PyJsHoisted_takeAux_)
        @Js
        def PyJsHoisted_splitAtAux_(_n, _cell, _prec, this, arguments, var=var):
            var = Scope({'_n':_n, '_cell':_cell, '_prec':_prec, 'this':this, 'arguments':arguments}, var)
            var.registers(['cell', '_prec', 'n', '_n', 'prec', 'cell$1', '_cell'])
            while Js(True):
                var.put('prec', var.get('_prec'))
                var.put('cell', var.get('_cell'))
                var.put('n', var.get('_n'))
                if PyJsStrictEq(var.get('n'),Js(0.0)):
                    return var.get('cell')
                else:
                    if var.get('cell'):
                        var.put('cell$1', Js([var.get('cell').get('0'), Js(0.0)]))
                        var.get('prec').put('1', var.get('cell$1'))
                        var.put('_prec', var.get('cell$1'))
                        var.put('_cell', var.get('cell').get('1'))
                        var.put('_n', ((var.get('n')-Js(1.0))|Js(0.0)))
                        continue
                    else:
                        return var.get('undefined')
            pass
        PyJsHoisted_splitAtAux_.func_name = 'splitAtAux'
        var.put('splitAtAux', PyJsHoisted_splitAtAux_)
        @Js
        def PyJsHoisted_take_(lst, n, this, arguments, var=var):
            var = Scope({'lst':lst, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['has', 'n', 'cell', 'lst'])
            if (var.get('n')<Js(0.0)):
                return var.get('undefined')
            else:
                if PyJsStrictEq(var.get('n'),Js(0.0)):
                    return Js(0.0)
                else:
                    if var.get('lst'):
                        var.put('cell', Js([var.get('lst').get('0'), Js(0.0)]))
                        var.put('has', var.get('takeAux')(((var.get('n')-Js(1.0))|Js(0.0)), var.get('lst').get('1'), var.get('cell')))
                        if var.get('has'):
                            return var.get('cell')
                        else:
                            return var.get('undefined')
                    else:
                        return var.get('undefined')
        PyJsHoisted_take_.func_name = 'take'
        var.put('take', PyJsHoisted_take_)
        @Js
        def PyJsHoisted_drop_(lst, n, this, arguments, var=var):
            var = Scope({'lst':lst, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['lst', 'n$1', 'n', '_n', '_l', 'l'])
            if (var.get('n')<Js(0.0)):
                return var.get('undefined')
            else:
                var.put('_l', var.get('lst'))
                var.put('_n', var.get('n'))
                while Js(True):
                    var.put('n$1', var.get('_n'))
                    var.put('l', var.get('_l'))
                    if PyJsStrictEq(var.get('n$1'),Js(0.0)):
                        return var.get('l')
                    else:
                        if var.get('l'):
                            var.put('_n', ((var.get('n$1')-Js(1.0))|Js(0.0)))
                            var.put('_l', var.get('l').get('1'))
                            continue
                        else:
                            return var.get('undefined')
                pass
        PyJsHoisted_drop_.func_name = 'drop'
        var.put('drop', PyJsHoisted_drop_)
        @Js
        def PyJsHoisted_splitAt_(lst, n, this, arguments, var=var):
            var = Scope({'lst':lst, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['lst', 'n', 'cell', 'rest'])
            if (var.get('n')<Js(0.0)):
                return var.get('undefined')
            else:
                if PyJsStrictEq(var.get('n'),Js(0.0)):
                    return Js([Js(0.0), var.get('lst')])
                else:
                    if var.get('lst'):
                        var.put('cell', Js([var.get('lst').get('0'), Js(0.0)]))
                        var.put('rest', var.get('splitAtAux')(((var.get('n')-Js(1.0))|Js(0.0)), var.get('lst').get('1'), var.get('cell')))
                        if PyJsStrictNeq(var.get('rest'),var.get('undefined')):
                            return Js([var.get('cell'), var.get('rest')])
                        else:
                            return var.get('undefined')
                    else:
                        return var.get('undefined')
        PyJsHoisted_splitAt_.func_name = 'splitAt'
        var.put('splitAt', PyJsHoisted_splitAt_)
        @Js
        def PyJsHoisted_concat_(xs, ys, this, arguments, var=var):
            var = Scope({'xs':xs, 'ys':ys, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'cell', 'ys'])
            if var.get('xs'):
                var.put('cell', Js([var.get('xs').get('0'), Js(0.0)]))
                var.get('copyAuxCont')(var.get('xs').get('1'), var.get('cell')).put('1', var.get('ys'))
                return var.get('cell')
            else:
                return var.get('ys')
        PyJsHoisted_concat_.func_name = 'concat'
        var.put('concat', PyJsHoisted_concat_)
        @Js
        def PyJsHoisted_mapU_(xs, f, this, arguments, var=var):
            var = Scope({'xs':xs, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'f', 'cell'])
            if var.get('xs'):
                var.put('cell', Js([var.get('f')(var.get('xs').get('0')), Js(0.0)]))
                var.get('copyAuxWithMap')(var.get('xs').get('1'), var.get('cell'), var.get('f'))
                return var.get('cell')
            else:
                return Js(0.0)
        PyJsHoisted_mapU_.func_name = 'mapU'
        var.put('mapU', PyJsHoisted_mapU_)
        @Js
        def PyJsHoisted_map_(xs, f, this, arguments, var=var):
            var = Scope({'xs':xs, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'f'])
            return var.get('mapU')(var.get('xs'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_map_.func_name = 'map'
        var.put('map', PyJsHoisted_map_)
        @Js
        def PyJsHoisted_zipByU_(l1, l2, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l2', 'cell', 'l1'])
            if (var.get('l1') and var.get('l2')):
                var.put('cell', Js([var.get('f')(var.get('l1').get('0'), var.get('l2').get('0')), Js(0.0)]))
                var.get('copyAuxWithMap2')(var.get('f'), var.get('l1').get('1'), var.get('l2').get('1'), var.get('cell'))
                return var.get('cell')
            else:
                return Js(0.0)
        PyJsHoisted_zipByU_.func_name = 'zipByU'
        var.put('zipByU', PyJsHoisted_zipByU_)
        @Js
        def PyJsHoisted_zipBy_(l1, l2, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l2', 'l1'])
            return var.get('zipByU')(var.get('l1'), var.get('l2'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_zipBy_.func_name = 'zipBy'
        var.put('zipBy', PyJsHoisted_zipBy_)
        @Js
        def PyJsHoisted_mapWithIndexU_(xs, f, this, arguments, var=var):
            var = Scope({'xs':xs, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'f', 'cell'])
            if var.get('xs'):
                var.put('cell', Js([var.get('f')(Js(0.0), var.get('xs').get('0')), Js(0.0)]))
                var.get('copyAuxWithMapI')(var.get('f'), Js(1.0), var.get('xs').get('1'), var.get('cell'))
                return var.get('cell')
            else:
                return Js(0.0)
        PyJsHoisted_mapWithIndexU_.func_name = 'mapWithIndexU'
        var.put('mapWithIndexU', PyJsHoisted_mapWithIndexU_)
        @Js
        def PyJsHoisted_mapWithIndex_(xs, f, this, arguments, var=var):
            var = Scope({'xs':xs, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'f'])
            return var.get('mapWithIndexU')(var.get('xs'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_mapWithIndex_.func_name = 'mapWithIndex'
        var.put('mapWithIndex', PyJsHoisted_mapWithIndex_)
        @Js
        def PyJsHoisted_makeByU_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'headX', 'v', 'cur', 'n', 'i'])
            if (var.get('n')<=Js(0.0)):
                return Js(0.0)
            else:
                var.put('headX', Js([var.get('f')(Js(0.0)), Js(0.0)]))
                var.put('cur', var.get('headX'))
                var.put('i', Js(1.0))
                while (var.get('i')<var.get('n')):
                    var.put('v', Js([var.get('f')(var.get('i')), Js(0.0)]))
                    var.get('cur').put('1', var.get('v'))
                    var.put('cur', var.get('v'))
                    var.put('i', ((var.get('i')+Js(1.0))|Js(0.0)))
                pass
                return var.get('headX')
        PyJsHoisted_makeByU_.func_name = 'makeByU'
        var.put('makeByU', PyJsHoisted_makeByU_)
        @Js
        def PyJsHoisted_makeBy_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n'])
            return var.get('makeByU')(var.get('n'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_makeBy_.func_name = 'makeBy'
        var.put('makeBy', PyJsHoisted_makeBy_)
        @Js
        def PyJsHoisted_make_(n, v, this, arguments, var=var):
            var = Scope({'n':n, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['headX', 'v$1', 'v', 'cur', 'n', 'i'])
            if (var.get('n')<=Js(0.0)):
                return Js(0.0)
            else:
                var.put('headX', Js([var.get('v'), Js(0.0)]))
                var.put('cur', var.get('headX'))
                var.put('i', Js(1.0))
                while (var.get('i')<var.get('n')):
                    var.put('v$1', Js([var.get('v'), Js(0.0)]))
                    var.get('cur').put('1', var.get('v$1'))
                    var.put('cur', var.get('v$1'))
                    var.put('i', ((var.get('i')+Js(1.0))|Js(0.0)))
                pass
                return var.get('headX')
        PyJsHoisted_make_.func_name = 'make'
        var.put('make', PyJsHoisted_make_)
        @Js
        def PyJsHoisted_length_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'acc', '_x', 'x', '_acc'])
            var.put('_x', var.get('xs'))
            var.put('_acc', Js(0.0))
            while Js(True):
                var.put('acc', var.get('_acc'))
                var.put('x', var.get('_x'))
                if var.get('x'):
                    var.put('_acc', ((var.get('acc')+Js(1.0))|Js(0.0)))
                    var.put('_x', var.get('x').get('1'))
                    continue
                else:
                    return var.get('acc')
            pass
        PyJsHoisted_length_.func_name = 'length'
        var.put('length', PyJsHoisted_length_)
        @Js
        def PyJsHoisted_fillAux_(arr, _i, _x, this, arguments, var=var):
            var = Scope({'arr':arr, '_i':_i, '_x':_x, 'this':this, 'arguments':arguments}, var)
            var.registers(['_x', 'x', '_i', 'arr', 'i'])
            while Js(True):
                var.put('x', var.get('_x'))
                var.put('i', var.get('_i'))
                if var.get('x'):
                    var.get('arr').put(var.get('i'), var.get('x').get('0'))
                    var.put('_x', var.get('x').get('1'))
                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_fillAux_.func_name = 'fillAux'
        var.put('fillAux', PyJsHoisted_fillAux_)
        @Js
        def PyJsHoisted_fromArray_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'res', '_res', 'a$1', '_i', 'i'])
            var.put('a$1', var.get('a'))
            var.put('_i', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            var.put('_res', Js(0.0))
            while Js(True):
                var.put('res', var.get('_res'))
                var.put('i', var.get('_i'))
                if (var.get('i')<Js(0.0)):
                    return var.get('res')
                else:
                    var.put('_res', Js([var.get('a$1').get(var.get('i')), var.get('res')]))
                    var.put('_i', ((var.get('i')-Js(1.0))|Js(0.0)))
                    continue
            pass
        PyJsHoisted_fromArray_.func_name = 'fromArray'
        var.put('fromArray', PyJsHoisted_fromArray_)
        @Js
        def PyJsHoisted_toArray_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'arr', 'x'])
            var.put('len', var.get('length')(var.get('x')))
            var.put('arr', var.get('Array').create(var.get('len')))
            var.get('fillAux')(var.get('arr'), Js(0.0), var.get('x'))
            return var.get('arr')
        PyJsHoisted_toArray_.func_name = 'toArray'
        var.put('toArray', PyJsHoisted_toArray_)
        @Js
        def PyJsHoisted_shuffle_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'v'])
            var.put('v', var.get('toArray')(var.get('xs')))
            var.get('Belt_Array').callprop('shuffleInPlace', var.get('v'))
            return var.get('fromArray')(var.get('v'))
        PyJsHoisted_shuffle_.func_name = 'shuffle'
        var.put('shuffle', PyJsHoisted_shuffle_)
        @Js
        def PyJsHoisted_reverseConcat_(_l1, _l2, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, 'this':this, 'arguments':arguments}, var)
            var.registers(['_l2', '_l1', 'l2', 'l1'])
            while Js(True):
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if var.get('l1'):
                    var.put('_l2', Js([var.get('l1').get('0'), var.get('l2')]))
                    var.put('_l1', var.get('l1').get('1'))
                    continue
                else:
                    return var.get('l2')
            pass
        PyJsHoisted_reverseConcat_.func_name = 'reverseConcat'
        var.put('reverseConcat', PyJsHoisted_reverseConcat_)
        @Js
        def PyJsHoisted_reverse_(l, this, arguments, var=var):
            var = Scope({'l':l, 'this':this, 'arguments':arguments}, var)
            var.registers(['l'])
            return var.get('reverseConcat')(var.get('l'), Js(0.0))
        PyJsHoisted_reverse_.func_name = 'reverse'
        var.put('reverse', PyJsHoisted_reverse_)
        @Js
        def PyJsHoisted_flattenAux_(_prec, _xs, this, arguments, var=var):
            var = Scope({'_prec':_prec, '_xs':_xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', '_prec', 'prec'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                var.put('prec', var.get('_prec'))
                if var.get('xs'):
                    var.put('_xs', var.get('xs').get('1'))
                    var.put('_prec', var.get('copyAuxCont')(var.get('xs').get('0'), var.get('prec')))
                    continue
                else:
                    var.get('prec').put('1', Js(0.0))
                    return Js(0.0)
            pass
        PyJsHoisted_flattenAux_.func_name = 'flattenAux'
        var.put('flattenAux', PyJsHoisted_flattenAux_)
        @Js
        def PyJsHoisted_flatten_(_xs, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', 'match', 'cell'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    var.put('match', var.get('xs').get('0'))
                    if var.get('match'):
                        var.put('cell', Js([var.get('match').get('0'), Js(0.0)]))
                        var.get('flattenAux')(var.get('copyAuxCont')(var.get('match').get('1'), var.get('cell')), var.get('xs').get('1'))
                        return var.get('cell')
                    else:
                        var.put('_xs', var.get('xs').get('1'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_flatten_.func_name = 'flatten'
        var.put('flatten', PyJsHoisted_flatten_)
        @Js
        def PyJsHoisted_concatMany_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'v', 'len$1', 'i'])
            var.put('len', var.get('xs').get('length'))
            if PyJsStrictNeq(var.get('len'),Js(1.0)):
                if PyJsStrictNeq(var.get('len'),Js(0.0)):
                    var.put('len$1', var.get('xs').get('length'))
                    var.put('v', var.get('xs').get(((var.get('len$1')-Js(1.0))|Js(0.0))))
                    #for JS loop
                    var.put('i', ((var.get('len$1')-Js(2.0))|Js(0.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            var.put('v', var.get('concat')(var.get('xs').get(var.get('i')), var.get('v')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
                    return var.get('v')
                else:
                    return Js(0.0)
            else:
                return var.get('xs').get('0')
        PyJsHoisted_concatMany_.func_name = 'concatMany'
        var.put('concatMany', PyJsHoisted_concatMany_)
        @Js
        def PyJsHoisted_mapReverseU_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'accu', 'f', '_accu', 'f$1', '_xs', 'l'])
            var.put('f$1', var.get('f'))
            var.put('_accu', Js(0.0))
            var.put('_xs', var.get('l'))
            while Js(True):
                var.put('xs', var.get('_xs'))
                var.put('accu', var.get('_accu'))
                if var.get('xs'):
                    var.put('_xs', var.get('xs').get('1'))
                    var.put('_accu', Js([var.get('f$1')(var.get('xs').get('0')), var.get('accu')]))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_mapReverseU_.func_name = 'mapReverseU'
        var.put('mapReverseU', PyJsHoisted_mapReverseU_)
        @Js
        def PyJsHoisted_mapReverse_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l'])
            return var.get('mapReverseU')(var.get('l'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_mapReverse_.func_name = 'mapReverse'
        var.put('mapReverse', PyJsHoisted_mapReverse_)
        @Js
        def PyJsHoisted_forEachU_(_xs, f, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', 'f'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    var.get('f')(var.get('xs').get('0'))
                    var.put('_xs', var.get('xs').get('1'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_forEachU_.func_name = 'forEachU'
        var.put('forEachU', PyJsHoisted_forEachU_)
        @Js
        def PyJsHoisted_forEach_(xs, f, this, arguments, var=var):
            var = Scope({'xs':xs, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'f'])
            return var.get('forEachU')(var.get('xs'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_forEach_.func_name = 'forEach'
        var.put('forEach', PyJsHoisted_forEach_)
        @Js
        def PyJsHoisted_forEachWithIndexU_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'f', 'f$1', '_xs', '_i', 'i', 'l'])
            var.put('_xs', var.get('l'))
            var.put('_i', Js(0.0))
            var.put('f$1', var.get('f'))
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    var.get('f$1')(var.get('i'), var.get('xs').get('0'))
                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                    var.put('_xs', var.get('xs').get('1'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_forEachWithIndexU_.func_name = 'forEachWithIndexU'
        var.put('forEachWithIndexU', PyJsHoisted_forEachWithIndexU_)
        @Js
        def PyJsHoisted_forEachWithIndex_(l, f, this, arguments, var=var):
            var = Scope({'l':l, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l'])
            return var.get('forEachWithIndexU')(var.get('l'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_forEachWithIndex_.func_name = 'forEachWithIndex'
        var.put('forEachWithIndex', PyJsHoisted_forEachWithIndex_)
        @Js
        def PyJsHoisted_reduceU_(_l, _accu, f, this, arguments, var=var):
            var = Scope({'_l':_l, '_accu':_accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', '_accu', '_l', 'l'])
            while Js(True):
                var.put('accu', var.get('_accu'))
                var.put('l', var.get('_l'))
                if var.get('l'):
                    var.put('_accu', var.get('f')(var.get('accu'), var.get('l').get('0')))
                    var.put('_l', var.get('l').get('1'))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_reduceU_.func_name = 'reduceU'
        var.put('reduceU', PyJsHoisted_reduceU_)
        @Js
        def PyJsHoisted_reduce_(l, accu, f, this, arguments, var=var):
            var = Scope({'l':l, 'accu':accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', 'l'])
            return var.get('reduceU')(var.get('l'), var.get('accu'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_reduce_.func_name = 'reduce'
        var.put('reduce', PyJsHoisted_reduce_)
        @Js
        def PyJsHoisted_reduceReverseUnsafeU_(l, accu, f, this, arguments, var=var):
            var = Scope({'l':l, 'accu':accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', 'l'])
            if var.get('l'):
                return var.get('f')(var.get('reduceReverseUnsafeU')(var.get('l').get('1'), var.get('accu'), var.get('f')), var.get('l').get('0'))
            else:
                return var.get('accu')
        PyJsHoisted_reduceReverseUnsafeU_.func_name = 'reduceReverseUnsafeU'
        var.put('reduceReverseUnsafeU', PyJsHoisted_reduceReverseUnsafeU_)
        @Js
        def PyJsHoisted_reduceReverseU_(l, acc, f, this, arguments, var=var):
            var = Scope({'l':l, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'f', 'acc', 'l'])
            var.put('len', var.get('length')(var.get('l')))
            if (var.get('len')<Js(1000.0)):
                return var.get('reduceReverseUnsafeU')(var.get('l'), var.get('acc'), var.get('f'))
            else:
                return var.get('Belt_Array').callprop('reduceReverseU', var.get('toArray')(var.get('l')), var.get('acc'), var.get('f'))
        PyJsHoisted_reduceReverseU_.func_name = 'reduceReverseU'
        var.put('reduceReverseU', PyJsHoisted_reduceReverseU_)
        @Js
        def PyJsHoisted_reduceReverse_(l, accu, f, this, arguments, var=var):
            var = Scope({'l':l, 'accu':accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', 'l'])
            return var.get('reduceReverseU')(var.get('l'), var.get('accu'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_reduceReverse_.func_name = 'reduceReverse'
        var.put('reduceReverse', PyJsHoisted_reduceReverse_)
        @Js
        def PyJsHoisted_reduceWithIndexU_(l, acc, f, this, arguments, var=var):
            var = Scope({'l':l, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc$1', 'f', 'l$1', 'acc', 'f$1', '_i', '_acc', '_l', 'i', 'l'])
            var.put('_l', var.get('l'))
            var.put('_acc', var.get('acc'))
            var.put('f$1', var.get('f'))
            var.put('_i', Js(0.0))
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('acc$1', var.get('_acc'))
                var.put('l$1', var.get('_l'))
                if var.get('l$1'):
                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                    var.put('_acc', var.get('f$1')(var.get('acc$1'), var.get('l$1').get('0'), var.get('i')))
                    var.put('_l', var.get('l$1').get('1'))
                    continue
                else:
                    return var.get('acc$1')
            pass
        PyJsHoisted_reduceWithIndexU_.func_name = 'reduceWithIndexU'
        var.put('reduceWithIndexU', PyJsHoisted_reduceWithIndexU_)
        @Js
        def PyJsHoisted_reduceWithIndex_(l, acc, f, this, arguments, var=var):
            var = Scope({'l':l, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', 'f', 'l'])
            return var.get('reduceWithIndexU')(var.get('l'), var.get('acc'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_reduceWithIndex_.func_name = 'reduceWithIndex'
        var.put('reduceWithIndex', PyJsHoisted_reduceWithIndex_)
        @Js
        def PyJsHoisted_mapReverse2U_(l1, l2, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', '_l1', 'l2', 'l1', 'l2$1', 'l1$1', '_accu', 'f$1', '_l2'])
            var.put('_l1', var.get('l1'))
            var.put('_l2', var.get('l2'))
            var.put('_accu', Js(0.0))
            var.put('f$1', var.get('f'))
            while Js(True):
                var.put('accu', var.get('_accu'))
                var.put('l2$1', var.get('_l2'))
                var.put('l1$1', var.get('_l1'))
                if (var.get('l1$1') and var.get('l2$1')):
                    var.put('_accu', Js([var.get('f$1')(var.get('l1$1').get('0'), var.get('l2$1').get('0')), var.get('accu')]))
                    var.put('_l2', var.get('l2$1').get('1'))
                    var.put('_l1', var.get('l1$1').get('1'))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_mapReverse2U_.func_name = 'mapReverse2U'
        var.put('mapReverse2U', PyJsHoisted_mapReverse2U_)
        @Js
        def PyJsHoisted_mapReverse2_(l1, l2, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l2', 'l1'])
            return var.get('mapReverse2U')(var.get('l1'), var.get('l2'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_mapReverse2_.func_name = 'mapReverse2'
        var.put('mapReverse2', PyJsHoisted_mapReverse2_)
        @Js
        def PyJsHoisted_forEach2U_(_l1, _l2, f, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', '_l1', 'l2', 'l1', '_l2'])
            while Js(True):
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if (var.get('l1') and var.get('l2')):
                    var.get('f')(var.get('l1').get('0'), var.get('l2').get('0'))
                    var.put('_l2', var.get('l2').get('1'))
                    var.put('_l1', var.get('l1').get('1'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_forEach2U_.func_name = 'forEach2U'
        var.put('forEach2U', PyJsHoisted_forEach2U_)
        @Js
        def PyJsHoisted_forEach2_(l1, l2, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l2', 'l1'])
            return var.get('forEach2U')(var.get('l1'), var.get('l2'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_forEach2_.func_name = 'forEach2'
        var.put('forEach2', PyJsHoisted_forEach2_)
        @Js
        def PyJsHoisted_reduce2U_(_l1, _l2, _accu, f, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, '_accu':_accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', '_l1', 'l2', 'l1', '_accu', '_l2'])
            while Js(True):
                var.put('accu', var.get('_accu'))
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if (var.get('l1') and var.get('l2')):
                    var.put('_accu', var.get('f')(var.get('accu'), var.get('l1').get('0'), var.get('l2').get('0')))
                    var.put('_l2', var.get('l2').get('1'))
                    var.put('_l1', var.get('l1').get('1'))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_reduce2U_.func_name = 'reduce2U'
        var.put('reduce2U', PyJsHoisted_reduce2U_)
        @Js
        def PyJsHoisted_reduce2_(l1, l2, acc, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', 'f', 'l2', 'l1'])
            return var.get('reduce2U')(var.get('l1'), var.get('l2'), var.get('acc'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_reduce2_.func_name = 'reduce2'
        var.put('reduce2', PyJsHoisted_reduce2_)
        @Js
        def PyJsHoisted_reduceReverse2UnsafeU_(l1, l2, accu, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'accu':accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', 'l2', 'l1'])
            if (var.get('l1') and var.get('l2')):
                return var.get('f')(var.get('reduceReverse2UnsafeU')(var.get('l1').get('1'), var.get('l2').get('1'), var.get('accu'), var.get('f')), var.get('l1').get('0'), var.get('l2').get('0'))
            else:
                return var.get('accu')
        PyJsHoisted_reduceReverse2UnsafeU_.func_name = 'reduceReverse2UnsafeU'
        var.put('reduceReverse2UnsafeU', PyJsHoisted_reduceReverse2UnsafeU_)
        @Js
        def PyJsHoisted_reduceReverse2U_(l1, l2, acc, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'f', 'l2', 'l1', 'acc'])
            var.put('len', var.get('length')(var.get('l1')))
            if (var.get('len')<Js(1000.0)):
                return var.get('reduceReverse2UnsafeU')(var.get('l1'), var.get('l2'), var.get('acc'), var.get('f'))
            else:
                return var.get('Belt_Array').callprop('reduceReverse2U', var.get('toArray')(var.get('l1')), var.get('toArray')(var.get('l2')), var.get('acc'), var.get('f'))
        PyJsHoisted_reduceReverse2U_.func_name = 'reduceReverse2U'
        var.put('reduceReverse2U', PyJsHoisted_reduceReverse2U_)
        @Js
        def PyJsHoisted_reduceReverse2_(l1, l2, acc, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', 'f', 'l2', 'l1'])
            return var.get('reduceReverse2U')(var.get('l1'), var.get('l2'), var.get('acc'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_reduceReverse2_.func_name = 'reduceReverse2'
        var.put('reduceReverse2', PyJsHoisted_reduceReverse2_)
        @Js
        def PyJsHoisted_everyU_(_xs, p, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', 'p'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    if var.get('p')(var.get('xs').get('0')):
                        var.put('_xs', var.get('xs').get('1'))
                        continue
                    else:
                        return Js(False)
                else:
                    return Js(True)
            pass
        PyJsHoisted_everyU_.func_name = 'everyU'
        var.put('everyU', PyJsHoisted_everyU_)
        @Js
        def PyJsHoisted_every_(xs, p, this, arguments, var=var):
            var = Scope({'xs':xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'p'])
            return var.get('everyU')(var.get('xs'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_every_.func_name = 'every'
        var.put('every', PyJsHoisted_every_)
        @Js
        def PyJsHoisted_someU_(_xs, p, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', 'p'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    if var.get('p')(var.get('xs').get('0')):
                        return Js(True)
                    else:
                        var.put('_xs', var.get('xs').get('1'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_someU_.func_name = 'someU'
        var.put('someU', PyJsHoisted_someU_)
        @Js
        def PyJsHoisted_some_(xs, p, this, arguments, var=var):
            var = Scope({'xs':xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'p'])
            return var.get('someU')(var.get('xs'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_some_.func_name = 'some'
        var.put('some', PyJsHoisted_some_)
        @Js
        def PyJsHoisted_every2U_(_l1, _l2, p, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['_l1', 'l2', 'l1', '_l2', 'p'])
            while Js(True):
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if (var.get('l1') and var.get('l2')):
                    if var.get('p')(var.get('l1').get('0'), var.get('l2').get('0')):
                        var.put('_l2', var.get('l2').get('1'))
                        var.put('_l1', var.get('l1').get('1'))
                        continue
                    else:
                        return Js(False)
                else:
                    return Js(True)
            pass
        PyJsHoisted_every2U_.func_name = 'every2U'
        var.put('every2U', PyJsHoisted_every2U_)
        @Js
        def PyJsHoisted_every2_(l1, l2, p, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['l2', 'p', 'l1'])
            return var.get('every2U')(var.get('l1'), var.get('l2'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_every2_.func_name = 'every2'
        var.put('every2', PyJsHoisted_every2_)
        @Js
        def PyJsHoisted_cmpByLength_(_l1, _l2, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, 'this':this, 'arguments':arguments}, var)
            var.registers(['_l2', '_l1', 'l2', 'l1'])
            while Js(True):
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if var.get('l1'):
                    if var.get('l2'):
                        var.put('_l2', var.get('l2').get('1'))
                        var.put('_l1', var.get('l1').get('1'))
                        continue
                    else:
                        return Js(1.0)
                else:
                    if var.get('l2'):
                        return (-Js(1.0))
                    else:
                        return Js(0.0)
            pass
        PyJsHoisted_cmpByLength_.func_name = 'cmpByLength'
        var.put('cmpByLength', PyJsHoisted_cmpByLength_)
        @Js
        def PyJsHoisted_cmpU_(_l1, _l2, p, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['l2', '_l1', 'l1', 'c', '_l2', 'p'])
            while Js(True):
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if var.get('l1'):
                    if var.get('l2'):
                        var.put('c', var.get('p')(var.get('l1').get('0'), var.get('l2').get('0')))
                        if PyJsStrictEq(var.get('c'),Js(0.0)):
                            var.put('_l2', var.get('l2').get('1'))
                            var.put('_l1', var.get('l1').get('1'))
                            continue
                        else:
                            return var.get('c')
                    else:
                        return Js(1.0)
                else:
                    if var.get('l2'):
                        return (-Js(1.0))
                    else:
                        return Js(0.0)
            pass
        PyJsHoisted_cmpU_.func_name = 'cmpU'
        var.put('cmpU', PyJsHoisted_cmpU_)
        @Js
        def PyJsHoisted_cmp_(l1, l2, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l2', 'l1'])
            return var.get('cmpU')(var.get('l1'), var.get('l2'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_cmp_.func_name = 'cmp'
        var.put('cmp', PyJsHoisted_cmp_)
        @Js
        def PyJsHoisted_eqU_(_l1, _l2, p, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['_l1', 'l2', 'l1', '_l2', 'p'])
            while Js(True):
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if var.get('l1'):
                    if (var.get('l2') and var.get('p')(var.get('l1').get('0'), var.get('l2').get('0'))):
                        var.put('_l2', var.get('l2').get('1'))
                        var.put('_l1', var.get('l1').get('1'))
                        continue
                    else:
                        return Js(False)
                else:
                    if var.get('l2'):
                        return Js(False)
                    else:
                        return Js(True)
            pass
        PyJsHoisted_eqU_.func_name = 'eqU'
        var.put('eqU', PyJsHoisted_eqU_)
        @Js
        def PyJsHoisted_eq_(l1, l2, f, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'l2', 'l1'])
            return var.get('eqU')(var.get('l1'), var.get('l2'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_some2U_(_l1, _l2, p, this, arguments, var=var):
            var = Scope({'_l1':_l1, '_l2':_l2, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['_l1', 'l2', 'l1', '_l2', 'p'])
            while Js(True):
                var.put('l2', var.get('_l2'))
                var.put('l1', var.get('_l1'))
                if (var.get('l1') and var.get('l2')):
                    if var.get('p')(var.get('l1').get('0'), var.get('l2').get('0')):
                        return Js(True)
                    else:
                        var.put('_l2', var.get('l2').get('1'))
                        var.put('_l1', var.get('l1').get('1'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_some2U_.func_name = 'some2U'
        var.put('some2U', PyJsHoisted_some2U_)
        @Js
        def PyJsHoisted_some2_(l1, l2, p, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['l2', 'p', 'l1'])
            return var.get('some2U')(var.get('l1'), var.get('l2'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_some2_.func_name = 'some2'
        var.put('some2', PyJsHoisted_some2_)
        @Js
        def PyJsHoisted_hasU_(_xs, x, eq, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', 'eq', 'x'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    if var.get('eq')(var.get('xs').get('0'), var.get('x')):
                        return Js(True)
                    else:
                        var.put('_xs', var.get('xs').get('1'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_hasU_.func_name = 'hasU'
        var.put('hasU', PyJsHoisted_hasU_)
        @Js
        def PyJsHoisted_has_(xs, x, eq, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', 'x'])
            return var.get('hasU')(var.get('xs'), var.get('x'), var.get('Curry').callprop('__2', var.get('eq')))
        PyJsHoisted_has_.func_name = 'has'
        var.put('has', PyJsHoisted_has_)
        @Js
        def PyJsHoisted_getAssocU_(_xs, x, eq, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', '_xs', 'x', 'match'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    var.put('match', var.get('xs').get('0'))
                    if var.get('eq')(var.get('match').get('0'), var.get('x')):
                        return var.get('Caml_option').callprop('some', var.get('match').get('1'))
                    else:
                        var.put('_xs', var.get('xs').get('1'))
                        continue
                else:
                    return var.get('undefined')
            pass
        PyJsHoisted_getAssocU_.func_name = 'getAssocU'
        var.put('getAssocU', PyJsHoisted_getAssocU_)
        @Js
        def PyJsHoisted_getAssoc_(xs, x, eq, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', 'x'])
            return var.get('getAssocU')(var.get('xs'), var.get('x'), var.get('Curry').callprop('__2', var.get('eq')))
        PyJsHoisted_getAssoc_.func_name = 'getAssoc'
        var.put('getAssoc', PyJsHoisted_getAssoc_)
        @Js
        def PyJsHoisted_hasAssocU_(_xs, x, eq, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', 'eq', 'x'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    if var.get('eq')(var.get('xs').get('0').get('0'), var.get('x')):
                        return Js(True)
                    else:
                        var.put('_xs', var.get('xs').get('1'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_hasAssocU_.func_name = 'hasAssocU'
        var.put('hasAssocU', PyJsHoisted_hasAssocU_)
        @Js
        def PyJsHoisted_hasAssoc_(xs, x, eq, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', 'x'])
            return var.get('hasAssocU')(var.get('xs'), var.get('x'), var.get('Curry').callprop('__2', var.get('eq')))
        PyJsHoisted_hasAssoc_.func_name = 'hasAssoc'
        var.put('hasAssoc', PyJsHoisted_hasAssoc_)
        @Js
        def PyJsHoisted_removeAssocU_(xs, x, eq, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', 'removed', 'cell', 'pair', 'x', 'l'])
            if var.get('xs'):
                var.put('l', var.get('xs').get('1'))
                var.put('pair', var.get('xs').get('0'))
                if var.get('eq')(var.get('pair').get('0'), var.get('x')):
                    return var.get('l')
                else:
                    var.put('cell', Js([var.get('pair'), Js(0.0)]))
                    var.put('removed', var.get('removeAssocAuxWithMap')(var.get('l'), var.get('x'), var.get('cell'), var.get('eq')))
                    if var.get('removed'):
                        return var.get('cell')
                    else:
                        return var.get('xs')
            else:
                return Js(0.0)
        PyJsHoisted_removeAssocU_.func_name = 'removeAssocU'
        var.put('removeAssocU', PyJsHoisted_removeAssocU_)
        @Js
        def PyJsHoisted_removeAssoc_(xs, x, eq, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', 'x'])
            return var.get('removeAssocU')(var.get('xs'), var.get('x'), var.get('Curry').callprop('__2', var.get('eq')))
        PyJsHoisted_removeAssoc_.func_name = 'removeAssoc'
        var.put('removeAssoc', PyJsHoisted_removeAssoc_)
        @Js
        def PyJsHoisted_setAssocU_(xs, x, k, eq, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'k':k, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', 'cell', 'pair', 'x', 'replaced', 'k', 'l'])
            if var.get('xs'):
                var.put('l', var.get('xs').get('1'))
                var.put('pair', var.get('xs').get('0'))
                if var.get('eq')(var.get('pair').get('0'), var.get('x')):
                    return Js([Js([var.get('x'), var.get('k')]), var.get('l')])
                else:
                    var.put('cell', Js([var.get('pair'), Js(0.0)]))
                    var.put('replaced', var.get('setAssocAuxWithMap')(var.get('l'), var.get('x'), var.get('k'), var.get('cell'), var.get('eq')))
                    if var.get('replaced'):
                        return var.get('cell')
                    else:
                        return Js([Js([var.get('x'), var.get('k')]), var.get('xs')])
            else:
                return Js([Js([var.get('x'), var.get('k')]), Js(0.0)])
        PyJsHoisted_setAssocU_.func_name = 'setAssocU'
        var.put('setAssocU', PyJsHoisted_setAssocU_)
        @Js
        def PyJsHoisted_setAssoc_(xs, x, k, eq, this, arguments, var=var):
            var = Scope({'xs':xs, 'x':x, 'k':k, 'eq':eq, 'this':this, 'arguments':arguments}, var)
            var.registers(['eq', 'xs', 'x', 'k'])
            return var.get('setAssocU')(var.get('xs'), var.get('x'), var.get('k'), var.get('Curry').callprop('__2', var.get('eq')))
        PyJsHoisted_setAssoc_.func_name = 'setAssoc'
        var.put('setAssoc', PyJsHoisted_setAssoc_)
        @Js
        def PyJsHoisted_sortU_(xs, cmp, this, arguments, var=var):
            var = Scope({'xs':xs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr', 'cmp', 'xs'])
            var.put('arr', var.get('toArray')(var.get('xs')))
            var.get('Belt_SortArray').callprop('stableSortInPlaceByU', var.get('arr'), var.get('cmp'))
            return var.get('fromArray')(var.get('arr'))
        PyJsHoisted_sortU_.func_name = 'sortU'
        var.put('sortU', PyJsHoisted_sortU_)
        @Js
        def PyJsHoisted_sort_(xs, cmp, this, arguments, var=var):
            var = Scope({'xs':xs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'cmp'])
            return var.get('sortU')(var.get('xs'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_sort_.func_name = 'sort'
        var.put('sort', PyJsHoisted_sort_)
        @Js
        def PyJsHoisted_getByU_(_xs, p, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['_xs', 'xs', 'x', 'p'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    var.put('x', var.get('xs').get('0'))
                    if var.get('p')(var.get('x')):
                        return var.get('Caml_option').callprop('some', var.get('x'))
                    else:
                        var.put('_xs', var.get('xs').get('1'))
                        continue
                else:
                    return var.get('undefined')
            pass
        PyJsHoisted_getByU_.func_name = 'getByU'
        var.put('getByU', PyJsHoisted_getByU_)
        @Js
        def PyJsHoisted_getBy_(xs, p, this, arguments, var=var):
            var = Scope({'xs':xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'p'])
            return var.get('getByU')(var.get('xs'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_getBy_.func_name = 'getBy'
        var.put('getBy', PyJsHoisted_getBy_)
        @Js
        def PyJsHoisted_keepU_(_xs, p, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 't', 'cell', '_xs', 'h', 'p'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    var.put('t', var.get('xs').get('1'))
                    var.put('h', var.get('xs').get('0'))
                    if var.get('p')(var.get('h')):
                        var.put('cell', Js([var.get('h'), Js(0.0)]))
                        var.get('copyAuxWitFilter')(var.get('p'), var.get('t'), var.get('cell'))
                        return var.get('cell')
                    else:
                        var.put('_xs', var.get('t'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_keepU_.func_name = 'keepU'
        var.put('keepU', PyJsHoisted_keepU_)
        @Js
        def PyJsHoisted_keep_(xs, p, this, arguments, var=var):
            var = Scope({'xs':xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'p'])
            return var.get('keepU')(var.get('xs'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_keep_.func_name = 'keep'
        var.put('keep', PyJsHoisted_keep_)
        @Js
        def PyJsHoisted_keepWithIndexU_(xs, p, this, arguments, var=var):
            var = Scope({'xs':xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 't', 'cell', 'p$1', '_xs', '_i', 'xs$1', 'h', 'i', 'p'])
            var.put('_xs', var.get('xs'))
            var.put('p$1', var.get('p'))
            var.put('_i', Js(0.0))
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('xs$1', var.get('_xs'))
                if var.get('xs$1'):
                    var.put('t', var.get('xs$1').get('1'))
                    var.put('h', var.get('xs$1').get('0'))
                    if var.get('p$1')(var.get('h'), var.get('i')):
                        var.put('cell', Js([var.get('h'), Js(0.0)]))
                        var.get('copyAuxWithFilterIndex')(var.get('p$1'), var.get('t'), var.get('cell'), ((var.get('i')+Js(1.0))|Js(0.0)))
                        return var.get('cell')
                    else:
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        var.put('_xs', var.get('t'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_keepWithIndexU_.func_name = 'keepWithIndexU'
        var.put('keepWithIndexU', PyJsHoisted_keepWithIndexU_)
        @Js
        def PyJsHoisted_keepWithIndex_(xs, p, this, arguments, var=var):
            var = Scope({'xs':xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'p'])
            return var.get('keepWithIndexU')(var.get('xs'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_keepWithIndex_.func_name = 'keepWithIndex'
        var.put('keepWithIndex', PyJsHoisted_keepWithIndex_)
        @Js
        def PyJsHoisted_keepMapU_(_xs, p, this, arguments, var=var):
            var = Scope({'_xs':_xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 't', 'cell', '_xs', 'match', 'p'])
            while Js(True):
                var.put('xs', var.get('_xs'))
                if var.get('xs'):
                    var.put('t', var.get('xs').get('1'))
                    var.put('match', var.get('p')(var.get('xs').get('0')))
                    if PyJsStrictNeq(var.get('match'),var.get('undefined')):
                        var.put('cell', Js([var.get('Caml_option').callprop('valFromOption', var.get('match')), Js(0.0)]))
                        var.get('copyAuxWitFilterMap')(var.get('p'), var.get('t'), var.get('cell'))
                        return var.get('cell')
                    else:
                        var.put('_xs', var.get('t'))
                        continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_keepMapU_.func_name = 'keepMapU'
        var.put('keepMapU', PyJsHoisted_keepMapU_)
        @Js
        def PyJsHoisted_keepMap_(xs, p, this, arguments, var=var):
            var = Scope({'xs':xs, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'p'])
            return var.get('keepMapU')(var.get('xs'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_keepMap_.func_name = 'keepMap'
        var.put('keepMap', PyJsHoisted_keepMap_)
        @Js
        def PyJsHoisted_partitionU_(l, p, this, arguments, var=var):
            var = Scope({'l':l, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['nextY', 'nextX', 'h', 'b', 'p', 'l'])
            if var.get('l'):
                var.put('h', var.get('l').get('0'))
                var.put('nextX', Js([var.get('h'), Js(0.0)]))
                var.put('nextY', Js([var.get('h'), Js(0.0)]))
                var.put('b', var.get('p')(var.get('h')))
                var.get('partitionAux')(var.get('p'), var.get('l').get('1'), var.get('nextX'), var.get('nextY'))
                if var.get('b'):
                    return Js([var.get('nextX'), var.get('nextY').get('1')])
                else:
                    return Js([var.get('nextX').get('1'), var.get('nextY')])
            else:
                return Js([Js(0.0), Js(0.0)])
        PyJsHoisted_partitionU_.func_name = 'partitionU'
        var.put('partitionU', PyJsHoisted_partitionU_)
        @Js
        def PyJsHoisted_partition_(l, p, this, arguments, var=var):
            var = Scope({'l':l, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'l'])
            return var.get('partitionU')(var.get('l'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_partition_.func_name = 'partition'
        var.put('partition', PyJsHoisted_partition_)
        @Js
        def PyJsHoisted_unzip_(xs, this, arguments, var=var):
            var = Scope({'xs':xs, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'cellY', 'match', 'cellX'])
            if var.get('xs'):
                var.put('match', var.get('xs').get('0'))
                var.put('cellX', Js([var.get('match').get('0'), Js(0.0)]))
                var.put('cellY', Js([var.get('match').get('1'), Js(0.0)]))
                var.get('splitAux')(var.get('xs').get('1'), var.get('cellX'), var.get('cellY'))
                return Js([var.get('cellX'), var.get('cellY')])
            else:
                return Js([Js(0.0), Js(0.0)])
        PyJsHoisted_unzip_.func_name = 'unzip'
        var.put('unzip', PyJsHoisted_unzip_)
        @Js
        def PyJsHoisted_zip_(l1, l2, this, arguments, var=var):
            var = Scope({'l1':l1, 'l2':l2, 'this':this, 'arguments':arguments}, var)
            var.registers(['l2', 'cell', 'l1'])
            if (var.get('l1') and var.get('l2')):
                var.put('cell', Js([Js([var.get('l1').get('0'), var.get('l2').get('0')]), Js(0.0)]))
                var.get('zipAux')(var.get('l1').get('1'), var.get('l2').get('1'), var.get('cell'))
                return var.get('cell')
            else:
                return Js(0.0)
        PyJsHoisted_zip_.func_name = 'zip'
        var.put('zip', PyJsHoisted_zip_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Belt_Array', var.get('require')(Js('./belt_Array.js')))
        var.put('Caml_option', var.get('require')(Js('./caml_option.js')))
        var.put('Belt_SortArray', var.get('require')(Js('./belt_SortArray.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('size', var.get('length'))
        var.put('filter', var.get('keep'))
        var.put('filterWithIndex', var.get('keepWithIndex'))
        var.get('exports').put('length', var.get('length'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('head', var.get('head'))
        var.get('exports').put('headExn', var.get('headExn'))
        var.get('exports').put('tail', var.get('tail'))
        var.get('exports').put('tailExn', var.get('tailExn'))
        var.get('exports').put('add', var.get('add'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('make', var.get('make'))
        var.get('exports').put('makeByU', var.get('makeByU'))
        var.get('exports').put('makeBy', var.get('makeBy'))
        var.get('exports').put('shuffle', var.get('shuffle'))
        var.get('exports').put('drop', var.get('drop'))
        var.get('exports').put('take', var.get('take'))
        var.get('exports').put('splitAt', var.get('splitAt'))
        var.get('exports').put('concat', var.get('concat'))
        var.get('exports').put('concatMany', var.get('concatMany'))
        var.get('exports').put('reverseConcat', var.get('reverseConcat'))
        var.get('exports').put('flatten', var.get('flatten'))
        var.get('exports').put('mapU', var.get('mapU'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('zip', var.get('zip'))
        var.get('exports').put('zipByU', var.get('zipByU'))
        var.get('exports').put('zipBy', var.get('zipBy'))
        var.get('exports').put('mapWithIndexU', var.get('mapWithIndexU'))
        var.get('exports').put('mapWithIndex', var.get('mapWithIndex'))
        var.get('exports').put('fromArray', var.get('fromArray'))
        var.get('exports').put('toArray', var.get('toArray'))
        var.get('exports').put('reverse', var.get('reverse'))
        var.get('exports').put('mapReverseU', var.get('mapReverseU'))
        var.get('exports').put('mapReverse', var.get('mapReverse'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('forEachWithIndexU', var.get('forEachWithIndexU'))
        var.get('exports').put('forEachWithIndex', var.get('forEachWithIndex'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('reduceWithIndexU', var.get('reduceWithIndexU'))
        var.get('exports').put('reduceWithIndex', var.get('reduceWithIndex'))
        var.get('exports').put('reduceReverseU', var.get('reduceReverseU'))
        var.get('exports').put('reduceReverse', var.get('reduceReverse'))
        var.get('exports').put('mapReverse2U', var.get('mapReverse2U'))
        var.get('exports').put('mapReverse2', var.get('mapReverse2'))
        var.get('exports').put('forEach2U', var.get('forEach2U'))
        var.get('exports').put('forEach2', var.get('forEach2'))
        var.get('exports').put('reduce2U', var.get('reduce2U'))
        var.get('exports').put('reduce2', var.get('reduce2'))
        var.get('exports').put('reduceReverse2U', var.get('reduceReverse2U'))
        var.get('exports').put('reduceReverse2', var.get('reduceReverse2'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('every2U', var.get('every2U'))
        var.get('exports').put('every2', var.get('every2'))
        var.get('exports').put('some2U', var.get('some2U'))
        var.get('exports').put('some2', var.get('some2'))
        var.get('exports').put('cmpByLength', var.get('cmpByLength'))
        var.get('exports').put('cmpU', var.get('cmpU'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eqU', var.get('eqU'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('hasU', var.get('hasU'))
        var.get('exports').put('has', var.get('has'))
        var.get('exports').put('getByU', var.get('getByU'))
        var.get('exports').put('getBy', var.get('getBy'))
        var.get('exports').put('keepU', var.get('keepU'))
        var.get('exports').put('keep', var.get('keep'))
        var.get('exports').put('filter', var.get('filter'))
        var.get('exports').put('keepWithIndexU', var.get('keepWithIndexU'))
        var.get('exports').put('keepWithIndex', var.get('keepWithIndex'))
        var.get('exports').put('filterWithIndex', var.get('filterWithIndex'))
        var.get('exports').put('keepMapU', var.get('keepMapU'))
        var.get('exports').put('keepMap', var.get('keepMap'))
        var.get('exports').put('partitionU', var.get('partitionU'))
        var.get('exports').put('partition', var.get('partition'))
        var.get('exports').put('unzip', var.get('unzip'))
        var.get('exports').put('getAssocU', var.get('getAssocU'))
        var.get('exports').put('getAssoc', var.get('getAssoc'))
        var.get('exports').put('hasAssocU', var.get('hasAssocU'))
        var.get('exports').put('hasAssoc', var.get('hasAssoc'))
        var.get('exports').put('removeAssocU', var.get('removeAssocU'))
        var.get('exports').put('removeAssoc', var.get('removeAssoc'))
        var.get('exports').put('setAssocU', var.get('setAssocU'))
        var.get('exports').put('setAssoc', var.get('setAssoc'))
        var.get('exports').put('sortU', var.get('sortU'))
        var.get('exports').put('sort', var.get('sort'))
    PyJs_anonymous_2_._set_name('anonymous')
    @Js
    def PyJs_anonymous_3_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['get', 'mapU', '$$String', 'update', 'exports', 'map', 'getId', 'maximum', 'some', 'maxKey', 'toArray', 'minKeyUndefined', 'every', 'mapWithKey', 'keysToArray', 'fromArray', 'getData', 'Int', 'mergeMany', 'remove', 'getWithDefault', 'maxUndefined', 'merge', 'everyU', 'mapWithKeyU', 'minKey', 'Belt_MapDict', 'module', 'updateU', 'size', 'cmpU', 'eq', 'findFirstBy', 'maxKeyUndefined', 'require', 'getExn', 'cmp', 'Curry', 'minUndefined', 'make', 'keep', 'Dict', 'partition', 'reduceU', 'valuesToArray', 'removeMany', 'isEmpty', 'toList', 'has', 'minimum', 'checkInvariantInternal', 'forEach', 'someU', 'eqU', 'split', 'getUndefined', 'keepU', 'findFirstByU', 'partitionU', 'set', 'reduce', 'packIdData', 'mergeU', 'forEachU'])
        @Js
        def PyJsHoisted_fromArray_(data, id, this, arguments, var=var):
            var = Scope({'data':data, 'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id', 'data', 'cmp'])
            var.put('cmp', var.get('id').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_MapDict').callprop('fromArray', var.get('data'), var.get('cmp'))})
        PyJsHoisted_fromArray_.func_name = 'fromArray'
        var.put('fromArray', PyJsHoisted_fromArray_)
        @Js
        def PyJsHoisted_remove_(m, x, this, arguments, var=var):
            var = Scope({'m':m, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp', 'newData', 'm', 'x', 'odata'])
            var.put('cmp', var.get('m').get('cmp'))
            var.put('odata', var.get('m').get('data'))
            var.put('newData', var.get('Belt_MapDict').callprop('remove', var.get('odata'), var.get('x'), var.get('cmp')))
            if PyJsStrictEq(var.get('newData'),var.get('odata')):
                return var.get('m')
            else:
                return Js({'cmp':var.get('cmp'),'data':var.get('newData')})
        PyJsHoisted_remove_.func_name = 'remove'
        var.put('remove', PyJsHoisted_remove_)
        @Js
        def PyJsHoisted_removeMany_(m, x, this, arguments, var=var):
            var = Scope({'m':m, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp', 'newData', 'm', 'x', 'odata'])
            var.put('cmp', var.get('m').get('cmp'))
            var.put('odata', var.get('m').get('data'))
            var.put('newData', var.get('Belt_MapDict').callprop('removeMany', var.get('odata'), var.get('x'), var.get('cmp')))
            return Js({'cmp':var.get('cmp'),'data':var.get('newData')})
        PyJsHoisted_removeMany_.func_name = 'removeMany'
        var.put('removeMany', PyJsHoisted_removeMany_)
        @Js
        def PyJsHoisted_set_(m, key, d, this, arguments, var=var):
            var = Scope({'m':m, 'key':key, 'd':d, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'cmp', 'd', 'key'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_MapDict').callprop('set', var.get('m').get('data'), var.get('key'), var.get('d'), var.get('cmp'))})
        PyJsHoisted_set_.func_name = 'set'
        var.put('set', PyJsHoisted_set_)
        @Js
        def PyJsHoisted_mergeMany_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'm', 'cmp'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_MapDict').callprop('mergeMany', var.get('m').get('data'), var.get('e'), var.get('cmp'))})
        PyJsHoisted_mergeMany_.func_name = 'mergeMany'
        var.put('mergeMany', PyJsHoisted_mergeMany_)
        @Js
        def PyJsHoisted_updateU_(m, key, f, this, arguments, var=var):
            var = Scope({'m':m, 'key':key, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm', 'cmp', 'key'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_MapDict').callprop('updateU', var.get('m').get('data'), var.get('key'), var.get('f'), var.get('cmp'))})
        PyJsHoisted_updateU_.func_name = 'updateU'
        var.put('updateU', PyJsHoisted_updateU_)
        @Js
        def PyJsHoisted_update_(m, key, f, this, arguments, var=var):
            var = Scope({'m':m, 'key':key, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm', 'key'])
            return var.get('updateU')(var.get('m'), var.get('key'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_update_.func_name = 'update'
        var.put('update', PyJsHoisted_update_)
        @Js
        def PyJsHoisted_split_(m, x, this, arguments, var=var):
            var = Scope({'m':m, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['match$1', 'cmp', 'm', 'match', 'x'])
            var.put('cmp', var.get('m').get('cmp'))
            var.put('match', var.get('Belt_MapDict').callprop('split', var.get('m').get('data'), var.get('x'), var.get('cmp')))
            var.put('match$1', var.get('match').get('0'))
            return Js([Js([Js({'cmp':var.get('cmp'),'data':var.get('match$1').get('0')}), Js({'cmp':var.get('cmp'),'data':var.get('match$1').get('1')})]), var.get('match').get('1')])
        PyJsHoisted_split_.func_name = 'split'
        var.put('split', PyJsHoisted_split_)
        @Js
        def PyJsHoisted_mergeU_(s1, s2, f, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['s1', 'f', 'cmp', 's2'])
            var.put('cmp', var.get('s1').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_MapDict').callprop('mergeU', var.get('s1').get('data'), var.get('s2').get('data'), var.get('f'), var.get('cmp'))})
        PyJsHoisted_mergeU_.func_name = 'mergeU'
        var.put('mergeU', PyJsHoisted_mergeU_)
        @Js
        def PyJsHoisted_merge_(s1, s2, f, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['s1', 'f', 's2'])
            return var.get('mergeU')(var.get('s1'), var.get('s2'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_merge_.func_name = 'merge'
        var.put('merge', PyJsHoisted_merge_)
        @Js
        def PyJsHoisted_make_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return Js({'cmp':var.get('id').get('cmp'),'data':var.get('Belt_MapDict').get('empty')})
        PyJsHoisted_make_.func_name = 'make'
        var.put('make', PyJsHoisted_make_)
        @Js
        def PyJsHoisted_isEmpty_(map, this, arguments, var=var):
            var = Scope({'map':map, 'this':this, 'arguments':arguments}, var)
            var.registers(['map'])
            return var.get('Belt_MapDict').callprop('isEmpty', var.get('map').get('data'))
        PyJsHoisted_isEmpty_.func_name = 'isEmpty'
        var.put('isEmpty', PyJsHoisted_isEmpty_)
        @Js
        def PyJsHoisted_findFirstByU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('findFirstByU', var.get('m').get('data'), var.get('f'))
        PyJsHoisted_findFirstByU_.func_name = 'findFirstByU'
        var.put('findFirstByU', PyJsHoisted_findFirstByU_)
        @Js
        def PyJsHoisted_findFirstBy_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('findFirstByU', var.get('m').get('data'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_findFirstBy_.func_name = 'findFirstBy'
        var.put('findFirstBy', PyJsHoisted_findFirstBy_)
        @Js
        def PyJsHoisted_forEachU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('forEachU', var.get('m').get('data'), var.get('f'))
        PyJsHoisted_forEachU_.func_name = 'forEachU'
        var.put('forEachU', PyJsHoisted_forEachU_)
        @Js
        def PyJsHoisted_forEach_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('forEachU', var.get('m').get('data'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_forEach_.func_name = 'forEach'
        var.put('forEach', PyJsHoisted_forEach_)
        @Js
        def PyJsHoisted_reduceU_(m, acc, f, this, arguments, var=var):
            var = Scope({'m':m, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', 'f', 'm'])
            return var.get('Belt_MapDict').callprop('reduceU', var.get('m').get('data'), var.get('acc'), var.get('f'))
        PyJsHoisted_reduceU_.func_name = 'reduceU'
        var.put('reduceU', PyJsHoisted_reduceU_)
        @Js
        def PyJsHoisted_reduce_(m, acc, f, this, arguments, var=var):
            var = Scope({'m':m, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', 'f', 'm'])
            return var.get('reduceU')(var.get('m'), var.get('acc'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_reduce_.func_name = 'reduce'
        var.put('reduce', PyJsHoisted_reduce_)
        @Js
        def PyJsHoisted_everyU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('everyU', var.get('m').get('data'), var.get('f'))
        PyJsHoisted_everyU_.func_name = 'everyU'
        var.put('everyU', PyJsHoisted_everyU_)
        @Js
        def PyJsHoisted_every_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('everyU', var.get('m').get('data'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_every_.func_name = 'every'
        var.put('every', PyJsHoisted_every_)
        @Js
        def PyJsHoisted_someU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('someU', var.get('m').get('data'), var.get('f'))
        PyJsHoisted_someU_.func_name = 'someU'
        var.put('someU', PyJsHoisted_someU_)
        @Js
        def PyJsHoisted_some_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_MapDict').callprop('someU', var.get('m').get('data'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_some_.func_name = 'some'
        var.put('some', PyJsHoisted_some_)
        @Js
        def PyJsHoisted_keepU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return Js({'cmp':var.get('m').get('cmp'),'data':var.get('Belt_MapDict').callprop('keepU', var.get('m').get('data'), var.get('f'))})
        PyJsHoisted_keepU_.func_name = 'keepU'
        var.put('keepU', PyJsHoisted_keepU_)
        @Js
        def PyJsHoisted_keep_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('keepU')(var.get('m'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_keep_.func_name = 'keep'
        var.put('keep', PyJsHoisted_keep_)
        @Js
        def PyJsHoisted_partitionU_(m, p, this, arguments, var=var):
            var = Scope({'m':m, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'm', 'cmp', 'p'])
            var.put('cmp', var.get('m').get('cmp'))
            var.put('match', var.get('Belt_MapDict').callprop('partitionU', var.get('m').get('data'), var.get('p')))
            return Js([Js({'cmp':var.get('cmp'),'data':var.get('match').get('0')}), Js({'cmp':var.get('cmp'),'data':var.get('match').get('1')})])
        PyJsHoisted_partitionU_.func_name = 'partitionU'
        var.put('partitionU', PyJsHoisted_partitionU_)
        @Js
        def PyJsHoisted_partition_(m, p, this, arguments, var=var):
            var = Scope({'m':m, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'p'])
            return var.get('partitionU')(var.get('m'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_partition_.func_name = 'partition'
        var.put('partition', PyJsHoisted_partition_)
        @Js
        def PyJsHoisted_mapU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return Js({'cmp':var.get('m').get('cmp'),'data':var.get('Belt_MapDict').callprop('mapU', var.get('m').get('data'), var.get('f'))})
        PyJsHoisted_mapU_.func_name = 'mapU'
        var.put('mapU', PyJsHoisted_mapU_)
        @Js
        def PyJsHoisted_map_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('mapU')(var.get('m'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_map_.func_name = 'map'
        var.put('map', PyJsHoisted_map_)
        @Js
        def PyJsHoisted_mapWithKeyU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return Js({'cmp':var.get('m').get('cmp'),'data':var.get('Belt_MapDict').callprop('mapWithKeyU', var.get('m').get('data'), var.get('f'))})
        PyJsHoisted_mapWithKeyU_.func_name = 'mapWithKeyU'
        var.put('mapWithKeyU', PyJsHoisted_mapWithKeyU_)
        @Js
        def PyJsHoisted_mapWithKey_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('mapWithKeyU')(var.get('m'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_mapWithKey_.func_name = 'mapWithKey'
        var.put('mapWithKey', PyJsHoisted_mapWithKey_)
        @Js
        def PyJsHoisted_size_(map, this, arguments, var=var):
            var = Scope({'map':map, 'this':this, 'arguments':arguments}, var)
            var.registers(['map'])
            return var.get('Belt_MapDict').callprop('size', var.get('map').get('data'))
        PyJsHoisted_size_.func_name = 'size'
        var.put('size', PyJsHoisted_size_)
        @Js
        def PyJsHoisted_toList_(map, this, arguments, var=var):
            var = Scope({'map':map, 'this':this, 'arguments':arguments}, var)
            var.registers(['map'])
            return var.get('Belt_MapDict').callprop('toList', var.get('map').get('data'))
        PyJsHoisted_toList_.func_name = 'toList'
        var.put('toList', PyJsHoisted_toList_)
        @Js
        def PyJsHoisted_toArray_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('toArray', var.get('m').get('data'))
        PyJsHoisted_toArray_.func_name = 'toArray'
        var.put('toArray', PyJsHoisted_toArray_)
        @Js
        def PyJsHoisted_keysToArray_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('keysToArray', var.get('m').get('data'))
        PyJsHoisted_keysToArray_.func_name = 'keysToArray'
        var.put('keysToArray', PyJsHoisted_keysToArray_)
        @Js
        def PyJsHoisted_valuesToArray_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('valuesToArray', var.get('m').get('data'))
        PyJsHoisted_valuesToArray_.func_name = 'valuesToArray'
        var.put('valuesToArray', PyJsHoisted_valuesToArray_)
        @Js
        def PyJsHoisted_minKey_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('minKey', var.get('m').get('data'))
        PyJsHoisted_minKey_.func_name = 'minKey'
        var.put('minKey', PyJsHoisted_minKey_)
        @Js
        def PyJsHoisted_minKeyUndefined_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('minKeyUndefined', var.get('m').get('data'))
        PyJsHoisted_minKeyUndefined_.func_name = 'minKeyUndefined'
        var.put('minKeyUndefined', PyJsHoisted_minKeyUndefined_)
        @Js
        def PyJsHoisted_maxKey_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('maxKey', var.get('m').get('data'))
        PyJsHoisted_maxKey_.func_name = 'maxKey'
        var.put('maxKey', PyJsHoisted_maxKey_)
        @Js
        def PyJsHoisted_maxKeyUndefined_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('maxKeyUndefined', var.get('m').get('data'))
        PyJsHoisted_maxKeyUndefined_.func_name = 'maxKeyUndefined'
        var.put('maxKeyUndefined', PyJsHoisted_maxKeyUndefined_)
        @Js
        def PyJsHoisted_minimum_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('minimum', var.get('m').get('data'))
        PyJsHoisted_minimum_.func_name = 'minimum'
        var.put('minimum', PyJsHoisted_minimum_)
        @Js
        def PyJsHoisted_minUndefined_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('minUndefined', var.get('m').get('data'))
        PyJsHoisted_minUndefined_.func_name = 'minUndefined'
        var.put('minUndefined', PyJsHoisted_minUndefined_)
        @Js
        def PyJsHoisted_maximum_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('maximum', var.get('m').get('data'))
        PyJsHoisted_maximum_.func_name = 'maximum'
        var.put('maximum', PyJsHoisted_maximum_)
        @Js
        def PyJsHoisted_maxUndefined_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('maxUndefined', var.get('m').get('data'))
        PyJsHoisted_maxUndefined_.func_name = 'maxUndefined'
        var.put('maxUndefined', PyJsHoisted_maxUndefined_)
        @Js
        def PyJsHoisted_get_(map, x, this, arguments, var=var):
            var = Scope({'map':map, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'map'])
            return var.get('Belt_MapDict').callprop('get', var.get('map').get('data'), var.get('x'), var.get('map').get('cmp'))
        PyJsHoisted_get_.func_name = 'get'
        var.put('get', PyJsHoisted_get_)
        @Js
        def PyJsHoisted_getUndefined_(map, x, this, arguments, var=var):
            var = Scope({'map':map, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'map'])
            return var.get('Belt_MapDict').callprop('getUndefined', var.get('map').get('data'), var.get('x'), var.get('map').get('cmp'))
        PyJsHoisted_getUndefined_.func_name = 'getUndefined'
        var.put('getUndefined', PyJsHoisted_getUndefined_)
        @Js
        def PyJsHoisted_getWithDefault_(map, x, PyJsArg_646566_, this, arguments, var=var):
            var = Scope({'map':map, 'x':x, 'def':PyJsArg_646566_, 'this':this, 'arguments':arguments}, var)
            var.registers(['def', 'x', 'map'])
            return var.get('Belt_MapDict').callprop('getWithDefault', var.get('map').get('data'), var.get('x'), var.get('def'), var.get('map').get('cmp'))
        PyJsHoisted_getWithDefault_.func_name = 'getWithDefault'
        var.put('getWithDefault', PyJsHoisted_getWithDefault_)
        @Js
        def PyJsHoisted_getExn_(map, x, this, arguments, var=var):
            var = Scope({'map':map, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'map'])
            return var.get('Belt_MapDict').callprop('getExn', var.get('map').get('data'), var.get('x'), var.get('map').get('cmp'))
        PyJsHoisted_getExn_.func_name = 'getExn'
        var.put('getExn', PyJsHoisted_getExn_)
        @Js
        def PyJsHoisted_has_(map, x, this, arguments, var=var):
            var = Scope({'map':map, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'map'])
            return var.get('Belt_MapDict').callprop('has', var.get('map').get('data'), var.get('x'), var.get('map').get('cmp'))
        PyJsHoisted_has_.func_name = 'has'
        var.put('has', PyJsHoisted_has_)
        @Js
        def PyJsHoisted_checkInvariantInternal_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_MapDict').callprop('checkInvariantInternal', var.get('m').get('data'))
        PyJsHoisted_checkInvariantInternal_.func_name = 'checkInvariantInternal'
        var.put('checkInvariantInternal', PyJsHoisted_checkInvariantInternal_)
        @Js
        def PyJsHoisted_eqU_(m1, m2, veq, this, arguments, var=var):
            var = Scope({'m1':m1, 'm2':m2, 'veq':veq, 'this':this, 'arguments':arguments}, var)
            var.registers(['veq', 'm1', 'm2'])
            return var.get('Belt_MapDict').callprop('eqU', var.get('m1').get('data'), var.get('m2').get('data'), var.get('m1').get('cmp'), var.get('veq'))
        PyJsHoisted_eqU_.func_name = 'eqU'
        var.put('eqU', PyJsHoisted_eqU_)
        @Js
        def PyJsHoisted_eq_(m1, m2, veq, this, arguments, var=var):
            var = Scope({'m1':m1, 'm2':m2, 'veq':veq, 'this':this, 'arguments':arguments}, var)
            var.registers(['veq', 'm1', 'm2'])
            return var.get('eqU')(var.get('m1'), var.get('m2'), var.get('Curry').callprop('__2', var.get('veq')))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_cmpU_(m1, m2, vcmp, this, arguments, var=var):
            var = Scope({'m1':m1, 'm2':m2, 'vcmp':vcmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['m1', 'm2', 'vcmp'])
            return var.get('Belt_MapDict').callprop('cmpU', var.get('m1').get('data'), var.get('m2').get('data'), var.get('m1').get('cmp'), var.get('vcmp'))
        PyJsHoisted_cmpU_.func_name = 'cmpU'
        var.put('cmpU', PyJsHoisted_cmpU_)
        @Js
        def PyJsHoisted_cmp_(m1, m2, vcmp, this, arguments, var=var):
            var = Scope({'m1':m1, 'm2':m2, 'vcmp':vcmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['m1', 'm2', 'vcmp'])
            return var.get('cmpU')(var.get('m1'), var.get('m2'), var.get('Curry').callprop('__2', var.get('vcmp')))
        PyJsHoisted_cmp_.func_name = 'cmp'
        var.put('cmp', PyJsHoisted_cmp_)
        @Js
        def PyJsHoisted_getData_(prim, this, arguments, var=var):
            var = Scope({'prim':prim, 'this':this, 'arguments':arguments}, var)
            var.registers(['prim'])
            return var.get('prim').get('data')
        PyJsHoisted_getData_.func_name = 'getData'
        var.put('getData', PyJsHoisted_getData_)
        @Js
        def PyJsHoisted_getId_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'cmp'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp')})
        PyJsHoisted_getId_.func_name = 'getId'
        var.put('getId', PyJsHoisted_getId_)
        @Js
        def PyJsHoisted_packIdData_(id, data, this, arguments, var=var):
            var = Scope({'id':id, 'data':data, 'this':this, 'arguments':arguments}, var)
            var.registers(['id', 'data'])
            return Js({'cmp':var.get('id').get('cmp'),'data':var.get('data')})
        PyJsHoisted_packIdData_.func_name = 'packIdData'
        var.put('packIdData', PyJsHoisted_packIdData_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Belt_MapDict', var.get('require')(Js('./belt_MapDict.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('Int', Js(0.0))
        var.put('$$String', Js(0.0))
        var.put('Dict', Js(0.0))
        var.get('exports').put('Int', var.get('Int'))
        var.get('exports').put('$$String', var.get('$$String'))
        var.get('exports').put('Dict', var.get('Dict'))
        var.get('exports').put('make', var.get('make'))
        var.get('exports').put('isEmpty', var.get('isEmpty'))
        var.get('exports').put('has', var.get('has'))
        var.get('exports').put('cmpU', var.get('cmpU'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eqU', var.get('eqU'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('findFirstByU', var.get('findFirstByU'))
        var.get('exports').put('findFirstBy', var.get('findFirstBy'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('toArray', var.get('toArray'))
        var.get('exports').put('toList', var.get('toList'))
        var.get('exports').put('fromArray', var.get('fromArray'))
        var.get('exports').put('keysToArray', var.get('keysToArray'))
        var.get('exports').put('valuesToArray', var.get('valuesToArray'))
        var.get('exports').put('minKey', var.get('minKey'))
        var.get('exports').put('minKeyUndefined', var.get('minKeyUndefined'))
        var.get('exports').put('maxKey', var.get('maxKey'))
        var.get('exports').put('maxKeyUndefined', var.get('maxKeyUndefined'))
        var.get('exports').put('minimum', var.get('minimum'))
        var.get('exports').put('minUndefined', var.get('minUndefined'))
        var.get('exports').put('maximum', var.get('maximum'))
        var.get('exports').put('maxUndefined', var.get('maxUndefined'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getUndefined', var.get('getUndefined'))
        var.get('exports').put('getWithDefault', var.get('getWithDefault'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('remove', var.get('remove'))
        var.get('exports').put('removeMany', var.get('removeMany'))
        var.get('exports').put('set', var.get('set'))
        var.get('exports').put('updateU', var.get('updateU'))
        var.get('exports').put('update', var.get('update'))
        var.get('exports').put('mergeMany', var.get('mergeMany'))
        var.get('exports').put('mergeU', var.get('mergeU'))
        var.get('exports').put('merge', var.get('merge'))
        var.get('exports').put('keepU', var.get('keepU'))
        var.get('exports').put('keep', var.get('keep'))
        var.get('exports').put('partitionU', var.get('partitionU'))
        var.get('exports').put('partition', var.get('partition'))
        var.get('exports').put('split', var.get('split'))
        var.get('exports').put('mapU', var.get('mapU'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('mapWithKeyU', var.get('mapWithKeyU'))
        var.get('exports').put('mapWithKey', var.get('mapWithKey'))
        var.get('exports').put('getData', var.get('getData'))
        var.get('exports').put('getId', var.get('getId'))
        var.get('exports').put('packIdData', var.get('packIdData'))
        var.get('exports').put('checkInvariantInternal', var.get('checkInvariantInternal'))
    PyJs_anonymous_3_._set_name('anonymous')
    @Js
    def PyJs_anonymous_4_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['get', 'mapU', 'exports', 'update', 'map', 'Caml_option', 'Belt_internalAVLtree', 'empty', 'maximum', 'some', 'maxKey', 'toArray', 'minKeyUndefined', 'every', 'keysToArray', 'mapWithKey', 'fromArray', 'splitAuxPivot', 'mergeMany', 'set', 'remove', 'getWithDefault', 'maxUndefined', 'merge', 'everyU', 'mapWithKeyU', 'minKey', 'module', 'updateU', 'size', 'cmpU', 'eq', 'findFirstBy', 'maxKeyUndefined', 'require', 'getExn', 'cmp', 'Curry', 'minUndefined', 'keep', 'partition', 'reduceU', 'valuesToArray', 'removeMany', 'isEmpty', 'has', 'toList', 'minimum', 'checkInvariantInternal', 'forEach', 'someU', 'eqU', 'split', 'getUndefined', 'keepU', 'findFirstByU', 'partitionU', 'removeAux0', 'reduce', 'mergeU', 'forEachU'])
        @Js
        def PyJsHoisted_set_(t, newK, newD, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'newK':newK, 'newD':newD, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'c', 'cmp', 'r', 'v', 'newD', 'newK', 'k', 'l'])
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('k', var.get('t').get('key'))
                var.put('c', var.get('cmp')(var.get('newK'), var.get('k')))
                if PyJsStrictEq(var.get('c'),Js(0.0)):
                    return var.get('Belt_internalAVLtree').callprop('updateValue', var.get('t'), var.get('newD'))
                else:
                    var.put('l', var.get('t').get('left'))
                    var.put('r', var.get('t').get('right'))
                    var.put('v', var.get('t').get('value'))
                    if (var.get('c')<Js(0.0)):
                        return var.get('Belt_internalAVLtree').callprop('bal', var.get('set')(var.get('l'), var.get('newK'), var.get('newD'), var.get('cmp')), var.get('k'), var.get('v'), var.get('r'))
                    else:
                        return var.get('Belt_internalAVLtree').callprop('bal', var.get('l'), var.get('k'), var.get('v'), var.get('set')(var.get('r'), var.get('newK'), var.get('newD'), var.get('cmp')))
            else:
                return var.get('Belt_internalAVLtree').callprop('singleton', var.get('newK'), var.get('newD'))
        PyJsHoisted_set_.func_name = 'set'
        var.put('set', PyJsHoisted_set_)
        @Js
        def PyJsHoisted_updateU_(t, newK, f, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'newK':newK, 'f':f, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'kr', 'l$1', 'r$2', 'll', 'match$1', 'vr', 'c', 'rr', 't', 'cmp', 'r', 'r$1', 'v', 'match', 'newK', 'k', 'l'])
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('k', var.get('t').get('key'))
                var.put('c', var.get('cmp')(var.get('newK'), var.get('k')))
                if PyJsStrictEq(var.get('c'),Js(0.0)):
                    var.put('match', var.get('f')(var.get('Caml_option').callprop('some', var.get('t').get('value'))))
                    if PyJsStrictNeq(var.get('match'),var.get('undefined')):
                        return var.get('Belt_internalAVLtree').callprop('updateValue', var.get('t'), var.get('Caml_option').callprop('valFromOption', var.get('match')))
                    else:
                        var.put('l', var.get('t').get('left'))
                        var.put('r', var.get('t').get('right'))
                        if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                            if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                                var.put('kr', Js({'contents':var.get('r').get('key')}))
                                var.put('vr', Js({'contents':var.get('r').get('value')}))
                                var.put('r$1', var.get('Belt_internalAVLtree').callprop('removeMinAuxWithRef', var.get('r'), var.get('kr'), var.get('vr')))
                                return var.get('Belt_internalAVLtree').callprop('bal', var.get('l'), var.get('kr').get('contents'), var.get('vr').get('contents'), var.get('r$1'))
                            else:
                                return var.get('l')
                        else:
                            return var.get('r')
                else:
                    var.put('l$1', var.get('t').get('left'))
                    var.put('r$2', var.get('t').get('right'))
                    var.put('v', var.get('t').get('value'))
                    if (var.get('c')<Js(0.0)):
                        var.put('ll', var.get('updateU')(var.get('l$1'), var.get('newK'), var.get('f'), var.get('cmp')))
                        if PyJsStrictEq(var.get('l$1'),var.get('ll')):
                            return var.get('t')
                        else:
                            return var.get('Belt_internalAVLtree').callprop('bal', var.get('ll'), var.get('k'), var.get('v'), var.get('r$2'))
                    else:
                        var.put('rr', var.get('updateU')(var.get('r$2'), var.get('newK'), var.get('f'), var.get('cmp')))
                        if PyJsStrictEq(var.get('r$2'),var.get('rr')):
                            return var.get('t')
                        else:
                            return var.get('Belt_internalAVLtree').callprop('bal', var.get('l$1'), var.get('k'), var.get('v'), var.get('rr'))
            else:
                var.put('match$1', var.get('f')(var.get('undefined')))
                if PyJsStrictNeq(var.get('match$1'),var.get('undefined')):
                    return var.get('Belt_internalAVLtree').callprop('singleton', var.get('newK'), var.get('Caml_option').callprop('valFromOption', var.get('match$1')))
                else:
                    return var.get('t')
        PyJsHoisted_updateU_.func_name = 'updateU'
        var.put('updateU', PyJsHoisted_updateU_)
        @Js
        def PyJsHoisted_update_(t, newK, f, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'newK':newK, 'f':f, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 't', 'cmp', 'newK'])
            return var.get('updateU')(var.get('t'), var.get('newK'), var.get('Curry').callprop('__1', var.get('f')), var.get('cmp'))
        PyJsHoisted_update_.func_name = 'update'
        var.put('update', PyJsHoisted_update_)
        @Js
        def PyJsHoisted_removeAux0_(n, x, cmp, this, arguments, var=var):
            var = Scope({'n':n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['kr', 'll', 'vr', 'c', 'rr', 'cmp', 'r', 'v', 'r$1', 'x', 'n', 'l'])
            var.put('l', var.get('n').get('left'))
            var.put('v', var.get('n').get('key'))
            var.put('r', var.get('n').get('right'))
            var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
            if PyJsStrictEq(var.get('c'),Js(0.0)):
                if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                    if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                        var.put('kr', Js({'contents':var.get('r').get('key')}))
                        var.put('vr', Js({'contents':var.get('r').get('value')}))
                        var.put('r$1', var.get('Belt_internalAVLtree').callprop('removeMinAuxWithRef', var.get('r'), var.get('kr'), var.get('vr')))
                        return var.get('Belt_internalAVLtree').callprop('bal', var.get('l'), var.get('kr').get('contents'), var.get('vr').get('contents'), var.get('r$1'))
                    else:
                        return var.get('l')
                else:
                    return var.get('r')
            else:
                if (var.get('c')<Js(0.0)):
                    if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                        var.put('ll', var.get('removeAux0')(var.get('l'), var.get('x'), var.get('cmp')))
                        if PyJsStrictEq(var.get('ll'),var.get('l')):
                            return var.get('n')
                        else:
                            return var.get('Belt_internalAVLtree').callprop('bal', var.get('ll'), var.get('v'), var.get('n').get('value'), var.get('r'))
                    else:
                        return var.get('n')
                else:
                    if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                        var.put('rr', var.get('removeAux0')(var.get('r'), var.get('x'), var.get('cmp')))
                        if PyJsStrictEq(var.get('rr'),var.get('r')):
                            return var.get('n')
                        else:
                            return var.get('Belt_internalAVLtree').callprop('bal', var.get('l'), var.get('v'), var.get('n').get('value'), var.get('rr'))
                    else:
                        return var.get('n')
        PyJsHoisted_removeAux0_.func_name = 'removeAux0'
        var.put('removeAux0', PyJsHoisted_removeAux0_)
        @Js
        def PyJsHoisted_remove_(n, x, cmp, this, arguments, var=var):
            var = Scope({'n':n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'n', 'cmp'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('removeAux0')(var.get('n'), var.get('x'), var.get('cmp'))
            else:
                return var.get(u"null")
        PyJsHoisted_remove_.func_name = 'remove'
        var.put('remove', PyJsHoisted_remove_)
        @Js
        def PyJsHoisted_mergeMany_(h, arr, cmp, this, arguments, var=var):
            var = Scope({'h':h, 'arr':arr, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'cmp', 'i_finish', 'v', 'match', 'h', 'arr', 'i'])
            var.put('len', var.get('arr').get('length'))
            var.put('v', var.get('h'))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('match', var.get('arr').get(var.get('i')))
                    var.put('v', var.get('set')(var.get('v'), var.get('match').get('0'), var.get('match').get('1'), var.get('cmp')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('v')
        PyJsHoisted_mergeMany_.func_name = 'mergeMany'
        var.put('mergeMany', PyJsHoisted_mergeMany_)
        @Js
        def PyJsHoisted_splitAuxPivot_(n, x, pres, cmp, this, arguments, var=var):
            var = Scope({'n':n, 'x':x, 'pres':pres, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['match$1', 'c', 'cmp', 'r', 'v', 'match', 'x', 'n', 'pres', 'd', 'l'])
            var.put('l', var.get('n').get('left'))
            var.put('v', var.get('n').get('key'))
            var.put('d', var.get('n').get('value'))
            var.put('r', var.get('n').get('right'))
            var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
            if PyJsStrictEq(var.get('c'),Js(0.0)):
                var.get('pres').put('contents', var.get('Caml_option').callprop('some', var.get('d')))
                return Js([var.get('l'), var.get('r')])
            else:
                if (var.get('c')<Js(0.0)):
                    if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                        var.put('match', var.get('splitAuxPivot')(var.get('l'), var.get('x'), var.get('pres'), var.get('cmp')))
                        return Js([var.get('match').get('0'), var.get('Belt_internalAVLtree').callprop('join', var.get('match').get('1'), var.get('v'), var.get('d'), var.get('r'))])
                    else:
                        return Js([var.get(u"null"), var.get('n')])
                else:
                    if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                        var.put('match$1', var.get('splitAuxPivot')(var.get('r'), var.get('x'), var.get('pres'), var.get('cmp')))
                        return Js([var.get('Belt_internalAVLtree').callprop('join', var.get('l'), var.get('v'), var.get('d'), var.get('match$1').get('0')), var.get('match$1').get('1')])
                    else:
                        return Js([var.get('n'), var.get(u"null")])
        PyJsHoisted_splitAuxPivot_.func_name = 'splitAuxPivot'
        var.put('splitAuxPivot', PyJsHoisted_splitAuxPivot_)
        @Js
        def PyJsHoisted_split_(n, x, cmp, this, arguments, var=var):
            var = Scope({'n':n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp', 'v', 'x', 'n', 'pres'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('pres', Js({'contents':var.get('undefined')}))
                var.put('v', var.get('splitAuxPivot')(var.get('n'), var.get('x'), var.get('pres'), var.get('cmp')))
                return Js([var.get('v'), var.get('pres').get('contents')])
            else:
                return Js([Js([var.get(u"null"), var.get(u"null")]), var.get('undefined')])
        PyJsHoisted_split_.func_name = 'split'
        var.put('split', PyJsHoisted_split_)
        @Js
        def PyJsHoisted_mergeU_(s1, s2, f, cmp, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'f':f, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['v1', 'newLeft', 'match', 'd2$1', 'd2', 'l2', 'l1', 'r2', 'newD', 'r1', 'newD$1', 'd1', 'match$1', 'cmp', 'd2$2', 'newRight$1', 's1', 'newLeft$1', 'f', 'd1$2', 'v2', 's2', 'newRight', 'd1$1'])
            if PyJsStrictNeq(var.get('s1'),var.get(u"null")):
                if PyJsStrictNeq(var.get('s2'),var.get(u"null")):
                    if (var.get('s1').get('height')>=var.get('s2').get('height')):
                        var.put('l1', var.get('s1').get('left'))
                        var.put('v1', var.get('s1').get('key'))
                        var.put('d1', var.get('s1').get('value'))
                        var.put('r1', var.get('s1').get('right'))
                        var.put('d2', Js({'contents':var.get('undefined')}))
                        var.put('match', var.get('splitAuxPivot')(var.get('s2'), var.get('v1'), var.get('d2'), var.get('cmp')))
                        var.put('d2$1', var.get('d2').get('contents'))
                        var.put('newLeft', var.get('mergeU')(var.get('l1'), var.get('match').get('0'), var.get('f'), var.get('cmp')))
                        var.put('newD', var.get('f')(var.get('v1'), var.get('Caml_option').callprop('some', var.get('d1')), var.get('d2$1')))
                        var.put('newRight', var.get('mergeU')(var.get('r1'), var.get('match').get('1'), var.get('f'), var.get('cmp')))
                        return var.get('Belt_internalAVLtree').callprop('concatOrJoin', var.get('newLeft'), var.get('v1'), var.get('newD'), var.get('newRight'))
                    else:
                        var.put('l2', var.get('s2').get('left'))
                        var.put('v2', var.get('s2').get('key'))
                        var.put('d2$2', var.get('s2').get('value'))
                        var.put('r2', var.get('s2').get('right'))
                        var.put('d1$1', Js({'contents':var.get('undefined')}))
                        var.put('match$1', var.get('splitAuxPivot')(var.get('s1'), var.get('v2'), var.get('d1$1'), var.get('cmp')))
                        var.put('d1$2', var.get('d1$1').get('contents'))
                        var.put('newLeft$1', var.get('mergeU')(var.get('match$1').get('0'), var.get('l2'), var.get('f'), var.get('cmp')))
                        var.put('newD$1', var.get('f')(var.get('v2'), var.get('d1$2'), var.get('Caml_option').callprop('some', var.get('d2$2'))))
                        var.put('newRight$1', var.get('mergeU')(var.get('match$1').get('1'), var.get('r2'), var.get('f'), var.get('cmp')))
                        return var.get('Belt_internalAVLtree').callprop('concatOrJoin', var.get('newLeft$1'), var.get('v2'), var.get('newD$1'), var.get('newRight$1'))
                else:
                    @Js
                    def PyJs_anonymous_5_(k, v, this, arguments, var=var):
                        var = Scope({'k':k, 'v':v, 'this':this, 'arguments':arguments}, var)
                        var.registers(['v', 'k'])
                        return var.get('f')(var.get('k'), var.get('Caml_option').callprop('some', var.get('v')), var.get('undefined'))
                    PyJs_anonymous_5_._set_name('anonymous')
                    return var.get('Belt_internalAVLtree').callprop('keepMapU', var.get('s1'), PyJs_anonymous_5_)
            else:
                if PyJsStrictNeq(var.get('s2'),var.get(u"null")):
                    @Js
                    def PyJs_anonymous_6_(k, v, this, arguments, var=var):
                        var = Scope({'k':k, 'v':v, 'this':this, 'arguments':arguments}, var)
                        var.registers(['v', 'k'])
                        return var.get('f')(var.get('k'), var.get('undefined'), var.get('Caml_option').callprop('some', var.get('v')))
                    PyJs_anonymous_6_._set_name('anonymous')
                    return var.get('Belt_internalAVLtree').callprop('keepMapU', var.get('s2'), PyJs_anonymous_6_)
                else:
                    return var.get(u"null")
        PyJsHoisted_mergeU_.func_name = 'mergeU'
        var.put('mergeU', PyJsHoisted_mergeU_)
        @Js
        def PyJsHoisted_merge_(s1, s2, f, cmp, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'f':f, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['s1', 'f', 'cmp', 's2'])
            return var.get('mergeU')(var.get('s1'), var.get('s2'), var.get('Curry').callprop('__3', var.get('f')), var.get('cmp'))
        PyJsHoisted_merge_.func_name = 'merge'
        var.put('merge', PyJsHoisted_merge_)
        @Js
        def PyJsHoisted_removeMany_(t, keys, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'keys':keys, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 't$1', 't', 'cmp', 'len$1', 'u', 'cmp$1', 'keys', '_i', 'ele', 'i', '_t'])
            var.put('len', var.get('keys').get('length'))
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('_t', var.get('t'))
                var.put('xs', var.get('keys'))
                var.put('_i', Js(0.0))
                var.put('len$1', var.get('len'))
                var.put('cmp$1', var.get('cmp'))
                while Js(True):
                    var.put('i', var.get('_i'))
                    var.put('t$1', var.get('_t'))
                    if (var.get('i')<var.get('len$1')):
                        var.put('ele', var.get('xs').get(var.get('i')))
                        var.put('u', var.get('removeAux0')(var.get('t$1'), var.get('ele'), var.get('cmp$1')))
                        if PyJsStrictNeq(var.get('u'),var.get(u"null")):
                            var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                            var.put('_t', var.get('u'))
                            continue
                        else:
                            return var.get('u')
                    else:
                        return var.get('t$1')
                pass
            else:
                return var.get(u"null")
        PyJsHoisted_removeMany_.func_name = 'removeMany'
        var.put('removeMany', PyJsHoisted_removeMany_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Caml_option', var.get('require')(Js('./caml_option.js')))
        var.put('Belt_internalAVLtree', var.get('require')(Js('./belt_internalAVLtree.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('empty', var.get(u"null"))
        var.put('isEmpty', var.get('Belt_internalAVLtree').get('isEmpty'))
        var.put('has', var.get('Belt_internalAVLtree').get('has'))
        var.put('cmpU', var.get('Belt_internalAVLtree').get('cmpU'))
        var.put('cmp', var.get('Belt_internalAVLtree').get('cmp'))
        var.put('eqU', var.get('Belt_internalAVLtree').get('eqU'))
        var.put('eq', var.get('Belt_internalAVLtree').get('eq'))
        var.put('findFirstByU', var.get('Belt_internalAVLtree').get('findFirstByU'))
        var.put('findFirstBy', var.get('Belt_internalAVLtree').get('findFirstBy'))
        var.put('forEachU', var.get('Belt_internalAVLtree').get('forEachU'))
        var.put('forEach', var.get('Belt_internalAVLtree').get('forEach'))
        var.put('reduceU', var.get('Belt_internalAVLtree').get('reduceU'))
        var.put('reduce', var.get('Belt_internalAVLtree').get('reduce'))
        var.put('everyU', var.get('Belt_internalAVLtree').get('everyU'))
        var.put('every', var.get('Belt_internalAVLtree').get('every'))
        var.put('someU', var.get('Belt_internalAVLtree').get('someU'))
        var.put('some', var.get('Belt_internalAVLtree').get('some'))
        var.put('size', var.get('Belt_internalAVLtree').get('size'))
        var.put('toList', var.get('Belt_internalAVLtree').get('toList'))
        var.put('toArray', var.get('Belt_internalAVLtree').get('toArray'))
        var.put('fromArray', var.get('Belt_internalAVLtree').get('fromArray'))
        var.put('keysToArray', var.get('Belt_internalAVLtree').get('keysToArray'))
        var.put('valuesToArray', var.get('Belt_internalAVLtree').get('valuesToArray'))
        var.put('minKey', var.get('Belt_internalAVLtree').get('minKey'))
        var.put('minKeyUndefined', var.get('Belt_internalAVLtree').get('minKeyUndefined'))
        var.put('maxKey', var.get('Belt_internalAVLtree').get('maxKey'))
        var.put('maxKeyUndefined', var.get('Belt_internalAVLtree').get('maxKeyUndefined'))
        var.put('minimum', var.get('Belt_internalAVLtree').get('minimum'))
        var.put('minUndefined', var.get('Belt_internalAVLtree').get('minUndefined'))
        var.put('maximum', var.get('Belt_internalAVLtree').get('maximum'))
        var.put('maxUndefined', var.get('Belt_internalAVLtree').get('maxUndefined'))
        var.put('get', var.get('Belt_internalAVLtree').get('get'))
        var.put('getUndefined', var.get('Belt_internalAVLtree').get('getUndefined'))
        var.put('getWithDefault', var.get('Belt_internalAVLtree').get('getWithDefault'))
        var.put('getExn', var.get('Belt_internalAVLtree').get('getExn'))
        var.put('checkInvariantInternal', var.get('Belt_internalAVLtree').get('checkInvariantInternal'))
        var.put('keepU', var.get('Belt_internalAVLtree').get('keepSharedU'))
        var.put('keep', var.get('Belt_internalAVLtree').get('keepShared'))
        var.put('partitionU', var.get('Belt_internalAVLtree').get('partitionSharedU'))
        var.put('partition', var.get('Belt_internalAVLtree').get('partitionShared'))
        var.put('mapU', var.get('Belt_internalAVLtree').get('mapU'))
        var.put('map', var.get('Belt_internalAVLtree').get('map'))
        var.put('mapWithKeyU', var.get('Belt_internalAVLtree').get('mapWithKeyU'))
        var.put('mapWithKey', var.get('Belt_internalAVLtree').get('mapWithKey'))
        var.get('exports').put('empty', var.get('empty'))
        var.get('exports').put('isEmpty', var.get('isEmpty'))
        var.get('exports').put('has', var.get('has'))
        var.get('exports').put('cmpU', var.get('cmpU'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eqU', var.get('eqU'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('findFirstByU', var.get('findFirstByU'))
        var.get('exports').put('findFirstBy', var.get('findFirstBy'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('toList', var.get('toList'))
        var.get('exports').put('toArray', var.get('toArray'))
        var.get('exports').put('fromArray', var.get('fromArray'))
        var.get('exports').put('keysToArray', var.get('keysToArray'))
        var.get('exports').put('valuesToArray', var.get('valuesToArray'))
        var.get('exports').put('minKey', var.get('minKey'))
        var.get('exports').put('minKeyUndefined', var.get('minKeyUndefined'))
        var.get('exports').put('maxKey', var.get('maxKey'))
        var.get('exports').put('maxKeyUndefined', var.get('maxKeyUndefined'))
        var.get('exports').put('minimum', var.get('minimum'))
        var.get('exports').put('minUndefined', var.get('minUndefined'))
        var.get('exports').put('maximum', var.get('maximum'))
        var.get('exports').put('maxUndefined', var.get('maxUndefined'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getUndefined', var.get('getUndefined'))
        var.get('exports').put('getWithDefault', var.get('getWithDefault'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('checkInvariantInternal', var.get('checkInvariantInternal'))
        var.get('exports').put('remove', var.get('remove'))
        var.get('exports').put('removeMany', var.get('removeMany'))
        var.get('exports').put('set', var.get('set'))
        var.get('exports').put('updateU', var.get('updateU'))
        var.get('exports').put('update', var.get('update'))
        var.get('exports').put('mergeU', var.get('mergeU'))
        var.get('exports').put('merge', var.get('merge'))
        var.get('exports').put('mergeMany', var.get('mergeMany'))
        var.get('exports').put('keepU', var.get('keepU'))
        var.get('exports').put('keep', var.get('keep'))
        var.get('exports').put('partitionU', var.get('partitionU'))
        var.get('exports').put('partition', var.get('partition'))
        var.get('exports').put('split', var.get('split'))
        var.get('exports').put('mapU', var.get('mapU'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('mapWithKeyU', var.get('mapWithKeyU'))
        var.get('exports').put('mapWithKey', var.get('mapWithKey'))
    PyJs_anonymous_4_._set_name('anonymous')
    @Js
    def PyJs_anonymous_7_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['mapU', 'exports', 'mapWithDefault', 'map', 'Caml_option', 'isSome', 'getWithDefault', 'flatMap', 'module', 'cmpU', 'eq', 'flatMapU', 'require', 'getExn', 'mapWithDefaultU', 'cmp', 'Curry', 'forEach', 'eqU', 'isNone', 'forEachU'])
        @Js
        def PyJsHoisted_forEachU_(opt, f, this, arguments, var=var):
            var = Scope({'opt':opt, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'opt'])
            if PyJsStrictNeq(var.get('opt'),var.get('undefined')):
                return var.get('f')(var.get('Caml_option').callprop('valFromOption', var.get('opt')))
            else:
                return Js(0.0)
        PyJsHoisted_forEachU_.func_name = 'forEachU'
        var.put('forEachU', PyJsHoisted_forEachU_)
        @Js
        def PyJsHoisted_forEach_(opt, f, this, arguments, var=var):
            var = Scope({'opt':opt, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'opt'])
            return var.get('forEachU')(var.get('opt'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_forEach_.func_name = 'forEach'
        var.put('forEach', PyJsHoisted_forEach_)
        @Js
        def PyJsHoisted_getExn_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            if PyJsStrictNeq(var.get('param'),var.get('undefined')):
                return var.get('Caml_option').callprop('valFromOption', var.get('param'))
            else:
                PyJsTempException = JsToPyException(var.get('Error').create(Js('getExn')))
                raise PyJsTempException
        PyJsHoisted_getExn_.func_name = 'getExn'
        var.put('getExn', PyJsHoisted_getExn_)
        @Js
        def PyJsHoisted_mapWithDefaultU_(opt, PyJsArg_242464656661756c74_, f, this, arguments, var=var):
            var = Scope({'opt':opt, '$$default':PyJsArg_242464656661756c74_, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', '$$default', 'opt'])
            if PyJsStrictNeq(var.get('opt'),var.get('undefined')):
                return var.get('f')(var.get('Caml_option').callprop('valFromOption', var.get('opt')))
            else:
                return var.get('$$default')
        PyJsHoisted_mapWithDefaultU_.func_name = 'mapWithDefaultU'
        var.put('mapWithDefaultU', PyJsHoisted_mapWithDefaultU_)
        @Js
        def PyJsHoisted_mapWithDefault_(opt, PyJsArg_242464656661756c74_, f, this, arguments, var=var):
            var = Scope({'opt':opt, '$$default':PyJsArg_242464656661756c74_, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', '$$default', 'opt'])
            return var.get('mapWithDefaultU')(var.get('opt'), var.get('$$default'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_mapWithDefault_.func_name = 'mapWithDefault'
        var.put('mapWithDefault', PyJsHoisted_mapWithDefault_)
        @Js
        def PyJsHoisted_mapU_(opt, f, this, arguments, var=var):
            var = Scope({'opt':opt, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'opt'])
            if PyJsStrictNeq(var.get('opt'),var.get('undefined')):
                return var.get('Caml_option').callprop('some', var.get('f')(var.get('Caml_option').callprop('valFromOption', var.get('opt'))))
        PyJsHoisted_mapU_.func_name = 'mapU'
        var.put('mapU', PyJsHoisted_mapU_)
        @Js
        def PyJsHoisted_map_(opt, f, this, arguments, var=var):
            var = Scope({'opt':opt, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'opt'])
            return var.get('mapU')(var.get('opt'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_map_.func_name = 'map'
        var.put('map', PyJsHoisted_map_)
        @Js
        def PyJsHoisted_flatMapU_(opt, f, this, arguments, var=var):
            var = Scope({'opt':opt, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'opt'])
            if PyJsStrictNeq(var.get('opt'),var.get('undefined')):
                return var.get('f')(var.get('Caml_option').callprop('valFromOption', var.get('opt')))
        PyJsHoisted_flatMapU_.func_name = 'flatMapU'
        var.put('flatMapU', PyJsHoisted_flatMapU_)
        @Js
        def PyJsHoisted_flatMap_(opt, f, this, arguments, var=var):
            var = Scope({'opt':opt, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'opt'])
            return var.get('flatMapU')(var.get('opt'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_flatMap_.func_name = 'flatMap'
        var.put('flatMap', PyJsHoisted_flatMap_)
        @Js
        def PyJsHoisted_getWithDefault_(opt, PyJsArg_242464656661756c74_, this, arguments, var=var):
            var = Scope({'opt':opt, '$$default':PyJsArg_242464656661756c74_, 'this':this, 'arguments':arguments}, var)
            var.registers(['$$default', 'opt'])
            if PyJsStrictNeq(var.get('opt'),var.get('undefined')):
                return var.get('Caml_option').callprop('valFromOption', var.get('opt'))
            else:
                return var.get('$$default')
        PyJsHoisted_getWithDefault_.func_name = 'getWithDefault'
        var.put('getWithDefault', PyJsHoisted_getWithDefault_)
        @Js
        def PyJsHoisted_isSome_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return PyJsStrictNeq(var.get('param'),var.get('undefined'))
        PyJsHoisted_isSome_.func_name = 'isSome'
        var.put('isSome', PyJsHoisted_isSome_)
        @Js
        def PyJsHoisted_isNone_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return PyJsStrictEq(var.get('x'),var.get('undefined'))
        PyJsHoisted_isNone_.func_name = 'isNone'
        var.put('isNone', PyJsHoisted_isNone_)
        @Js
        def PyJsHoisted_eqU_(a, b, f, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'f'])
            if PyJsStrictNeq(var.get('a'),var.get('undefined')):
                if PyJsStrictNeq(var.get('b'),var.get('undefined')):
                    return var.get('f')(var.get('Caml_option').callprop('valFromOption', var.get('a')), var.get('Caml_option').callprop('valFromOption', var.get('b')))
                else:
                    return Js(False)
            else:
                return PyJsStrictEq(var.get('b'),var.get('undefined'))
        PyJsHoisted_eqU_.func_name = 'eqU'
        var.put('eqU', PyJsHoisted_eqU_)
        @Js
        def PyJsHoisted_eq_(a, b, f, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'f'])
            return var.get('eqU')(var.get('a'), var.get('b'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_cmpU_(a, b, f, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'f'])
            if PyJsStrictNeq(var.get('a'),var.get('undefined')):
                if PyJsStrictNeq(var.get('b'),var.get('undefined')):
                    return var.get('f')(var.get('Caml_option').callprop('valFromOption', var.get('a')), var.get('Caml_option').callprop('valFromOption', var.get('b')))
                else:
                    return Js(1.0)
            else:
                if PyJsStrictNeq(var.get('b'),var.get('undefined')):
                    return (-Js(1.0))
                else:
                    return Js(0.0)
        PyJsHoisted_cmpU_.func_name = 'cmpU'
        var.put('cmpU', PyJsHoisted_cmpU_)
        @Js
        def PyJsHoisted_cmp_(a, b, f, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'f'])
            return var.get('cmpU')(var.get('a'), var.get('b'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_cmp_.func_name = 'cmp'
        var.put('cmp', PyJsHoisted_cmp_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Caml_option', var.get('require')(Js('./caml_option.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('mapWithDefaultU', var.get('mapWithDefaultU'))
        var.get('exports').put('mapWithDefault', var.get('mapWithDefault'))
        var.get('exports').put('mapU', var.get('mapU'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('flatMapU', var.get('flatMapU'))
        var.get('exports').put('flatMap', var.get('flatMap'))
        var.get('exports').put('getWithDefault', var.get('getWithDefault'))
        var.get('exports').put('isSome', var.get('isSome'))
        var.get('exports').put('isNone', var.get('isNone'))
        var.get('exports').put('eqU', var.get('eqU'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('cmpU', var.get('cmpU'))
        var.get('exports').put('cmp', var.get('cmp'))
    PyJs_anonymous_7_._set_name('anonymous')
    @Js
    def PyJs_anonymous_8_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['get', '$$String', 'exports', 'getId', 'intersect', 'maximum', 'some', 'Dict', 'toArray', 'every', 'getData', 'fromArray', 'Int', 'mergeMany', 'fromSortedArrayUnsafe', 'remove', 'maxUndefined', 'everyU', 'module', 'size', 'eq', 'require', 'add', 'subset', 'getExn', 'cmp', 'Curry', 'minUndefined', 'make', 'keep', 'partition', 'reduceU', 'removeMany', 'Belt_SetDict', 'isEmpty', 'toList', 'has', 'minimum', 'checkInvariantInternal', 'forEach', 'union', 'someU', 'diff', 'split', 'getUndefined', 'keepU', 'partitionU', 'reduce', 'packIdData', 'forEachU'])
        @Js
        def PyJsHoisted_fromArray_(data, id, this, arguments, var=var):
            var = Scope({'data':data, 'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id', 'data', 'cmp'])
            var.put('cmp', var.get('id').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_SetDict').callprop('fromArray', var.get('data'), var.get('cmp'))})
        PyJsHoisted_fromArray_.func_name = 'fromArray'
        var.put('fromArray', PyJsHoisted_fromArray_)
        @Js
        def PyJsHoisted_remove_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'cmp', 'newData', 'm', 'data'])
            var.put('cmp', var.get('m').get('cmp'))
            var.put('data', var.get('m').get('data'))
            var.put('newData', var.get('Belt_SetDict').callprop('remove', var.get('data'), var.get('e'), var.get('cmp')))
            if PyJsStrictEq(var.get('newData'),var.get('data')):
                return var.get('m')
            else:
                return Js({'cmp':var.get('cmp'),'data':var.get('newData')})
        PyJsHoisted_remove_.func_name = 'remove'
        var.put('remove', PyJsHoisted_remove_)
        @Js
        def PyJsHoisted_add_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'cmp', 'newData', 'm', 'data'])
            var.put('cmp', var.get('m').get('cmp'))
            var.put('data', var.get('m').get('data'))
            var.put('newData', var.get('Belt_SetDict').callprop('add', var.get('data'), var.get('e'), var.get('cmp')))
            if PyJsStrictEq(var.get('newData'),var.get('data')):
                return var.get('m')
            else:
                return Js({'cmp':var.get('cmp'),'data':var.get('newData')})
        PyJsHoisted_add_.func_name = 'add'
        var.put('add', PyJsHoisted_add_)
        @Js
        def PyJsHoisted_mergeMany_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'm', 'cmp'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_SetDict').callprop('mergeMany', var.get('m').get('data'), var.get('e'), var.get('cmp'))})
        PyJsHoisted_mergeMany_.func_name = 'mergeMany'
        var.put('mergeMany', PyJsHoisted_mergeMany_)
        @Js
        def PyJsHoisted_removeMany_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'm', 'cmp'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_SetDict').callprop('removeMany', var.get('m').get('data'), var.get('e'), var.get('cmp'))})
        PyJsHoisted_removeMany_.func_name = 'removeMany'
        var.put('removeMany', PyJsHoisted_removeMany_)
        @Js
        def PyJsHoisted_union_(m, n, this, arguments, var=var):
            var = Scope({'m':m, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'cmp', 'n'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_SetDict').callprop('union', var.get('m').get('data'), var.get('n').get('data'), var.get('cmp'))})
        PyJsHoisted_union_.func_name = 'union'
        var.put('union', PyJsHoisted_union_)
        @Js
        def PyJsHoisted_intersect_(m, n, this, arguments, var=var):
            var = Scope({'m':m, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'cmp', 'n'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_SetDict').callprop('intersect', var.get('m').get('data'), var.get('n').get('data'), var.get('cmp'))})
        PyJsHoisted_intersect_.func_name = 'intersect'
        var.put('intersect', PyJsHoisted_intersect_)
        @Js
        def PyJsHoisted_diff_(m, n, this, arguments, var=var):
            var = Scope({'m':m, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'cmp', 'n'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp'),'data':var.get('Belt_SetDict').callprop('diff', var.get('m').get('data'), var.get('n').get('data'), var.get('cmp'))})
        PyJsHoisted_diff_.func_name = 'diff'
        var.put('diff', PyJsHoisted_diff_)
        @Js
        def PyJsHoisted_subset_(m, n, this, arguments, var=var):
            var = Scope({'m':m, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'cmp', 'n'])
            var.put('cmp', var.get('m').get('cmp'))
            return var.get('Belt_SetDict').callprop('subset', var.get('m').get('data'), var.get('n').get('data'), var.get('cmp'))
        PyJsHoisted_subset_.func_name = 'subset'
        var.put('subset', PyJsHoisted_subset_)
        @Js
        def PyJsHoisted_split_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'match$1', 'cmp', 'm', 'match'])
            var.put('cmp', var.get('m').get('cmp'))
            var.put('match', var.get('Belt_SetDict').callprop('split', var.get('m').get('data'), var.get('e'), var.get('cmp')))
            var.put('match$1', var.get('match').get('0'))
            return Js([Js([Js({'cmp':var.get('cmp'),'data':var.get('match$1').get('0')}), Js({'cmp':var.get('cmp'),'data':var.get('match$1').get('1')})]), var.get('match').get('1')])
        PyJsHoisted_split_.func_name = 'split'
        var.put('split', PyJsHoisted_split_)
        @Js
        def PyJsHoisted_make_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return Js({'cmp':var.get('id').get('cmp'),'data':var.get('Belt_SetDict').get('empty')})
        PyJsHoisted_make_.func_name = 'make'
        var.put('make', PyJsHoisted_make_)
        @Js
        def PyJsHoisted_isEmpty_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('isEmpty', var.get('m').get('data'))
        PyJsHoisted_isEmpty_.func_name = 'isEmpty'
        var.put('isEmpty', PyJsHoisted_isEmpty_)
        @Js
        def PyJsHoisted_cmp_(m, n, this, arguments, var=var):
            var = Scope({'m':m, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp$1', 'm', 'n'])
            var.put('cmp$1', var.get('m').get('cmp'))
            return var.get('Belt_SetDict').callprop('cmp', var.get('m').get('data'), var.get('n').get('data'), var.get('cmp$1'))
        PyJsHoisted_cmp_.func_name = 'cmp'
        var.put('cmp', PyJsHoisted_cmp_)
        @Js
        def PyJsHoisted_eq_(m, n, this, arguments, var=var):
            var = Scope({'m':m, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'n'])
            return var.get('Belt_SetDict').callprop('eq', var.get('m').get('data'), var.get('n').get('data'), var.get('m').get('cmp'))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_forEachU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_SetDict').callprop('forEachU', var.get('m').get('data'), var.get('f'))
        PyJsHoisted_forEachU_.func_name = 'forEachU'
        var.put('forEachU', PyJsHoisted_forEachU_)
        @Js
        def PyJsHoisted_forEach_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_SetDict').callprop('forEachU', var.get('m').get('data'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_forEach_.func_name = 'forEach'
        var.put('forEach', PyJsHoisted_forEach_)
        @Js
        def PyJsHoisted_reduceU_(m, acc, f, this, arguments, var=var):
            var = Scope({'m':m, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', 'f', 'm'])
            return var.get('Belt_SetDict').callprop('reduceU', var.get('m').get('data'), var.get('acc'), var.get('f'))
        PyJsHoisted_reduceU_.func_name = 'reduceU'
        var.put('reduceU', PyJsHoisted_reduceU_)
        @Js
        def PyJsHoisted_reduce_(m, acc, f, this, arguments, var=var):
            var = Scope({'m':m, 'acc':acc, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', 'f', 'm'])
            return var.get('reduceU')(var.get('m'), var.get('acc'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_reduce_.func_name = 'reduce'
        var.put('reduce', PyJsHoisted_reduce_)
        @Js
        def PyJsHoisted_everyU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_SetDict').callprop('everyU', var.get('m').get('data'), var.get('f'))
        PyJsHoisted_everyU_.func_name = 'everyU'
        var.put('everyU', PyJsHoisted_everyU_)
        @Js
        def PyJsHoisted_every_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_SetDict').callprop('everyU', var.get('m').get('data'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_every_.func_name = 'every'
        var.put('every', PyJsHoisted_every_)
        @Js
        def PyJsHoisted_someU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_SetDict').callprop('someU', var.get('m').get('data'), var.get('f'))
        PyJsHoisted_someU_.func_name = 'someU'
        var.put('someU', PyJsHoisted_someU_)
        @Js
        def PyJsHoisted_some_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('Belt_SetDict').callprop('someU', var.get('m').get('data'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_some_.func_name = 'some'
        var.put('some', PyJsHoisted_some_)
        @Js
        def PyJsHoisted_keepU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return Js({'cmp':var.get('m').get('cmp'),'data':var.get('Belt_SetDict').callprop('keepU', var.get('m').get('data'), var.get('f'))})
        PyJsHoisted_keepU_.func_name = 'keepU'
        var.put('keepU', PyJsHoisted_keepU_)
        @Js
        def PyJsHoisted_keep_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('keepU')(var.get('m'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_keep_.func_name = 'keep'
        var.put('keep', PyJsHoisted_keep_)
        @Js
        def PyJsHoisted_partitionU_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm', 'match', 'cmp'])
            var.put('match', var.get('Belt_SetDict').callprop('partitionU', var.get('m').get('data'), var.get('f')))
            var.put('cmp', var.get('m').get('cmp'))
            return Js([Js({'cmp':var.get('cmp'),'data':var.get('match').get('0')}), Js({'cmp':var.get('cmp'),'data':var.get('match').get('1')})])
        PyJsHoisted_partitionU_.func_name = 'partitionU'
        var.put('partitionU', PyJsHoisted_partitionU_)
        @Js
        def PyJsHoisted_partition_(m, f, this, arguments, var=var):
            var = Scope({'m':m, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'm'])
            return var.get('partitionU')(var.get('m'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_partition_.func_name = 'partition'
        var.put('partition', PyJsHoisted_partition_)
        @Js
        def PyJsHoisted_size_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('size', var.get('m').get('data'))
        PyJsHoisted_size_.func_name = 'size'
        var.put('size', PyJsHoisted_size_)
        @Js
        def PyJsHoisted_toList_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('toList', var.get('m').get('data'))
        PyJsHoisted_toList_.func_name = 'toList'
        var.put('toList', PyJsHoisted_toList_)
        @Js
        def PyJsHoisted_toArray_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('toArray', var.get('m').get('data'))
        PyJsHoisted_toArray_.func_name = 'toArray'
        var.put('toArray', PyJsHoisted_toArray_)
        @Js
        def PyJsHoisted_minimum_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('minimum', var.get('m').get('data'))
        PyJsHoisted_minimum_.func_name = 'minimum'
        var.put('minimum', PyJsHoisted_minimum_)
        @Js
        def PyJsHoisted_minUndefined_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('minUndefined', var.get('m').get('data'))
        PyJsHoisted_minUndefined_.func_name = 'minUndefined'
        var.put('minUndefined', PyJsHoisted_minUndefined_)
        @Js
        def PyJsHoisted_maximum_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('maximum', var.get('m').get('data'))
        PyJsHoisted_maximum_.func_name = 'maximum'
        var.put('maximum', PyJsHoisted_maximum_)
        @Js
        def PyJsHoisted_maxUndefined_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            return var.get('Belt_SetDict').callprop('maxUndefined', var.get('m').get('data'))
        PyJsHoisted_maxUndefined_.func_name = 'maxUndefined'
        var.put('maxUndefined', PyJsHoisted_maxUndefined_)
        @Js
        def PyJsHoisted_get_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'm'])
            return var.get('Belt_SetDict').callprop('get', var.get('m').get('data'), var.get('e'), var.get('m').get('cmp'))
        PyJsHoisted_get_.func_name = 'get'
        var.put('get', PyJsHoisted_get_)
        @Js
        def PyJsHoisted_getUndefined_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'm'])
            return var.get('Belt_SetDict').callprop('getUndefined', var.get('m').get('data'), var.get('e'), var.get('m').get('cmp'))
        PyJsHoisted_getUndefined_.func_name = 'getUndefined'
        var.put('getUndefined', PyJsHoisted_getUndefined_)
        @Js
        def PyJsHoisted_getExn_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'm'])
            return var.get('Belt_SetDict').callprop('getExn', var.get('m').get('data'), var.get('e'), var.get('m').get('cmp'))
        PyJsHoisted_getExn_.func_name = 'getExn'
        var.put('getExn', PyJsHoisted_getExn_)
        @Js
        def PyJsHoisted_has_(m, e, this, arguments, var=var):
            var = Scope({'m':m, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'm'])
            return var.get('Belt_SetDict').callprop('has', var.get('m').get('data'), var.get('e'), var.get('m').get('cmp'))
        PyJsHoisted_has_.func_name = 'has'
        var.put('has', PyJsHoisted_has_)
        @Js
        def PyJsHoisted_fromSortedArrayUnsafe_(xs, id, this, arguments, var=var):
            var = Scope({'xs':xs, 'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['xs', 'id'])
            return Js({'cmp':var.get('id').get('cmp'),'data':var.get('Belt_SetDict').callprop('fromSortedArrayUnsafe', var.get('xs'))})
        PyJsHoisted_fromSortedArrayUnsafe_.func_name = 'fromSortedArrayUnsafe'
        var.put('fromSortedArrayUnsafe', PyJsHoisted_fromSortedArrayUnsafe_)
        @Js
        def PyJsHoisted_getData_(prim, this, arguments, var=var):
            var = Scope({'prim':prim, 'this':this, 'arguments':arguments}, var)
            var.registers(['prim'])
            return var.get('prim').get('data')
        PyJsHoisted_getData_.func_name = 'getData'
        var.put('getData', PyJsHoisted_getData_)
        @Js
        def PyJsHoisted_getId_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'cmp'])
            var.put('cmp', var.get('m').get('cmp'))
            return Js({'cmp':var.get('cmp')})
        PyJsHoisted_getId_.func_name = 'getId'
        var.put('getId', PyJsHoisted_getId_)
        @Js
        def PyJsHoisted_packIdData_(id, data, this, arguments, var=var):
            var = Scope({'id':id, 'data':data, 'this':this, 'arguments':arguments}, var)
            var.registers(['id', 'data'])
            return Js({'cmp':var.get('id').get('cmp'),'data':var.get('data')})
        PyJsHoisted_packIdData_.func_name = 'packIdData'
        var.put('packIdData', PyJsHoisted_packIdData_)
        @Js
        def PyJsHoisted_checkInvariantInternal_(d, this, arguments, var=var):
            var = Scope({'d':d, 'this':this, 'arguments':arguments}, var)
            var.registers(['d'])
            return var.get('Belt_SetDict').callprop('checkInvariantInternal', var.get('d').get('data'))
        PyJsHoisted_checkInvariantInternal_.func_name = 'checkInvariantInternal'
        var.put('checkInvariantInternal', PyJsHoisted_checkInvariantInternal_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Belt_SetDict', var.get('require')(Js('./belt_SetDict.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('Int', Js(0.0))
        var.put('$$String', Js(0.0))
        var.put('Dict', Js(0.0))
        var.get('exports').put('Int', var.get('Int'))
        var.get('exports').put('$$String', var.get('$$String'))
        var.get('exports').put('Dict', var.get('Dict'))
        var.get('exports').put('make', var.get('make'))
        var.get('exports').put('fromArray', var.get('fromArray'))
        var.get('exports').put('fromSortedArrayUnsafe', var.get('fromSortedArrayUnsafe'))
        var.get('exports').put('isEmpty', var.get('isEmpty'))
        var.get('exports').put('has', var.get('has'))
        var.get('exports').put('add', var.get('add'))
        var.get('exports').put('mergeMany', var.get('mergeMany'))
        var.get('exports').put('remove', var.get('remove'))
        var.get('exports').put('removeMany', var.get('removeMany'))
        var.get('exports').put('union', var.get('union'))
        var.get('exports').put('intersect', var.get('intersect'))
        var.get('exports').put('diff', var.get('diff'))
        var.get('exports').put('subset', var.get('subset'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('keepU', var.get('keepU'))
        var.get('exports').put('keep', var.get('keep'))
        var.get('exports').put('partitionU', var.get('partitionU'))
        var.get('exports').put('partition', var.get('partition'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('toArray', var.get('toArray'))
        var.get('exports').put('toList', var.get('toList'))
        var.get('exports').put('minimum', var.get('minimum'))
        var.get('exports').put('minUndefined', var.get('minUndefined'))
        var.get('exports').put('maximum', var.get('maximum'))
        var.get('exports').put('maxUndefined', var.get('maxUndefined'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getUndefined', var.get('getUndefined'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('split', var.get('split'))
        var.get('exports').put('checkInvariantInternal', var.get('checkInvariantInternal'))
        var.get('exports').put('getData', var.get('getData'))
        var.get('exports').put('getId', var.get('getId'))
        var.get('exports').put('packIdData', var.get('packIdData'))
    PyJs_anonymous_8_._set_name('anonymous')
    @Js
    def PyJs_anonymous_9_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['get', 'exports', 'splitAuxNoPivot', 'intersect', 'empty', 'maximum', 'some', 'toArray', 'every', 'fromArray', 'splitAuxPivot', 'mergeMany', 'fromSortedArrayUnsafe', 'remove', 'maxUndefined', 'everyU', 'module', 'size', 'eq', 'require', 'add', 'subset', 'getExn', 'cmp', 'minUndefined', 'keep', 'partition', 'reduceU', 'removeMany', 'isEmpty', 'Belt_internalAVLset', 'has', 'toList', 'minimum', 'checkInvariantInternal', 'forEach', 'union', 'someU', 'diff', 'split', 'getUndefined', 'keepU', 'partitionU', 'reduce', 'forEachU'])
        @Js
        def PyJsHoisted_add_(t, x, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 't', 'c', 'rr', 'cmp', 'r', 'x', 'k', 'l'])
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('k', var.get('t').get('value'))
                var.put('c', var.get('cmp')(var.get('x'), var.get('k')))
                if PyJsStrictEq(var.get('c'),Js(0.0)):
                    return var.get('t')
                else:
                    var.put('l', var.get('t').get('left'))
                    var.put('r', var.get('t').get('right'))
                    if (var.get('c')<Js(0.0)):
                        var.put('ll', var.get('add')(var.get('l'), var.get('x'), var.get('cmp')))
                        if PyJsStrictEq(var.get('ll'),var.get('l')):
                            return var.get('t')
                        else:
                            return var.get('Belt_internalAVLset').callprop('bal', var.get('ll'), var.get('k'), var.get('r'))
                    else:
                        var.put('rr', var.get('add')(var.get('r'), var.get('x'), var.get('cmp')))
                        if PyJsStrictEq(var.get('rr'),var.get('r')):
                            return var.get('t')
                        else:
                            return var.get('Belt_internalAVLset').callprop('bal', var.get('l'), var.get('k'), var.get('rr'))
            else:
                return var.get('Belt_internalAVLset').callprop('singleton', var.get('x'))
        PyJsHoisted_add_.func_name = 'add'
        var.put('add', PyJsHoisted_add_)
        @Js
        def PyJsHoisted_remove_(t, x, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 't', 'v$1', 'c', 'rr', 'cmp', 'r', 'v', 'r$1', 'x', 'l'])
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('l', var.get('t').get('left'))
                var.put('v', var.get('t').get('value'))
                var.put('r', var.get('t').get('right'))
                var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                if PyJsStrictEq(var.get('c'),Js(0.0)):
                    if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                        if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                            var.put('v$1', Js({'contents':var.get('r').get('value')}))
                            var.put('r$1', var.get('Belt_internalAVLset').callprop('removeMinAuxWithRef', var.get('r'), var.get('v$1')))
                            return var.get('Belt_internalAVLset').callprop('bal', var.get('l'), var.get('v$1').get('contents'), var.get('r$1'))
                        else:
                            return var.get('l')
                    else:
                        return var.get('r')
                else:
                    if (var.get('c')<Js(0.0)):
                        var.put('ll', var.get('remove')(var.get('l'), var.get('x'), var.get('cmp')))
                        if PyJsStrictEq(var.get('ll'),var.get('l')):
                            return var.get('t')
                        else:
                            return var.get('Belt_internalAVLset').callprop('bal', var.get('ll'), var.get('v'), var.get('r'))
                    else:
                        var.put('rr', var.get('remove')(var.get('r'), var.get('x'), var.get('cmp')))
                        if PyJsStrictEq(var.get('rr'),var.get('r')):
                            return var.get('t')
                        else:
                            return var.get('Belt_internalAVLset').callprop('bal', var.get('l'), var.get('v'), var.get('rr'))
            else:
                return var.get('t')
        PyJsHoisted_remove_.func_name = 'remove'
        var.put('remove', PyJsHoisted_remove_)
        @Js
        def PyJsHoisted_mergeMany_(h, arr, cmp, this, arguments, var=var):
            var = Scope({'h':h, 'arr':arr, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'cmp', 'i_finish', 'v', 'h', 'key', 'arr', 'i'])
            var.put('len', var.get('arr').get('length'))
            var.put('v', var.get('h'))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('key', var.get('arr').get(var.get('i')))
                    var.put('v', var.get('add')(var.get('v'), var.get('key'), var.get('cmp')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('v')
        PyJsHoisted_mergeMany_.func_name = 'mergeMany'
        var.put('mergeMany', PyJsHoisted_mergeMany_)
        @Js
        def PyJsHoisted_removeMany_(h, arr, cmp, this, arguments, var=var):
            var = Scope({'h':h, 'arr':arr, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'cmp', 'i_finish', 'v', 'h', 'key', 'arr', 'i'])
            var.put('len', var.get('arr').get('length'))
            var.put('v', var.get('h'))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('key', var.get('arr').get(var.get('i')))
                    var.put('v', var.get('remove')(var.get('v'), var.get('key'), var.get('cmp')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('v')
        PyJsHoisted_removeMany_.func_name = 'removeMany'
        var.put('removeMany', PyJsHoisted_removeMany_)
        @Js
        def PyJsHoisted_splitAuxNoPivot_(cmp, n, x, this, arguments, var=var):
            var = Scope({'cmp':cmp, 'n':n, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['match$1', 'c', 'cmp', 'r', 'v', 'match', 'x', 'n', 'l'])
            var.put('l', var.get('n').get('left'))
            var.put('v', var.get('n').get('value'))
            var.put('r', var.get('n').get('right'))
            var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
            if PyJsStrictEq(var.get('c'),Js(0.0)):
                return Js([var.get('l'), var.get('r')])
            else:
                if (var.get('c')<Js(0.0)):
                    if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                        var.put('match', var.get('splitAuxNoPivot')(var.get('cmp'), var.get('l'), var.get('x')))
                        return Js([var.get('match').get('0'), var.get('Belt_internalAVLset').callprop('joinShared', var.get('match').get('1'), var.get('v'), var.get('r'))])
                    else:
                        return Js([var.get(u"null"), var.get('n')])
                else:
                    if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                        var.put('match$1', var.get('splitAuxNoPivot')(var.get('cmp'), var.get('r'), var.get('x')))
                        return Js([var.get('Belt_internalAVLset').callprop('joinShared', var.get('l'), var.get('v'), var.get('match$1').get('0')), var.get('match$1').get('1')])
                    else:
                        return Js([var.get('n'), var.get(u"null")])
        PyJsHoisted_splitAuxNoPivot_.func_name = 'splitAuxNoPivot'
        var.put('splitAuxNoPivot', PyJsHoisted_splitAuxNoPivot_)
        @Js
        def PyJsHoisted_splitAuxPivot_(cmp, n, x, pres, this, arguments, var=var):
            var = Scope({'cmp':cmp, 'n':n, 'x':x, 'pres':pres, 'this':this, 'arguments':arguments}, var)
            var.registers(['match$1', 'c', 'cmp', 'r', 'v', 'match', 'x', 'n', 'pres', 'l'])
            var.put('l', var.get('n').get('left'))
            var.put('v', var.get('n').get('value'))
            var.put('r', var.get('n').get('right'))
            var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
            if PyJsStrictEq(var.get('c'),Js(0.0)):
                var.get('pres').put('contents', Js(True))
                return Js([var.get('l'), var.get('r')])
            else:
                if (var.get('c')<Js(0.0)):
                    if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                        var.put('match', var.get('splitAuxPivot')(var.get('cmp'), var.get('l'), var.get('x'), var.get('pres')))
                        return Js([var.get('match').get('0'), var.get('Belt_internalAVLset').callprop('joinShared', var.get('match').get('1'), var.get('v'), var.get('r'))])
                    else:
                        return Js([var.get(u"null"), var.get('n')])
                else:
                    if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                        var.put('match$1', var.get('splitAuxPivot')(var.get('cmp'), var.get('r'), var.get('x'), var.get('pres')))
                        return Js([var.get('Belt_internalAVLset').callprop('joinShared', var.get('l'), var.get('v'), var.get('match$1').get('0')), var.get('match$1').get('1')])
                    else:
                        return Js([var.get('n'), var.get(u"null")])
        PyJsHoisted_splitAuxPivot_.func_name = 'splitAuxPivot'
        var.put('splitAuxPivot', PyJsHoisted_splitAuxPivot_)
        @Js
        def PyJsHoisted_split_(t, x, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'cmp', 'v', 'x', 'pres'])
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('pres', Js({'contents':Js(False)}))
                var.put('v', var.get('splitAuxPivot')(var.get('cmp'), var.get('t'), var.get('x'), var.get('pres')))
                return Js([var.get('v'), var.get('pres').get('contents')])
            else:
                return Js([Js([var.get(u"null"), var.get(u"null")]), Js(False)])
        PyJsHoisted_split_.func_name = 'split'
        var.put('split', PyJsHoisted_split_)
        @Js
        def PyJsHoisted_union_(s1, s2, cmp, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['h1', 'l2', 'match$1', 'l1', 'r2', 'cmp', 'v2', 's2', 'match', 's1', 'r1', 'v1', 'h2'])
            if PyJsStrictNeq(var.get('s1'),var.get(u"null")):
                if PyJsStrictNeq(var.get('s2'),var.get(u"null")):
                    var.put('h1', var.get('s1').get('height'))
                    var.put('h2', var.get('s2').get('height'))
                    if (var.get('h1')>=var.get('h2')):
                        if PyJsStrictEq(var.get('h2'),Js(1.0)):
                            return var.get('add')(var.get('s1'), var.get('s2').get('value'), var.get('cmp'))
                        else:
                            var.put('l1', var.get('s1').get('left'))
                            var.put('v1', var.get('s1').get('value'))
                            var.put('r1', var.get('s1').get('right'))
                            var.put('match', var.get('splitAuxNoPivot')(var.get('cmp'), var.get('s2'), var.get('v1')))
                            return var.get('Belt_internalAVLset').callprop('joinShared', var.get('union')(var.get('l1'), var.get('match').get('0'), var.get('cmp')), var.get('v1'), var.get('union')(var.get('r1'), var.get('match').get('1'), var.get('cmp')))
                    else:
                        if PyJsStrictEq(var.get('h1'),Js(1.0)):
                            return var.get('add')(var.get('s2'), var.get('s1').get('value'), var.get('cmp'))
                        else:
                            var.put('l2', var.get('s2').get('left'))
                            var.put('v2', var.get('s2').get('value'))
                            var.put('r2', var.get('s2').get('right'))
                            var.put('match$1', var.get('splitAuxNoPivot')(var.get('cmp'), var.get('s1'), var.get('v2')))
                            return var.get('Belt_internalAVLset').callprop('joinShared', var.get('union')(var.get('match$1').get('0'), var.get('l2'), var.get('cmp')), var.get('v2'), var.get('union')(var.get('match$1').get('1'), var.get('r2'), var.get('cmp')))
                else:
                    return var.get('s1')
            else:
                return var.get('s2')
        PyJsHoisted_union_.func_name = 'union'
        var.put('union', PyJsHoisted_union_)
        @Js
        def PyJsHoisted_intersect_(s1, s2, cmp, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 'l1', 'rr', 'cmp', 's2', 'r1', 'match', 's1', 'pres', 'v1'])
            if (PyJsStrictNeq(var.get('s1'),var.get(u"null")) and PyJsStrictNeq(var.get('s2'),var.get(u"null"))):
                var.put('l1', var.get('s1').get('left'))
                var.put('v1', var.get('s1').get('value'))
                var.put('r1', var.get('s1').get('right'))
                var.put('pres', Js({'contents':Js(False)}))
                var.put('match', var.get('splitAuxPivot')(var.get('cmp'), var.get('s2'), var.get('v1'), var.get('pres')))
                var.put('ll', var.get('intersect')(var.get('l1'), var.get('match').get('0'), var.get('cmp')))
                var.put('rr', var.get('intersect')(var.get('r1'), var.get('match').get('1'), var.get('cmp')))
                if var.get('pres').get('contents'):
                    return var.get('Belt_internalAVLset').callprop('joinShared', var.get('ll'), var.get('v1'), var.get('rr'))
                else:
                    return var.get('Belt_internalAVLset').callprop('concatShared', var.get('ll'), var.get('rr'))
            else:
                return var.get(u"null")
        PyJsHoisted_intersect_.func_name = 'intersect'
        var.put('intersect', PyJsHoisted_intersect_)
        @Js
        def PyJsHoisted_diff_(s1, s2, cmp, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 'l1', 'rr', 'cmp', 's2', 'r1', 'match', 's1', 'pres', 'v1'])
            if (PyJsStrictNeq(var.get('s1'),var.get(u"null")) and PyJsStrictNeq(var.get('s2'),var.get(u"null"))):
                var.put('l1', var.get('s1').get('left'))
                var.put('v1', var.get('s1').get('value'))
                var.put('r1', var.get('s1').get('right'))
                var.put('pres', Js({'contents':Js(False)}))
                var.put('match', var.get('splitAuxPivot')(var.get('cmp'), var.get('s2'), var.get('v1'), var.get('pres')))
                var.put('ll', var.get('diff')(var.get('l1'), var.get('match').get('0'), var.get('cmp')))
                var.put('rr', var.get('diff')(var.get('r1'), var.get('match').get('1'), var.get('cmp')))
                if var.get('pres').get('contents'):
                    return var.get('Belt_internalAVLset').callprop('concatShared', var.get('ll'), var.get('rr'))
                else:
                    return var.get('Belt_internalAVLset').callprop('joinShared', var.get('ll'), var.get('v1'), var.get('rr'))
            else:
                return var.get('s1')
        PyJsHoisted_diff_.func_name = 'diff'
        var.put('diff', PyJsHoisted_diff_)
        Js('use strict')
        var.put('Belt_internalAVLset', var.get('require')(Js('./belt_internalAVLset.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('empty', var.get(u"null"))
        var.put('fromArray', var.get('Belt_internalAVLset').get('fromArray'))
        var.put('fromSortedArrayUnsafe', var.get('Belt_internalAVLset').get('fromSortedArrayUnsafe'))
        var.put('isEmpty', var.get('Belt_internalAVLset').get('isEmpty'))
        var.put('has', var.get('Belt_internalAVLset').get('has'))
        var.put('subset', var.get('Belt_internalAVLset').get('subset'))
        var.put('cmp', var.get('Belt_internalAVLset').get('cmp'))
        var.put('eq', var.get('Belt_internalAVLset').get('eq'))
        var.put('forEachU', var.get('Belt_internalAVLset').get('forEachU'))
        var.put('forEach', var.get('Belt_internalAVLset').get('forEach'))
        var.put('reduceU', var.get('Belt_internalAVLset').get('reduceU'))
        var.put('reduce', var.get('Belt_internalAVLset').get('reduce'))
        var.put('everyU', var.get('Belt_internalAVLset').get('everyU'))
        var.put('every', var.get('Belt_internalAVLset').get('every'))
        var.put('someU', var.get('Belt_internalAVLset').get('someU'))
        var.put('some', var.get('Belt_internalAVLset').get('some'))
        var.put('keepU', var.get('Belt_internalAVLset').get('keepSharedU'))
        var.put('keep', var.get('Belt_internalAVLset').get('keepShared'))
        var.put('partitionU', var.get('Belt_internalAVLset').get('partitionSharedU'))
        var.put('partition', var.get('Belt_internalAVLset').get('partitionShared'))
        var.put('size', var.get('Belt_internalAVLset').get('size'))
        var.put('toList', var.get('Belt_internalAVLset').get('toList'))
        var.put('toArray', var.get('Belt_internalAVLset').get('toArray'))
        var.put('minimum', var.get('Belt_internalAVLset').get('minimum'))
        var.put('minUndefined', var.get('Belt_internalAVLset').get('minUndefined'))
        var.put('maximum', var.get('Belt_internalAVLset').get('maximum'))
        var.put('maxUndefined', var.get('Belt_internalAVLset').get('maxUndefined'))
        var.put('get', var.get('Belt_internalAVLset').get('get'))
        var.put('getUndefined', var.get('Belt_internalAVLset').get('getUndefined'))
        var.put('getExn', var.get('Belt_internalAVLset').get('getExn'))
        var.put('checkInvariantInternal', var.get('Belt_internalAVLset').get('checkInvariantInternal'))
        var.get('exports').put('empty', var.get('empty'))
        var.get('exports').put('fromArray', var.get('fromArray'))
        var.get('exports').put('fromSortedArrayUnsafe', var.get('fromSortedArrayUnsafe'))
        var.get('exports').put('isEmpty', var.get('isEmpty'))
        var.get('exports').put('has', var.get('has'))
        var.get('exports').put('add', var.get('add'))
        var.get('exports').put('mergeMany', var.get('mergeMany'))
        var.get('exports').put('remove', var.get('remove'))
        var.get('exports').put('removeMany', var.get('removeMany'))
        var.get('exports').put('union', var.get('union'))
        var.get('exports').put('intersect', var.get('intersect'))
        var.get('exports').put('diff', var.get('diff'))
        var.get('exports').put('subset', var.get('subset'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('keepU', var.get('keepU'))
        var.get('exports').put('keep', var.get('keep'))
        var.get('exports').put('partitionU', var.get('partitionU'))
        var.get('exports').put('partition', var.get('partition'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('toList', var.get('toList'))
        var.get('exports').put('toArray', var.get('toArray'))
        var.get('exports').put('minimum', var.get('minimum'))
        var.get('exports').put('minUndefined', var.get('minUndefined'))
        var.get('exports').put('maximum', var.get('maximum'))
        var.get('exports').put('maxUndefined', var.get('maxUndefined'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getUndefined', var.get('getUndefined'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('split', var.get('split'))
        var.get('exports').put('checkInvariantInternal', var.get('checkInvariantInternal'))
    PyJs_anonymous_9_._set_name('anonymous')
    @Js
    def PyJs_anonymous_10_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['$$String', 'exports', 'isSorted', 'intersect', 'diffU', 'isSortedU', 'Int', 'insertionSort', 'strictlySortedLengthU', 'stableSortInPlaceBy', 'binarySearchByU', 'merge', 'unionU', 'module', 'sortedLengthAuxMore', 'require', 'intersectU', 'Belt_Array', 'stableSortBy', 'sortTo', 'Curry', 'strictlySortedLength', 'union', 'diff', 'stableSortByU', 'binarySearchBy', 'stableSortInPlaceByU'])
        @Js
        def PyJsHoisted_sortedLengthAuxMore_(xs, _prec, _acc, len, lt, this, arguments, var=var):
            var = Scope({'xs':xs, '_prec':_prec, '_acc':_acc, 'len':len, 'lt':lt, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'acc', 'v', 'lt', '_prec', '_acc', 'prec'])
            while Js(True):
                var.put('acc', var.get('_acc'))
                var.put('prec', var.get('_prec'))
                if (var.get('acc')>=var.get('len')):
                    return var.get('acc')
                else:
                    var.put('v', var.get('xs').get(var.get('acc')))
                    if var.get('lt')(var.get('v'), var.get('prec')):
                        var.put('_acc', ((var.get('acc')+Js(1.0))|Js(0.0)))
                        var.put('_prec', var.get('v'))
                        continue
                    else:
                        return var.get('acc')
            pass
        PyJsHoisted_sortedLengthAuxMore_.func_name = 'sortedLengthAuxMore'
        var.put('sortedLengthAuxMore', PyJsHoisted_sortedLengthAuxMore_)
        @Js
        def PyJsHoisted_strictlySortedLengthU_(xs, lt, this, arguments, var=var):
            var = Scope({'xs':xs, 'lt':lt, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'lt$1', 'x1', 'acc', 'x0', 'v', 'len$1', 'lt', '_prec', '_acc', 'prec', 'xs$1'])
            var.put('len', var.get('xs').get('length'))
            if (PyJsStrictEq(var.get('len'),Js(0.0)) or PyJsStrictEq(var.get('len'),Js(1.0))):
                return var.get('len')
            else:
                var.put('x0', var.get('xs').get('0'))
                var.put('x1', var.get('xs').get('1'))
                if var.get('lt')(var.get('x0'), var.get('x1')):
                    var.put('xs$1', var.get('xs'))
                    var.put('_prec', var.get('x1'))
                    var.put('_acc', Js(2.0))
                    var.put('len$1', var.get('len'))
                    var.put('lt$1', var.get('lt'))
                    while Js(True):
                        var.put('acc', var.get('_acc'))
                        var.put('prec', var.get('_prec'))
                        if (var.get('acc')>=var.get('len$1')):
                            return var.get('acc')
                        else:
                            var.put('v', var.get('xs$1').get(var.get('acc')))
                            if var.get('lt$1')(var.get('prec'), var.get('v')):
                                var.put('_acc', ((var.get('acc')+Js(1.0))|Js(0.0)))
                                var.put('_prec', var.get('v'))
                                continue
                            else:
                                return var.get('acc')
                    pass
                else:
                    if var.get('lt')(var.get('x1'), var.get('x0')):
                        return ((-var.get('sortedLengthAuxMore')(var.get('xs'), var.get('x1'), Js(2.0), var.get('len'), var.get('lt')))|Js(0.0))
                    else:
                        return Js(1.0)
        PyJsHoisted_strictlySortedLengthU_.func_name = 'strictlySortedLengthU'
        var.put('strictlySortedLengthU', PyJsHoisted_strictlySortedLengthU_)
        @Js
        def PyJsHoisted_strictlySortedLength_(xs, lt, this, arguments, var=var):
            var = Scope({'xs':xs, 'lt':lt, 'this':this, 'arguments':arguments}, var)
            var.registers(['lt', 'xs'])
            return var.get('strictlySortedLengthU')(var.get('xs'), var.get('Curry').callprop('__2', var.get('lt')))
        PyJsHoisted_strictlySortedLength_.func_name = 'strictlySortedLength'
        var.put('strictlySortedLength', PyJsHoisted_strictlySortedLength_)
        @Js
        def PyJsHoisted_isSortedU_(a, cmp, this, arguments, var=var):
            var = Scope({'a':a, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'a', 'cmp', 'last_bound', 'cmp$1', 'a$1', '_i', 'i'])
            var.put('len', var.get('a').get('length'))
            if PyJsStrictEq(var.get('len'),Js(0.0)):
                return Js(True)
            else:
                var.put('a$1', var.get('a'))
                var.put('_i', Js(0.0))
                var.put('cmp$1', var.get('cmp'))
                var.put('last_bound', ((var.get('len')-Js(1.0))|Js(0.0)))
                while Js(True):
                    var.put('i', var.get('_i'))
                    if PyJsStrictEq(var.get('i'),var.get('last_bound')):
                        return Js(True)
                    else:
                        if (var.get('cmp$1')(var.get('a$1').get(var.get('i')), var.get('a$1').get(((var.get('i')+Js(1.0))|Js(0.0))))<=Js(0.0)):
                            var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                            continue
                        else:
                            return Js(False)
                pass
        PyJsHoisted_isSortedU_.func_name = 'isSortedU'
        var.put('isSortedU', PyJsHoisted_isSortedU_)
        @Js
        def PyJsHoisted_isSorted_(a, cmp, this, arguments, var=var):
            var = Scope({'a':a, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'cmp'])
            return var.get('isSortedU')(var.get('a'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_isSorted_.func_name = 'isSorted'
        var.put('isSorted', PyJsHoisted_isSorted_)
        @Js
        def PyJsHoisted_merge_(src, src1ofs, src1len, src2, src2ofs, src2len, dst, dstofs, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'src1ofs':src1ofs, 'src1len':src1len, 'src2':src2, 'src2ofs':src2ofs, 'src2len':src2len, 'dst':dst, 'dstofs':dstofs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', '_i1', 'i2$1', 'i1', '_s1', 'src2len', 'dstofs', '_i2', 'src1ofs', '_d', 'src1len', 'i1$1', 'src2r', 'cmp', '_s2', 's1', 'd', 'src2ofs', 'src2', 'src1r', 'i2', 's2', 'src'])
            var.put('src1r', ((var.get('src1ofs')+var.get('src1len'))|Js(0.0)))
            var.put('src2r', ((var.get('src2ofs')+var.get('src2len'))|Js(0.0)))
            var.put('_i1', var.get('src1ofs'))
            var.put('_s1', var.get('src').get(var.get('src1ofs')))
            var.put('_i2', var.get('src2ofs'))
            var.put('_s2', var.get('src2').get(var.get('src2ofs')))
            var.put('_d', var.get('dstofs'))
            while Js(True):
                var.put('d', var.get('_d'))
                var.put('s2', var.get('_s2'))
                var.put('i2', var.get('_i2'))
                var.put('s1', var.get('_s1'))
                var.put('i1', var.get('_i1'))
                if (var.get('cmp')(var.get('s1'), var.get('s2'))<=Js(0.0)):
                    var.get('dst').put(var.get('d'), var.get('s1'))
                    var.put('i1$1', ((var.get('i1')+Js(1.0))|Js(0.0)))
                    if (var.get('i1$1')<var.get('src1r')):
                        var.put('_d', ((var.get('d')+Js(1.0))|Js(0.0)))
                        var.put('_s1', var.get('src').get(var.get('i1$1')))
                        var.put('_i1', var.get('i1$1'))
                        continue
                    else:
                        return var.get('Belt_Array').callprop('blitUnsafe', var.get('src2'), var.get('i2'), var.get('dst'), ((var.get('d')+Js(1.0))|Js(0.0)), ((var.get('src2r')-var.get('i2'))|Js(0.0)))
                else:
                    var.get('dst').put(var.get('d'), var.get('s2'))
                    var.put('i2$1', ((var.get('i2')+Js(1.0))|Js(0.0)))
                    if (var.get('i2$1')<var.get('src2r')):
                        var.put('_d', ((var.get('d')+Js(1.0))|Js(0.0)))
                        var.put('_s2', var.get('src2').get(var.get('i2$1')))
                        var.put('_i2', var.get('i2$1'))
                        continue
                    else:
                        return var.get('Belt_Array').callprop('blitUnsafe', var.get('src'), var.get('i1'), var.get('dst'), ((var.get('d')+Js(1.0))|Js(0.0)), ((var.get('src1r')-var.get('i1'))|Js(0.0)))
            pass
        PyJsHoisted_merge_.func_name = 'merge'
        var.put('merge', PyJsHoisted_merge_)
        @Js
        def PyJsHoisted_unionU_(src, src1ofs, src1len, src2, src2ofs, src2len, dst, dstofs, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'src1ofs':src1ofs, 'src1len':src1len, 'src2':src2, 'src2ofs':src2ofs, 'src2len':src2len, 'dst':dst, 'dstofs':dstofs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', '_i1', 'i2$1', 'i1', '_s1', 'src2len', 'dstofs', '_i2', 'src1ofs', 'd$3', '_d', 'src1len', 'i1$2', 'i2$2', 'i1$1', 'd$1', 'src2r', 'cmp', '_s2', 'd$2', 's1', 'd', 'src2ofs', 'c', 'src2', 'src1r', 'i2', 's2', 'src'])
            var.put('src1r', ((var.get('src1ofs')+var.get('src1len'))|Js(0.0)))
            var.put('src2r', ((var.get('src2ofs')+var.get('src2len'))|Js(0.0)))
            var.put('_i1', var.get('src1ofs'))
            var.put('_s1', var.get('src').get(var.get('src1ofs')))
            var.put('_i2', var.get('src2ofs'))
            var.put('_s2', var.get('src2').get(var.get('src2ofs')))
            var.put('_d', var.get('dstofs'))
            while Js(True):
                var.put('d', var.get('_d'))
                var.put('s2', var.get('_s2'))
                var.put('i2', var.get('_i2'))
                var.put('s1', var.get('_s1'))
                var.put('i1', var.get('_i1'))
                var.put('c', var.get('cmp')(var.get('s1'), var.get('s2')))
                if (var.get('c')<Js(0.0)):
                    var.get('dst').put(var.get('d'), var.get('s1'))
                    var.put('i1$1', ((var.get('i1')+Js(1.0))|Js(0.0)))
                    var.put('d$1', ((var.get('d')+Js(1.0))|Js(0.0)))
                    if (var.get('i1$1')<var.get('src1r')):
                        var.put('_d', var.get('d$1'))
                        var.put('_s1', var.get('src').get(var.get('i1$1')))
                        var.put('_i1', var.get('i1$1'))
                        continue
                    else:
                        var.get('Belt_Array').callprop('blitUnsafe', var.get('src2'), var.get('i2'), var.get('dst'), var.get('d$1'), ((var.get('src2r')-var.get('i2'))|Js(0.0)))
                        return ((((var.get('d$1')+var.get('src2r'))|Js(0.0))-var.get('i2'))|Js(0.0))
                else:
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        var.get('dst').put(var.get('d'), var.get('s1'))
                        var.put('i1$2', ((var.get('i1')+Js(1.0))|Js(0.0)))
                        var.put('i2$1', ((var.get('i2')+Js(1.0))|Js(0.0)))
                        var.put('d$2', ((var.get('d')+Js(1.0))|Js(0.0)))
                        if ((var.get('i1$2')<var.get('src1r')) and (var.get('i2$1')<var.get('src2r'))):
                            var.put('_d', var.get('d$2'))
                            var.put('_s2', var.get('src2').get(var.get('i2$1')))
                            var.put('_i2', var.get('i2$1'))
                            var.put('_s1', var.get('src').get(var.get('i1$2')))
                            var.put('_i1', var.get('i1$2'))
                            continue
                        else:
                            if PyJsStrictEq(var.get('i1$2'),var.get('src1r')):
                                var.get('Belt_Array').callprop('blitUnsafe', var.get('src2'), var.get('i2$1'), var.get('dst'), var.get('d$2'), ((var.get('src2r')-var.get('i2$1'))|Js(0.0)))
                                return ((((var.get('d$2')+var.get('src2r'))|Js(0.0))-var.get('i2$1'))|Js(0.0))
                            else:
                                var.get('Belt_Array').callprop('blitUnsafe', var.get('src'), var.get('i1$2'), var.get('dst'), var.get('d$2'), ((var.get('src1r')-var.get('i1$2'))|Js(0.0)))
                                return ((((var.get('d$2')+var.get('src1r'))|Js(0.0))-var.get('i1$2'))|Js(0.0))
                    else:
                        var.get('dst').put(var.get('d'), var.get('s2'))
                        var.put('i2$2', ((var.get('i2')+Js(1.0))|Js(0.0)))
                        var.put('d$3', ((var.get('d')+Js(1.0))|Js(0.0)))
                        if (var.get('i2$2')<var.get('src2r')):
                            var.put('_d', var.get('d$3'))
                            var.put('_s2', var.get('src2').get(var.get('i2$2')))
                            var.put('_i2', var.get('i2$2'))
                            continue
                        else:
                            var.get('Belt_Array').callprop('blitUnsafe', var.get('src'), var.get('i1'), var.get('dst'), var.get('d$3'), ((var.get('src1r')-var.get('i1'))|Js(0.0)))
                            return ((((var.get('d$3')+var.get('src1r'))|Js(0.0))-var.get('i1'))|Js(0.0))
            pass
        PyJsHoisted_unionU_.func_name = 'unionU'
        var.put('unionU', PyJsHoisted_unionU_)
        @Js
        def PyJsHoisted_union_(src, src1ofs, src1len, src2, src2ofs, src2len, dst, dstofs, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'src1ofs':src1ofs, 'src1len':src1len, 'src2':src2, 'src2ofs':src2ofs, 'src2len':src2len, 'dst':dst, 'dstofs':dstofs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', 'src1ofs', 'src1len', 'src2', 'cmp', 'src2len', 'src', 'dstofs', 'src2ofs'])
            return var.get('unionU')(var.get('src'), var.get('src1ofs'), var.get('src1len'), var.get('src2'), var.get('src2ofs'), var.get('src2len'), var.get('dst'), var.get('dstofs'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_union_.func_name = 'union'
        var.put('union', PyJsHoisted_union_)
        @Js
        def PyJsHoisted_intersectU_(src, src1ofs, src1len, src2, src2ofs, src2len, dst, dstofs, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'src1ofs':src1ofs, 'src1len':src1len, 'src2':src2, 'src2ofs':src2ofs, 'src2len':src2len, 'dst':dst, 'dstofs':dstofs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', '_i1', 'i2$1', 'i1', '_s1', 'src2len', 'dstofs', '_i2', 'src1ofs', '_d', 'src1len', 'i1$2', 'i2$2', 'i1$1', 'd$1', 'src2r', 'cmp', '_s2', 's1', 'd', 'src2ofs', 'c', 'src2', 'src1r', 'i2', 's2', 'src'])
            var.put('src1r', ((var.get('src1ofs')+var.get('src1len'))|Js(0.0)))
            var.put('src2r', ((var.get('src2ofs')+var.get('src2len'))|Js(0.0)))
            var.put('_i1', var.get('src1ofs'))
            var.put('_s1', var.get('src').get(var.get('src1ofs')))
            var.put('_i2', var.get('src2ofs'))
            var.put('_s2', var.get('src2').get(var.get('src2ofs')))
            var.put('_d', var.get('dstofs'))
            while Js(True):
                var.put('d', var.get('_d'))
                var.put('s2', var.get('_s2'))
                var.put('i2', var.get('_i2'))
                var.put('s1', var.get('_s1'))
                var.put('i1', var.get('_i1'))
                var.put('c', var.get('cmp')(var.get('s1'), var.get('s2')))
                if (var.get('c')<Js(0.0)):
                    var.put('i1$1', ((var.get('i1')+Js(1.0))|Js(0.0)))
                    if (var.get('i1$1')<var.get('src1r')):
                        var.put('_s1', var.get('src').get(var.get('i1$1')))
                        var.put('_i1', var.get('i1$1'))
                        continue
                    else:
                        return var.get('d')
                else:
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        var.get('dst').put(var.get('d'), var.get('s1'))
                        var.put('i1$2', ((var.get('i1')+Js(1.0))|Js(0.0)))
                        var.put('i2$1', ((var.get('i2')+Js(1.0))|Js(0.0)))
                        var.put('d$1', ((var.get('d')+Js(1.0))|Js(0.0)))
                        if ((var.get('i1$2')<var.get('src1r')) and (var.get('i2$1')<var.get('src2r'))):
                            var.put('_d', var.get('d$1'))
                            var.put('_s2', var.get('src2').get(var.get('i2$1')))
                            var.put('_i2', var.get('i2$1'))
                            var.put('_s1', var.get('src').get(var.get('i1$2')))
                            var.put('_i1', var.get('i1$2'))
                            continue
                        else:
                            return var.get('d$1')
                    else:
                        var.put('i2$2', ((var.get('i2')+Js(1.0))|Js(0.0)))
                        if (var.get('i2$2')<var.get('src2r')):
                            var.put('_s2', var.get('src2').get(var.get('i2$2')))
                            var.put('_i2', var.get('i2$2'))
                            continue
                        else:
                            return var.get('d')
            pass
        PyJsHoisted_intersectU_.func_name = 'intersectU'
        var.put('intersectU', PyJsHoisted_intersectU_)
        @Js
        def PyJsHoisted_intersect_(src, src1ofs, src1len, src2, src2ofs, src2len, dst, dstofs, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'src1ofs':src1ofs, 'src1len':src1len, 'src2':src2, 'src2ofs':src2ofs, 'src2len':src2len, 'dst':dst, 'dstofs':dstofs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', 'src1ofs', 'src1len', 'src2', 'cmp', 'src2len', 'src', 'dstofs', 'src2ofs'])
            return var.get('intersectU')(var.get('src'), var.get('src1ofs'), var.get('src1len'), var.get('src2'), var.get('src2ofs'), var.get('src2len'), var.get('dst'), var.get('dstofs'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_intersect_.func_name = 'intersect'
        var.put('intersect', PyJsHoisted_intersect_)
        @Js
        def PyJsHoisted_diffU_(src, src1ofs, src1len, src2, src2ofs, src2len, dst, dstofs, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'src1ofs':src1ofs, 'src1len':src1len, 'src2':src2, 'src2ofs':src2ofs, 'src2len':src2len, 'dst':dst, 'dstofs':dstofs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', '_i1', 'i2$1', 'i1', '_s1', 'src2len', 'dstofs', '_i2', 'src1ofs', '_d', 'src1len', 'i1$2', 'i2$2', 'i1$1', 'd$1', 'src2r', 'cmp', '_s2', 's1', 'd', 'src2ofs', 'c', 'src2', 'src1r', 'i2', 's2', 'src'])
            var.put('src1r', ((var.get('src1ofs')+var.get('src1len'))|Js(0.0)))
            var.put('src2r', ((var.get('src2ofs')+var.get('src2len'))|Js(0.0)))
            var.put('_i1', var.get('src1ofs'))
            var.put('_s1', var.get('src').get(var.get('src1ofs')))
            var.put('_i2', var.get('src2ofs'))
            var.put('_s2', var.get('src2').get(var.get('src2ofs')))
            var.put('_d', var.get('dstofs'))
            while Js(True):
                var.put('d', var.get('_d'))
                var.put('s2', var.get('_s2'))
                var.put('i2', var.get('_i2'))
                var.put('s1', var.get('_s1'))
                var.put('i1', var.get('_i1'))
                var.put('c', var.get('cmp')(var.get('s1'), var.get('s2')))
                if (var.get('c')<Js(0.0)):
                    var.get('dst').put(var.get('d'), var.get('s1'))
                    var.put('d$1', ((var.get('d')+Js(1.0))|Js(0.0)))
                    var.put('i1$1', ((var.get('i1')+Js(1.0))|Js(0.0)))
                    if (var.get('i1$1')<var.get('src1r')):
                        var.put('_d', var.get('d$1'))
                        var.put('_s1', var.get('src').get(var.get('i1$1')))
                        var.put('_i1', var.get('i1$1'))
                        continue
                    else:
                        return var.get('d$1')
                else:
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        var.put('i1$2', ((var.get('i1')+Js(1.0))|Js(0.0)))
                        var.put('i2$1', ((var.get('i2')+Js(1.0))|Js(0.0)))
                        if ((var.get('i1$2')<var.get('src1r')) and (var.get('i2$1')<var.get('src2r'))):
                            var.put('_s2', var.get('src2').get(var.get('i2$1')))
                            var.put('_i2', var.get('i2$1'))
                            var.put('_s1', var.get('src').get(var.get('i1$2')))
                            var.put('_i1', var.get('i1$2'))
                            continue
                        else:
                            if PyJsStrictEq(var.get('i1$2'),var.get('src1r')):
                                return var.get('d')
                            else:
                                var.get('Belt_Array').callprop('blitUnsafe', var.get('src'), var.get('i1$2'), var.get('dst'), var.get('d'), ((var.get('src1r')-var.get('i1$2'))|Js(0.0)))
                                return ((((var.get('d')+var.get('src1r'))|Js(0.0))-var.get('i1$2'))|Js(0.0))
                    else:
                        var.put('i2$2', ((var.get('i2')+Js(1.0))|Js(0.0)))
                        if (var.get('i2$2')<var.get('src2r')):
                            var.put('_s2', var.get('src2').get(var.get('i2$2')))
                            var.put('_i2', var.get('i2$2'))
                            continue
                        else:
                            var.get('Belt_Array').callprop('blitUnsafe', var.get('src'), var.get('i1'), var.get('dst'), var.get('d'), ((var.get('src1r')-var.get('i1'))|Js(0.0)))
                            return ((((var.get('d')+var.get('src1r'))|Js(0.0))-var.get('i1'))|Js(0.0))
            pass
        PyJsHoisted_diffU_.func_name = 'diffU'
        var.put('diffU', PyJsHoisted_diffU_)
        @Js
        def PyJsHoisted_diff_(src, src1ofs, src1len, src2, src2ofs, src2len, dst, dstofs, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'src1ofs':src1ofs, 'src1len':src1len, 'src2':src2, 'src2ofs':src2ofs, 'src2len':src2len, 'dst':dst, 'dstofs':dstofs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', 'src1ofs', 'src1len', 'src2', 'cmp', 'src2len', 'src', 'dstofs', 'src2ofs'])
            return var.get('diffU')(var.get('src'), var.get('src1ofs'), var.get('src1len'), var.get('src2'), var.get('src2ofs'), var.get('src2len'), var.get('dst'), var.get('dstofs'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_diff_.func_name = 'diff'
        var.put('diff', PyJsHoisted_diff_)
        @Js
        def PyJsHoisted_insertionSort_(src, srcofs, dst, dstofs, len, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'srcofs':srcofs, 'dst':dst, 'dstofs':dstofs, 'len':len, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', 'len', 'e', 'j', 'cmp', 'i_finish', 'srcofs', 'src', 'i', 'dstofs'])
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('e', var.get('src').get(((var.get('srcofs')+var.get('i'))|Js(0.0))))
                    var.put('j', ((((var.get('dstofs')+var.get('i'))|Js(0.0))-Js(1.0))|Js(0.0)))
                    while ((var.get('j')>=var.get('dstofs')) and (var.get('cmp')(var.get('dst').get(var.get('j')), var.get('e'))>Js(0.0))):
                        var.get('dst').put(((var.get('j')+Js(1.0))|Js(0.0)), var.get('dst').get(var.get('j')))
                        var.put('j', ((var.get('j')-Js(1.0))|Js(0.0)))
                    pass
                    var.get('dst').put(((var.get('j')+Js(1.0))|Js(0.0)), var.get('e'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_insertionSort_.func_name = 'insertionSort'
        var.put('insertionSort', PyJsHoisted_insertionSort_)
        @Js
        def PyJsHoisted_sortTo_(src, srcofs, dst, dstofs, len, cmp, this, arguments, var=var):
            var = Scope({'src':src, 'srcofs':srcofs, 'dst':dst, 'dstofs':dstofs, 'len':len, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', 'len', 'l2', 'l1', 'cmp', 'srcofs', 'src', 'dstofs'])
            if (var.get('len')<=Js(5.0)):
                return var.get('insertionSort')(var.get('src'), var.get('srcofs'), var.get('dst'), var.get('dstofs'), var.get('len'), var.get('cmp'))
            else:
                var.put('l1', ((var.get('len')/Js(2.0))|Js(0.0)))
                var.put('l2', ((var.get('len')-var.get('l1'))|Js(0.0)))
                var.get('sortTo')(var.get('src'), ((var.get('srcofs')+var.get('l1'))|Js(0.0)), var.get('dst'), ((var.get('dstofs')+var.get('l1'))|Js(0.0)), var.get('l2'), var.get('cmp'))
                var.get('sortTo')(var.get('src'), var.get('srcofs'), var.get('src'), ((var.get('srcofs')+var.get('l2'))|Js(0.0)), var.get('l1'), var.get('cmp'))
                return var.get('merge')(var.get('src'), ((var.get('srcofs')+var.get('l2'))|Js(0.0)), var.get('l1'), var.get('dst'), ((var.get('dstofs')+var.get('l1'))|Js(0.0)), var.get('l2'), var.get('dst'), var.get('dstofs'), var.get('cmp'))
        PyJsHoisted_sortTo_.func_name = 'sortTo'
        var.put('sortTo', PyJsHoisted_sortTo_)
        @Js
        def PyJsHoisted_stableSortInPlaceByU_(a, cmp, this, arguments, var=var):
            var = Scope({'a':a, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'l2', 'l1', 'a', 'cmp', 'l'])
            var.put('l', var.get('a').get('length'))
            if (var.get('l')<=Js(5.0)):
                return var.get('insertionSort')(var.get('a'), Js(0.0), var.get('a'), Js(0.0), var.get('l'), var.get('cmp'))
            else:
                var.put('l1', ((var.get('l')/Js(2.0))|Js(0.0)))
                var.put('l2', ((var.get('l')-var.get('l1'))|Js(0.0)))
                var.put('t', var.get('Array').create(var.get('l2')))
                var.get('sortTo')(var.get('a'), var.get('l1'), var.get('t'), Js(0.0), var.get('l2'), var.get('cmp'))
                var.get('sortTo')(var.get('a'), Js(0.0), var.get('a'), var.get('l2'), var.get('l1'), var.get('cmp'))
                return var.get('merge')(var.get('a'), var.get('l2'), var.get('l1'), var.get('t'), Js(0.0), var.get('l2'), var.get('a'), Js(0.0), var.get('cmp'))
        PyJsHoisted_stableSortInPlaceByU_.func_name = 'stableSortInPlaceByU'
        var.put('stableSortInPlaceByU', PyJsHoisted_stableSortInPlaceByU_)
        @Js
        def PyJsHoisted_stableSortInPlaceBy_(a, cmp, this, arguments, var=var):
            var = Scope({'a':a, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'cmp'])
            return var.get('stableSortInPlaceByU')(var.get('a'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_stableSortInPlaceBy_.func_name = 'stableSortInPlaceBy'
        var.put('stableSortInPlaceBy', PyJsHoisted_stableSortInPlaceBy_)
        @Js
        def PyJsHoisted_stableSortByU_(a, cmp, this, arguments, var=var):
            var = Scope({'a':a, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b', 'cmp'])
            var.put('b', var.get('a').callprop('slice', Js(0.0)))
            var.get('stableSortInPlaceByU')(var.get('b'), var.get('cmp'))
            return var.get('b')
        PyJsHoisted_stableSortByU_.func_name = 'stableSortByU'
        var.put('stableSortByU', PyJsHoisted_stableSortByU_)
        @Js
        def PyJsHoisted_stableSortBy_(a, cmp, this, arguments, var=var):
            var = Scope({'a':a, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'cmp'])
            return var.get('stableSortByU')(var.get('a'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_stableSortBy_.func_name = 'stableSortBy'
        var.put('stableSortBy', PyJsHoisted_stableSortBy_)
        @Js
        def PyJsHoisted_binarySearchByU_(sorted, key, cmp, this, arguments, var=var):
            var = Scope({'sorted':sorted, 'key':key, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'hi$1', 'key$1', 'midVal', '_hi', 'mid', 'c', 'lo', 'hi', 'cmp', 'c2', '_lo', 'cmp$1', 'c$1', 'key', 'lo$1', 'arr', 'sorted'])
            var.put('len', var.get('sorted').get('length'))
            if PyJsStrictEq(var.get('len'),Js(0.0)):
                return (-Js(1.0))
            else:
                var.put('lo', var.get('sorted').get('0'))
                var.put('c', var.get('cmp')(var.get('key'), var.get('lo')))
                if (var.get('c')<Js(0.0)):
                    return (-Js(1.0))
                else:
                    var.put('hi', var.get('sorted').get(((var.get('len')-Js(1.0))|Js(0.0))))
                    var.put('c2', var.get('cmp')(var.get('key'), var.get('hi')))
                    if (var.get('c2')>Js(0.0)):
                        return ((-((var.get('len')+Js(1.0))|Js(0.0)))|Js(0.0))
                    else:
                        var.put('arr', var.get('sorted'))
                        var.put('_lo', Js(0.0))
                        var.put('_hi', ((var.get('len')-Js(1.0))|Js(0.0)))
                        var.put('key$1', var.get('key'))
                        var.put('cmp$1', var.get('cmp'))
                        while Js(True):
                            var.put('hi$1', var.get('_hi'))
                            var.put('lo$1', var.get('_lo'))
                            var.put('mid', ((((var.get('lo$1')+var.get('hi$1'))|Js(0.0))/Js(2.0))|Js(0.0)))
                            var.put('midVal', var.get('arr').get(var.get('mid')))
                            var.put('c$1', var.get('cmp$1')(var.get('key$1'), var.get('midVal')))
                            if PyJsStrictEq(var.get('c$1'),Js(0.0)):
                                return var.get('mid')
                            else:
                                if (var.get('c$1')<Js(0.0)):
                                    if PyJsStrictEq(var.get('hi$1'),var.get('mid')):
                                        if PyJsStrictEq(var.get('cmp$1')(var.get('arr').get(var.get('lo$1')), var.get('key$1')),Js(0.0)):
                                            return var.get('lo$1')
                                        else:
                                            return ((-((var.get('hi$1')+Js(1.0))|Js(0.0)))|Js(0.0))
                                    else:
                                        var.put('_hi', var.get('mid'))
                                        continue
                                else:
                                    if PyJsStrictEq(var.get('lo$1'),var.get('mid')):
                                        if PyJsStrictEq(var.get('cmp$1')(var.get('arr').get(var.get('hi$1')), var.get('key$1')),Js(0.0)):
                                            return var.get('hi$1')
                                        else:
                                            return ((-((var.get('hi$1')+Js(1.0))|Js(0.0)))|Js(0.0))
                                    else:
                                        var.put('_lo', var.get('mid'))
                                        continue
                        pass
        PyJsHoisted_binarySearchByU_.func_name = 'binarySearchByU'
        var.put('binarySearchByU', PyJsHoisted_binarySearchByU_)
        @Js
        def PyJsHoisted_binarySearchBy_(sorted, key, cmp, this, arguments, var=var):
            var = Scope({'sorted':sorted, 'key':key, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp', 'key', 'sorted'])
            return var.get('binarySearchByU')(var.get('sorted'), var.get('key'), var.get('Curry').callprop('__2', var.get('cmp')))
        PyJsHoisted_binarySearchBy_.func_name = 'binarySearchBy'
        var.put('binarySearchBy', PyJsHoisted_binarySearchBy_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Belt_Array', var.get('require')(Js('./belt_Array.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('Int', Js(0.0))
        var.put('$$String', Js(0.0))
        var.get('exports').put('Int', var.get('Int'))
        var.get('exports').put('$$String', var.get('$$String'))
        var.get('exports').put('strictlySortedLengthU', var.get('strictlySortedLengthU'))
        var.get('exports').put('strictlySortedLength', var.get('strictlySortedLength'))
        var.get('exports').put('isSortedU', var.get('isSortedU'))
        var.get('exports').put('isSorted', var.get('isSorted'))
        var.get('exports').put('stableSortInPlaceByU', var.get('stableSortInPlaceByU'))
        var.get('exports').put('stableSortInPlaceBy', var.get('stableSortInPlaceBy'))
        var.get('exports').put('stableSortByU', var.get('stableSortByU'))
        var.get('exports').put('stableSortBy', var.get('stableSortBy'))
        var.get('exports').put('binarySearchByU', var.get('binarySearchByU'))
        var.get('exports').put('binarySearchBy', var.get('binarySearchBy'))
        var.get('exports').put('unionU', var.get('unionU'))
        var.get('exports').put('union', var.get('union'))
        var.get('exports').put('intersectU', var.get('intersectU'))
        var.get('exports').put('intersect', var.get('intersect'))
        var.get('exports').put('diffU', var.get('diffU'))
        var.get('exports').put('diff', var.get('diff'))
    PyJs_anonymous_10_._set_name('anonymous')
    @Js
    def PyJs_anonymous_11_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['get', 'exports', 'addMutate', 'partitionCopy', 'Caml_option', 'maximum', 'keepCopy', 'stackAllLeft', 'some', 'min0Aux', 'toArray', 'every', 'partitionCopyU', 'heightUpdateMutate', 'fromArray', 'addMinElement', 'balMutate', 'treeHeight', 'joinShared', 'fillArrayWithFilter', 'fromSortedArrayUnsafe', 'fromSortedArrayRevAux', 'lengthNode', 'doubleWithRightChild', 'keepShared', 'maxUndefined', 'toListAux', 'partitionSharedU', 'everyU', 'module', 'size', 'removeMinAuxWithRef', 'keepCopyU', 'concatShared', 'partitionShared', 'create', 'copy', 'eq', 'require', 'rotateWithLeftChild', 'subset', 'getExn', 'fillArrayWithPartition', 'rotateWithRightChild', 'cmp', 'Curry', 'minUndefined', 'addMaxElement', 'fromSortedArrayAux', 'singleton', 'reduceU', 'isEmpty', 'toList', 'has', 'minimum', 'checkInvariantInternal', 'forEach', 'someU', 'keepSharedU', 'Belt_SortArray', 'fillArray', 'max0Aux', 'getUndefined', 'heightGe', 'removeMinAuxWithRootMutate', 'bal', 'reduce', 'doubleWithLeftChild', 'forEachU'])
        @Js
        def PyJsHoisted_treeHeight_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('n').get('height')
            else:
                return Js(0.0)
        PyJsHoisted_treeHeight_.func_name = 'treeHeight'
        var.put('treeHeight', PyJsHoisted_treeHeight_)
        @Js
        def PyJsHoisted_copy_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'l'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('l', var.get('n').get('left'))
                var.put('r', var.get('n').get('right'))
                return Js({'value':var.get('n').get('value'),'height':var.get('n').get('height'),'left':var.get('copy')(var.get('l')),'right':var.get('copy')(var.get('r'))})
            else:
                return var.get('n')
        PyJsHoisted_copy_.func_name = 'copy'
        var.put('copy', PyJsHoisted_copy_)
        @Js
        def PyJsHoisted_create_(l, v, r, this, arguments, var=var):
            var = Scope({'l':l, 'v':v, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['hl', 'hr', 'r', 'v', 'l'])
            var.put('hl', (var.get('l').get('height') if PyJsStrictNeq(var.get('l'),var.get(u"null")) else Js(0.0)))
            var.put('hr', (var.get('r').get('height') if PyJsStrictNeq(var.get('r'),var.get(u"null")) else Js(0.0)))
            return Js({'value':var.get('v'),'height':(((var.get('hl')+Js(1.0))|Js(0.0)) if (var.get('hl')>=var.get('hr')) else ((var.get('hr')+Js(1.0))|Js(0.0))),'left':var.get('l'),'right':var.get('r')})
        PyJsHoisted_create_.func_name = 'create'
        var.put('create', PyJsHoisted_create_)
        @Js
        def PyJsHoisted_singleton_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return Js({'value':var.get('x'),'height':Js(1.0),'left':var.get(u"null"),'right':var.get(u"null")})
        PyJsHoisted_singleton_.func_name = 'singleton'
        var.put('singleton', PyJsHoisted_singleton_)
        @Js
        def PyJsHoisted_heightGe_(l, r, this, arguments, var=var):
            var = Scope({'l':l, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'l'])
            if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                    return (var.get('l').get('height')>=var.get('r').get('height'))
                else:
                    return Js(False)
            else:
                return Js(True)
        PyJsHoisted_heightGe_.func_name = 'heightGe'
        var.put('heightGe', PyJsHoisted_heightGe_)
        @Js
        def PyJsHoisted_bal_(l, v, r, this, arguments, var=var):
            var = Scope({'l':l, 'v':v, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 'hl', 'rv', 'hr', 'rlr', 'rr', 'rl', 'r', 'v', 'lv', 'rll', 'lr', 'lrv', 'rlv', 'lrl', 'lrr', 'l'])
            var.put('hl', (var.get('l').get('height') if PyJsStrictNeq(var.get('l'),var.get(u"null")) else Js(0.0)))
            var.put('hr', (var.get('r').get('height') if PyJsStrictNeq(var.get('r'),var.get(u"null")) else Js(0.0)))
            if (var.get('hl')>((var.get('hr')+Js(2.0))|Js(0.0))):
                var.put('ll', var.get('l').get('left'))
                var.put('lv', var.get('l').get('value'))
                var.put('lr', var.get('l').get('right'))
                if var.get('heightGe')(var.get('ll'), var.get('lr')):
                    return var.get('create')(var.get('ll'), var.get('lv'), var.get('create')(var.get('lr'), var.get('v'), var.get('r')))
                else:
                    var.put('lrl', var.get('lr').get('left'))
                    var.put('lrv', var.get('lr').get('value'))
                    var.put('lrr', var.get('lr').get('right'))
                    return var.get('create')(var.get('create')(var.get('ll'), var.get('lv'), var.get('lrl')), var.get('lrv'), var.get('create')(var.get('lrr'), var.get('v'), var.get('r')))
            else:
                if (var.get('hr')>((var.get('hl')+Js(2.0))|Js(0.0))):
                    var.put('rl', var.get('r').get('left'))
                    var.put('rv', var.get('r').get('value'))
                    var.put('rr', var.get('r').get('right'))
                    if var.get('heightGe')(var.get('rr'), var.get('rl')):
                        return var.get('create')(var.get('create')(var.get('l'), var.get('v'), var.get('rl')), var.get('rv'), var.get('rr'))
                    else:
                        var.put('rll', var.get('rl').get('left'))
                        var.put('rlv', var.get('rl').get('value'))
                        var.put('rlr', var.get('rl').get('right'))
                        return var.get('create')(var.get('create')(var.get('l'), var.get('v'), var.get('rll')), var.get('rlv'), var.get('create')(var.get('rlr'), var.get('rv'), var.get('rr')))
                else:
                    return Js({'value':var.get('v'),'height':(((var.get('hl')+Js(1.0))|Js(0.0)) if (var.get('hl')>=var.get('hr')) else ((var.get('hr')+Js(1.0))|Js(0.0))),'left':var.get('l'),'right':var.get('r')})
        PyJsHoisted_bal_.func_name = 'bal'
        var.put('bal', PyJsHoisted_bal_)
        @Js
        def PyJsHoisted_min0Aux_(_n, this, arguments, var=var):
            var = Scope({'_n':_n, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                var.put('match', var.get('n').get('left'))
                if PyJsStrictNeq(var.get('match'),var.get(u"null")):
                    var.put('_n', var.get('match'))
                    continue
                else:
                    return var.get('n').get('value')
            pass
        PyJsHoisted_min0Aux_.func_name = 'min0Aux'
        var.put('min0Aux', PyJsHoisted_min0Aux_)
        @Js
        def PyJsHoisted_minimum_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('Caml_option').callprop('some', var.get('min0Aux')(var.get('n')))
        PyJsHoisted_minimum_.func_name = 'minimum'
        var.put('minimum', PyJsHoisted_minimum_)
        @Js
        def PyJsHoisted_minUndefined_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('min0Aux')(var.get('n'))
        PyJsHoisted_minUndefined_.func_name = 'minUndefined'
        var.put('minUndefined', PyJsHoisted_minUndefined_)
        @Js
        def PyJsHoisted_max0Aux_(_n, this, arguments, var=var):
            var = Scope({'_n':_n, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                var.put('match', var.get('n').get('right'))
                if PyJsStrictNeq(var.get('match'),var.get(u"null")):
                    var.put('_n', var.get('match'))
                    continue
                else:
                    return var.get('n').get('value')
            pass
        PyJsHoisted_max0Aux_.func_name = 'max0Aux'
        var.put('max0Aux', PyJsHoisted_max0Aux_)
        @Js
        def PyJsHoisted_maximum_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('Caml_option').callprop('some', var.get('max0Aux')(var.get('n')))
        PyJsHoisted_maximum_.func_name = 'maximum'
        var.put('maximum', PyJsHoisted_maximum_)
        @Js
        def PyJsHoisted_maxUndefined_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('max0Aux')(var.get('n'))
        PyJsHoisted_maxUndefined_.func_name = 'maxUndefined'
        var.put('maxUndefined', PyJsHoisted_maxUndefined_)
        @Js
        def PyJsHoisted_removeMinAuxWithRef_(n, v, this, arguments, var=var):
            var = Scope({'n':n, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', 'n', 'ln', 'rn', 'kn'])
            var.put('ln', var.get('n').get('left'))
            var.put('rn', var.get('n').get('right'))
            var.put('kn', var.get('n').get('value'))
            if PyJsStrictNeq(var.get('ln'),var.get(u"null")):
                return var.get('bal')(var.get('removeMinAuxWithRef')(var.get('ln'), var.get('v')), var.get('kn'), var.get('rn'))
            else:
                var.get('v').put('contents', var.get('kn'))
                return var.get('rn')
        PyJsHoisted_removeMinAuxWithRef_.func_name = 'removeMinAuxWithRef'
        var.put('removeMinAuxWithRef', PyJsHoisted_removeMinAuxWithRef_)
        @Js
        def PyJsHoisted_isEmpty_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return PyJsStrictEq(var.get('n'),var.get(u"null"))
        PyJsHoisted_isEmpty_.func_name = 'isEmpty'
        var.put('isEmpty', PyJsHoisted_isEmpty_)
        @Js
        def PyJsHoisted_stackAllLeft_(_v, _s, this, arguments, var=var):
            var = Scope({'_v':_v, '_s':_s, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', '_s', 's', '_v'])
            while Js(True):
                var.put('s', var.get('_s'))
                var.put('v', var.get('_v'))
                if PyJsStrictNeq(var.get('v'),var.get(u"null")):
                    var.put('_s', Js([var.get('v'), var.get('s')]))
                    var.put('_v', var.get('v').get('left'))
                    continue
                else:
                    return var.get('s')
            pass
        PyJsHoisted_stackAllLeft_.func_name = 'stackAllLeft'
        var.put('stackAllLeft', PyJsHoisted_stackAllLeft_)
        @Js
        def PyJsHoisted_forEachU_(_n, f, this, arguments, var=var):
            var = Scope({'_n':_n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.get('forEachU')(var.get('n').get('left'), var.get('f'))
                    var.get('f')(var.get('n').get('value'))
                    var.put('_n', var.get('n').get('right'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_forEachU_.func_name = 'forEachU'
        var.put('forEachU', PyJsHoisted_forEachU_)
        @Js
        def PyJsHoisted_forEach_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n'])
            return var.get('forEachU')(var.get('n'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_forEach_.func_name = 'forEach'
        var.put('forEach', PyJsHoisted_forEach_)
        @Js
        def PyJsHoisted_reduceU_(_s, _accu, f, this, arguments, var=var):
            var = Scope({'_s':_s, '_accu':_accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', 'r', '_s', '_accu', 'k', 's', 'l'])
            while Js(True):
                var.put('accu', var.get('_accu'))
                var.put('s', var.get('_s'))
                if PyJsStrictNeq(var.get('s'),var.get(u"null")):
                    var.put('l', var.get('s').get('left'))
                    var.put('k', var.get('s').get('value'))
                    var.put('r', var.get('s').get('right'))
                    var.put('_accu', var.get('f')(var.get('reduceU')(var.get('l'), var.get('accu'), var.get('f')), var.get('k')))
                    var.put('_s', var.get('r'))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_reduceU_.func_name = 'reduceU'
        var.put('reduceU', PyJsHoisted_reduceU_)
        @Js
        def PyJsHoisted_reduce_(s, accu, f, this, arguments, var=var):
            var = Scope({'s':s, 'accu':accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', 's'])
            return var.get('reduceU')(var.get('s'), var.get('accu'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_reduce_.func_name = 'reduce'
        var.put('reduce', PyJsHoisted_reduce_)
        @Js
        def PyJsHoisted_everyU_(_n, p, this, arguments, var=var):
            var = Scope({'_n':_n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    if (var.get('p')(var.get('n').get('value')) and var.get('everyU')(var.get('n').get('left'), var.get('p'))):
                        var.put('_n', var.get('n').get('right'))
                        continue
                    else:
                        return Js(False)
                else:
                    return Js(True)
            pass
        PyJsHoisted_everyU_.func_name = 'everyU'
        var.put('everyU', PyJsHoisted_everyU_)
        @Js
        def PyJsHoisted_every_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('everyU')(var.get('n'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_every_.func_name = 'every'
        var.put('every', PyJsHoisted_every_)
        @Js
        def PyJsHoisted_someU_(_n, p, this, arguments, var=var):
            var = Scope({'_n':_n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    if (var.get('p')(var.get('n').get('value')) or var.get('someU')(var.get('n').get('left'), var.get('p'))):
                        return Js(True)
                    else:
                        var.put('_n', var.get('n').get('right'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_someU_.func_name = 'someU'
        var.put('someU', PyJsHoisted_someU_)
        @Js
        def PyJsHoisted_some_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('someU')(var.get('n'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_some_.func_name = 'some'
        var.put('some', PyJsHoisted_some_)
        @Js
        def PyJsHoisted_addMinElement_(n, v, this, arguments, var=var):
            var = Scope({'n':n, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', 'n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('bal')(var.get('addMinElement')(var.get('n').get('left'), var.get('v')), var.get('n').get('value'), var.get('n').get('right'))
            else:
                return var.get('singleton')(var.get('v'))
        PyJsHoisted_addMinElement_.func_name = 'addMinElement'
        var.put('addMinElement', PyJsHoisted_addMinElement_)
        @Js
        def PyJsHoisted_addMaxElement_(n, v, this, arguments, var=var):
            var = Scope({'n':n, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', 'n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('bal')(var.get('n').get('left'), var.get('n').get('value'), var.get('addMaxElement')(var.get('n').get('right'), var.get('v')))
            else:
                return var.get('singleton')(var.get('v'))
        PyJsHoisted_addMaxElement_.func_name = 'addMaxElement'
        var.put('addMaxElement', PyJsHoisted_addMaxElement_)
        @Js
        def PyJsHoisted_joinShared_(ln, v, rn, this, arguments, var=var):
            var = Scope({'ln':ln, 'v':v, 'rn':rn, 'this':this, 'arguments':arguments}, var)
            var.registers(['rh', 'lh', 'v', 'ln', 'rn'])
            if PyJsStrictNeq(var.get('ln'),var.get(u"null")):
                if PyJsStrictNeq(var.get('rn'),var.get(u"null")):
                    var.put('lh', var.get('ln').get('height'))
                    var.put('rh', var.get('rn').get('height'))
                    if (var.get('lh')>((var.get('rh')+Js(2.0))|Js(0.0))):
                        return var.get('bal')(var.get('ln').get('left'), var.get('ln').get('value'), var.get('joinShared')(var.get('ln').get('right'), var.get('v'), var.get('rn')))
                    else:
                        if (var.get('rh')>((var.get('lh')+Js(2.0))|Js(0.0))):
                            return var.get('bal')(var.get('joinShared')(var.get('ln'), var.get('v'), var.get('rn').get('left')), var.get('rn').get('value'), var.get('rn').get('right'))
                        else:
                            return var.get('create')(var.get('ln'), var.get('v'), var.get('rn'))
                else:
                    return var.get('addMaxElement')(var.get('ln'), var.get('v'))
            else:
                return var.get('addMinElement')(var.get('rn'), var.get('v'))
        PyJsHoisted_joinShared_.func_name = 'joinShared'
        var.put('joinShared', PyJsHoisted_joinShared_)
        @Js
        def PyJsHoisted_concatShared_(t1, t2, this, arguments, var=var):
            var = Scope({'t1':t1, 't2':t2, 'this':this, 'arguments':arguments}, var)
            var.registers(['t2', 't2r', 'v', 't1'])
            if PyJsStrictNeq(var.get('t1'),var.get(u"null")):
                if PyJsStrictNeq(var.get('t2'),var.get(u"null")):
                    var.put('v', Js({'contents':var.get('t2').get('value')}))
                    var.put('t2r', var.get('removeMinAuxWithRef')(var.get('t2'), var.get('v')))
                    return var.get('joinShared')(var.get('t1'), var.get('v').get('contents'), var.get('t2r'))
                else:
                    return var.get('t1')
            else:
                return var.get('t2')
        PyJsHoisted_concatShared_.func_name = 'concatShared'
        var.put('concatShared', PyJsHoisted_concatShared_)
        @Js
        def PyJsHoisted_partitionSharedU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['lf', 'value', 'match$1', 'pv', 'rf', 'lt', 'match', 'n', 'rt', 'p'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('value', var.get('n').get('value'))
                var.put('match', var.get('partitionSharedU')(var.get('n').get('left'), var.get('p')))
                var.put('lf', var.get('match').get('1'))
                var.put('lt', var.get('match').get('0'))
                var.put('pv', var.get('p')(var.get('value')))
                var.put('match$1', var.get('partitionSharedU')(var.get('n').get('right'), var.get('p')))
                var.put('rf', var.get('match$1').get('1'))
                var.put('rt', var.get('match$1').get('0'))
                if var.get('pv'):
                    return Js([var.get('joinShared')(var.get('lt'), var.get('value'), var.get('rt')), var.get('concatShared')(var.get('lf'), var.get('rf'))])
                else:
                    return Js([var.get('concatShared')(var.get('lt'), var.get('rt')), var.get('joinShared')(var.get('lf'), var.get('value'), var.get('rf'))])
            else:
                return Js([var.get(u"null"), var.get(u"null")])
        PyJsHoisted_partitionSharedU_.func_name = 'partitionSharedU'
        var.put('partitionSharedU', PyJsHoisted_partitionSharedU_)
        @Js
        def PyJsHoisted_partitionShared_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('partitionSharedU')(var.get('n'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_partitionShared_.func_name = 'partitionShared'
        var.put('partitionShared', PyJsHoisted_partitionShared_)
        @Js
        def PyJsHoisted_lengthNode_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['sizeL', 'sizeR', 'r', 'n', 'l'])
            var.put('l', var.get('n').get('left'))
            var.put('r', var.get('n').get('right'))
            var.put('sizeL', (var.get('lengthNode')(var.get('l')) if PyJsStrictNeq(var.get('l'),var.get(u"null")) else Js(0.0)))
            var.put('sizeR', (var.get('lengthNode')(var.get('r')) if PyJsStrictNeq(var.get('r'),var.get(u"null")) else Js(0.0)))
            return ((((Js(1.0)+var.get('sizeL'))|Js(0.0))+var.get('sizeR'))|Js(0.0))
        PyJsHoisted_lengthNode_.func_name = 'lengthNode'
        var.put('lengthNode', PyJsHoisted_lengthNode_)
        @Js
        def PyJsHoisted_size_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('lengthNode')(var.get('n'))
            else:
                return Js(0.0)
        PyJsHoisted_size_.func_name = 'size'
        var.put('size', PyJsHoisted_size_)
        @Js
        def PyJsHoisted_toListAux_(_n, _accu, this, arguments, var=var):
            var = Scope({'_n':_n, '_accu':_accu, 'this':this, 'arguments':arguments}, var)
            var.registers(['accu', '_accu', 'n', '_n'])
            while Js(True):
                var.put('accu', var.get('_accu'))
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('_accu', Js([var.get('n').get('value'), var.get('toListAux')(var.get('n').get('right'), var.get('accu'))]))
                    var.put('_n', var.get('n').get('left'))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_toListAux_.func_name = 'toListAux'
        var.put('toListAux', PyJsHoisted_toListAux_)
        @Js
        def PyJsHoisted_toList_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('toListAux')(var.get('s'), Js(0.0))
        PyJsHoisted_toList_.func_name = 'toList'
        var.put('toList', PyJsHoisted_toList_)
        @Js
        def PyJsHoisted_checkInvariantInternal_(_v, this, arguments, var=var):
            var = Scope({'_v':_v, 'this':this, 'arguments':arguments}, var)
            var.registers(['_v', 'r', 'v', 'diff', 'l'])
            while Js(True):
                var.put('v', var.get('_v'))
                if PyJsStrictNeq(var.get('v'),var.get(u"null")):
                    var.put('l', var.get('v').get('left'))
                    var.put('r', var.get('v').get('right'))
                    var.put('diff', ((var.get('treeHeight')(var.get('l'))-var.get('treeHeight')(var.get('r')))|Js(0.0)))
                    if ((var.get('diff')<=Js(2.0)) and (var.get('diff')>=(-Js(2.0)))).neg():
                        PyJsTempException = JsToPyException(var.get('Error').create(Js('File "belt_internalAVLset.ml", line 304, characters 6-12')))
                        raise PyJsTempException
                    var.get('checkInvariantInternal')(var.get('l'))
                    var.put('_v', var.get('r'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_checkInvariantInternal_.func_name = 'checkInvariantInternal'
        var.put('checkInvariantInternal', PyJsHoisted_checkInvariantInternal_)
        @Js
        def PyJsHoisted_fillArray_(_n, _i, arr, this, arguments, var=var):
            var = Scope({'_n':_n, '_i':_i, 'arr':arr, 'this':this, 'arguments':arguments}, var)
            var.registers(['rnext', 'r', 'v', 'next', '_i', 'n', '_n', 'arr', 'i', 'l'])
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('n', var.get('_n'))
                var.put('l', var.get('n').get('left'))
                var.put('v', var.get('n').get('value'))
                var.put('r', var.get('n').get('right'))
                var.put('next', (var.get('fillArray')(var.get('l'), var.get('i'), var.get('arr')) if PyJsStrictNeq(var.get('l'),var.get(u"null")) else var.get('i')))
                var.get('arr').put(var.get('next'), var.get('v'))
                var.put('rnext', ((var.get('next')+Js(1.0))|Js(0.0)))
                if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                    var.put('_i', var.get('rnext'))
                    var.put('_n', var.get('r'))
                    continue
                else:
                    return var.get('rnext')
            pass
        PyJsHoisted_fillArray_.func_name = 'fillArray'
        var.put('fillArray', PyJsHoisted_fillArray_)
        @Js
        def PyJsHoisted_fillArrayWithPartition_(_n, cursor, arr, p, this, arguments, var=var):
            var = Scope({'_n':_n, 'cursor':cursor, 'arr':arr, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'r', 'v', 'cursor', 'c$1', 'n', '_n', 'arr', 'p', 'l'])
            while Js(True):
                var.put('n', var.get('_n'))
                var.put('l', var.get('n').get('left'))
                var.put('v', var.get('n').get('value'))
                var.put('r', var.get('n').get('right'))
                if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                    var.get('fillArrayWithPartition')(var.get('l'), var.get('cursor'), var.get('arr'), var.get('p'))
                if var.get('p')(var.get('v')):
                    var.put('c', var.get('cursor').get('forward'))
                    var.get('arr').put(var.get('c'), var.get('v'))
                    var.get('cursor').put('forward', ((var.get('c')+Js(1.0))|Js(0.0)))
                else:
                    var.put('c$1', var.get('cursor').get('backward'))
                    var.get('arr').put(var.get('c$1'), var.get('v'))
                    var.get('cursor').put('backward', ((var.get('c$1')-Js(1.0))|Js(0.0)))
                if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                    var.put('_n', var.get('r'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_fillArrayWithPartition_.func_name = 'fillArrayWithPartition'
        var.put('fillArrayWithPartition', PyJsHoisted_fillArrayWithPartition_)
        @Js
        def PyJsHoisted_fillArrayWithFilter_(_n, _i, arr, p, this, arguments, var=var):
            var = Scope({'_n':_n, '_i':_i, 'arr':arr, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['rnext', 'p', 'r', 'v', 'next', '_i', 'n', '_n', 'arr', 'i', 'l'])
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('n', var.get('_n'))
                var.put('l', var.get('n').get('left'))
                var.put('v', var.get('n').get('value'))
                var.put('r', var.get('n').get('right'))
                var.put('next', (var.get('fillArrayWithFilter')(var.get('l'), var.get('i'), var.get('arr'), var.get('p')) if PyJsStrictNeq(var.get('l'),var.get(u"null")) else var.get('i')))
                var.put('rnext', (PyJsComma(var.get('arr').put(var.get('next'), var.get('v')),((var.get('next')+Js(1.0))|Js(0.0))) if var.get('p')(var.get('v')) else var.get('next')))
                if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                    var.put('_i', var.get('rnext'))
                    var.put('_n', var.get('r'))
                    continue
                else:
                    return var.get('rnext')
            pass
        PyJsHoisted_fillArrayWithFilter_.func_name = 'fillArrayWithFilter'
        var.put('fillArrayWithFilter', PyJsHoisted_fillArrayWithFilter_)
        @Js
        def PyJsHoisted_toArray_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['size', 'n', 'v'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('size', var.get('lengthNode')(var.get('n')))
                var.put('v', var.get('Array').create(var.get('size')))
                var.get('fillArray')(var.get('n'), Js(0.0), var.get('v'))
                return var.get('v')
            else:
                return Js([])
        PyJsHoisted_toArray_.func_name = 'toArray'
        var.put('toArray', PyJsHoisted_toArray_)
        @Js
        def PyJsHoisted_fromSortedArrayRevAux_(arr, off, len, this, arguments, var=var):
            var = Scope({'arr':arr, 'off':off, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'nl', 'off', 'x1', 'mid', 'x0', 'x1$1', 'x2', 'x0$1', 'arr', 'left', 'right'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('len'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    return var.get(u"null")
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('singleton')(var.get('arr').get(var.get('off')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('x0', var.get('arr').get(var.get('off')))
                    var.put('x1', var.get('arr').get(((var.get('off')-Js(1.0))|Js(0.0))))
                    return Js({'value':var.get('x1'),'height':Js(2.0),'left':var.get('singleton')(var.get('x0')),'right':var.get(u"null")})
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('x0$1', var.get('arr').get(var.get('off')))
                    var.put('x1$1', var.get('arr').get(((var.get('off')-Js(1.0))|Js(0.0))))
                    var.put('x2', var.get('arr').get(((var.get('off')-Js(2.0))|Js(0.0))))
                    return Js({'value':var.get('x1$1'),'height':Js(2.0),'left':var.get('singleton')(var.get('x0$1')),'right':var.get('singleton')(var.get('x2'))})
                if True:
                    SWITCHED = True
                    var.put('nl', ((var.get('len')/Js(2.0))|Js(0.0)))
                    var.put('left', var.get('fromSortedArrayRevAux')(var.get('arr'), var.get('off'), var.get('nl')))
                    var.put('mid', var.get('arr').get(((var.get('off')-var.get('nl'))|Js(0.0))))
                    var.put('right', var.get('fromSortedArrayRevAux')(var.get('arr'), ((((var.get('off')-var.get('nl'))|Js(0.0))-Js(1.0))|Js(0.0)), ((((var.get('len')-var.get('nl'))|Js(0.0))-Js(1.0))|Js(0.0))))
                    return var.get('create')(var.get('left'), var.get('mid'), var.get('right'))
                SWITCHED = True
                break
        PyJsHoisted_fromSortedArrayRevAux_.func_name = 'fromSortedArrayRevAux'
        var.put('fromSortedArrayRevAux', PyJsHoisted_fromSortedArrayRevAux_)
        @Js
        def PyJsHoisted_fromSortedArrayAux_(arr, off, len, this, arguments, var=var):
            var = Scope({'arr':arr, 'off':off, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'nl', 'off', 'x1', 'mid', 'x0', 'x1$1', 'x2', 'x0$1', 'arr', 'left', 'right'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('len'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    return var.get(u"null")
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('singleton')(var.get('arr').get(var.get('off')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('x0', var.get('arr').get(var.get('off')))
                    var.put('x1', var.get('arr').get(((var.get('off')+Js(1.0))|Js(0.0))))
                    return Js({'value':var.get('x1'),'height':Js(2.0),'left':var.get('singleton')(var.get('x0')),'right':var.get(u"null")})
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('x0$1', var.get('arr').get(var.get('off')))
                    var.put('x1$1', var.get('arr').get(((var.get('off')+Js(1.0))|Js(0.0))))
                    var.put('x2', var.get('arr').get(((var.get('off')+Js(2.0))|Js(0.0))))
                    return Js({'value':var.get('x1$1'),'height':Js(2.0),'left':var.get('singleton')(var.get('x0$1')),'right':var.get('singleton')(var.get('x2'))})
                if True:
                    SWITCHED = True
                    var.put('nl', ((var.get('len')/Js(2.0))|Js(0.0)))
                    var.put('left', var.get('fromSortedArrayAux')(var.get('arr'), var.get('off'), var.get('nl')))
                    var.put('mid', var.get('arr').get(((var.get('off')+var.get('nl'))|Js(0.0))))
                    var.put('right', var.get('fromSortedArrayAux')(var.get('arr'), ((((var.get('off')+var.get('nl'))|Js(0.0))+Js(1.0))|Js(0.0)), ((((var.get('len')-var.get('nl'))|Js(0.0))-Js(1.0))|Js(0.0))))
                    return var.get('create')(var.get('left'), var.get('mid'), var.get('right'))
                SWITCHED = True
                break
        PyJsHoisted_fromSortedArrayAux_.func_name = 'fromSortedArrayAux'
        var.put('fromSortedArrayAux', PyJsHoisted_fromSortedArrayAux_)
        @Js
        def PyJsHoisted_fromSortedArrayUnsafe_(arr, this, arguments, var=var):
            var = Scope({'arr':arr, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr'])
            return var.get('fromSortedArrayAux')(var.get('arr'), Js(0.0), var.get('arr').get('length'))
        PyJsHoisted_fromSortedArrayUnsafe_.func_name = 'fromSortedArrayUnsafe'
        var.put('fromSortedArrayUnsafe', PyJsHoisted_fromSortedArrayUnsafe_)
        @Js
        def PyJsHoisted_keepSharedU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['newL', 'pv', 'r', 'v', 'n', 'p', 'newR', 'l'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('l', var.get('n').get('left'))
                var.put('v', var.get('n').get('value'))
                var.put('r', var.get('n').get('right'))
                var.put('newL', var.get('keepSharedU')(var.get('l'), var.get('p')))
                var.put('pv', var.get('p')(var.get('v')))
                var.put('newR', var.get('keepSharedU')(var.get('r'), var.get('p')))
                if var.get('pv'):
                    if (PyJsStrictEq(var.get('l'),var.get('newL')) and PyJsStrictEq(var.get('r'),var.get('newR'))):
                        return var.get('n')
                    else:
                        return var.get('joinShared')(var.get('newL'), var.get('v'), var.get('newR'))
                else:
                    return var.get('concatShared')(var.get('newL'), var.get('newR'))
            else:
                return var.get(u"null")
        PyJsHoisted_keepSharedU_.func_name = 'keepSharedU'
        var.put('keepSharedU', PyJsHoisted_keepSharedU_)
        @Js
        def PyJsHoisted_keepShared_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('keepSharedU')(var.get('n'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_keepShared_.func_name = 'keepShared'
        var.put('keepShared', PyJsHoisted_keepShared_)
        @Js
        def PyJsHoisted_keepCopyU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', 'size', 'last', 'n', 'p'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('size', var.get('lengthNode')(var.get('n')))
                var.put('v', var.get('Array').create(var.get('size')))
                var.put('last', var.get('fillArrayWithFilter')(var.get('n'), Js(0.0), var.get('v'), var.get('p')))
                return var.get('fromSortedArrayAux')(var.get('v'), Js(0.0), var.get('last'))
            else:
                return var.get(u"null")
        PyJsHoisted_keepCopyU_.func_name = 'keepCopyU'
        var.put('keepCopyU', PyJsHoisted_keepCopyU_)
        @Js
        def PyJsHoisted_keepCopy_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('keepCopyU')(var.get('n'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_keepCopy_.func_name = 'keepCopy'
        var.put('keepCopy', PyJsHoisted_keepCopy_)
        @Js
        def PyJsHoisted_partitionCopyU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['forwardLen', 'v', 'backward', 'size', 'n', 'p', 'cursor'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('size', var.get('lengthNode')(var.get('n')))
                var.put('v', var.get('Array').create(var.get('size')))
                var.put('backward', ((var.get('size')-Js(1.0))|Js(0.0)))
                var.put('cursor', Js({'forward':Js(0.0),'backward':var.get('backward')}))
                var.get('fillArrayWithPartition')(var.get('n'), var.get('cursor'), var.get('v'), var.get('p'))
                var.put('forwardLen', var.get('cursor').get('forward'))
                return Js([var.get('fromSortedArrayAux')(var.get('v'), Js(0.0), var.get('forwardLen')), var.get('fromSortedArrayRevAux')(var.get('v'), var.get('backward'), ((var.get('size')-var.get('forwardLen'))|Js(0.0)))])
            else:
                return Js([var.get(u"null"), var.get(u"null")])
        PyJsHoisted_partitionCopyU_.func_name = 'partitionCopyU'
        var.put('partitionCopyU', PyJsHoisted_partitionCopyU_)
        @Js
        def PyJsHoisted_partitionCopy_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('partitionCopyU')(var.get('n'), var.get('Curry').callprop('__1', var.get('p')))
        PyJsHoisted_partitionCopy_.func_name = 'partitionCopy'
        var.put('partitionCopy', PyJsHoisted_partitionCopy_)
        @Js
        def PyJsHoisted_has_(_t, x, cmp, this, arguments, var=var):
            var = Scope({'_t':_t, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['t', 'c', 'cmp', 'v', 'x', '_t'])
            while Js(True):
                var.put('t', var.get('_t'))
                if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                    var.put('v', var.get('t').get('value'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return Js(True)
                    else:
                        var.put('_t', (var.get('t').get('left') if (var.get('c')<Js(0.0)) else var.get('t').get('right')))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_has_.func_name = 'has'
        var.put('has', PyJsHoisted_has_)
        @Js
        def PyJsHoisted_cmp_(s1, s2, PyJsArg_636d702431_, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'cmp$1':PyJsArg_636d702431_, 'this':this, 'arguments':arguments}, var)
            var.registers(['cmp$2', 'h1', '_e2', 'len1', 'c', 'e1', 's2', 'cmp$1', 's1', 'e2', '_e1', 'h2', 'len2'])
            var.put('len1', var.get('size')(var.get('s1')))
            var.put('len2', var.get('size')(var.get('s2')))
            if PyJsStrictEq(var.get('len1'),var.get('len2')):
                var.put('_e1', var.get('stackAllLeft')(var.get('s1'), Js(0.0)))
                var.put('_e2', var.get('stackAllLeft')(var.get('s2'), Js(0.0)))
                var.put('cmp$2', var.get('cmp$1'))
                while Js(True):
                    var.put('e2', var.get('_e2'))
                    var.put('e1', var.get('_e1'))
                    if (var.get('e1') and var.get('e2')):
                        var.put('h2', var.get('e2').get('0'))
                        var.put('h1', var.get('e1').get('0'))
                        var.put('c', var.get('cmp$2')(var.get('h1').get('value'), var.get('h2').get('value')))
                        if PyJsStrictEq(var.get('c'),Js(0.0)):
                            var.put('_e2', var.get('stackAllLeft')(var.get('h2').get('right'), var.get('e2').get('1')))
                            var.put('_e1', var.get('stackAllLeft')(var.get('h1').get('right'), var.get('e1').get('1')))
                            continue
                        else:
                            return var.get('c')
                    else:
                        return Js(0.0)
                pass
            else:
                if (var.get('len1')<var.get('len2')):
                    return (-Js(1.0))
                else:
                    return Js(1.0)
        PyJsHoisted_cmp_.func_name = 'cmp'
        var.put('cmp', PyJsHoisted_cmp_)
        @Js
        def PyJsHoisted_eq_(s1, s2, c, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['s1', 's2', 'c'])
            return PyJsStrictEq(var.get('cmp')(var.get('s1'), var.get('s2'), var.get('c')),Js(0.0))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_subset_(_s1, _s2, cmp, this, arguments, var=var):
            var = Scope({'_s1':_s1, '_s2':_s2, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['l2', 'l1', 'r2', 'c', 'cmp', 'v2', 's2', '_s1', '_s2', 's1', 'r1', 'v1'])
            while Js(True):
                var.put('s2', var.get('_s2'))
                var.put('s1', var.get('_s1'))
                if PyJsStrictNeq(var.get('s1'),var.get(u"null")):
                    if PyJsStrictNeq(var.get('s2'),var.get(u"null")):
                        var.put('l1', var.get('s1').get('left'))
                        var.put('v1', var.get('s1').get('value'))
                        var.put('r1', var.get('s1').get('right'))
                        var.put('l2', var.get('s2').get('left'))
                        var.put('v2', var.get('s2').get('value'))
                        var.put('r2', var.get('s2').get('right'))
                        var.put('c', var.get('cmp')(var.get('v1'), var.get('v2')))
                        if PyJsStrictEq(var.get('c'),Js(0.0)):
                            if var.get('subset')(var.get('l1'), var.get('l2'), var.get('cmp')):
                                var.put('_s2', var.get('r2'))
                                var.put('_s1', var.get('r1'))
                                continue
                            else:
                                return Js(False)
                        else:
                            if (var.get('c')<Js(0.0)):
                                if var.get('subset')(var.get('create')(var.get('l1'), var.get('v1'), var.get(u"null")), var.get('l2'), var.get('cmp')):
                                    var.put('_s1', var.get('r1'))
                                    continue
                                else:
                                    return Js(False)
                            else:
                                if var.get('subset')(var.get('create')(var.get(u"null"), var.get('v1'), var.get('r1')), var.get('r2'), var.get('cmp')):
                                    var.put('_s1', var.get('l1'))
                                    continue
                                else:
                                    return Js(False)
                    else:
                        return Js(False)
                else:
                    return Js(True)
            pass
        PyJsHoisted_subset_.func_name = 'subset'
        var.put('subset', PyJsHoisted_subset_)
        @Js
        def PyJsHoisted_get_(_n, x, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('value'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return var.get('Caml_option').callprop('some', var.get('v'))
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    return var.get('undefined')
            pass
        PyJsHoisted_get_.func_name = 'get'
        var.put('get', PyJsHoisted_get_)
        @Js
        def PyJsHoisted_getUndefined_(_n, x, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('value'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return var.get('v')
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    return var.get('undefined')
            pass
        PyJsHoisted_getUndefined_.func_name = 'getUndefined'
        var.put('getUndefined', PyJsHoisted_getUndefined_)
        @Js
        def PyJsHoisted_getExn_(_n, x, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('value'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return var.get('v')
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    PyJsTempException = JsToPyException(var.get('Error').create(Js('getExn0')))
                    raise PyJsTempException
            pass
        PyJsHoisted_getExn_.func_name = 'getExn'
        var.put('getExn', PyJsHoisted_getExn_)
        @Js
        def PyJsHoisted_rotateWithLeftChild_(k2, this, arguments, var=var):
            var = Scope({'k2':k2, 'this':this, 'arguments':arguments}, var)
            var.registers(['hrk2', 'hk2', 'k2', 'hlk2', 'hlk1', 'k1'])
            var.put('k1', var.get('k2').get('left'))
            var.get('k2').put('left', var.get('k1').get('right'))
            var.get('k1').put('right', var.get('k2'))
            var.put('hlk2', var.get('treeHeight')(var.get('k2').get('left')))
            var.put('hrk2', var.get('treeHeight')(var.get('k2').get('right')))
            var.get('k2').put('height', (((var.get('hlk2') if (var.get('hlk2')>var.get('hrk2')) else var.get('hrk2'))+Js(1.0))|Js(0.0)))
            var.put('hlk1', var.get('treeHeight')(var.get('k1').get('left')))
            var.put('hk2', var.get('k2').get('height'))
            var.get('k1').put('height', (((var.get('hlk1') if (var.get('hlk1')>var.get('hk2')) else var.get('hk2'))+Js(1.0))|Js(0.0)))
            return var.get('k1')
        PyJsHoisted_rotateWithLeftChild_.func_name = 'rotateWithLeftChild'
        var.put('rotateWithLeftChild', PyJsHoisted_rotateWithLeftChild_)
        @Js
        def PyJsHoisted_rotateWithRightChild_(k1, this, arguments, var=var):
            var = Scope({'k1':k1, 'this':this, 'arguments':arguments}, var)
            var.registers(['hrk1', 'hrk2', 'k2', 'hlk1', 'k1', 'hk1'])
            var.put('k2', var.get('k1').get('right'))
            var.get('k1').put('right', var.get('k2').get('left'))
            var.get('k2').put('left', var.get('k1'))
            var.put('hlk1', var.get('treeHeight')(var.get('k1').get('left')))
            var.put('hrk1', var.get('treeHeight')(var.get('k1').get('right')))
            var.get('k1').put('height', (((var.get('hlk1') if (var.get('hlk1')>var.get('hrk1')) else var.get('hrk1'))+Js(1.0))|Js(0.0)))
            var.put('hrk2', var.get('treeHeight')(var.get('k2').get('right')))
            var.put('hk1', var.get('k1').get('height'))
            var.get('k2').put('height', (((var.get('hrk2') if (var.get('hrk2')>var.get('hk1')) else var.get('hk1'))+Js(1.0))|Js(0.0)))
            return var.get('k2')
        PyJsHoisted_rotateWithRightChild_.func_name = 'rotateWithRightChild'
        var.put('rotateWithRightChild', PyJsHoisted_rotateWithRightChild_)
        @Js
        def PyJsHoisted_doubleWithLeftChild_(k3, this, arguments, var=var):
            var = Scope({'k3':k3, 'this':this, 'arguments':arguments}, var)
            var.registers(['k3', 'v'])
            var.put('v', var.get('rotateWithRightChild')(var.get('k3').get('left')))
            var.get('k3').put('left', var.get('v'))
            return var.get('rotateWithLeftChild')(var.get('k3'))
        PyJsHoisted_doubleWithLeftChild_.func_name = 'doubleWithLeftChild'
        var.put('doubleWithLeftChild', PyJsHoisted_doubleWithLeftChild_)
        @Js
        def PyJsHoisted_doubleWithRightChild_(k2, this, arguments, var=var):
            var = Scope({'k2':k2, 'this':this, 'arguments':arguments}, var)
            var.registers(['k2', 'v'])
            var.put('v', var.get('rotateWithLeftChild')(var.get('k2').get('right')))
            var.get('k2').put('right', var.get('v'))
            return var.get('rotateWithRightChild')(var.get('k2'))
        PyJsHoisted_doubleWithRightChild_.func_name = 'doubleWithRightChild'
        var.put('doubleWithRightChild', PyJsHoisted_doubleWithRightChild_)
        @Js
        def PyJsHoisted_heightUpdateMutate_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['hlt', 't', 'hrt'])
            var.put('hlt', var.get('treeHeight')(var.get('t').get('left')))
            var.put('hrt', var.get('treeHeight')(var.get('t').get('right')))
            var.get('t').put('height', (((var.get('hlt') if (var.get('hlt')>var.get('hrt')) else var.get('hrt'))+Js(1.0))|Js(0.0)))
            return var.get('t')
        PyJsHoisted_heightUpdateMutate_.func_name = 'heightUpdateMutate'
        var.put('heightUpdateMutate', PyJsHoisted_heightUpdateMutate_)
        @Js
        def PyJsHoisted_balMutate_(nt, this, arguments, var=var):
            var = Scope({'nt':nt, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 'hl', 'hr', 'rr', 'nt', 'r', 'lr', 'rl', 'l'])
            var.put('l', var.get('nt').get('left'))
            var.put('r', var.get('nt').get('right'))
            var.put('hl', var.get('treeHeight')(var.get('l')))
            var.put('hr', var.get('treeHeight')(var.get('r')))
            if (var.get('hl')>((Js(2.0)+var.get('hr'))|Js(0.0))):
                var.put('ll', var.get('l').get('left'))
                var.put('lr', var.get('l').get('right'))
                if var.get('heightGe')(var.get('ll'), var.get('lr')):
                    return var.get('heightUpdateMutate')(var.get('rotateWithLeftChild')(var.get('nt')))
                else:
                    return var.get('heightUpdateMutate')(var.get('doubleWithLeftChild')(var.get('nt')))
            else:
                if (var.get('hr')>((Js(2.0)+var.get('hl'))|Js(0.0))):
                    var.put('rl', var.get('r').get('left'))
                    var.put('rr', var.get('r').get('right'))
                    if var.get('heightGe')(var.get('rr'), var.get('rl')):
                        return var.get('heightUpdateMutate')(var.get('rotateWithRightChild')(var.get('nt')))
                    else:
                        return var.get('heightUpdateMutate')(var.get('doubleWithRightChild')(var.get('nt')))
                else:
                    var.get('nt').put('height', (((var.get('hl') if (var.get('hl')>var.get('hr')) else var.get('hr'))+Js(1.0))|Js(0.0)))
                    return var.get('nt')
        PyJsHoisted_balMutate_.func_name = 'balMutate'
        var.put('balMutate', PyJsHoisted_balMutate_)
        @Js
        def PyJsHoisted_addMutate_(cmp, t, x, this, arguments, var=var):
            var = Scope({'cmp':cmp, 't':t, 'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 't', 'c', 'cmp', 'r', 'x', 'k', 'l'])
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('k', var.get('t').get('value'))
                var.put('c', var.get('cmp')(var.get('x'), var.get('k')))
                if PyJsStrictEq(var.get('c'),Js(0.0)):
                    return var.get('t')
                else:
                    var.put('l', var.get('t').get('left'))
                    var.put('r', var.get('t').get('right'))
                    if (var.get('c')<Js(0.0)):
                        var.put('ll', var.get('addMutate')(var.get('cmp'), var.get('l'), var.get('x')))
                        var.get('t').put('left', var.get('ll'))
                    else:
                        var.get('t').put('right', var.get('addMutate')(var.get('cmp'), var.get('r'), var.get('x')))
                    return var.get('balMutate')(var.get('t'))
            else:
                return var.get('singleton')(var.get('x'))
        PyJsHoisted_addMutate_.func_name = 'addMutate'
        var.put('addMutate', PyJsHoisted_addMutate_)
        @Js
        def PyJsHoisted_fromArray_(xs, cmp, this, arguments, var=var):
            var = Scope({'xs':xs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'result', 'i_finish', 'cmp', 'next', 'i'])
            var.put('len', var.get('xs').get('length'))
            if PyJsStrictEq(var.get('len'),Js(0.0)):
                return var.get(u"null")
            else:
                @Js
                def PyJs_anonymous_12_(x, y, this, arguments, var=var):
                    var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
                    var.registers(['y', 'x'])
                    return (var.get('cmp')(var.get('x'), var.get('y'))<Js(0.0))
                PyJs_anonymous_12_._set_name('anonymous')
                var.put('next', var.get('Belt_SortArray').callprop('strictlySortedLengthU', var.get('xs'), PyJs_anonymous_12_))
                pass
                if (var.get('next')>=Js(0.0)):
                    var.put('result', var.get('fromSortedArrayAux')(var.get('xs'), Js(0.0), var.get('next')))
                else:
                    var.put('next', ((-var.get('next'))|Js(0.0)))
                    var.put('result', var.get('fromSortedArrayRevAux')(var.get('xs'), ((var.get('next')-Js(1.0))|Js(0.0)), var.get('next')))
                #for JS loop
                var.put('i', var.get('next'))
                var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.put('result', var.get('addMutate')(var.get('cmp'), var.get('result'), var.get('xs').get(var.get('i'))))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('result')
        PyJsHoisted_fromArray_.func_name = 'fromArray'
        var.put('fromArray', PyJsHoisted_fromArray_)
        @Js
        def PyJsHoisted_removeMinAuxWithRootMutate_(nt, n, this, arguments, var=var):
            var = Scope({'nt':nt, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['ln', 'nt', 'rn', 'n'])
            var.put('rn', var.get('n').get('right'))
            var.put('ln', var.get('n').get('left'))
            if PyJsStrictNeq(var.get('ln'),var.get(u"null")):
                var.get('n').put('left', var.get('removeMinAuxWithRootMutate')(var.get('nt'), var.get('ln')))
                return var.get('balMutate')(var.get('n'))
            else:
                var.get('nt').put('value', var.get('n').get('value'))
                return var.get('rn')
        PyJsHoisted_removeMinAuxWithRootMutate_.func_name = 'removeMinAuxWithRootMutate'
        var.put('removeMinAuxWithRootMutate', PyJsHoisted_removeMinAuxWithRootMutate_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Caml_option', var.get('require')(Js('./caml_option.js')))
        var.put('Belt_SortArray', var.get('require')(Js('./belt_SortArray.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('copy', var.get('copy'))
        var.get('exports').put('create', var.get('create'))
        var.get('exports').put('bal', var.get('bal'))
        var.get('exports').put('singleton', var.get('singleton'))
        var.get('exports').put('minimum', var.get('minimum'))
        var.get('exports').put('minUndefined', var.get('minUndefined'))
        var.get('exports').put('maximum', var.get('maximum'))
        var.get('exports').put('maxUndefined', var.get('maxUndefined'))
        var.get('exports').put('removeMinAuxWithRef', var.get('removeMinAuxWithRef'))
        var.get('exports').put('isEmpty', var.get('isEmpty'))
        var.get('exports').put('stackAllLeft', var.get('stackAllLeft'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('joinShared', var.get('joinShared'))
        var.get('exports').put('concatShared', var.get('concatShared'))
        var.get('exports').put('keepSharedU', var.get('keepSharedU'))
        var.get('exports').put('keepShared', var.get('keepShared'))
        var.get('exports').put('keepCopyU', var.get('keepCopyU'))
        var.get('exports').put('keepCopy', var.get('keepCopy'))
        var.get('exports').put('partitionSharedU', var.get('partitionSharedU'))
        var.get('exports').put('partitionShared', var.get('partitionShared'))
        var.get('exports').put('partitionCopyU', var.get('partitionCopyU'))
        var.get('exports').put('partitionCopy', var.get('partitionCopy'))
        var.get('exports').put('lengthNode', var.get('lengthNode'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('toList', var.get('toList'))
        var.get('exports').put('checkInvariantInternal', var.get('checkInvariantInternal'))
        var.get('exports').put('fillArray', var.get('fillArray'))
        var.get('exports').put('toArray', var.get('toArray'))
        var.get('exports').put('fromSortedArrayAux', var.get('fromSortedArrayAux'))
        var.get('exports').put('fromSortedArrayRevAux', var.get('fromSortedArrayRevAux'))
        var.get('exports').put('fromSortedArrayUnsafe', var.get('fromSortedArrayUnsafe'))
        var.get('exports').put('has', var.get('has'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('subset', var.get('subset'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getUndefined', var.get('getUndefined'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('fromArray', var.get('fromArray'))
        var.get('exports').put('addMutate', var.get('addMutate'))
        var.get('exports').put('balMutate', var.get('balMutate'))
        var.get('exports').put('removeMinAuxWithRootMutate', var.get('removeMinAuxWithRootMutate'))
    PyJs_anonymous_11_._set_name('anonymous')
    @Js
    def PyJs_anonymous_13_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['minKey0Aux', 'minKeyUndefined', 'keysToArray', 'heightUpdateMutate', 'addMinElement', 'doubleWithRightChild', 'everyU', 'removeMinAuxWithRef', 'fillArrayKey', 'concatOrJoin', 'eq', 'rotateWithRightChild', 'cmp', 'minUndefined', 'addMaxElement', 'reduceU', 'isEmpty', 'forEach', 'keepMap', 'bal', 'get', 'maxKV0Aux', 'treeHeight', 'fromSortedArrayRevAux', 'partitionSharedU', 'partitionShared', 'minKV0Aux', 'maxKey0Aux', 'maxKeyUndefined', 'require', 'rotateWithLeftChild', 'getExn', 'updateValue', 'someU', 'heightGe', 'findFirstByU', 'fillArrayValue', 'reduce', 'updateMutate', 'Belt_SortArray', 'mapU', 'Caml_option', 'maximum', 'toArray', 'every', 'lengthNode', 'getWithDefault', 'toListAux', 'module', 'size', 'keepMapU', 'cmpU', 'copy', 'findFirstBy', 'singleton', 'toList', 'keepSharedU', 'concat', 'eqU', 'getUndefined', 'removeMinAuxWithRootMutate', 'join', 'doubleWithLeftChild', 'forEachU', 'exports', 'map', 'stackAllLeft', 'maxKey', 'some', 'mapWithKey', 'fromArray', 'balMutate', 'fromSortedArrayUnsafe', 'keepShared', 'maxUndefined', 'mapWithKeyU', 'minKey', 'create', 'Curry', 'fromSortedArrayAux', 'valuesToArray', 'has', 'minimum', 'checkInvariantInternal', 'fillArray'])
        @Js
        def PyJsHoisted_treeHeight_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('n').get('height')
            else:
                return Js(0.0)
        PyJsHoisted_treeHeight_.func_name = 'treeHeight'
        var.put('treeHeight', PyJsHoisted_treeHeight_)
        @Js
        def PyJsHoisted_copy_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'l'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('l', var.get('n').get('left'))
                var.put('r', var.get('n').get('right'))
                return Js({'key':var.get('n').get('key'),'value':var.get('n').get('value'),'height':var.get('n').get('height'),'left':var.get('copy')(var.get('l')),'right':var.get('copy')(var.get('r'))})
            else:
                return var.get('n')
        PyJsHoisted_copy_.func_name = 'copy'
        var.put('copy', PyJsHoisted_copy_)
        @Js
        def PyJsHoisted_create_(l, x, d, r, this, arguments, var=var):
            var = Scope({'l':l, 'x':x, 'd':d, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['hl', 'hr', 'r', 'x', 'd', 'l'])
            var.put('hl', var.get('treeHeight')(var.get('l')))
            var.put('hr', var.get('treeHeight')(var.get('r')))
            return Js({'key':var.get('x'),'value':var.get('d'),'height':(((var.get('hl')+Js(1.0))|Js(0.0)) if (var.get('hl')>=var.get('hr')) else ((var.get('hr')+Js(1.0))|Js(0.0))),'left':var.get('l'),'right':var.get('r')})
        PyJsHoisted_create_.func_name = 'create'
        var.put('create', PyJsHoisted_create_)
        @Js
        def PyJsHoisted_singleton_(x, d, this, arguments, var=var):
            var = Scope({'x':x, 'd':d, 'this':this, 'arguments':arguments}, var)
            var.registers(['d', 'x'])
            return Js({'key':var.get('x'),'value':var.get('d'),'height':Js(1.0),'left':var.get(u"null"),'right':var.get(u"null")})
        PyJsHoisted_singleton_.func_name = 'singleton'
        var.put('singleton', PyJsHoisted_singleton_)
        @Js
        def PyJsHoisted_heightGe_(l, r, this, arguments, var=var):
            var = Scope({'l':l, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'l'])
            if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                if PyJsStrictNeq(var.get('l'),var.get(u"null")):
                    return (var.get('l').get('height')>=var.get('r').get('height'))
                else:
                    return Js(False)
            else:
                return Js(True)
        PyJsHoisted_heightGe_.func_name = 'heightGe'
        var.put('heightGe', PyJsHoisted_heightGe_)
        @Js
        def PyJsHoisted_updateValue_(n, newValue, this, arguments, var=var):
            var = Scope({'n':n, 'newValue':newValue, 'this':this, 'arguments':arguments}, var)
            var.registers(['newValue', 'n'])
            if PyJsStrictEq(var.get('n').get('value'),var.get('newValue')):
                return var.get('n')
            else:
                return Js({'key':var.get('n').get('key'),'value':var.get('newValue'),'height':var.get('n').get('height'),'left':var.get('n').get('left'),'right':var.get('n').get('right')})
        PyJsHoisted_updateValue_.func_name = 'updateValue'
        var.put('updateValue', PyJsHoisted_updateValue_)
        @Js
        def PyJsHoisted_bal_(l, x, d, r, this, arguments, var=var):
            var = Scope({'l':l, 'x':x, 'd':d, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['ld', 'hr', 'rlr', 'rd', 'rld', 'lrd', 'll', 'rv', 'rr', 'r', 'x', 'rl', 'lrv', 'lrl', 'd', 'hl', 'lv', 'rll', 'lr', 'rlv', 'lrr', 'l'])
            var.put('hl', (var.get('l').get('height') if PyJsStrictNeq(var.get('l'),var.get(u"null")) else Js(0.0)))
            var.put('hr', (var.get('r').get('height') if PyJsStrictNeq(var.get('r'),var.get(u"null")) else Js(0.0)))
            if (var.get('hl')>((var.get('hr')+Js(2.0))|Js(0.0))):
                var.put('ll', var.get('l').get('left'))
                var.put('lv', var.get('l').get('key'))
                var.put('ld', var.get('l').get('value'))
                var.put('lr', var.get('l').get('right'))
                if (var.get('treeHeight')(var.get('ll'))>=var.get('treeHeight')(var.get('lr'))):
                    return var.get('create')(var.get('ll'), var.get('lv'), var.get('ld'), var.get('create')(var.get('lr'), var.get('x'), var.get('d'), var.get('r')))
                else:
                    var.put('lrl', var.get('lr').get('left'))
                    var.put('lrv', var.get('lr').get('key'))
                    var.put('lrd', var.get('lr').get('value'))
                    var.put('lrr', var.get('lr').get('right'))
                    return var.get('create')(var.get('create')(var.get('ll'), var.get('lv'), var.get('ld'), var.get('lrl')), var.get('lrv'), var.get('lrd'), var.get('create')(var.get('lrr'), var.get('x'), var.get('d'), var.get('r')))
            else:
                if (var.get('hr')>((var.get('hl')+Js(2.0))|Js(0.0))):
                    var.put('rl', var.get('r').get('left'))
                    var.put('rv', var.get('r').get('key'))
                    var.put('rd', var.get('r').get('value'))
                    var.put('rr', var.get('r').get('right'))
                    if (var.get('treeHeight')(var.get('rr'))>=var.get('treeHeight')(var.get('rl'))):
                        return var.get('create')(var.get('create')(var.get('l'), var.get('x'), var.get('d'), var.get('rl')), var.get('rv'), var.get('rd'), var.get('rr'))
                    else:
                        var.put('rll', var.get('rl').get('left'))
                        var.put('rlv', var.get('rl').get('key'))
                        var.put('rld', var.get('rl').get('value'))
                        var.put('rlr', var.get('rl').get('right'))
                        return var.get('create')(var.get('create')(var.get('l'), var.get('x'), var.get('d'), var.get('rll')), var.get('rlv'), var.get('rld'), var.get('create')(var.get('rlr'), var.get('rv'), var.get('rd'), var.get('rr')))
                else:
                    return Js({'key':var.get('x'),'value':var.get('d'),'height':(((var.get('hl')+Js(1.0))|Js(0.0)) if (var.get('hl')>=var.get('hr')) else ((var.get('hr')+Js(1.0))|Js(0.0))),'left':var.get('l'),'right':var.get('r')})
        PyJsHoisted_bal_.func_name = 'bal'
        var.put('bal', PyJsHoisted_bal_)
        @Js
        def PyJsHoisted_minKey0Aux_(_n, this, arguments, var=var):
            var = Scope({'_n':_n, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                var.put('match', var.get('n').get('left'))
                if PyJsStrictNeq(var.get('match'),var.get(u"null")):
                    var.put('_n', var.get('match'))
                    continue
                else:
                    return var.get('n').get('key')
            pass
        PyJsHoisted_minKey0Aux_.func_name = 'minKey0Aux'
        var.put('minKey0Aux', PyJsHoisted_minKey0Aux_)
        @Js
        def PyJsHoisted_minKey_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('Caml_option').callprop('some', var.get('minKey0Aux')(var.get('n')))
        PyJsHoisted_minKey_.func_name = 'minKey'
        var.put('minKey', PyJsHoisted_minKey_)
        @Js
        def PyJsHoisted_minKeyUndefined_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('minKey0Aux')(var.get('n'))
        PyJsHoisted_minKeyUndefined_.func_name = 'minKeyUndefined'
        var.put('minKeyUndefined', PyJsHoisted_minKeyUndefined_)
        @Js
        def PyJsHoisted_maxKey0Aux_(_n, this, arguments, var=var):
            var = Scope({'_n':_n, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                var.put('match', var.get('n').get('right'))
                if PyJsStrictNeq(var.get('match'),var.get(u"null")):
                    var.put('_n', var.get('match'))
                    continue
                else:
                    return var.get('n').get('key')
            pass
        PyJsHoisted_maxKey0Aux_.func_name = 'maxKey0Aux'
        var.put('maxKey0Aux', PyJsHoisted_maxKey0Aux_)
        @Js
        def PyJsHoisted_maxKey_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('Caml_option').callprop('some', var.get('maxKey0Aux')(var.get('n')))
        PyJsHoisted_maxKey_.func_name = 'maxKey'
        var.put('maxKey', PyJsHoisted_maxKey_)
        @Js
        def PyJsHoisted_maxKeyUndefined_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('maxKey0Aux')(var.get('n'))
        PyJsHoisted_maxKeyUndefined_.func_name = 'maxKeyUndefined'
        var.put('maxKeyUndefined', PyJsHoisted_maxKeyUndefined_)
        @Js
        def PyJsHoisted_minKV0Aux_(_n, this, arguments, var=var):
            var = Scope({'_n':_n, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                var.put('match', var.get('n').get('left'))
                if PyJsStrictNeq(var.get('match'),var.get(u"null")):
                    var.put('_n', var.get('match'))
                    continue
                else:
                    return Js([var.get('n').get('key'), var.get('n').get('value')])
            pass
        PyJsHoisted_minKV0Aux_.func_name = 'minKV0Aux'
        var.put('minKV0Aux', PyJsHoisted_minKV0Aux_)
        @Js
        def PyJsHoisted_minimum_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('minKV0Aux')(var.get('n'))
        PyJsHoisted_minimum_.func_name = 'minimum'
        var.put('minimum', PyJsHoisted_minimum_)
        @Js
        def PyJsHoisted_minUndefined_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('minKV0Aux')(var.get('n'))
        PyJsHoisted_minUndefined_.func_name = 'minUndefined'
        var.put('minUndefined', PyJsHoisted_minUndefined_)
        @Js
        def PyJsHoisted_maxKV0Aux_(_n, this, arguments, var=var):
            var = Scope({'_n':_n, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                var.put('match', var.get('n').get('right'))
                if PyJsStrictNeq(var.get('match'),var.get(u"null")):
                    var.put('_n', var.get('match'))
                    continue
                else:
                    return Js([var.get('n').get('key'), var.get('n').get('value')])
            pass
        PyJsHoisted_maxKV0Aux_.func_name = 'maxKV0Aux'
        var.put('maxKV0Aux', PyJsHoisted_maxKV0Aux_)
        @Js
        def PyJsHoisted_maximum_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('maxKV0Aux')(var.get('n'))
        PyJsHoisted_maximum_.func_name = 'maximum'
        var.put('maximum', PyJsHoisted_maximum_)
        @Js
        def PyJsHoisted_maxUndefined_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('maxKV0Aux')(var.get('n'))
        PyJsHoisted_maxUndefined_.func_name = 'maxUndefined'
        var.put('maxUndefined', PyJsHoisted_maxUndefined_)
        @Js
        def PyJsHoisted_removeMinAuxWithRef_(n, kr, vr, this, arguments, var=var):
            var = Scope({'n':n, 'kr':kr, 'vr':vr, 'this':this, 'arguments':arguments}, var)
            var.registers(['kr', 'vr', 'vn', 'n', 'ln', 'rn', 'kn'])
            var.put('ln', var.get('n').get('left'))
            var.put('rn', var.get('n').get('right'))
            var.put('kn', var.get('n').get('key'))
            var.put('vn', var.get('n').get('value'))
            if PyJsStrictNeq(var.get('ln'),var.get(u"null")):
                return var.get('bal')(var.get('removeMinAuxWithRef')(var.get('ln'), var.get('kr'), var.get('vr')), var.get('kn'), var.get('vn'), var.get('rn'))
            else:
                var.get('kr').put('contents', var.get('kn'))
                var.get('vr').put('contents', var.get('vn'))
                return var.get('rn')
        PyJsHoisted_removeMinAuxWithRef_.func_name = 'removeMinAuxWithRef'
        var.put('removeMinAuxWithRef', PyJsHoisted_removeMinAuxWithRef_)
        @Js
        def PyJsHoisted_isEmpty_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return PyJsStrictEq(var.get('x'),var.get(u"null"))
        PyJsHoisted_isEmpty_.func_name = 'isEmpty'
        var.put('isEmpty', PyJsHoisted_isEmpty_)
        @Js
        def PyJsHoisted_stackAllLeft_(_v, _s, this, arguments, var=var):
            var = Scope({'_v':_v, '_s':_s, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', '_s', 's', '_v'])
            while Js(True):
                var.put('s', var.get('_s'))
                var.put('v', var.get('_v'))
                if PyJsStrictNeq(var.get('v'),var.get(u"null")):
                    var.put('_s', Js([var.get('v'), var.get('s')]))
                    var.put('_v', var.get('v').get('left'))
                    continue
                else:
                    return var.get('s')
            pass
        PyJsHoisted_stackAllLeft_.func_name = 'stackAllLeft'
        var.put('stackAllLeft', PyJsHoisted_stackAllLeft_)
        @Js
        def PyJsHoisted_findFirstByU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['d', 'right', 'v', 'n', 'left', 'pvd', 'p'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('left', var.get('findFirstByU')(var.get('n').get('left'), var.get('p')))
                if PyJsStrictNeq(var.get('left'),var.get('undefined')):
                    return var.get('left')
                else:
                    var.put('v', var.get('n').get('key'))
                    var.put('d', var.get('n').get('value'))
                    var.put('pvd', var.get('p')(var.get('v'), var.get('d')))
                    if var.get('pvd'):
                        return Js([var.get('v'), var.get('d')])
                    else:
                        var.put('right', var.get('findFirstByU')(var.get('n').get('right'), var.get('p')))
                        if PyJsStrictNeq(var.get('right'),var.get('undefined')):
                            return var.get('right')
                        else:
                            return var.get('undefined')
        PyJsHoisted_findFirstByU_.func_name = 'findFirstByU'
        var.put('findFirstByU', PyJsHoisted_findFirstByU_)
        @Js
        def PyJsHoisted_findFirstBy_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('findFirstByU')(var.get('n'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_findFirstBy_.func_name = 'findFirstBy'
        var.put('findFirstBy', PyJsHoisted_findFirstBy_)
        @Js
        def PyJsHoisted_forEachU_(_n, f, this, arguments, var=var):
            var = Scope({'_n':_n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.get('forEachU')(var.get('n').get('left'), var.get('f'))
                    var.get('f')(var.get('n').get('key'), var.get('n').get('value'))
                    var.put('_n', var.get('n').get('right'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_forEachU_.func_name = 'forEachU'
        var.put('forEachU', PyJsHoisted_forEachU_)
        @Js
        def PyJsHoisted_forEach_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n'])
            return var.get('forEachU')(var.get('n'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_forEach_.func_name = 'forEach'
        var.put('forEach', PyJsHoisted_forEach_)
        @Js
        def PyJsHoisted_mapU_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'newLeft', 'newD', 'newRight', 'n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('newLeft', var.get('mapU')(var.get('n').get('left'), var.get('f')))
                var.put('newD', var.get('f')(var.get('n').get('value')))
                var.put('newRight', var.get('mapU')(var.get('n').get('right'), var.get('f')))
                return Js({'key':var.get('n').get('key'),'value':var.get('newD'),'height':var.get('n').get('height'),'left':var.get('newLeft'),'right':var.get('newRight')})
            else:
                return var.get(u"null")
        PyJsHoisted_mapU_.func_name = 'mapU'
        var.put('mapU', PyJsHoisted_mapU_)
        @Js
        def PyJsHoisted_map_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n'])
            return var.get('mapU')(var.get('n'), var.get('Curry').callprop('__1', var.get('f')))
        PyJsHoisted_map_.func_name = 'map'
        var.put('map', PyJsHoisted_map_)
        @Js
        def PyJsHoisted_mapWithKeyU_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'newLeft', 'newD', 'newRight', 'n', 'key'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('key', var.get('n').get('key'))
                var.put('newLeft', var.get('mapWithKeyU')(var.get('n').get('left'), var.get('f')))
                var.put('newD', var.get('f')(var.get('key'), var.get('n').get('value')))
                var.put('newRight', var.get('mapWithKeyU')(var.get('n').get('right'), var.get('f')))
                return Js({'key':var.get('key'),'value':var.get('newD'),'height':var.get('n').get('height'),'left':var.get('newLeft'),'right':var.get('newRight')})
            else:
                return var.get(u"null")
        PyJsHoisted_mapWithKeyU_.func_name = 'mapWithKeyU'
        var.put('mapWithKeyU', PyJsHoisted_mapWithKeyU_)
        @Js
        def PyJsHoisted_mapWithKey_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n'])
            return var.get('mapWithKeyU')(var.get('n'), var.get('Curry').callprop('__2', var.get('f')))
        PyJsHoisted_mapWithKey_.func_name = 'mapWithKey'
        var.put('mapWithKey', PyJsHoisted_mapWithKey_)
        @Js
        def PyJsHoisted_reduceU_(_m, _accu, f, this, arguments, var=var):
            var = Scope({'_m':_m, '_accu':_accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['_m', 'f', 'accu', 'r', 'v', '_accu', 'm', 'd', 'l'])
            while Js(True):
                var.put('accu', var.get('_accu'))
                var.put('m', var.get('_m'))
                if PyJsStrictNeq(var.get('m'),var.get(u"null")):
                    var.put('l', var.get('m').get('left'))
                    var.put('v', var.get('m').get('key'))
                    var.put('d', var.get('m').get('value'))
                    var.put('r', var.get('m').get('right'))
                    var.put('_accu', var.get('f')(var.get('reduceU')(var.get('l'), var.get('accu'), var.get('f')), var.get('v'), var.get('d')))
                    var.put('_m', var.get('r'))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_reduceU_.func_name = 'reduceU'
        var.put('reduceU', PyJsHoisted_reduceU_)
        @Js
        def PyJsHoisted_reduce_(m, accu, f, this, arguments, var=var):
            var = Scope({'m':m, 'accu':accu, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'accu', 'm'])
            return var.get('reduceU')(var.get('m'), var.get('accu'), var.get('Curry').callprop('__3', var.get('f')))
        PyJsHoisted_reduce_.func_name = 'reduce'
        var.put('reduce', PyJsHoisted_reduce_)
        @Js
        def PyJsHoisted_everyU_(_n, p, this, arguments, var=var):
            var = Scope({'_n':_n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    if (var.get('p')(var.get('n').get('key'), var.get('n').get('value')) and var.get('everyU')(var.get('n').get('left'), var.get('p'))):
                        var.put('_n', var.get('n').get('right'))
                        continue
                    else:
                        return Js(False)
                else:
                    return Js(True)
            pass
        PyJsHoisted_everyU_.func_name = 'everyU'
        var.put('everyU', PyJsHoisted_everyU_)
        @Js
        def PyJsHoisted_every_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('everyU')(var.get('n'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_every_.func_name = 'every'
        var.put('every', PyJsHoisted_every_)
        @Js
        def PyJsHoisted_someU_(_n, p, this, arguments, var=var):
            var = Scope({'_n':_n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    if (var.get('p')(var.get('n').get('key'), var.get('n').get('value')) or var.get('someU')(var.get('n').get('left'), var.get('p'))):
                        return Js(True)
                    else:
                        var.put('_n', var.get('n').get('right'))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_someU_.func_name = 'someU'
        var.put('someU', PyJsHoisted_someU_)
        @Js
        def PyJsHoisted_some_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('someU')(var.get('n'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_some_.func_name = 'some'
        var.put('some', PyJsHoisted_some_)
        @Js
        def PyJsHoisted_addMinElement_(n, k, v, this, arguments, var=var):
            var = Scope({'n':n, 'k':k, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', 'k', 'n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('bal')(var.get('addMinElement')(var.get('n').get('left'), var.get('k'), var.get('v')), var.get('n').get('key'), var.get('n').get('value'), var.get('n').get('right'))
            else:
                return var.get('singleton')(var.get('k'), var.get('v'))
        PyJsHoisted_addMinElement_.func_name = 'addMinElement'
        var.put('addMinElement', PyJsHoisted_addMinElement_)
        @Js
        def PyJsHoisted_addMaxElement_(n, k, v, this, arguments, var=var):
            var = Scope({'n':n, 'k':k, 'v':v, 'this':this, 'arguments':arguments}, var)
            var.registers(['v', 'k', 'n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('bal')(var.get('n').get('left'), var.get('n').get('key'), var.get('n').get('value'), var.get('addMaxElement')(var.get('n').get('right'), var.get('k'), var.get('v')))
            else:
                return var.get('singleton')(var.get('k'), var.get('v'))
        PyJsHoisted_addMaxElement_.func_name = 'addMaxElement'
        var.put('addMaxElement', PyJsHoisted_addMaxElement_)
        @Js
        def PyJsHoisted_join_(ln, v, d, rn, this, arguments, var=var):
            var = Scope({'ln':ln, 'v':v, 'd':d, 'rn':rn, 'this':this, 'arguments':arguments}, var)
            var.registers(['rh', 'll', 'lh', 'rv', 'ld', 'rn', 'rr', 'v', 'lv', 'rd', 'lr', 'ln', 'd', 'rl'])
            if PyJsStrictNeq(var.get('ln'),var.get(u"null")):
                if PyJsStrictNeq(var.get('rn'),var.get(u"null")):
                    var.put('ll', var.get('ln').get('left'))
                    var.put('lv', var.get('ln').get('key'))
                    var.put('ld', var.get('ln').get('value'))
                    var.put('lr', var.get('ln').get('right'))
                    var.put('lh', var.get('ln').get('height'))
                    var.put('rl', var.get('rn').get('left'))
                    var.put('rv', var.get('rn').get('key'))
                    var.put('rd', var.get('rn').get('value'))
                    var.put('rr', var.get('rn').get('right'))
                    var.put('rh', var.get('rn').get('height'))
                    if (var.get('lh')>((var.get('rh')+Js(2.0))|Js(0.0))):
                        return var.get('bal')(var.get('ll'), var.get('lv'), var.get('ld'), var.get('join')(var.get('lr'), var.get('v'), var.get('d'), var.get('rn')))
                    else:
                        if (var.get('rh')>((var.get('lh')+Js(2.0))|Js(0.0))):
                            return var.get('bal')(var.get('join')(var.get('ln'), var.get('v'), var.get('d'), var.get('rl')), var.get('rv'), var.get('rd'), var.get('rr'))
                        else:
                            return var.get('create')(var.get('ln'), var.get('v'), var.get('d'), var.get('rn'))
                else:
                    return var.get('addMaxElement')(var.get('ln'), var.get('v'), var.get('d'))
            else:
                return var.get('addMinElement')(var.get('rn'), var.get('v'), var.get('d'))
        PyJsHoisted_join_.func_name = 'join'
        var.put('join', PyJsHoisted_join_)
        @Js
        def PyJsHoisted_concat_(t1, t2, this, arguments, var=var):
            var = Scope({'t1':t1, 't2':t2, 'this':this, 'arguments':arguments}, var)
            var.registers(['kr', 't1', 'vr', 't2', 't2r'])
            if PyJsStrictNeq(var.get('t1'),var.get(u"null")):
                if PyJsStrictNeq(var.get('t2'),var.get(u"null")):
                    var.put('kr', Js({'contents':var.get('t2').get('key')}))
                    var.put('vr', Js({'contents':var.get('t2').get('value')}))
                    var.put('t2r', var.get('removeMinAuxWithRef')(var.get('t2'), var.get('kr'), var.get('vr')))
                    return var.get('join')(var.get('t1'), var.get('kr').get('contents'), var.get('vr').get('contents'), var.get('t2r'))
                else:
                    return var.get('t1')
            else:
                return var.get('t2')
        PyJsHoisted_concat_.func_name = 'concat'
        var.put('concat', PyJsHoisted_concat_)
        @Js
        def PyJsHoisted_concatOrJoin_(t1, v, d, t2, this, arguments, var=var):
            var = Scope({'t1':t1, 'v':v, 'd':d, 't2':t2, 'this':this, 'arguments':arguments}, var)
            var.registers(['t2', 'd', 'v', 't1'])
            if PyJsStrictNeq(var.get('d'),var.get('undefined')):
                return var.get('join')(var.get('t1'), var.get('v'), var.get('Caml_option').callprop('valFromOption', var.get('d')), var.get('t2'))
            else:
                return var.get('concat')(var.get('t1'), var.get('t2'))
        PyJsHoisted_concatOrJoin_.func_name = 'concatOrJoin'
        var.put('concatOrJoin', PyJsHoisted_concatOrJoin_)
        @Js
        def PyJsHoisted_keepSharedU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['newLeft', 'v', 'newRight', 'n', 'd', 'pvd', 'p'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('v', var.get('n').get('key'))
                var.put('d', var.get('n').get('value'))
                var.put('newLeft', var.get('keepSharedU')(var.get('n').get('left'), var.get('p')))
                var.put('pvd', var.get('p')(var.get('v'), var.get('d')))
                var.put('newRight', var.get('keepSharedU')(var.get('n').get('right'), var.get('p')))
                if var.get('pvd'):
                    return var.get('join')(var.get('newLeft'), var.get('v'), var.get('d'), var.get('newRight'))
                else:
                    return var.get('concat')(var.get('newLeft'), var.get('newRight'))
            else:
                return var.get(u"null")
        PyJsHoisted_keepSharedU_.func_name = 'keepSharedU'
        var.put('keepSharedU', PyJsHoisted_keepSharedU_)
        @Js
        def PyJsHoisted_keepShared_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('keepSharedU')(var.get('n'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_keepShared_.func_name = 'keepShared'
        var.put('keepShared', PyJsHoisted_keepShared_)
        @Js
        def PyJsHoisted_keepMapU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['newLeft', 'v', 'newRight', 'n', 'd', 'pvd', 'p'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('v', var.get('n').get('key'))
                var.put('d', var.get('n').get('value'))
                var.put('newLeft', var.get('keepMapU')(var.get('n').get('left'), var.get('p')))
                var.put('pvd', var.get('p')(var.get('v'), var.get('d')))
                var.put('newRight', var.get('keepMapU')(var.get('n').get('right'), var.get('p')))
                if PyJsStrictNeq(var.get('pvd'),var.get('undefined')):
                    return var.get('join')(var.get('newLeft'), var.get('v'), var.get('Caml_option').callprop('valFromOption', var.get('pvd')), var.get('newRight'))
                else:
                    return var.get('concat')(var.get('newLeft'), var.get('newRight'))
            else:
                return var.get(u"null")
        PyJsHoisted_keepMapU_.func_name = 'keepMapU'
        var.put('keepMapU', PyJsHoisted_keepMapU_)
        @Js
        def PyJsHoisted_keepMap_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('keepMapU')(var.get('n'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_keepMap_.func_name = 'keepMap'
        var.put('keepMap', PyJsHoisted_keepMap_)
        @Js
        def PyJsHoisted_partitionSharedU_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['lf', 'value', 'match$1', 'rf', 'lt', 'match', 'key', 'n', 'rt', 'pvd', 'p'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('key', var.get('n').get('key'))
                var.put('value', var.get('n').get('value'))
                var.put('match', var.get('partitionSharedU')(var.get('n').get('left'), var.get('p')))
                var.put('lf', var.get('match').get('1'))
                var.put('lt', var.get('match').get('0'))
                var.put('pvd', var.get('p')(var.get('key'), var.get('value')))
                var.put('match$1', var.get('partitionSharedU')(var.get('n').get('right'), var.get('p')))
                var.put('rf', var.get('match$1').get('1'))
                var.put('rt', var.get('match$1').get('0'))
                if var.get('pvd'):
                    return Js([var.get('join')(var.get('lt'), var.get('key'), var.get('value'), var.get('rt')), var.get('concat')(var.get('lf'), var.get('rf'))])
                else:
                    return Js([var.get('concat')(var.get('lt'), var.get('rt')), var.get('join')(var.get('lf'), var.get('key'), var.get('value'), var.get('rf'))])
            else:
                return Js([var.get(u"null"), var.get(u"null")])
        PyJsHoisted_partitionSharedU_.func_name = 'partitionSharedU'
        var.put('partitionSharedU', PyJsHoisted_partitionSharedU_)
        @Js
        def PyJsHoisted_partitionShared_(n, p, this, arguments, var=var):
            var = Scope({'n':n, 'p':p, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'n'])
            return var.get('partitionSharedU')(var.get('n'), var.get('Curry').callprop('__2', var.get('p')))
        PyJsHoisted_partitionShared_.func_name = 'partitionShared'
        var.put('partitionShared', PyJsHoisted_partitionShared_)
        @Js
        def PyJsHoisted_lengthNode_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['sizeL', 'sizeR', 'r', 'n', 'l'])
            var.put('l', var.get('n').get('left'))
            var.put('r', var.get('n').get('right'))
            var.put('sizeL', (var.get('lengthNode')(var.get('l')) if PyJsStrictNeq(var.get('l'),var.get(u"null")) else Js(0.0)))
            var.put('sizeR', (var.get('lengthNode')(var.get('r')) if PyJsStrictNeq(var.get('r'),var.get(u"null")) else Js(0.0)))
            return ((((Js(1.0)+var.get('sizeL'))|Js(0.0))+var.get('sizeR'))|Js(0.0))
        PyJsHoisted_lengthNode_.func_name = 'lengthNode'
        var.put('lengthNode', PyJsHoisted_lengthNode_)
        @Js
        def PyJsHoisted_size_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                return var.get('lengthNode')(var.get('n'))
            else:
                return Js(0.0)
        PyJsHoisted_size_.func_name = 'size'
        var.put('size', PyJsHoisted_size_)
        @Js
        def PyJsHoisted_toListAux_(_n, _accu, this, arguments, var=var):
            var = Scope({'_n':_n, '_accu':_accu, 'this':this, 'arguments':arguments}, var)
            var.registers(['accu', 'r', 'v', '_accu', '_n', 'k', 'n', 'l'])
            while Js(True):
                var.put('accu', var.get('_accu'))
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('l', var.get('n').get('left'))
                    var.put('r', var.get('n').get('right'))
                    var.put('k', var.get('n').get('key'))
                    var.put('v', var.get('n').get('value'))
                    var.put('_accu', Js([Js([var.get('k'), var.get('v')]), var.get('toListAux')(var.get('r'), var.get('accu'))]))
                    var.put('_n', var.get('l'))
                    continue
                else:
                    return var.get('accu')
            pass
        PyJsHoisted_toListAux_.func_name = 'toListAux'
        var.put('toListAux', PyJsHoisted_toListAux_)
        @Js
        def PyJsHoisted_toList_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('toListAux')(var.get('s'), Js(0.0))
        PyJsHoisted_toList_.func_name = 'toList'
        var.put('toList', PyJsHoisted_toList_)
        @Js
        def PyJsHoisted_checkInvariantInternal_(_v, this, arguments, var=var):
            var = Scope({'_v':_v, 'this':this, 'arguments':arguments}, var)
            var.registers(['_v', 'r', 'v', 'diff', 'l'])
            while Js(True):
                var.put('v', var.get('_v'))
                if PyJsStrictNeq(var.get('v'),var.get(u"null")):
                    var.put('l', var.get('v').get('left'))
                    var.put('r', var.get('v').get('right'))
                    var.put('diff', ((var.get('treeHeight')(var.get('l'))-var.get('treeHeight')(var.get('r')))|Js(0.0)))
                    if ((var.get('diff')<=Js(2.0)) and (var.get('diff')>=(-Js(2.0)))).neg():
                        PyJsTempException = JsToPyException(var.get('Error').create(Js('File "belt_internalAVLtree.ml", line 385, characters 6-12')))
                        raise PyJsTempException
                    var.get('checkInvariantInternal')(var.get('l'))
                    var.put('_v', var.get('r'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_checkInvariantInternal_.func_name = 'checkInvariantInternal'
        var.put('checkInvariantInternal', PyJsHoisted_checkInvariantInternal_)
        @Js
        def PyJsHoisted_fillArrayKey_(_n, _i, arr, this, arguments, var=var):
            var = Scope({'_n':_n, '_i':_i, 'arr':arr, 'this':this, 'arguments':arguments}, var)
            var.registers(['rnext', 'r', 'v', 'next', '_i', 'n', '_n', 'arr', 'i', 'l'])
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('n', var.get('_n'))
                var.put('l', var.get('n').get('left'))
                var.put('v', var.get('n').get('key'))
                var.put('r', var.get('n').get('right'))
                var.put('next', (var.get('fillArrayKey')(var.get('l'), var.get('i'), var.get('arr')) if PyJsStrictNeq(var.get('l'),var.get(u"null")) else var.get('i')))
                var.get('arr').put(var.get('next'), var.get('v'))
                var.put('rnext', ((var.get('next')+Js(1.0))|Js(0.0)))
                if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                    var.put('_i', var.get('rnext'))
                    var.put('_n', var.get('r'))
                    continue
                else:
                    return var.get('rnext')
            pass
        PyJsHoisted_fillArrayKey_.func_name = 'fillArrayKey'
        var.put('fillArrayKey', PyJsHoisted_fillArrayKey_)
        @Js
        def PyJsHoisted_fillArrayValue_(_n, _i, arr, this, arguments, var=var):
            var = Scope({'_n':_n, '_i':_i, 'arr':arr, 'this':this, 'arguments':arguments}, var)
            var.registers(['rnext', 'r', 'next', '_i', 'n', '_n', 'arr', 'i', 'l'])
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('n', var.get('_n'))
                var.put('l', var.get('n').get('left'))
                var.put('r', var.get('n').get('right'))
                var.put('next', (var.get('fillArrayValue')(var.get('l'), var.get('i'), var.get('arr')) if PyJsStrictNeq(var.get('l'),var.get(u"null")) else var.get('i')))
                var.get('arr').put(var.get('next'), var.get('n').get('value'))
                var.put('rnext', ((var.get('next')+Js(1.0))|Js(0.0)))
                if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                    var.put('_i', var.get('rnext'))
                    var.put('_n', var.get('r'))
                    continue
                else:
                    return var.get('rnext')
            pass
        PyJsHoisted_fillArrayValue_.func_name = 'fillArrayValue'
        var.put('fillArrayValue', PyJsHoisted_fillArrayValue_)
        @Js
        def PyJsHoisted_fillArray_(_n, _i, arr, this, arguments, var=var):
            var = Scope({'_n':_n, '_i':_i, 'arr':arr, 'this':this, 'arguments':arguments}, var)
            var.registers(['rnext', 'r', 'v', 'next', '_i', 'n', '_n', 'arr', 'i', 'l'])
            while Js(True):
                var.put('i', var.get('_i'))
                var.put('n', var.get('_n'))
                var.put('l', var.get('n').get('left'))
                var.put('v', var.get('n').get('key'))
                var.put('r', var.get('n').get('right'))
                var.put('next', (var.get('fillArray')(var.get('l'), var.get('i'), var.get('arr')) if PyJsStrictNeq(var.get('l'),var.get(u"null")) else var.get('i')))
                var.get('arr').put(var.get('next'), Js([var.get('v'), var.get('n').get('value')]))
                var.put('rnext', ((var.get('next')+Js(1.0))|Js(0.0)))
                if PyJsStrictNeq(var.get('r'),var.get(u"null")):
                    var.put('_i', var.get('rnext'))
                    var.put('_n', var.get('r'))
                    continue
                else:
                    return var.get('rnext')
            pass
        PyJsHoisted_fillArray_.func_name = 'fillArray'
        var.put('fillArray', PyJsHoisted_fillArray_)
        @Js
        def PyJsHoisted_toArray_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['size', 'n', 'v'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('size', var.get('lengthNode')(var.get('n')))
                var.put('v', var.get('Array').create(var.get('size')))
                var.get('fillArray')(var.get('n'), Js(0.0), var.get('v'))
                return var.get('v')
            else:
                return Js([])
        PyJsHoisted_toArray_.func_name = 'toArray'
        var.put('toArray', PyJsHoisted_toArray_)
        @Js
        def PyJsHoisted_keysToArray_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['size', 'n', 'v'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('size', var.get('lengthNode')(var.get('n')))
                var.put('v', var.get('Array').create(var.get('size')))
                var.get('fillArrayKey')(var.get('n'), Js(0.0), var.get('v'))
                return var.get('v')
            else:
                return Js([])
        PyJsHoisted_keysToArray_.func_name = 'keysToArray'
        var.put('keysToArray', PyJsHoisted_keysToArray_)
        @Js
        def PyJsHoisted_valuesToArray_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['size', 'n', 'v'])
            if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                var.put('size', var.get('lengthNode')(var.get('n')))
                var.put('v', var.get('Array').create(var.get('size')))
                var.get('fillArrayValue')(var.get('n'), Js(0.0), var.get('v'))
                return var.get('v')
            else:
                return Js([])
        PyJsHoisted_valuesToArray_.func_name = 'valuesToArray'
        var.put('valuesToArray', PyJsHoisted_valuesToArray_)
        @Js
        def PyJsHoisted_fromSortedArrayRevAux_(arr, off, len, this, arguments, var=var):
            var = Scope({'arr':arr, 'off':off, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['match$5', 'len', 'match_000', 'match$1', 'match_001', 'nl', 'off', 'match_002', 'match$3', 'match', 'match$4', 'match_000$1', 'match$2', 'arr', 'match_001$1', 'left', 'right', 'match$6'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('len'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    return var.get(u"null")
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('match', var.get('arr').get(var.get('off')))
                    return var.get('singleton')(var.get('match').get('0'), var.get('match').get('1'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('match_000', var.get('arr').get(var.get('off')))
                    var.put('match_001', var.get('arr').get(((var.get('off')-Js(1.0))|Js(0.0))))
                    var.put('match$1', var.get('match_001'))
                    var.put('match$2', var.get('match_000'))
                    return Js({'key':var.get('match$1').get('0'),'value':var.get('match$1').get('1'),'height':Js(2.0),'left':var.get('singleton')(var.get('match$2').get('0'), var.get('match$2').get('1')),'right':var.get(u"null")})
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('match_000$1', var.get('arr').get(var.get('off')))
                    var.put('match_001$1', var.get('arr').get(((var.get('off')-Js(1.0))|Js(0.0))))
                    var.put('match_002', var.get('arr').get(((var.get('off')-Js(2.0))|Js(0.0))))
                    var.put('match$3', var.get('match_002'))
                    var.put('match$4', var.get('match_001$1'))
                    var.put('match$5', var.get('match_000$1'))
                    return Js({'key':var.get('match$4').get('0'),'value':var.get('match$4').get('1'),'height':Js(2.0),'left':var.get('singleton')(var.get('match$5').get('0'), var.get('match$5').get('1')),'right':var.get('singleton')(var.get('match$3').get('0'), var.get('match$3').get('1'))})
                if True:
                    SWITCHED = True
                    var.put('nl', ((var.get('len')/Js(2.0))|Js(0.0)))
                    var.put('left', var.get('fromSortedArrayRevAux')(var.get('arr'), var.get('off'), var.get('nl')))
                    var.put('match$6', var.get('arr').get(((var.get('off')-var.get('nl'))|Js(0.0))))
                    var.put('right', var.get('fromSortedArrayRevAux')(var.get('arr'), ((((var.get('off')-var.get('nl'))|Js(0.0))-Js(1.0))|Js(0.0)), ((((var.get('len')-var.get('nl'))|Js(0.0))-Js(1.0))|Js(0.0))))
                    return var.get('create')(var.get('left'), var.get('match$6').get('0'), var.get('match$6').get('1'), var.get('right'))
                SWITCHED = True
                break
        PyJsHoisted_fromSortedArrayRevAux_.func_name = 'fromSortedArrayRevAux'
        var.put('fromSortedArrayRevAux', PyJsHoisted_fromSortedArrayRevAux_)
        @Js
        def PyJsHoisted_fromSortedArrayAux_(arr, off, len, this, arguments, var=var):
            var = Scope({'arr':arr, 'off':off, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['match$5', 'len', 'match_000', 'match$1', 'match_001', 'nl', 'off', 'match_002', 'match$3', 'match', 'match$4', 'match_000$1', 'match$2', 'arr', 'match_001$1', 'left', 'right', 'match$6'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('len'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    return var.get(u"null")
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('match', var.get('arr').get(var.get('off')))
                    return var.get('singleton')(var.get('match').get('0'), var.get('match').get('1'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('match_000', var.get('arr').get(var.get('off')))
                    var.put('match_001', var.get('arr').get(((var.get('off')+Js(1.0))|Js(0.0))))
                    var.put('match$1', var.get('match_001'))
                    var.put('match$2', var.get('match_000'))
                    return Js({'key':var.get('match$1').get('0'),'value':var.get('match$1').get('1'),'height':Js(2.0),'left':var.get('singleton')(var.get('match$2').get('0'), var.get('match$2').get('1')),'right':var.get(u"null")})
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    var.put('match_000$1', var.get('arr').get(var.get('off')))
                    var.put('match_001$1', var.get('arr').get(((var.get('off')+Js(1.0))|Js(0.0))))
                    var.put('match_002', var.get('arr').get(((var.get('off')+Js(2.0))|Js(0.0))))
                    var.put('match$3', var.get('match_002'))
                    var.put('match$4', var.get('match_001$1'))
                    var.put('match$5', var.get('match_000$1'))
                    return Js({'key':var.get('match$4').get('0'),'value':var.get('match$4').get('1'),'height':Js(2.0),'left':var.get('singleton')(var.get('match$5').get('0'), var.get('match$5').get('1')),'right':var.get('singleton')(var.get('match$3').get('0'), var.get('match$3').get('1'))})
                if True:
                    SWITCHED = True
                    var.put('nl', ((var.get('len')/Js(2.0))|Js(0.0)))
                    var.put('left', var.get('fromSortedArrayAux')(var.get('arr'), var.get('off'), var.get('nl')))
                    var.put('match$6', var.get('arr').get(((var.get('off')+var.get('nl'))|Js(0.0))))
                    var.put('right', var.get('fromSortedArrayAux')(var.get('arr'), ((((var.get('off')+var.get('nl'))|Js(0.0))+Js(1.0))|Js(0.0)), ((((var.get('len')-var.get('nl'))|Js(0.0))-Js(1.0))|Js(0.0))))
                    return var.get('create')(var.get('left'), var.get('match$6').get('0'), var.get('match$6').get('1'), var.get('right'))
                SWITCHED = True
                break
        PyJsHoisted_fromSortedArrayAux_.func_name = 'fromSortedArrayAux'
        var.put('fromSortedArrayAux', PyJsHoisted_fromSortedArrayAux_)
        @Js
        def PyJsHoisted_fromSortedArrayUnsafe_(arr, this, arguments, var=var):
            var = Scope({'arr':arr, 'this':this, 'arguments':arguments}, var)
            var.registers(['arr'])
            return var.get('fromSortedArrayAux')(var.get('arr'), Js(0.0), var.get('arr').get('length'))
        PyJsHoisted_fromSortedArrayUnsafe_.func_name = 'fromSortedArrayUnsafe'
        var.put('fromSortedArrayUnsafe', PyJsHoisted_fromSortedArrayUnsafe_)
        @Js
        def PyJsHoisted_cmpU_(s1, s2, kcmp, vcmp, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'kcmp':kcmp, 'vcmp':vcmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['h1', '_e2', 'vcmp$1', 'len1', 'c', 'e1', 'vcmp', 'cx', 'kcmp', 's2', 's1', 'kcmp$1', 'e2', '_e1', 'h2', 'len2'])
            var.put('len1', var.get('size')(var.get('s1')))
            var.put('len2', var.get('size')(var.get('s2')))
            if PyJsStrictEq(var.get('len1'),var.get('len2')):
                var.put('_e1', var.get('stackAllLeft')(var.get('s1'), Js(0.0)))
                var.put('_e2', var.get('stackAllLeft')(var.get('s2'), Js(0.0)))
                var.put('kcmp$1', var.get('kcmp'))
                var.put('vcmp$1', var.get('vcmp'))
                while Js(True):
                    var.put('e2', var.get('_e2'))
                    var.put('e1', var.get('_e1'))
                    if (var.get('e1') and var.get('e2')):
                        var.put('h2', var.get('e2').get('0'))
                        var.put('h1', var.get('e1').get('0'))
                        var.put('c', var.get('kcmp$1')(var.get('h1').get('key'), var.get('h2').get('key')))
                        if PyJsStrictEq(var.get('c'),Js(0.0)):
                            var.put('cx', var.get('vcmp$1')(var.get('h1').get('value'), var.get('h2').get('value')))
                            if PyJsStrictEq(var.get('cx'),Js(0.0)):
                                var.put('_e2', var.get('stackAllLeft')(var.get('h2').get('right'), var.get('e2').get('1')))
                                var.put('_e1', var.get('stackAllLeft')(var.get('h1').get('right'), var.get('e1').get('1')))
                                continue
                            else:
                                return var.get('cx')
                        else:
                            return var.get('c')
                    else:
                        return Js(0.0)
                pass
            else:
                if (var.get('len1')<var.get('len2')):
                    return (-Js(1.0))
                else:
                    return Js(1.0)
        PyJsHoisted_cmpU_.func_name = 'cmpU'
        var.put('cmpU', PyJsHoisted_cmpU_)
        @Js
        def PyJsHoisted_cmp_(s1, s2, kcmp, vcmp, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'kcmp':kcmp, 'vcmp':vcmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['kcmp', 's1', 's2', 'vcmp'])
            return var.get('cmpU')(var.get('s1'), var.get('s2'), var.get('kcmp'), var.get('Curry').callprop('__2', var.get('vcmp')))
        PyJsHoisted_cmp_.func_name = 'cmp'
        var.put('cmp', PyJsHoisted_cmp_)
        @Js
        def PyJsHoisted_eqU_(s1, s2, kcmp, veq, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'kcmp':kcmp, 'veq':veq, 'this':this, 'arguments':arguments}, var)
            var.registers(['h1', '_e2', 'len1', 'veq$1', 'e1', 'kcmp', 's2', 's1', 'veq', 'kcmp$1', 'e2', '_e1', 'h2', 'len2'])
            var.put('len1', var.get('size')(var.get('s1')))
            var.put('len2', var.get('size')(var.get('s2')))
            if PyJsStrictEq(var.get('len1'),var.get('len2')):
                var.put('_e1', var.get('stackAllLeft')(var.get('s1'), Js(0.0)))
                var.put('_e2', var.get('stackAllLeft')(var.get('s2'), Js(0.0)))
                var.put('kcmp$1', var.get('kcmp'))
                var.put('veq$1', var.get('veq'))
                while Js(True):
                    var.put('e2', var.get('_e2'))
                    var.put('e1', var.get('_e1'))
                    if (var.get('e1') and var.get('e2')):
                        var.put('h2', var.get('e2').get('0'))
                        var.put('h1', var.get('e1').get('0'))
                        if (PyJsStrictEq(var.get('kcmp$1')(var.get('h1').get('key'), var.get('h2').get('key')),Js(0.0)) and var.get('veq$1')(var.get('h1').get('value'), var.get('h2').get('value'))):
                            var.put('_e2', var.get('stackAllLeft')(var.get('h2').get('right'), var.get('e2').get('1')))
                            var.put('_e1', var.get('stackAllLeft')(var.get('h1').get('right'), var.get('e1').get('1')))
                            continue
                        else:
                            return Js(False)
                    else:
                        return Js(True)
                pass
            else:
                return Js(False)
        PyJsHoisted_eqU_.func_name = 'eqU'
        var.put('eqU', PyJsHoisted_eqU_)
        @Js
        def PyJsHoisted_eq_(s1, s2, kcmp, veq, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'kcmp':kcmp, 'veq':veq, 'this':this, 'arguments':arguments}, var)
            var.registers(['kcmp', 's1', 'veq', 's2'])
            return var.get('eqU')(var.get('s1'), var.get('s2'), var.get('kcmp'), var.get('Curry').callprop('__2', var.get('veq')))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_get_(_n, x, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('key'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return var.get('Caml_option').callprop('some', var.get('n').get('value'))
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    return var.get('undefined')
            pass
        PyJsHoisted_get_.func_name = 'get'
        var.put('get', PyJsHoisted_get_)
        @Js
        def PyJsHoisted_getUndefined_(_n, x, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('key'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return var.get('n').get('value')
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    return var.get('undefined')
            pass
        PyJsHoisted_getUndefined_.func_name = 'getUndefined'
        var.put('getUndefined', PyJsHoisted_getUndefined_)
        @Js
        def PyJsHoisted_getExn_(_n, x, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('key'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return var.get('n').get('value')
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    PyJsTempException = JsToPyException(var.get('Error').create(Js('getExn0')))
                    raise PyJsTempException
            pass
        PyJsHoisted_getExn_.func_name = 'getExn'
        var.put('getExn', PyJsHoisted_getExn_)
        @Js
        def PyJsHoisted_getWithDefault_(_n, x, PyJsArg_646566_, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'def':PyJsArg_646566_, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['def', 'c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('key'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return var.get('n').get('value')
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    return var.get('def')
            pass
        PyJsHoisted_getWithDefault_.func_name = 'getWithDefault'
        var.put('getWithDefault', PyJsHoisted_getWithDefault_)
        @Js
        def PyJsHoisted_has_(_n, x, cmp, this, arguments, var=var):
            var = Scope({'_n':_n, 'x':x, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'cmp', 'v', 'x', 'n', '_n'])
            while Js(True):
                var.put('n', var.get('_n'))
                if PyJsStrictNeq(var.get('n'),var.get(u"null")):
                    var.put('v', var.get('n').get('key'))
                    var.put('c', var.get('cmp')(var.get('x'), var.get('v')))
                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                        return Js(True)
                    else:
                        var.put('_n', (var.get('n').get('left') if (var.get('c')<Js(0.0)) else var.get('n').get('right')))
                        continue
                else:
                    return Js(False)
            pass
        PyJsHoisted_has_.func_name = 'has'
        var.put('has', PyJsHoisted_has_)
        @Js
        def PyJsHoisted_rotateWithLeftChild_(k2, this, arguments, var=var):
            var = Scope({'k2':k2, 'this':this, 'arguments':arguments}, var)
            var.registers(['hrk2', 'hk2', 'k2', 'hlk2', 'hlk1', 'k1'])
            var.put('k1', var.get('k2').get('left'))
            var.get('k2').put('left', var.get('k1').get('right'))
            var.get('k1').put('right', var.get('k2'))
            var.put('hlk2', var.get('treeHeight')(var.get('k2').get('left')))
            var.put('hrk2', var.get('treeHeight')(var.get('k2').get('right')))
            var.get('k2').put('height', (((var.get('hlk2') if (var.get('hlk2')>var.get('hrk2')) else var.get('hrk2'))+Js(1.0))|Js(0.0)))
            var.put('hlk1', var.get('treeHeight')(var.get('k1').get('left')))
            var.put('hk2', var.get('k2').get('height'))
            var.get('k1').put('height', (((var.get('hlk1') if (var.get('hlk1')>var.get('hk2')) else var.get('hk2'))+Js(1.0))|Js(0.0)))
            return var.get('k1')
        PyJsHoisted_rotateWithLeftChild_.func_name = 'rotateWithLeftChild'
        var.put('rotateWithLeftChild', PyJsHoisted_rotateWithLeftChild_)
        @Js
        def PyJsHoisted_rotateWithRightChild_(k1, this, arguments, var=var):
            var = Scope({'k1':k1, 'this':this, 'arguments':arguments}, var)
            var.registers(['hrk1', 'hrk2', 'k2', 'hlk1', 'k1', 'hk1'])
            var.put('k2', var.get('k1').get('right'))
            var.get('k1').put('right', var.get('k2').get('left'))
            var.get('k2').put('left', var.get('k1'))
            var.put('hlk1', var.get('treeHeight')(var.get('k1').get('left')))
            var.put('hrk1', var.get('treeHeight')(var.get('k1').get('right')))
            var.get('k1').put('height', (((var.get('hlk1') if (var.get('hlk1')>var.get('hrk1')) else var.get('hrk1'))+Js(1.0))|Js(0.0)))
            var.put('hrk2', var.get('treeHeight')(var.get('k2').get('right')))
            var.put('hk1', var.get('k1').get('height'))
            var.get('k2').put('height', (((var.get('hrk2') if (var.get('hrk2')>var.get('hk1')) else var.get('hk1'))+Js(1.0))|Js(0.0)))
            return var.get('k2')
        PyJsHoisted_rotateWithRightChild_.func_name = 'rotateWithRightChild'
        var.put('rotateWithRightChild', PyJsHoisted_rotateWithRightChild_)
        @Js
        def PyJsHoisted_doubleWithLeftChild_(k3, this, arguments, var=var):
            var = Scope({'k3':k3, 'this':this, 'arguments':arguments}, var)
            var.registers(['k3', 'v'])
            var.put('v', var.get('rotateWithRightChild')(var.get('k3').get('left')))
            var.get('k3').put('left', var.get('v'))
            return var.get('rotateWithLeftChild')(var.get('k3'))
        PyJsHoisted_doubleWithLeftChild_.func_name = 'doubleWithLeftChild'
        var.put('doubleWithLeftChild', PyJsHoisted_doubleWithLeftChild_)
        @Js
        def PyJsHoisted_doubleWithRightChild_(k2, this, arguments, var=var):
            var = Scope({'k2':k2, 'this':this, 'arguments':arguments}, var)
            var.registers(['k2', 'v'])
            var.put('v', var.get('rotateWithLeftChild')(var.get('k2').get('right')))
            var.get('k2').put('right', var.get('v'))
            return var.get('rotateWithRightChild')(var.get('k2'))
        PyJsHoisted_doubleWithRightChild_.func_name = 'doubleWithRightChild'
        var.put('doubleWithRightChild', PyJsHoisted_doubleWithRightChild_)
        @Js
        def PyJsHoisted_heightUpdateMutate_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['hlt', 't', 'hrt'])
            var.put('hlt', var.get('treeHeight')(var.get('t').get('left')))
            var.put('hrt', var.get('treeHeight')(var.get('t').get('right')))
            var.get('t').put('height', (((var.get('hlt') if (var.get('hlt')>var.get('hrt')) else var.get('hrt'))+Js(1.0))|Js(0.0)))
            return var.get('t')
        PyJsHoisted_heightUpdateMutate_.func_name = 'heightUpdateMutate'
        var.put('heightUpdateMutate', PyJsHoisted_heightUpdateMutate_)
        @Js
        def PyJsHoisted_balMutate_(nt, this, arguments, var=var):
            var = Scope({'nt':nt, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 'hl', 'hr', 'rr', 'nt', 'r', 'lr', 'rl', 'l'])
            var.put('l', var.get('nt').get('left'))
            var.put('r', var.get('nt').get('right'))
            var.put('hl', var.get('treeHeight')(var.get('l')))
            var.put('hr', var.get('treeHeight')(var.get('r')))
            if (var.get('hl')>((Js(2.0)+var.get('hr'))|Js(0.0))):
                var.put('ll', var.get('l').get('left'))
                var.put('lr', var.get('l').get('right'))
                if var.get('heightGe')(var.get('ll'), var.get('lr')):
                    return var.get('heightUpdateMutate')(var.get('rotateWithLeftChild')(var.get('nt')))
                else:
                    return var.get('heightUpdateMutate')(var.get('doubleWithLeftChild')(var.get('nt')))
            else:
                if (var.get('hr')>((Js(2.0)+var.get('hl'))|Js(0.0))):
                    var.put('rl', var.get('r').get('left'))
                    var.put('rr', var.get('r').get('right'))
                    if var.get('heightGe')(var.get('rr'), var.get('rl')):
                        return var.get('heightUpdateMutate')(var.get('rotateWithRightChild')(var.get('nt')))
                    else:
                        return var.get('heightUpdateMutate')(var.get('doubleWithRightChild')(var.get('nt')))
                else:
                    var.get('nt').put('height', (((var.get('hl') if (var.get('hl')>var.get('hr')) else var.get('hr'))+Js(1.0))|Js(0.0)))
                    return var.get('nt')
        PyJsHoisted_balMutate_.func_name = 'balMutate'
        var.put('balMutate', PyJsHoisted_balMutate_)
        @Js
        def PyJsHoisted_updateMutate_(t, x, data, cmp, this, arguments, var=var):
            var = Scope({'t':t, 'x':x, 'data':data, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['ll', 't', 'c', 'cmp', 'r', 'x', 'k', 'data', 'l'])
            if PyJsStrictNeq(var.get('t'),var.get(u"null")):
                var.put('k', var.get('t').get('key'))
                var.put('c', var.get('cmp')(var.get('x'), var.get('k')))
                if PyJsStrictEq(var.get('c'),Js(0.0)):
                    var.get('t').put('value', var.get('data'))
                    return var.get('t')
                else:
                    var.put('l', var.get('t').get('left'))
                    var.put('r', var.get('t').get('right'))
                    if (var.get('c')<Js(0.0)):
                        var.put('ll', var.get('updateMutate')(var.get('l'), var.get('x'), var.get('data'), var.get('cmp')))
                        var.get('t').put('left', var.get('ll'))
                    else:
                        var.get('t').put('right', var.get('updateMutate')(var.get('r'), var.get('x'), var.get('data'), var.get('cmp')))
                    return var.get('balMutate')(var.get('t'))
            else:
                return var.get('singleton')(var.get('x'), var.get('data'))
        PyJsHoisted_updateMutate_.func_name = 'updateMutate'
        var.put('updateMutate', PyJsHoisted_updateMutate_)
        @Js
        def PyJsHoisted_fromArray_(xs, cmp, this, arguments, var=var):
            var = Scope({'xs':xs, 'cmp':cmp, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'xs', 'result', 'i_finish', 'cmp', 'next', 'match', 'i'])
            var.put('len', var.get('xs').get('length'))
            if PyJsStrictEq(var.get('len'),Js(0.0)):
                return var.get(u"null")
            else:
                @Js
                def PyJs_anonymous_14_(param, PyJsArg_706172616d2431_, this, arguments, var=var):
                    var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'this':this, 'arguments':arguments}, var)
                    var.registers(['param$1', 'param'])
                    return (var.get('cmp')(var.get('param').get('0'), var.get('param$1').get('0'))<Js(0.0))
                PyJs_anonymous_14_._set_name('anonymous')
                var.put('next', var.get('Belt_SortArray').callprop('strictlySortedLengthU', var.get('xs'), PyJs_anonymous_14_))
                pass
                if (var.get('next')>=Js(0.0)):
                    var.put('result', var.get('fromSortedArrayAux')(var.get('xs'), Js(0.0), var.get('next')))
                else:
                    var.put('next', ((-var.get('next'))|Js(0.0)))
                    var.put('result', var.get('fromSortedArrayRevAux')(var.get('xs'), ((var.get('next')-Js(1.0))|Js(0.0)), var.get('next')))
                #for JS loop
                var.put('i', var.get('next'))
                var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.put('match', var.get('xs').get(var.get('i')))
                        var.put('result', var.get('updateMutate')(var.get('result'), var.get('match').get('0'), var.get('match').get('1'), var.get('cmp')))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('result')
        PyJsHoisted_fromArray_.func_name = 'fromArray'
        var.put('fromArray', PyJsHoisted_fromArray_)
        @Js
        def PyJsHoisted_removeMinAuxWithRootMutate_(nt, n, this, arguments, var=var):
            var = Scope({'nt':nt, 'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['ln', 'nt', 'rn', 'n'])
            var.put('rn', var.get('n').get('right'))
            var.put('ln', var.get('n').get('left'))
            if PyJsStrictNeq(var.get('ln'),var.get(u"null")):
                var.get('n').put('left', var.get('removeMinAuxWithRootMutate')(var.get('nt'), var.get('ln')))
                return var.get('balMutate')(var.get('n'))
            else:
                var.get('nt').put('key', var.get('n').get('key'))
                return var.get('rn')
        PyJsHoisted_removeMinAuxWithRootMutate_.func_name = 'removeMinAuxWithRootMutate'
        var.put('removeMinAuxWithRootMutate', PyJsHoisted_removeMinAuxWithRootMutate_)
        Js('use strict')
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Caml_option', var.get('require')(Js('./caml_option.js')))
        var.put('Belt_SortArray', var.get('require')(Js('./belt_SortArray.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('copy', var.get('copy'))
        var.get('exports').put('create', var.get('create'))
        var.get('exports').put('bal', var.get('bal'))
        var.get('exports').put('singleton', var.get('singleton'))
        var.get('exports').put('updateValue', var.get('updateValue'))
        var.get('exports').put('minKey', var.get('minKey'))
        var.get('exports').put('minKeyUndefined', var.get('minKeyUndefined'))
        var.get('exports').put('maxKey', var.get('maxKey'))
        var.get('exports').put('maxKeyUndefined', var.get('maxKeyUndefined'))
        var.get('exports').put('minimum', var.get('minimum'))
        var.get('exports').put('minUndefined', var.get('minUndefined'))
        var.get('exports').put('maximum', var.get('maximum'))
        var.get('exports').put('maxUndefined', var.get('maxUndefined'))
        var.get('exports').put('removeMinAuxWithRef', var.get('removeMinAuxWithRef'))
        var.get('exports').put('isEmpty', var.get('isEmpty'))
        var.get('exports').put('stackAllLeft', var.get('stackAllLeft'))
        var.get('exports').put('findFirstByU', var.get('findFirstByU'))
        var.get('exports').put('findFirstBy', var.get('findFirstBy'))
        var.get('exports').put('forEachU', var.get('forEachU'))
        var.get('exports').put('forEach', var.get('forEach'))
        var.get('exports').put('mapU', var.get('mapU'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('mapWithKeyU', var.get('mapWithKeyU'))
        var.get('exports').put('mapWithKey', var.get('mapWithKey'))
        var.get('exports').put('reduceU', var.get('reduceU'))
        var.get('exports').put('reduce', var.get('reduce'))
        var.get('exports').put('everyU', var.get('everyU'))
        var.get('exports').put('every', var.get('every'))
        var.get('exports').put('someU', var.get('someU'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('join', var.get('join'))
        var.get('exports').put('concat', var.get('concat'))
        var.get('exports').put('concatOrJoin', var.get('concatOrJoin'))
        var.get('exports').put('keepSharedU', var.get('keepSharedU'))
        var.get('exports').put('keepShared', var.get('keepShared'))
        var.get('exports').put('keepMapU', var.get('keepMapU'))
        var.get('exports').put('keepMap', var.get('keepMap'))
        var.get('exports').put('partitionSharedU', var.get('partitionSharedU'))
        var.get('exports').put('partitionShared', var.get('partitionShared'))
        var.get('exports').put('lengthNode', var.get('lengthNode'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('toList', var.get('toList'))
        var.get('exports').put('checkInvariantInternal', var.get('checkInvariantInternal'))
        var.get('exports').put('fillArray', var.get('fillArray'))
        var.get('exports').put('toArray', var.get('toArray'))
        var.get('exports').put('keysToArray', var.get('keysToArray'))
        var.get('exports').put('valuesToArray', var.get('valuesToArray'))
        var.get('exports').put('fromSortedArrayAux', var.get('fromSortedArrayAux'))
        var.get('exports').put('fromSortedArrayRevAux', var.get('fromSortedArrayRevAux'))
        var.get('exports').put('fromSortedArrayUnsafe', var.get('fromSortedArrayUnsafe'))
        var.get('exports').put('cmpU', var.get('cmpU'))
        var.get('exports').put('cmp', var.get('cmp'))
        var.get('exports').put('eqU', var.get('eqU'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('getUndefined', var.get('getUndefined'))
        var.get('exports').put('getWithDefault', var.get('getWithDefault'))
        var.get('exports').put('getExn', var.get('getExn'))
        var.get('exports').put('has', var.get('has'))
        var.get('exports').put('fromArray', var.get('fromArray'))
        var.get('exports').put('updateMutate', var.get('updateMutate'))
        var.get('exports').put('balMutate', var.get('balMutate'))
        var.get('exports').put('removeMinAuxWithRootMutate', var.get('removeMinAuxWithRootMutate'))
    PyJs_anonymous_13_._set_name('anonymous')
    @Js
    def PyJs_anonymous_15_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', '__', 'require', 'module'])
        @Js
        def PyJsHoisted____(tag, block, this, arguments, var=var):
            var = Scope({'tag':tag, 'block':block, 'this':this, 'arguments':arguments}, var)
            var.registers(['tag', 'block'])
            var.get('block').put('tag', var.get('tag'))
            return var.get('block')
        PyJsHoisted____.func_name = '__'
        var.put('__', PyJsHoisted____)
        Js('use strict')
        pass
        var.get('exports').put('__', var.get('__'))
    PyJs_anonymous_15_._set_name('anonymous')
    @Js
    def PyJs_anonymous_16_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['of_string', 'exports', 'map', 'sub', 'Caml_primitive', 'empty', 'uppercase', 'Char', 'apply1', 'rindex_opt', 'capitalize_ascii', 'iter', 'init', 'capitalize', 'trim', 'uppercase_ascii', 'Caml_bytes', 'rindex', 'rindex_from_opt', 'unsafe_to_string', 'mapi', 'rindex_rec_opt', 'iteri', 'unsafe_of_string', 'module', 'lowercase_ascii', 'fill', 'is_space', 'contains_from', 'index_rec_opt', 'copy', 'require', 'sub_string', 'uncapitalize', 'index_from', 'cat', 'Curry', 'index_from_opt', 'make', 'index', 'rindex_rec', 'rindex_from', 'Caml_builtin_exceptions', 'rcontains_from', 'to_string', 'blit_string', 'ensure_ge', 'compare', 'index_opt', 'concat', 'extend', 'equal', 'uncapitalize_ascii', 'lowercase', 'blit', 'contains', '$plus$plus', 'index_rec', 'escaped', 'sum_lengths'])
        @Js
        def PyJsHoisted_make_(n, c, this, arguments, var=var):
            var = Scope({'n':n, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'n', 's'])
            var.put('s', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('n')))
            var.get('Caml_bytes').callprop('caml_fill_bytes', var.get('s'), Js(0.0), var.get('n'), var.get('c'))
            return var.get('s')
        PyJsHoisted_make_.func_name = 'make'
        var.put('make', PyJsHoisted_make_)
        @Js
        def PyJsHoisted_init_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'i_finish', 's', 'n', 'i'])
            var.put('s', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('n')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('n')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('s').put(var.get('i'), var.get('Curry').callprop('_1', var.get('f'), var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('s')
        PyJsHoisted_init_.func_name = 'init'
        var.put('init', PyJsHoisted_init_)
        @Js
        def PyJsHoisted_copy_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'r', 's'])
            var.put('len', var.get('s').get('length'))
            var.put('r', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('len')))
            var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('s'), Js(0.0), var.get('r'), Js(0.0), var.get('len'))
            return var.get('r')
        PyJsHoisted_copy_.func_name = 'copy'
        var.put('copy', PyJsHoisted_copy_)
        @Js
        def PyJsHoisted_to_string_(b, this, arguments, var=var):
            var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['b'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('copy')(var.get('b')))
        PyJsHoisted_to_string_.func_name = 'to_string'
        var.put('to_string', PyJsHoisted_to_string_)
        @Js
        def PyJsHoisted_of_string_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('copy')(var.get('Caml_bytes').callprop('bytes_of_string', var.get('s')))
        PyJsHoisted_of_string_.func_name = 'of_string'
        var.put('of_string', PyJsHoisted_of_string_)
        @Js
        def PyJsHoisted_sub_(s, ofs, len, this, arguments, var=var):
            var = Scope({'s':s, 'ofs':ofs, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'ofs', 'r', 's'])
            if (((var.get('ofs')<Js(0.0)) or (var.get('len')<Js(0.0))) or (var.get('ofs')>((var.get('s').get('length')-var.get('len'))|Js(0.0)))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.sub / Bytes.sub')]))
                raise PyJsTempException
            var.put('r', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('len')))
            var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('s'), var.get('ofs'), var.get('r'), Js(0.0), var.get('len'))
            return var.get('r')
        PyJsHoisted_sub_.func_name = 'sub'
        var.put('sub', PyJsHoisted_sub_)
        @Js
        def PyJsHoisted_sub_string_(b, ofs, len, this, arguments, var=var):
            var = Scope({'b':b, 'ofs':ofs, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'b', 'ofs'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('sub')(var.get('b'), var.get('ofs'), var.get('len')))
        PyJsHoisted_sub_string_.func_name = 'sub_string'
        var.put('sub_string', PyJsHoisted_sub_string_)
        @Js
        def PyJsHoistedNonPyName(a, b, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['match$1', 'c', 'a', 'match', 'match$2', 'b'])
            var.put('c', ((var.get('a')+var.get('b'))|Js(0.0)))
            var.put('match', (var.get('a')<Js(0.0)))
            var.put('match$1', (var.get('b')<Js(0.0)))
            var.put('match$2', (var.get('c')<Js(0.0)))
            if var.get('match'):
                if (var.get('match$1') and var.get('match$2').neg()):
                    PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('Bytes.extend')]))
                    raise PyJsTempException
                else:
                    return var.get('c')
            else:
                if var.get('match$1'):
                    return var.get('c')
                else:
                    if var.get('match$2'):
                        PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('Bytes.extend')]))
                        raise PyJsTempException
                    return var.get('c')
        PyJsHoistedNonPyName.func_name = '$plus$plus'
        var.put('$plus$plus', PyJsHoistedNonPyName)
        @Js
        def PyJsHoisted_extend_(s, left, right, this, arguments, var=var):
            var = Scope({'s':s, 'left':left, 'right':right, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'srcoff', 'r', 'match', 's', 'dstoff', 'left', 'right', 'cpylen'])
            var.put('len', var.get('$plus$plus')(var.get('$plus$plus')(var.get('s').get('length'), var.get('left')), var.get('right')))
            var.put('r', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('len')))
            var.put('match', (Js([((-var.get('left'))|Js(0.0)), Js(0.0)]) if (var.get('left')<Js(0.0)) else Js([Js(0.0), var.get('left')])))
            var.put('dstoff', var.get('match').get('1'))
            var.put('srcoff', var.get('match').get('0'))
            var.put('cpylen', var.get('Caml_primitive').callprop('caml_int_min', ((var.get('s').get('length')-var.get('srcoff'))|Js(0.0)), ((var.get('len')-var.get('dstoff'))|Js(0.0))))
            if (var.get('cpylen')>Js(0.0)):
                var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('s'), var.get('srcoff'), var.get('r'), var.get('dstoff'), var.get('cpylen'))
            return var.get('r')
        PyJsHoisted_extend_.func_name = 'extend'
        var.put('extend', PyJsHoisted_extend_)
        @Js
        def PyJsHoisted_fill_(s, ofs, len, c, this, arguments, var=var):
            var = Scope({'s':s, 'ofs':ofs, 'len':len, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'c', 'ofs', 's'])
            if (((var.get('ofs')<Js(0.0)) or (var.get('len')<Js(0.0))) or (var.get('ofs')>((var.get('s').get('length')-var.get('len'))|Js(0.0)))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.fill / Bytes.fill')]))
                raise PyJsTempException
            return var.get('Caml_bytes').callprop('caml_fill_bytes', var.get('s'), var.get('ofs'), var.get('len'), var.get('c'))
        PyJsHoisted_fill_.func_name = 'fill'
        var.put('fill', PyJsHoisted_fill_)
        @Js
        def PyJsHoisted_blit_(s1, ofs1, s2, ofs2, len, this, arguments, var=var):
            var = Scope({'s1':s1, 'ofs1':ofs1, 's2':s2, 'ofs2':ofs2, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'ofs2', 's2', 's1', 'ofs1'])
            if (((((var.get('len')<Js(0.0)) or (var.get('ofs1')<Js(0.0))) or (var.get('ofs1')>((var.get('s1').get('length')-var.get('len'))|Js(0.0)))) or (var.get('ofs2')<Js(0.0))) or (var.get('ofs2')>((var.get('s2').get('length')-var.get('len'))|Js(0.0)))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('Bytes.blit')]))
                raise PyJsTempException
            return var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('s1'), var.get('ofs1'), var.get('s2'), var.get('ofs2'), var.get('len'))
        PyJsHoisted_blit_.func_name = 'blit'
        var.put('blit', PyJsHoisted_blit_)
        @Js
        def PyJsHoisted_blit_string_(s1, ofs1, s2, ofs2, len, this, arguments, var=var):
            var = Scope({'s1':s1, 'ofs1':ofs1, 's2':s2, 'ofs2':ofs2, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'ofs2', 's2', 's1', 'ofs1'])
            if (((((var.get('len')<Js(0.0)) or (var.get('ofs1')<Js(0.0))) or (var.get('ofs1')>((var.get('s1').get('length')-var.get('len'))|Js(0.0)))) or (var.get('ofs2')<Js(0.0))) or (var.get('ofs2')>((var.get('s2').get('length')-var.get('len'))|Js(0.0)))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.blit / Bytes.blit_string')]))
                raise PyJsTempException
            return var.get('Caml_bytes').callprop('caml_blit_string', var.get('s1'), var.get('ofs1'), var.get('s2'), var.get('ofs2'), var.get('len'))
        PyJsHoisted_blit_string_.func_name = 'blit_string'
        var.put('blit_string', PyJsHoisted_blit_string_)
        @Js
        def PyJsHoisted_iter_(f, a, this, arguments, var=var):
            var = Scope({'f':f, 'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'a', 'i', 'i_finish'])
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('Curry').callprop('_1', var.get('f'), var.get('a').get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_iter_.func_name = 'iter'
        var.put('iter', PyJsHoisted_iter_)
        @Js
        def PyJsHoisted_iteri_(f, a, this, arguments, var=var):
            var = Scope({'f':f, 'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'a', 'i', 'i_finish'])
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('a').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('Curry').callprop('_2', var.get('f'), var.get('i'), var.get('a').get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_iteri_.func_name = 'iteri'
        var.put('iteri', PyJsHoisted_iteri_)
        @Js
        def PyJsHoisted_ensure_ge_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')>=var.get('y')):
                return var.get('x')
            else:
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('Bytes.concat')]))
                raise PyJsTempException
        PyJsHoisted_ensure_ge_.func_name = 'ensure_ge'
        var.put('ensure_ge', PyJsHoisted_ensure_ge_)
        @Js
        def PyJsHoisted_sum_lengths_(_acc, seplen, _param, this, arguments, var=var):
            var = Scope({'_acc':_acc, 'seplen':seplen, '_param':_param, 'this':this, 'arguments':arguments}, var)
            var.registers(['_param', 'tl', 'acc', 'hd', 'seplen', '_acc', 'param'])
            while Js(True):
                var.put('param', var.get('_param'))
                var.put('acc', var.get('_acc'))
                if var.get('param'):
                    var.put('tl', var.get('param').get('1'))
                    var.put('hd', var.get('param').get('0'))
                    if var.get('tl'):
                        var.put('_param', var.get('tl'))
                        var.put('_acc', var.get('ensure_ge')(((((var.get('hd').get('length')+var.get('seplen'))|Js(0.0))+var.get('acc'))|Js(0.0)), var.get('acc')))
                        continue
                    else:
                        return ((var.get('hd').get('length')+var.get('acc'))|Js(0.0))
                else:
                    return var.get('acc')
            pass
        PyJsHoisted_sum_lengths_.func_name = 'sum_lengths'
        var.put('sum_lengths', PyJsHoisted_sum_lengths_)
        @Js
        def PyJsHoisted_concat_(sep, l, this, arguments, var=var):
            var = Scope({'sep':sep, 'l':l, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', '_pos', '_param', 'tl', 'pos', 'sep$1', 'seplen', 'hd', 'sep', 'seplen$1', 'param', 'l'])
            if var.get('l'):
                var.put('seplen', var.get('sep').get('length'))
                var.put('dst', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('sum_lengths')(Js(0.0), var.get('seplen'), var.get('l'))))
                var.put('_pos', Js(0.0))
                var.put('sep$1', var.get('sep'))
                var.put('seplen$1', var.get('seplen'))
                var.put('_param', var.get('l'))
                while Js(True):
                    var.put('param', var.get('_param'))
                    var.put('pos', var.get('_pos'))
                    if var.get('param'):
                        var.put('tl', var.get('param').get('1'))
                        var.put('hd', var.get('param').get('0'))
                        if var.get('tl'):
                            var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('hd'), Js(0.0), var.get('dst'), var.get('pos'), var.get('hd').get('length'))
                            var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('sep$1'), Js(0.0), var.get('dst'), ((var.get('pos')+var.get('hd').get('length'))|Js(0.0)), var.get('seplen$1'))
                            var.put('_param', var.get('tl'))
                            var.put('_pos', ((((var.get('pos')+var.get('hd').get('length'))|Js(0.0))+var.get('seplen$1'))|Js(0.0)))
                            continue
                        else:
                            var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('hd'), Js(0.0), var.get('dst'), var.get('pos'), var.get('hd').get('length'))
                            return var.get('dst')
                    else:
                        return var.get('dst')
                pass
            else:
                return var.get('empty')
        PyJsHoisted_concat_.func_name = 'concat'
        var.put('concat', PyJsHoisted_concat_)
        @Js
        def PyJsHoisted_cat_(s1, s2, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'this':this, 'arguments':arguments}, var)
            var.registers(['l2', 'l1', 'r', 's2', 's1'])
            var.put('l1', var.get('s1').get('length'))
            var.put('l2', var.get('s2').get('length'))
            var.put('r', var.get('Caml_bytes').callprop('caml_create_bytes', ((var.get('l1')+var.get('l2'))|Js(0.0))))
            var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('s1'), Js(0.0), var.get('r'), Js(0.0), var.get('l1'))
            var.get('Caml_bytes').callprop('caml_blit_bytes', var.get('s2'), Js(0.0), var.get('r'), var.get('l1'), var.get('l2'))
            return var.get('r')
        PyJsHoisted_cat_.func_name = 'cat'
        var.put('cat', PyJsHoisted_cat_)
        @Js
        def PyJsHoisted_is_space_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['switcher', 'param'])
            var.put('switcher', ((var.get('param')-Js(9.0))|Js(0.0)))
            if ((var.get('switcher')>Js(4.0)) or (var.get('switcher')<Js(0.0))):
                return PyJsStrictEq(var.get('switcher'),Js(23.0))
            else:
                return PyJsStrictNeq(var.get('switcher'),Js(2.0))
        PyJsHoisted_is_space_.func_name = 'is_space'
        var.put('is_space', PyJsHoisted_is_space_)
        @Js
        def PyJsHoisted_trim_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'i', 'j', 's'])
            var.put('len', var.get('s').get('length'))
            var.put('i', Js(0.0))
            while ((var.get('i')<var.get('len')) and var.get('is_space')(var.get('s').get(var.get('i')))):
                var.put('i', ((var.get('i')+Js(1.0))|Js(0.0)))
            pass
            var.put('j', ((var.get('len')-Js(1.0))|Js(0.0)))
            while ((var.get('j')>=var.get('i')) and var.get('is_space')(var.get('s').get(var.get('j')))):
                var.put('j', ((var.get('j')-Js(1.0))|Js(0.0)))
            pass
            if (var.get('j')>=var.get('i')):
                return var.get('sub')(var.get('s'), var.get('i'), ((((var.get('j')-var.get('i'))|Js(0.0))+Js(1.0))|Js(0.0)))
            else:
                return var.get('empty')
        PyJsHoisted_trim_.func_name = 'trim'
        var.put('trim', PyJsHoisted_trim_)
        @Js
        def PyJsHoisted_escaped_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['i$1', 'i_finish$1', 'switcher', 'c', 'tmp', 'i_finish', 'exit', 'match', 's$prime', 'n', 's', 'i'])
            var.put('n', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('s').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.put('match', var.get('s').get(var.get('i')))
                    pass
                    if (var.get('match')>=Js(32.0)):
                        var.put('switcher', ((var.get('match')-Js(34.0))|Js(0.0)))
                        var.put('tmp', ((Js(4.0) if (var.get('switcher')>=Js(93.0)) else Js(1.0)) if ((var.get('switcher')>Js(58.0)) or (var.get('switcher')<Js(0.0))) else (Js(2.0) if ((var.get('switcher')>Js(57.0)) or (var.get('switcher')<Js(1.0))) else Js(1.0))))
                    else:
                        var.put('tmp', ((Js(4.0) if PyJsStrictNeq(var.get('match'),Js(13.0)) else Js(2.0)) if (var.get('match')>=Js(11.0)) else (Js(2.0) if (var.get('match')>=Js(8.0)) else Js(4.0))))
                    var.put('n', ((var.get('n')+var.get('tmp'))|Js(0.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if PyJsStrictEq(var.get('n'),var.get('s').get('length')):
                return var.get('copy')(var.get('s'))
            else:
                var.put('s$prime', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('n')))
                var.put('n', Js(0.0))
                #for JS loop
                var.put('i$1', Js(0.0))
                var.put('i_finish$1', ((var.get('s').get('length')-Js(1.0))|Js(0.0)))
                while (var.get('i$1')<=var.get('i_finish$1')):
                    try:
                        var.put('c', var.get('s').get(var.get('i$1')))
                        var.put('exit', Js(0.0))
                        if (var.get('c')>=Js(35.0)):
                            if PyJsStrictNeq(var.get('c'),Js(92.0)):
                                if (var.get('c')>=Js(127.0)):
                                    var.put('exit', Js(1.0))
                                else:
                                    var.get('s$prime').put(var.get('n'), var.get('c'))
                            else:
                                var.put('exit', Js(2.0))
                        else:
                            if (var.get('c')>=Js(32.0)):
                                if (var.get('c')>=Js(34.0)):
                                    var.put('exit', Js(2.0))
                                else:
                                    var.get('s$prime').put(var.get('n'), var.get('c'))
                            else:
                                if (var.get('c')>=Js(14.0)):
                                    var.put('exit', Js(1.0))
                                else:
                                    while 1:
                                        SWITCHED = False
                                        CONDITION = (var.get('c'))
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
                                            SWITCHED = True
                                            var.get('s$prime').put(var.get('n'), Js(92.0))
                                            var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                            var.get('s$prime').put(var.get('n'), Js(98.0))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
                                            SWITCHED = True
                                            var.get('s$prime').put(var.get('n'), Js(92.0))
                                            var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                            var.get('s$prime').put(var.get('n'), Js(116.0))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
                                            SWITCHED = True
                                            var.get('s$prime').put(var.get('n'), Js(92.0))
                                            var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                            var.get('s$prime').put(var.get('n'), Js(110.0))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
                                            SWITCHED = True
                                            pass
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
                                            SWITCHED = True
                                            var.put('exit', Js(1.0))
                                            break
                                        if SWITCHED or PyJsStrictEq(CONDITION, Js(13.0)):
                                            SWITCHED = True
                                            var.get('s$prime').put(var.get('n'), Js(92.0))
                                            var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                            var.get('s$prime').put(var.get('n'), Js(114.0))
                                            break
                                        SWITCHED = True
                                        break
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('exit'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                SWITCHED = True
                                var.get('s$prime').put(var.get('n'), Js(92.0))
                                var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                var.get('s$prime').put(var.get('n'), ((Js(48.0)+((var.get('c')/Js(100.0))|Js(0.0)))|Js(0.0)))
                                var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                var.get('s$prime').put(var.get('n'), ((Js(48.0)+(((var.get('c')/Js(10.0))|Js(0.0))%Js(10.0)))|Js(0.0)))
                                var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                var.get('s$prime').put(var.get('n'), ((Js(48.0)+(var.get('c')%Js(10.0)))|Js(0.0)))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                SWITCHED = True
                                var.get('s$prime').put(var.get('n'), Js(92.0))
                                var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                                var.get('s$prime').put(var.get('n'), var.get('c'))
                                break
                            SWITCHED = True
                            break
                        var.put('n', ((var.get('n')+Js(1.0))|Js(0.0)))
                    finally:
                            var.put('i$1',Js(var.get('i$1').to_number())+Js(1))
                return var.get('s$prime')
        PyJsHoisted_escaped_.func_name = 'escaped'
        var.put('escaped', PyJsHoisted_escaped_)
        @Js
        def PyJsHoisted_map_(f, s, this, arguments, var=var):
            var = Scope({'f':f, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'i_finish', 'r', 's', 'i', 'l'])
            var.put('l', var.get('s').get('length'))
            if PyJsStrictEq(var.get('l'),Js(0.0)):
                return var.get('s')
            else:
                var.put('r', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('l')))
                #for JS loop
                var.put('i', Js(0.0))
                var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.get('r').put(var.get('i'), var.get('Curry').callprop('_1', var.get('f'), var.get('s').get(var.get('i'))))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('r')
        PyJsHoisted_map_.func_name = 'map'
        var.put('map', PyJsHoisted_map_)
        @Js
        def PyJsHoisted_mapi_(f, s, this, arguments, var=var):
            var = Scope({'f':f, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'i_finish', 'r', 's', 'i', 'l'])
            var.put('l', var.get('s').get('length'))
            if PyJsStrictEq(var.get('l'),Js(0.0)):
                return var.get('s')
            else:
                var.put('r', var.get('Caml_bytes').callprop('caml_create_bytes', var.get('l')))
                #for JS loop
                var.put('i', Js(0.0))
                var.put('i_finish', ((var.get('l')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.get('r').put(var.get('i'), var.get('Curry').callprop('_2', var.get('f'), var.get('i'), var.get('s').get(var.get('i'))))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return var.get('r')
        PyJsHoisted_mapi_.func_name = 'mapi'
        var.put('mapi', PyJsHoisted_mapi_)
        @Js
        def PyJsHoisted_uppercase_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('map')(var.get('Char').get('uppercase_ascii'), var.get('s'))
        PyJsHoisted_uppercase_ascii_.func_name = 'uppercase_ascii'
        var.put('uppercase_ascii', PyJsHoisted_uppercase_ascii_)
        @Js
        def PyJsHoisted_lowercase_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('map')(var.get('Char').get('lowercase_ascii'), var.get('s'))
        PyJsHoisted_lowercase_ascii_.func_name = 'lowercase_ascii'
        var.put('lowercase_ascii', PyJsHoisted_lowercase_ascii_)
        @Js
        def PyJsHoisted_apply1_(f, s, this, arguments, var=var):
            var = Scope({'f':f, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'r', 's'])
            if PyJsStrictEq(var.get('s').get('length'),Js(0.0)):
                return var.get('s')
            else:
                var.put('r', var.get('copy')(var.get('s')))
                var.get('r').put('0', var.get('Curry').callprop('_1', var.get('f'), var.get('s').get('0')))
                return var.get('r')
        PyJsHoisted_apply1_.func_name = 'apply1'
        var.put('apply1', PyJsHoisted_apply1_)
        @Js
        def PyJsHoisted_capitalize_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('apply1')(var.get('Char').get('uppercase_ascii'), var.get('s'))
        PyJsHoisted_capitalize_ascii_.func_name = 'capitalize_ascii'
        var.put('capitalize_ascii', PyJsHoisted_capitalize_ascii_)
        @Js
        def PyJsHoisted_uncapitalize_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('apply1')(var.get('Char').get('lowercase_ascii'), var.get('s'))
        PyJsHoisted_uncapitalize_ascii_.func_name = 'uncapitalize_ascii'
        var.put('uncapitalize_ascii', PyJsHoisted_uncapitalize_ascii_)
        @Js
        def PyJsHoisted_index_rec_(s, lim, _i, c, this, arguments, var=var):
            var = Scope({'s':s, 'lim':lim, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['lim', 'c', '_i', 's', 'i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')>=var.get('lim')):
                    PyJsTempException = JsToPyException(var.get('Caml_builtin_exceptions').get('not_found'))
                    raise PyJsTempException
                if PyJsStrictEq(var.get('s').get(var.get('i')),var.get('c')):
                    return var.get('i')
                else:
                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                    continue
            pass
        PyJsHoisted_index_rec_.func_name = 'index_rec'
        var.put('index_rec', PyJsHoisted_index_rec_)
        @Js
        def PyJsHoisted_index_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('index_rec')(var.get('s'), var.get('s').get('length'), Js(0.0), var.get('c'))
        PyJsHoisted_index_.func_name = 'index'
        var.put('index', PyJsHoisted_index_)
        @Js
        def PyJsHoisted_index_rec_opt_(s, lim, _i, c, this, arguments, var=var):
            var = Scope({'s':s, 'lim':lim, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['lim', 'c', '_i', 's', 'i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')>=var.get('lim')):
                    return var.get('undefined')
                else:
                    if PyJsStrictEq(var.get('s').get(var.get('i')),var.get('c')):
                        return var.get('i')
                    else:
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        continue
            pass
        PyJsHoisted_index_rec_opt_.func_name = 'index_rec_opt'
        var.put('index_rec_opt', PyJsHoisted_index_rec_opt_)
        @Js
        def PyJsHoisted_index_opt_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('index_rec_opt')(var.get('s'), var.get('s').get('length'), Js(0.0), var.get('c'))
        PyJsHoisted_index_opt_.func_name = 'index_opt'
        var.put('index_opt', PyJsHoisted_index_opt_)
        @Js
        def PyJsHoisted_index_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', 'l'])
            var.put('l', var.get('s').get('length'))
            if ((var.get('i')<Js(0.0)) or (var.get('i')>var.get('l'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.index_from / Bytes.index_from')]))
                raise PyJsTempException
            return var.get('index_rec')(var.get('s'), var.get('l'), var.get('i'), var.get('c'))
        PyJsHoisted_index_from_.func_name = 'index_from'
        var.put('index_from', PyJsHoisted_index_from_)
        @Js
        def PyJsHoisted_index_from_opt_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', 'l'])
            var.put('l', var.get('s').get('length'))
            if ((var.get('i')<Js(0.0)) or (var.get('i')>var.get('l'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.index_from_opt / Bytes.index_from_opt')]))
                raise PyJsTempException
            return var.get('index_rec_opt')(var.get('s'), var.get('l'), var.get('i'), var.get('c'))
        PyJsHoisted_index_from_opt_.func_name = 'index_from_opt'
        var.put('index_from_opt', PyJsHoisted_index_from_opt_)
        @Js
        def PyJsHoisted_rindex_rec_(s, _i, c, this, arguments, var=var):
            var = Scope({'s':s, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', '_i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')<Js(0.0)):
                    PyJsTempException = JsToPyException(var.get('Caml_builtin_exceptions').get('not_found'))
                    raise PyJsTempException
                if PyJsStrictEq(var.get('s').get(var.get('i')),var.get('c')):
                    return var.get('i')
                else:
                    var.put('_i', ((var.get('i')-Js(1.0))|Js(0.0)))
                    continue
            pass
        PyJsHoisted_rindex_rec_.func_name = 'rindex_rec'
        var.put('rindex_rec', PyJsHoisted_rindex_rec_)
        @Js
        def PyJsHoisted_rindex_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('rindex_rec')(var.get('s'), ((var.get('s').get('length')-Js(1.0))|Js(0.0)), var.get('c'))
        PyJsHoisted_rindex_.func_name = 'rindex'
        var.put('rindex', PyJsHoisted_rindex_)
        @Js
        def PyJsHoisted_rindex_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's'])
            if ((var.get('i')<(-Js(1.0))) or (var.get('i')>=var.get('s').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.rindex_from / Bytes.rindex_from')]))
                raise PyJsTempException
            return var.get('rindex_rec')(var.get('s'), var.get('i'), var.get('c'))
        PyJsHoisted_rindex_from_.func_name = 'rindex_from'
        var.put('rindex_from', PyJsHoisted_rindex_from_)
        @Js
        def PyJsHoisted_rindex_rec_opt_(s, _i, c, this, arguments, var=var):
            var = Scope({'s':s, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', '_i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')<Js(0.0)):
                    return var.get('undefined')
                else:
                    if PyJsStrictEq(var.get('s').get(var.get('i')),var.get('c')):
                        return var.get('i')
                    else:
                        var.put('_i', ((var.get('i')-Js(1.0))|Js(0.0)))
                        continue
            pass
        PyJsHoisted_rindex_rec_opt_.func_name = 'rindex_rec_opt'
        var.put('rindex_rec_opt', PyJsHoisted_rindex_rec_opt_)
        @Js
        def PyJsHoisted_rindex_opt_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('rindex_rec_opt')(var.get('s'), ((var.get('s').get('length')-Js(1.0))|Js(0.0)), var.get('c'))
        PyJsHoisted_rindex_opt_.func_name = 'rindex_opt'
        var.put('rindex_opt', PyJsHoisted_rindex_opt_)
        @Js
        def PyJsHoisted_rindex_from_opt_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's'])
            if ((var.get('i')<(-Js(1.0))) or (var.get('i')>=var.get('s').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.rindex_from_opt / Bytes.rindex_from_opt')]))
                raise PyJsTempException
            return var.get('rindex_rec_opt')(var.get('s'), var.get('i'), var.get('c'))
        PyJsHoisted_rindex_from_opt_.func_name = 'rindex_from_opt'
        var.put('rindex_from_opt', PyJsHoisted_rindex_from_opt_)
        @Js
        def PyJsHoisted_contains_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', 'l'])
            var.put('l', var.get('s').get('length'))
            if ((var.get('i')<Js(0.0)) or (var.get('i')>var.get('l'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.contains_from / Bytes.contains_from')]))
                raise PyJsTempException
            try:
                var.get('index_rec')(var.get('s'), var.get('l'), var.get('i'), var.get('c'))
                return Js(True)
            except PyJsException as PyJsTempException:
                PyJsHolder_65786e_64738238 = var.own.get('exn')
                var.force_own_put('exn', PyExceptionToJs(PyJsTempException))
                try:
                    if PyJsStrictEq(var.get('exn'),var.get('Caml_builtin_exceptions').get('not_found')):
                        return Js(False)
                    else:
                        PyJsTempException = JsToPyException(var.get('exn'))
                        raise PyJsTempException
                finally:
                    if PyJsHolder_65786e_64738238 is not None:
                        var.own['exn'] = PyJsHolder_65786e_64738238
                    else:
                        del var.own['exn']
                    del PyJsHolder_65786e_64738238
        PyJsHoisted_contains_from_.func_name = 'contains_from'
        var.put('contains_from', PyJsHoisted_contains_from_)
        @Js
        def PyJsHoisted_contains_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('contains_from')(var.get('s'), Js(0.0), var.get('c'))
        PyJsHoisted_contains_.func_name = 'contains'
        var.put('contains', PyJsHoisted_contains_)
        @Js
        def PyJsHoisted_rcontains_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's'])
            if ((var.get('i')<Js(0.0)) or (var.get('i')>=var.get('s').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.rcontains_from / Bytes.rcontains_from')]))
                raise PyJsTempException
            try:
                var.get('rindex_rec')(var.get('s'), var.get('i'), var.get('c'))
                return Js(True)
            except PyJsException as PyJsTempException:
                PyJsHolder_65786e_31298553 = var.own.get('exn')
                var.force_own_put('exn', PyExceptionToJs(PyJsTempException))
                try:
                    if PyJsStrictEq(var.get('exn'),var.get('Caml_builtin_exceptions').get('not_found')):
                        return Js(False)
                    else:
                        PyJsTempException = JsToPyException(var.get('exn'))
                        raise PyJsTempException
                finally:
                    if PyJsHolder_65786e_31298553 is not None:
                        var.own['exn'] = PyJsHolder_65786e_31298553
                    else:
                        del var.own['exn']
                    del PyJsHolder_65786e_31298553
        PyJsHoisted_rcontains_from_.func_name = 'rcontains_from'
        var.put('rcontains_from', PyJsHoisted_rcontains_from_)
        @Js
        def PyJsHoisted_uppercase_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('map')(var.get('Char').get('uppercase'), var.get('s'))
        PyJsHoisted_uppercase_.func_name = 'uppercase'
        var.put('uppercase', PyJsHoisted_uppercase_)
        @Js
        def PyJsHoisted_lowercase_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('map')(var.get('Char').get('lowercase'), var.get('s'))
        PyJsHoisted_lowercase_.func_name = 'lowercase'
        var.put('lowercase', PyJsHoisted_lowercase_)
        @Js
        def PyJsHoisted_capitalize_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('apply1')(var.get('Char').get('uppercase'), var.get('s'))
        PyJsHoisted_capitalize_.func_name = 'capitalize'
        var.put('capitalize', PyJsHoisted_capitalize_)
        @Js
        def PyJsHoisted_uncapitalize_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('apply1')(var.get('Char').get('lowercase'), var.get('s'))
        PyJsHoisted_uncapitalize_.func_name = 'uncapitalize'
        var.put('uncapitalize', PyJsHoisted_uncapitalize_)
        Js('use strict')
        var.put('Char', var.get('require')(Js('./char.js')))
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Caml_bytes', var.get('require')(Js('./caml_bytes.js')))
        var.put('Caml_primitive', var.get('require')(Js('./caml_primitive.js')))
        var.put('Caml_builtin_exceptions', var.get('require')(Js('./caml_builtin_exceptions.js')))
        pass
        pass
        var.put('empty', Js([]))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('compare', var.get('Caml_primitive').get('caml_bytes_compare'))
        pass
        pass
        pass
        pass
        var.put('equal', var.get('Caml_primitive').get('caml_bytes_equal'))
        var.put('unsafe_to_string', var.get('Caml_bytes').get('bytes_to_string'))
        var.put('unsafe_of_string', var.get('Caml_bytes').get('bytes_of_string'))
        var.get('exports').put('make', var.get('make'))
        var.get('exports').put('init', var.get('init'))
        var.get('exports').put('empty', var.get('empty'))
        var.get('exports').put('copy', var.get('copy'))
        var.get('exports').put('of_string', var.get('of_string'))
        var.get('exports').put('to_string', var.get('to_string'))
        var.get('exports').put('sub', var.get('sub'))
        var.get('exports').put('sub_string', var.get('sub_string'))
        var.get('exports').put('extend', var.get('extend'))
        var.get('exports').put('fill', var.get('fill'))
        var.get('exports').put('blit', var.get('blit'))
        var.get('exports').put('blit_string', var.get('blit_string'))
        var.get('exports').put('concat', var.get('concat'))
        var.get('exports').put('cat', var.get('cat'))
        var.get('exports').put('iter', var.get('iter'))
        var.get('exports').put('iteri', var.get('iteri'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('mapi', var.get('mapi'))
        var.get('exports').put('trim', var.get('trim'))
        var.get('exports').put('escaped', var.get('escaped'))
        var.get('exports').put('index', var.get('index'))
        var.get('exports').put('index_opt', var.get('index_opt'))
        var.get('exports').put('rindex', var.get('rindex'))
        var.get('exports').put('rindex_opt', var.get('rindex_opt'))
        var.get('exports').put('index_from', var.get('index_from'))
        var.get('exports').put('index_from_opt', var.get('index_from_opt'))
        var.get('exports').put('rindex_from', var.get('rindex_from'))
        var.get('exports').put('rindex_from_opt', var.get('rindex_from_opt'))
        var.get('exports').put('contains', var.get('contains'))
        var.get('exports').put('contains_from', var.get('contains_from'))
        var.get('exports').put('rcontains_from', var.get('rcontains_from'))
        var.get('exports').put('uppercase', var.get('uppercase'))
        var.get('exports').put('lowercase', var.get('lowercase'))
        var.get('exports').put('capitalize', var.get('capitalize'))
        var.get('exports').put('uncapitalize', var.get('uncapitalize'))
        var.get('exports').put('uppercase_ascii', var.get('uppercase_ascii'))
        var.get('exports').put('lowercase_ascii', var.get('lowercase_ascii'))
        var.get('exports').put('capitalize_ascii', var.get('capitalize_ascii'))
        var.get('exports').put('uncapitalize_ascii', var.get('uncapitalize_ascii'))
        var.get('exports').put('compare', var.get('compare'))
        var.get('exports').put('equal', var.get('equal'))
        var.get('exports').put('unsafe_to_string', var.get('unsafe_to_string'))
        var.get('exports').put('unsafe_of_string', var.get('unsafe_of_string'))
    PyJs_anonymous_16_._set_name('anonymous')
    @Js
    def PyJs_anonymous_17_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['len', 'exports', 'require', 'caml_array_set', 'caml_array_get', 'caml_array_blit', 'module', 'caml_array_sub', 'Caml_builtin_exceptions', 'caml_make_vect', 'fill', 'caml_make_float_vect', 'caml_array_dup', 'caml_array_concat'])
        @Js
        def PyJsHoisted_caml_array_sub_(x, offset, len, this, arguments, var=var):
            var = Scope({'x':x, 'offset':offset, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'j', 'result', 'x', 'offset', 'i'])
            var.put('result', var.get('Array').create(var.get('len')))
            var.put('j', Js(0.0))
            var.put('i', var.get('offset'))
            while (var.get('j')<var.get('len')):
                var.get('result').put(var.get('j'), var.get('x').get(var.get('i')))
                var.put('j', ((var.get('j')+Js(1.0))|Js(0.0)))
                var.put('i', ((var.get('i')+Js(1.0))|Js(0.0)))
            pass
            return var.get('result')
        PyJsHoisted_caml_array_sub_.func_name = 'caml_array_sub'
        var.put('caml_array_sub', PyJsHoisted_caml_array_sub_)
        @Js
        def PyJsHoisted_len_(_acc, _l, this, arguments, var=var):
            var = Scope({'_acc':_acc, '_l':_l, 'this':this, 'arguments':arguments}, var)
            var.registers(['acc', '_l', '_acc', 'l'])
            while Js(True):
                var.put('l', var.get('_l'))
                var.put('acc', var.get('_acc'))
                if var.get('l'):
                    var.put('_l', var.get('l').get('1'))
                    var.put('_acc', ((var.get('l').get('0').get('length')+var.get('acc'))|Js(0.0)))
                    continue
                else:
                    return var.get('acc')
            pass
        PyJsHoisted_len_.func_name = 'len'
        var.put('len', PyJsHoisted_len_)
        @Js
        def PyJsHoisted_fill_(arr, _i, _l, this, arguments, var=var):
            var = Scope({'arr':arr, '_i':_i, '_l':_l, 'this':this, 'arguments':arguments}, var)
            var.registers(['l$1', 'j', 'x', '_i', 'k', 'arr', '_l', 'i', 'l'])
            while Js(True):
                var.put('l', var.get('_l'))
                var.put('i', var.get('_i'))
                if var.get('l'):
                    var.put('x', var.get('l').get('0'))
                    var.put('l$1', var.get('x').get('length'))
                    var.put('k', var.get('i'))
                    var.put('j', Js(0.0))
                    while (var.get('j')<var.get('l$1')):
                        var.get('arr').put(var.get('k'), var.get('x').get(var.get('j')))
                        var.put('k', ((var.get('k')+Js(1.0))|Js(0.0)))
                        var.put('j', ((var.get('j')+Js(1.0))|Js(0.0)))
                    pass
                    var.put('_l', var.get('l').get('1'))
                    var.put('_i', var.get('k'))
                    continue
                else:
                    return Js(0.0)
            pass
        PyJsHoisted_fill_.func_name = 'fill'
        var.put('fill', PyJsHoisted_fill_)
        @Js
        def PyJsHoisted_caml_array_concat_(l, this, arguments, var=var):
            var = Scope({'l':l, 'this':this, 'arguments':arguments}, var)
            var.registers(['result', 'v', 'l'])
            var.put('v', var.get('len')(Js(0.0), var.get('l')))
            var.put('result', var.get('Array').create(var.get('v')))
            var.get('fill')(var.get('result'), Js(0.0), var.get('l'))
            return var.get('result')
        PyJsHoisted_caml_array_concat_.func_name = 'caml_array_concat'
        var.put('caml_array_concat', PyJsHoisted_caml_array_concat_)
        @Js
        def PyJsHoisted_caml_array_set_(xs, index, newval, this, arguments, var=var):
            var = Scope({'xs':xs, 'index':index, 'newval':newval, 'this':this, 'arguments':arguments}, var)
            var.registers(['index', 'xs', 'newval'])
            if ((var.get('index')<Js(0.0)) or (var.get('index')>=var.get('xs').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('index out of bounds')]))
                raise PyJsTempException
            var.get('xs').put(var.get('index'), var.get('newval'))
            return Js(0.0)
        PyJsHoisted_caml_array_set_.func_name = 'caml_array_set'
        var.put('caml_array_set', PyJsHoisted_caml_array_set_)
        @Js
        def PyJsHoisted_caml_array_get_(xs, index, this, arguments, var=var):
            var = Scope({'xs':xs, 'index':index, 'this':this, 'arguments':arguments}, var)
            var.registers(['index', 'xs'])
            if ((var.get('index')<Js(0.0)) or (var.get('index')>=var.get('xs').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('index out of bounds')]))
                raise PyJsTempException
            return var.get('xs').get(var.get('index'))
        PyJsHoisted_caml_array_get_.func_name = 'caml_array_get'
        var.put('caml_array_get', PyJsHoisted_caml_array_get_)
        @Js
        def PyJsHoisted_caml_make_vect_(len, init, this, arguments, var=var):
            var = Scope({'len':len, 'init':init, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'i_finish', 'init', 'b', 'i'])
            var.put('b', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('b').put(var.get('i'), var.get('init'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('b')
        PyJsHoisted_caml_make_vect_.func_name = 'caml_make_vect'
        var.put('caml_make_vect', PyJsHoisted_caml_make_vect_)
        @Js
        def PyJsHoisted_caml_make_float_vect_(len, this, arguments, var=var):
            var = Scope({'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'b', 'i', 'i_finish'])
            var.put('b', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('b').put(var.get('i'), Js(0.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('b')
        PyJsHoisted_caml_make_float_vect_.func_name = 'caml_make_float_vect'
        var.put('caml_make_float_vect', PyJsHoisted_caml_make_float_vect_)
        @Js
        def PyJsHoisted_caml_array_blit_(a1, i1, a2, i2, len, this, arguments, var=var):
            var = Scope({'a1':a1, 'i1':i1, 'a2':a2, 'i2':i2, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'a1', 'j', 'a2', 'i2', 'i1', 'j$1', 'j_finish'])
            if (var.get('i2')<=var.get('i1')):
                #for JS loop
                var.put('j', Js(0.0))
                var.put('j_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
                while (var.get('j')<=var.get('j_finish')):
                    try:
                        var.get('a2').put(((var.get('j')+var.get('i2'))|Js(0.0)), var.get('a1').get(((var.get('j')+var.get('i1'))|Js(0.0))))
                    finally:
                            var.put('j',Js(var.get('j').to_number())+Js(1))
                return Js(0.0)
            else:
                #for JS loop
                var.put('j$1', ((var.get('len')-Js(1.0))|Js(0.0)))
                while (var.get('j$1')>=Js(0.0)):
                    try:
                        var.get('a2').put(((var.get('j$1')+var.get('i2'))|Js(0.0)), var.get('a1').get(((var.get('j$1')+var.get('i1'))|Js(0.0))))
                    finally:
                            var.put('j$1',Js(var.get('j$1').to_number())-Js(1))
                return Js(0.0)
        PyJsHoisted_caml_array_blit_.func_name = 'caml_array_blit'
        var.put('caml_array_blit', PyJsHoisted_caml_array_blit_)
        @Js
        def PyJsHoisted_caml_array_dup_(prim, this, arguments, var=var):
            var = Scope({'prim':prim, 'this':this, 'arguments':arguments}, var)
            var.registers(['prim'])
            return var.get('prim').callprop('slice', Js(0.0))
        PyJsHoisted_caml_array_dup_.func_name = 'caml_array_dup'
        var.put('caml_array_dup', PyJsHoisted_caml_array_dup_)
        Js('use strict')
        var.put('Caml_builtin_exceptions', var.get('require')(Js('./caml_builtin_exceptions.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('caml_array_dup', var.get('caml_array_dup'))
        var.get('exports').put('caml_array_sub', var.get('caml_array_sub'))
        var.get('exports').put('caml_array_concat', var.get('caml_array_concat'))
        var.get('exports').put('caml_make_vect', var.get('caml_make_vect'))
        var.get('exports').put('caml_make_float_vect', var.get('caml_make_float_vect'))
        var.get('exports').put('caml_array_blit', var.get('caml_array_blit'))
        var.get('exports').put('caml_array_get', var.get('caml_array_get'))
        var.get('exports').put('caml_array_set', var.get('caml_array_set'))
    PyJs_anonymous_17_._set_name('anonymous')
    @Js
    def PyJs_anonymous_18_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['out_of_memory', 'exports', 'match_failure', 'stack_overflow', 'require', 'failure', 'not_found', 'module', 'invalid_argument', 'assert_failure', 'sys_error', 'division_by_zero', 'undefined_recursive_module', 'end_of_file', 'sys_blocked_io'])
        Js('use strict')
        var.put('out_of_memory', Js([Js('Out_of_memory'), Js(0.0)]))
        var.put('sys_error', Js([Js('Sys_error'), (-Js(1.0))]))
        var.put('failure', Js([Js('Failure'), (-Js(2.0))]))
        var.put('invalid_argument', Js([Js('Invalid_argument'), (-Js(3.0))]))
        var.put('end_of_file', Js([Js('End_of_file'), (-Js(4.0))]))
        var.put('division_by_zero', Js([Js('Division_by_zero'), (-Js(5.0))]))
        var.put('not_found', Js([Js('Not_found'), (-Js(6.0))]))
        var.put('match_failure', Js([Js('Match_failure'), (-Js(7.0))]))
        var.put('stack_overflow', Js([Js('Stack_overflow'), (-Js(8.0))]))
        var.put('sys_blocked_io', Js([Js('Sys_blocked_io'), (-Js(9.0))]))
        var.put('assert_failure', Js([Js('Assert_failure'), (-Js(10.0))]))
        var.put('undefined_recursive_module', Js([Js('Undefined_recursive_module'), (-Js(11.0))]))
        var.get('out_of_memory').put('tag', Js(248.0))
        var.get('sys_error').put('tag', Js(248.0))
        var.get('failure').put('tag', Js(248.0))
        var.get('invalid_argument').put('tag', Js(248.0))
        var.get('end_of_file').put('tag', Js(248.0))
        var.get('division_by_zero').put('tag', Js(248.0))
        var.get('not_found').put('tag', Js(248.0))
        var.get('match_failure').put('tag', Js(248.0))
        var.get('stack_overflow').put('tag', Js(248.0))
        var.get('sys_blocked_io').put('tag', Js(248.0))
        var.get('assert_failure').put('tag', Js(248.0))
        var.get('undefined_recursive_module').put('tag', Js(248.0))
        var.get('exports').put('out_of_memory', var.get('out_of_memory'))
        var.get('exports').put('sys_error', var.get('sys_error'))
        var.get('exports').put('failure', var.get('failure'))
        var.get('exports').put('invalid_argument', var.get('invalid_argument'))
        var.get('exports').put('end_of_file', var.get('end_of_file'))
        var.get('exports').put('division_by_zero', var.get('division_by_zero'))
        var.get('exports').put('not_found', var.get('not_found'))
        var.get('exports').put('match_failure', var.get('match_failure'))
        var.get('exports').put('stack_overflow', var.get('stack_overflow'))
        var.get('exports').put('sys_blocked_io', var.get('sys_blocked_io'))
        var.get('exports').put('assert_failure', var.get('assert_failure'))
        var.get('exports').put('undefined_recursive_module', var.get('undefined_recursive_module'))
    PyJs_anonymous_18_._set_name('anonymous')
    @Js
    def PyJs_anonymous_19_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['get', 'caml_create_bytes', 'exports', 'require', 'caml_fill_bytes', 'bytes_of_string', 'module', 'Caml_builtin_exceptions', 'caml_blit_bytes', 'bytes_to_string', 'caml_blit_string'])
        @Js
        def PyJsHoisted_get_(s, i, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 's'])
            if ((var.get('i')<Js(0.0)) or (var.get('i')>=var.get('s').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('index out of bounds')]))
                raise PyJsTempException
            return var.get('s').get(var.get('i'))
        PyJsHoisted_get_.func_name = 'get'
        var.put('get', PyJsHoisted_get_)
        @Js
        def PyJsHoisted_caml_fill_bytes_(s, i, l, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'l':l, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'k_finish', 'k', 's', 'i', 'l'])
            if (var.get('l')>Js(0.0)):
                #for JS loop
                var.put('k', var.get('i'))
                var.put('k_finish', ((((var.get('l')+var.get('i'))|Js(0.0))-Js(1.0))|Js(0.0)))
                while (var.get('k')<=var.get('k_finish')):
                    try:
                        var.get('s').put(var.get('k'), var.get('c'))
                    finally:
                            var.put('k',Js(var.get('k').to_number())+Js(1))
                return Js(0.0)
            else:
                return Js(0.0)
        PyJsHoisted_caml_fill_bytes_.func_name = 'caml_fill_bytes'
        var.put('caml_fill_bytes', PyJsHoisted_caml_fill_bytes_)
        @Js
        def PyJsHoisted_caml_create_bytes_(len, this, arguments, var=var):
            var = Scope({'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'i', 'result', 'i_finish'])
            if (var.get('len')<Js(0.0)):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.create')]))
                raise PyJsTempException
            var.put('result', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('result').put(var.get('i'), Js(0.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('result')
        PyJsHoisted_caml_create_bytes_.func_name = 'caml_create_bytes'
        var.put('caml_create_bytes', PyJsHoisted_caml_create_bytes_)
        @Js
        def PyJsHoisted_caml_blit_bytes_(s1, i1, s2, i2, len, this, arguments, var=var):
            var = Scope({'s1':s1, 'i1':i1, 's2':s2, 'i2':i2, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'i2$1', 'range_a', 'range_a$1', 'i1', 'i$2', 'i_finish$2', 'i', 's1$1', 'len$1', 'range_b$1', 'k', 'range', 'i$1', 'i1$1', 'j', 'range_b', 'i_finish', 'off1', 's1', 'i_finish$1', 'range$1', 'i2', 's2'])
            if (var.get('len')>Js(0.0)):
                if PyJsStrictEq(var.get('s1'),var.get('s2')):
                    var.put('s1$1', var.get('s1'))
                    var.put('i1$1', var.get('i1'))
                    var.put('i2$1', var.get('i2'))
                    var.put('len$1', var.get('len'))
                    if (var.get('i1$1')<var.get('i2$1')):
                        var.put('range_a', ((((var.get('s1$1').get('length')-var.get('i2$1'))|Js(0.0))-Js(1.0))|Js(0.0)))
                        var.put('range_b', ((var.get('len$1')-Js(1.0))|Js(0.0)))
                        var.put('range', (var.get('range_b') if (var.get('range_a')>var.get('range_b')) else var.get('range_a')))
                        #for JS loop
                        var.put('j', var.get('range'))
                        while (var.get('j')>=Js(0.0)):
                            try:
                                var.get('s1$1').put(((var.get('i2$1')+var.get('j'))|Js(0.0)), var.get('s1$1').get(((var.get('i1$1')+var.get('j'))|Js(0.0))))
                            finally:
                                    var.put('j',Js(var.get('j').to_number())-Js(1))
                        return Js(0.0)
                    else:
                        if (var.get('i1$1')>var.get('i2$1')):
                            var.put('range_a$1', ((((var.get('s1$1').get('length')-var.get('i1$1'))|Js(0.0))-Js(1.0))|Js(0.0)))
                            var.put('range_b$1', ((var.get('len$1')-Js(1.0))|Js(0.0)))
                            var.put('range$1', (var.get('range_b$1') if (var.get('range_a$1')>var.get('range_b$1')) else var.get('range_a$1')))
                            #for JS loop
                            var.put('k', Js(0.0))
                            while (var.get('k')<=var.get('range$1')):
                                try:
                                    var.get('s1$1').put(((var.get('i2$1')+var.get('k'))|Js(0.0)), var.get('s1$1').get(((var.get('i1$1')+var.get('k'))|Js(0.0))))
                                finally:
                                        var.put('k',Js(var.get('k').to_number())+Js(1))
                            return Js(0.0)
                        else:
                            return Js(0.0)
                else:
                    var.put('off1', ((var.get('s1').get('length')-var.get('i1'))|Js(0.0)))
                    if (var.get('len')<=var.get('off1')):
                        #for JS loop
                        var.put('i', Js(0.0))
                        var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
                        while (var.get('i')<=var.get('i_finish')):
                            try:
                                var.get('s2').put(((var.get('i2')+var.get('i'))|Js(0.0)), var.get('s1').get(((var.get('i1')+var.get('i'))|Js(0.0))))
                            finally:
                                    var.put('i',Js(var.get('i').to_number())+Js(1))
                        return Js(0.0)
                    else:
                        #for JS loop
                        var.put('i$1', Js(0.0))
                        var.put('i_finish$1', ((var.get('off1')-Js(1.0))|Js(0.0)))
                        while (var.get('i$1')<=var.get('i_finish$1')):
                            try:
                                var.get('s2').put(((var.get('i2')+var.get('i$1'))|Js(0.0)), var.get('s1').get(((var.get('i1')+var.get('i$1'))|Js(0.0))))
                            finally:
                                    var.put('i$1',Js(var.get('i$1').to_number())+Js(1))
                        #for JS loop
                        var.put('i$2', var.get('off1'))
                        var.put('i_finish$2', ((var.get('len')-Js(1.0))|Js(0.0)))
                        while (var.get('i$2')<=var.get('i_finish$2')):
                            try:
                                var.get('s2').put(((var.get('i2')+var.get('i$2'))|Js(0.0)), Js(0.0))
                            finally:
                                    var.put('i$2',Js(var.get('i$2').to_number())+Js(1))
                        return Js(0.0)
            else:
                return Js(0.0)
        PyJsHoisted_caml_blit_bytes_.func_name = 'caml_blit_bytes'
        var.put('caml_blit_bytes', PyJsHoisted_caml_blit_bytes_)
        @Js
        def PyJsHoisted_bytes_to_string_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 's_len', 'tmp_bytes', 'a', 'bytes', 'next', 'offset', 's', 'i'])
            var.put('bytes', var.get('a'))
            var.put('i', Js(0.0))
            var.put('len', var.get('a').get('length'))
            var.put('s', Js(''))
            var.put('s_len', var.get('len'))
            if ((PyJsStrictEq(var.get('i'),Js(0.0)) and (var.get('len')<=Js(4096.0))) and PyJsStrictEq(var.get('len'),var.get('bytes').get('length'))):
                return var.get('String').get('fromCharCode').callprop('apply', var.get(u"null"), var.get('bytes'))
            else:
                var.put('offset', Js(0.0))
                while (var.get('s_len')>Js(0.0)):
                    var.put('next', (var.get('s_len') if (var.get('s_len')<Js(1024.0)) else Js(1024.0)))
                    var.put('tmp_bytes', var.get('Array').create(var.get('next')))
                    var.get('caml_blit_bytes')(var.get('bytes'), var.get('offset'), var.get('tmp_bytes'), Js(0.0), var.get('next'))
                    var.put('s', (var.get('s')+var.get('String').get('fromCharCode').callprop('apply', var.get(u"null"), var.get('tmp_bytes'))))
                    var.put('s_len', ((var.get('s_len')-var.get('next'))|Js(0.0)))
                    var.put('offset', ((var.get('offset')+var.get('next'))|Js(0.0)))
                pass
                return var.get('s')
        PyJsHoisted_bytes_to_string_.func_name = 'bytes_to_string'
        var.put('bytes_to_string', PyJsHoisted_bytes_to_string_)
        @Js
        def PyJsHoisted_caml_blit_string_(s1, i1, s2, i2, len, this, arguments, var=var):
            var = Scope({'s1':s1, 'i1':i1, 's2':s2, 'i2':i2, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'i$1', 'i_finish$1', 'i_finish', 'i2', 'i1', 's2', 'off1', 'i$2', 's1', 'i_finish$2', 'i'])
            if (var.get('len')>Js(0.0)):
                var.put('off1', ((var.get('s1').get('length')-var.get('i1'))|Js(0.0)))
                if (var.get('len')<=var.get('off1')):
                    #for JS loop
                    var.put('i', Js(0.0))
                    var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
                    while (var.get('i')<=var.get('i_finish')):
                        try:
                            var.get('s2').put(((var.get('i2')+var.get('i'))|Js(0.0)), var.get('s1').callprop('charCodeAt', ((var.get('i1')+var.get('i'))|Js(0.0))))
                        finally:
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                    return Js(0.0)
                else:
                    #for JS loop
                    var.put('i$1', Js(0.0))
                    var.put('i_finish$1', ((var.get('off1')-Js(1.0))|Js(0.0)))
                    while (var.get('i$1')<=var.get('i_finish$1')):
                        try:
                            var.get('s2').put(((var.get('i2')+var.get('i$1'))|Js(0.0)), var.get('s1').callprop('charCodeAt', ((var.get('i1')+var.get('i$1'))|Js(0.0))))
                        finally:
                                var.put('i$1',Js(var.get('i$1').to_number())+Js(1))
                    #for JS loop
                    var.put('i$2', var.get('off1'))
                    var.put('i_finish$2', ((var.get('len')-Js(1.0))|Js(0.0)))
                    while (var.get('i$2')<=var.get('i_finish$2')):
                        try:
                            var.get('s2').put(((var.get('i2')+var.get('i$2'))|Js(0.0)), Js(0.0))
                        finally:
                                var.put('i$2',Js(var.get('i$2').to_number())+Js(1))
                    return Js(0.0)
            else:
                return Js(0.0)
        PyJsHoisted_caml_blit_string_.func_name = 'caml_blit_string'
        var.put('caml_blit_string', PyJsHoisted_caml_blit_string_)
        @Js
        def PyJsHoisted_bytes_of_string_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'res', 'i_finish', 's', 'i'])
            var.put('len', var.get('s').get('length'))
            var.put('res', var.get('Array').create(var.get('len')))
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('res').put(var.get('i'), var.get('s').callprop('charCodeAt', var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('res')
        PyJsHoisted_bytes_of_string_.func_name = 'bytes_of_string'
        var.put('bytes_of_string', PyJsHoisted_bytes_of_string_)
        Js('use strict')
        var.put('Caml_builtin_exceptions', var.get('require')(Js('./caml_builtin_exceptions.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('caml_create_bytes', var.get('caml_create_bytes'))
        var.get('exports').put('caml_fill_bytes', var.get('caml_fill_bytes'))
        var.get('exports').put('get', var.get('get'))
        var.get('exports').put('bytes_to_string', var.get('bytes_to_string'))
        var.get('exports').put('caml_blit_bytes', var.get('caml_blit_bytes'))
        var.get('exports').put('caml_blit_string', var.get('caml_blit_string'))
        var.get('exports').put('bytes_of_string', var.get('bytes_of_string'))
    PyJs_anonymous_19_._set_name('anonymous')
    @Js
    def PyJs_anonymous_20_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'caml_equal_nullable', 'caml_notequal', 'Caml_primitive', 'caml_lessequal', 'caml_max', 'caml_lazy_make_forward', 'caml_obj_set_tag', 'caml_obj_dup', 'caml_obj_block', 'caml_greaterequal', 'module', 'caml_obj_truncate', 'caml_update_dummy', 'Block', 'caml_compare', 'require', 'caml_equal_undefined', 'caml_equal', 'Caml_builtin_exceptions', 'caml_min', 'caml_equal_null', 'for_in', 'caml_lazy_make', 'caml_lessthan', 'caml_greaterthan'])
        @Js
        def PyJsHoisted_caml_obj_block_(tag, size, this, arguments, var=var):
            var = Scope({'tag':tag, 'size':size, 'this':this, 'arguments':arguments}, var)
            var.registers(['size', 'tag', 'v'])
            var.put('v', var.get('Array').create(var.get('size')))
            var.get('v').put('tag', var.get('tag'))
            return var.get('v')
        PyJsHoisted_caml_obj_block_.func_name = 'caml_obj_block'
        var.put('caml_obj_block', PyJsHoisted_caml_obj_block_)
        @Js
        def PyJsHoisted_caml_obj_dup_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'i_finish', 'v', 'x', 'i'])
            if var.get('Array').callprop('isArray', var.get('x')):
                var.put('len', (var.get('x').get('length')|Js(0.0)))
                var.put('v', var.get('Array').create(var.get('len')))
                #for JS loop
                var.put('i', Js(0.0))
                var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.get('v').put(var.get('i'), var.get('x').get(var.get('i')))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                var.get('v').put('tag', (var.get('x').get('tag')|Js(0.0)))
                return var.get('v')
            else:
                return var.get('Object').callprop('assign', Js({}), var.get('x'))
        PyJsHoisted_caml_obj_dup_.func_name = 'caml_obj_dup'
        var.put('caml_obj_dup', PyJsHoisted_caml_obj_dup_)
        @Js
        def PyJsHoisted_caml_obj_truncate_(x, new_size, this, arguments, var=var):
            var = Scope({'x':x, 'new_size':new_size, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'new_size', 'i_finish', 'x', 'i'])
            var.put('len', (var.get('x').get('length')|Js(0.0)))
            if ((var.get('new_size')<=Js(0.0)) or (var.get('new_size')>var.get('len'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('Obj.truncate')]))
                raise PyJsTempException
            if PyJsStrictNeq(var.get('len'),var.get('new_size')):
                #for JS loop
                var.put('i', var.get('new_size'))
                var.put('i_finish', ((var.get('len')-Js(1.0))|Js(0.0)))
                while (var.get('i')<=var.get('i_finish')):
                    try:
                        var.get('x').put(var.get('i'), Js(0.0))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                var.get('x').put('length', var.get('new_size'))
                return Js(0.0)
            else:
                return Js(0.0)
        PyJsHoisted_caml_obj_truncate_.func_name = 'caml_obj_truncate'
        var.put('caml_obj_truncate', PyJsHoisted_caml_obj_truncate_)
        @Js
        def PyJsHoisted_caml_lazy_make_forward_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return var.get('Block').callprop('__', Js(250.0), Js([var.get('x')]))
        PyJsHoisted_caml_lazy_make_forward_.func_name = 'caml_lazy_make_forward'
        var.put('caml_lazy_make_forward', PyJsHoisted_caml_lazy_make_forward_)
        @Js
        def PyJsHoisted_caml_lazy_make_(fn, this, arguments, var=var):
            var = Scope({'fn':fn, 'this':this, 'arguments':arguments}, var)
            var.registers(['fn', 'block'])
            var.put('block', Js([var.get('fn')]))
            var.get('block').put('tag', Js(246.0))
            return var.get('block')
        PyJsHoisted_caml_lazy_make_.func_name = 'caml_lazy_make'
        var.put('caml_lazy_make', PyJsHoisted_caml_lazy_make_)
        @Js
        def PyJsHoisted_caml_compare_(_a, _b, this, arguments, var=var):
            var = Scope({'_a':_a, '_b':_b, 'this':this, 'arguments':arguments}, var)
            var.registers(['tag_b', 'b$1', 'len_a', 'do_key', 'b$4', '_b', 'len_b', 'match', 'i$2', 'same_length', 'i', 'a$4', 'a$3', 'b$3', 'res', 'a_type', 'short_length$1', 'min_key_lhs', 'i$1', 'match$1', 'b_type', 'b$2', 'do_key_a', '_i', '_i$1', 'b', 'res$2', 'a', 'a$2', 'partial_arg$1', 'short_length', '_i$2', 'min_key_rhs', 'do_key_b', '_a', 'a$1', 'tag_a', 'res$1', 'partial_arg'])
            while Js(True):
                var.put('b', var.get('_b'))
                var.put('a', var.get('_a'))
                if PyJsStrictEq(var.get('a'),var.get('b')):
                    return Js(0.0)
                else:
                    var.put('a_type', var.get('a',throw=False).typeof())
                    var.put('b_type', var.get('b',throw=False).typeof())
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get('a_type'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('boolean')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('b_type'),Js('boolean')):
                                return var.get('Caml_primitive').callprop('caml_bool_compare', var.get('a'), var.get('b'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('function')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('b_type'),Js('function')):
                                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('compare: functional value')]))
                                raise PyJsTempException
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('number')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('b_type'),Js('number')):
                                return var.get('Caml_primitive').callprop('caml_int_compare', var.get('a'), var.get('b'))
                            break
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('string')):
                            SWITCHED = True
                            if PyJsStrictEq(var.get('b_type'),Js('string')):
                                return var.get('Caml_primitive').callprop('caml_string_compare', var.get('a'), var.get('b'))
                            else:
                                return Js(1.0)
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('undefined')):
                            SWITCHED = True
                            return (-Js(1.0))
                        if True:
                            SWITCHED = True
                            pass
                        SWITCHED = True
                        break
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get('b_type'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('string')):
                            SWITCHED = True
                            return (-Js(1.0))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js('undefined')):
                            SWITCHED = True
                            return Js(1.0)
                        if True:
                            SWITCHED = True
                            if PyJsStrictEq(var.get('a_type'),Js('boolean')):
                                return Js(1.0)
                            else:
                                if PyJsStrictEq(var.get('b_type'),Js('boolean')):
                                    return (-Js(1.0))
                                else:
                                    if PyJsStrictEq(var.get('a_type'),Js('function')):
                                        return Js(1.0)
                                    else:
                                        if PyJsStrictEq(var.get('b_type'),Js('function')):
                                            return (-Js(1.0))
                                        else:
                                            if PyJsStrictEq(var.get('a_type'),Js('number')):
                                                if (PyJsStrictEq(var.get('b'),var.get(u"null")) or PyJsStrictEq(var.get('b').get('tag'),Js(256.0))):
                                                    return Js(1.0)
                                                else:
                                                    return (-Js(1.0))
                                            else:
                                                if PyJsStrictEq(var.get('b_type'),Js('number')):
                                                    if (PyJsStrictEq(var.get('a'),var.get(u"null")) or PyJsStrictEq(var.get('a').get('tag'),Js(256.0))):
                                                        return (-Js(1.0))
                                                    else:
                                                        return Js(1.0)
                                                else:
                                                    if PyJsStrictEq(var.get('a'),var.get(u"null")):
                                                        if PyJsStrictEq(var.get('b').get('tag'),Js(256.0)):
                                                            return Js(1.0)
                                                        else:
                                                            return (-Js(1.0))
                                                    else:
                                                        if PyJsStrictEq(var.get('b'),var.get(u"null")):
                                                            if PyJsStrictEq(var.get('a').get('tag'),Js(256.0)):
                                                                return (-Js(1.0))
                                                            else:
                                                                return Js(1.0)
                                                        else:
                                                            var.put('tag_a', (var.get('a').get('tag')|Js(0.0)))
                                                            var.put('tag_b', (var.get('b').get('tag')|Js(0.0)))
                                                            if PyJsStrictEq(var.get('tag_a'),Js(250.0)):
                                                                var.put('_a', var.get('a').get('0'))
                                                                continue
                                                            else:
                                                                if PyJsStrictEq(var.get('tag_b'),Js(250.0)):
                                                                    var.put('_b', var.get('b').get('0'))
                                                                    continue
                                                                else:
                                                                    if PyJsStrictEq(var.get('tag_a'),Js(256.0)):
                                                                        if PyJsStrictEq(var.get('tag_b'),Js(256.0)):
                                                                            return var.get('Caml_primitive').callprop('caml_int_compare', var.get('a').get('1'), var.get('b').get('1'))
                                                                        else:
                                                                            return (-Js(1.0))
                                                                    else:
                                                                        if PyJsStrictEq(var.get('tag_a'),Js(248.0)):
                                                                            return var.get('Caml_primitive').callprop('caml_int_compare', var.get('a').get('1'), var.get('b').get('1'))
                                                                        else:
                                                                            if PyJsStrictEq(var.get('tag_a'),Js(251.0)):
                                                                                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('equal: abstract value')]))
                                                                                raise PyJsTempException
                                                                            if PyJsStrictNeq(var.get('tag_a'),var.get('tag_b')):
                                                                                if (var.get('tag_a')<var.get('tag_b')):
                                                                                    return (-Js(1.0))
                                                                                else:
                                                                                    return Js(1.0)
                                                                            else:
                                                                                var.put('len_a', (var.get('a').get('length')|Js(0.0)))
                                                                                var.put('len_b', (var.get('b').get('length')|Js(0.0)))
                                                                                if PyJsStrictEq(var.get('len_a'),var.get('len_b')):
                                                                                    if var.get('Array').callprop('isArray', var.get('a')):
                                                                                        var.put('a$1', var.get('a'))
                                                                                        var.put('b$1', var.get('b'))
                                                                                        var.put('_i', Js(0.0))
                                                                                        var.put('same_length', var.get('len_a'))
                                                                                        while Js(True):
                                                                                            var.put('i', var.get('_i'))
                                                                                            if PyJsStrictEq(var.get('i'),var.get('same_length')):
                                                                                                return Js(0.0)
                                                                                            else:
                                                                                                var.put('res', var.get('caml_compare')(var.get('a$1').get(var.get('i')), var.get('b$1').get(var.get('i'))))
                                                                                                if PyJsStrictNeq(var.get('res'),Js(0.0)):
                                                                                                    return var.get('res')
                                                                                                else:
                                                                                                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                                                                                                    continue
                                                                                        pass
                                                                                    else:
                                                                                        if (var.get('a').instanceof(var.get('Date')) and var.get('b').instanceof(var.get('Date'))):
                                                                                            return (var.get('a')-var.get('b'))
                                                                                        else:
                                                                                            var.put('a$2', var.get('a'))
                                                                                            var.put('b$2', var.get('b'))
                                                                                            var.put('min_key_lhs', Js({'contents':var.get('undefined')}))
                                                                                            var.put('min_key_rhs', Js({'contents':var.get('undefined')}))
                                                                                            @Js
                                                                                            def PyJs_anonymous_23_(param, key, this, arguments, var=var):
                                                                                                var = Scope({'param':param, 'key':key, 'this':this, 'arguments':arguments}, var)
                                                                                                var.registers(['min_key', 'match', 'key', 'b', 'param'])
                                                                                                var.put('min_key', var.get('param').get('2'))
                                                                                                var.put('b', var.get('param').get('1'))
                                                                                                if (var.get('b').callprop('hasOwnProperty', var.get('key')).neg() or (var.get('caml_compare')(var.get('param').get('0').get(var.get('key')), var.get('b').get(var.get('key')))>Js(0.0))):
                                                                                                    var.put('match', var.get('min_key').get('contents'))
                                                                                                    if (PyJsStrictNeq(var.get('match'),var.get('undefined')) and (var.get('key')>=var.get('match'))):
                                                                                                        return Js(0.0)
                                                                                                    else:
                                                                                                        var.get('min_key').put('contents', var.get('key'))
                                                                                                        return Js(0.0)
                                                                                                else:
                                                                                                    return Js(0.0)
                                                                                            PyJs_anonymous_23_._set_name('anonymous')
                                                                                            var.put('do_key', PyJs_anonymous_23_)
                                                                                            var.put('partial_arg', Js([var.get('a$2'), var.get('b$2'), var.get('min_key_rhs')]))
                                                                                            @Js
                                                                                            def PyJs_anonymous_24_(partial_arg, this, arguments, var=var):
                                                                                                var = Scope({'partial_arg':partial_arg, 'this':this, 'arguments':arguments}, var)
                                                                                                var.registers(['partial_arg'])
                                                                                                @Js
                                                                                                def PyJs_do_key_a_25_(param, this, arguments, var=var):
                                                                                                    var = Scope({'param':param, 'this':this, 'arguments':arguments, 'do_key_a':PyJs_do_key_a_25_}, var)
                                                                                                    var.registers(['param'])
                                                                                                    return var.get('do_key')(var.get('partial_arg'), var.get('param'))
                                                                                                PyJs_do_key_a_25_._set_name('do_key_a')
                                                                                                return PyJs_do_key_a_25_
                                                                                            PyJs_anonymous_24_._set_name('anonymous')
                                                                                            var.put('do_key_a', PyJs_anonymous_24_(var.get('partial_arg')))
                                                                                            var.put('partial_arg$1', Js([var.get('b$2'), var.get('a$2'), var.get('min_key_lhs')]))
                                                                                            @Js
                                                                                            def PyJs_anonymous_26_(PyJsArg_7061727469616c5f6172672431_, this, arguments, var=var):
                                                                                                var = Scope({'partial_arg$1':PyJsArg_7061727469616c5f6172672431_, 'this':this, 'arguments':arguments}, var)
                                                                                                var.registers(['partial_arg$1'])
                                                                                                @Js
                                                                                                def PyJs_do_key_b_27_(param, this, arguments, var=var):
                                                                                                    var = Scope({'param':param, 'this':this, 'arguments':arguments, 'do_key_b':PyJs_do_key_b_27_}, var)
                                                                                                    var.registers(['param'])
                                                                                                    return var.get('do_key')(var.get('partial_arg$1'), var.get('param'))
                                                                                                PyJs_do_key_b_27_._set_name('do_key_b')
                                                                                                return PyJs_do_key_b_27_
                                                                                            PyJs_anonymous_26_._set_name('anonymous')
                                                                                            var.put('do_key_b', PyJs_anonymous_26_(var.get('partial_arg$1')))
                                                                                            var.get('for_in')(var.get('a$2'), var.get('do_key_a'))
                                                                                            var.get('for_in')(var.get('b$2'), var.get('do_key_b'))
                                                                                            var.put('match', var.get('min_key_lhs').get('contents'))
                                                                                            var.put('match$1', var.get('min_key_rhs').get('contents'))
                                                                                            if PyJsStrictNeq(var.get('match'),var.get('undefined')):
                                                                                                if PyJsStrictNeq(var.get('match$1'),var.get('undefined')):
                                                                                                    return var.get('Caml_primitive').callprop('caml_string_compare', var.get('match'), var.get('match$1'))
                                                                                                else:
                                                                                                    return (-Js(1.0))
                                                                                            else:
                                                                                                if PyJsStrictNeq(var.get('match$1'),var.get('undefined')):
                                                                                                    return Js(1.0)
                                                                                                else:
                                                                                                    return Js(0.0)
                                                                                else:
                                                                                    if (var.get('len_a')<var.get('len_b')):
                                                                                        var.put('a$3', var.get('a'))
                                                                                        var.put('b$3', var.get('b'))
                                                                                        var.put('_i$1', Js(0.0))
                                                                                        var.put('short_length', var.get('len_a'))
                                                                                        while Js(True):
                                                                                            var.put('i$1', var.get('_i$1'))
                                                                                            if PyJsStrictEq(var.get('i$1'),var.get('short_length')):
                                                                                                return (-Js(1.0))
                                                                                            else:
                                                                                                var.put('res$1', var.get('caml_compare')(var.get('a$3').get(var.get('i$1')), var.get('b$3').get(var.get('i$1'))))
                                                                                                if PyJsStrictNeq(var.get('res$1'),Js(0.0)):
                                                                                                    return var.get('res$1')
                                                                                                else:
                                                                                                    var.put('_i$1', ((var.get('i$1')+Js(1.0))|Js(0.0)))
                                                                                                    continue
                                                                                        pass
                                                                                    else:
                                                                                        var.put('a$4', var.get('a'))
                                                                                        var.put('b$4', var.get('b'))
                                                                                        var.put('_i$2', Js(0.0))
                                                                                        var.put('short_length$1', var.get('len_b'))
                                                                                        while Js(True):
                                                                                            var.put('i$2', var.get('_i$2'))
                                                                                            if PyJsStrictEq(var.get('i$2'),var.get('short_length$1')):
                                                                                                return Js(1.0)
                                                                                            else:
                                                                                                var.put('res$2', var.get('caml_compare')(var.get('a$4').get(var.get('i$2')), var.get('b$4').get(var.get('i$2'))))
                                                                                                if PyJsStrictNeq(var.get('res$2'),Js(0.0)):
                                                                                                    return var.get('res$2')
                                                                                                else:
                                                                                                    var.put('_i$2', ((var.get('i$2')+Js(1.0))|Js(0.0)))
                                                                                                    continue
                                                                                        pass
                        SWITCHED = True
                        break
            pass
        PyJsHoisted_caml_compare_.func_name = 'caml_compare'
        var.put('caml_compare', PyJsHoisted_caml_compare_)
        @Js
        def PyJsHoisted_caml_equal_(_a, _b, this, arguments, var=var):
            var = Scope({'_a':_a, '_b':_b, 'this':this, 'arguments':arguments}, var)
            var.registers(['tag_b', 'b$1', 'len_a', '_b', 'len_b', 'same_length', 'i', 'a_type', 'b_type', 'b$2', 'result', 'do_key_a', '_i', 'b', 'a', 'a$2', 'do_key_b', '_a', 'a$1', 'tag_a'])
            while Js(True):
                var.put('b', var.get('_b'))
                var.put('a', var.get('_a'))
                if PyJsStrictEq(var.get('a'),var.get('b')):
                    return Js(True)
                else:
                    var.put('a_type', var.get('a',throw=False).typeof())
                    if ((((PyJsStrictEq(var.get('a_type'),Js('string')) or PyJsStrictEq(var.get('a_type'),Js('number'))) or PyJsStrictEq(var.get('a_type'),Js('boolean'))) or PyJsStrictEq(var.get('a_type'),Js('undefined'))) or PyJsStrictEq(var.get('a'),var.get(u"null"))):
                        return Js(False)
                    else:
                        var.put('b_type', var.get('b',throw=False).typeof())
                        if (PyJsStrictEq(var.get('a_type'),Js('function')) or PyJsStrictEq(var.get('b_type'),Js('function'))):
                            PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('equal: functional value')]))
                            raise PyJsTempException
                        if ((PyJsStrictEq(var.get('b_type'),Js('number')) or PyJsStrictEq(var.get('b_type'),Js('undefined'))) or PyJsStrictEq(var.get('b'),var.get(u"null"))):
                            return Js(False)
                        else:
                            var.put('tag_a', (var.get('a').get('tag')|Js(0.0)))
                            var.put('tag_b', (var.get('b').get('tag')|Js(0.0)))
                            if PyJsStrictEq(var.get('tag_a'),Js(250.0)):
                                var.put('_a', var.get('a').get('0'))
                                continue
                            else:
                                if PyJsStrictEq(var.get('tag_b'),Js(250.0)):
                                    var.put('_b', var.get('b').get('0'))
                                    continue
                                else:
                                    if PyJsStrictEq(var.get('tag_a'),Js(248.0)):
                                        return PyJsStrictEq(var.get('a').get('1'),var.get('b').get('1'))
                                    else:
                                        if PyJsStrictEq(var.get('tag_a'),Js(251.0)):
                                            PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('equal: abstract value')]))
                                            raise PyJsTempException
                                        if PyJsStrictNeq(var.get('tag_a'),var.get('tag_b')):
                                            return Js(False)
                                        else:
                                            if PyJsStrictEq(var.get('tag_a'),Js(256.0)):
                                                return PyJsStrictEq(var.get('a').get('1'),var.get('b').get('1'))
                                            else:
                                                var.put('len_a', (var.get('a').get('length')|Js(0.0)))
                                                var.put('len_b', (var.get('b').get('length')|Js(0.0)))
                                                if PyJsStrictEq(var.get('len_a'),var.get('len_b')):
                                                    if var.get('Array').callprop('isArray', var.get('a')):
                                                        var.put('a$1', var.get('a'))
                                                        var.put('b$1', var.get('b'))
                                                        var.put('_i', Js(0.0))
                                                        var.put('same_length', var.get('len_a'))
                                                        while Js(True):
                                                            var.put('i', var.get('_i'))
                                                            if PyJsStrictEq(var.get('i'),var.get('same_length')):
                                                                return Js(True)
                                                            else:
                                                                if var.get('caml_equal')(var.get('a$1').get(var.get('i')), var.get('b$1').get(var.get('i'))):
                                                                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                                                                    continue
                                                                else:
                                                                    return Js(False)
                                                        pass
                                                    else:
                                                        if (var.get('a').instanceof(var.get('Date')) and var.get('b').instanceof(var.get('Date'))):
                                                            return ((var.get('a')>var.get('b')) or (var.get('a')<var.get('b'))).neg()
                                                        else:
                                                            var.put('a$2', var.get('a'))
                                                            var.put('b$2', var.get('b'))
                                                            var.put('result', Js({'contents':Js(True)}))
                                                            @Js
                                                            def PyJs_anonymous_28_(PyJsArg_622432_, result, this, arguments, var=var):
                                                                var = Scope({'b$2':PyJsArg_622432_, 'result':result, 'this':this, 'arguments':arguments}, var)
                                                                var.registers(['result', 'b$2'])
                                                                @Js
                                                                def PyJs_do_key_a_29_(key, this, arguments, var=var):
                                                                    var = Scope({'key':key, 'this':this, 'arguments':arguments, 'do_key_a':PyJs_do_key_a_29_}, var)
                                                                    var.registers(['key'])
                                                                    if var.get('b$2').callprop('hasOwnProperty', var.get('key')):
                                                                        return Js(0.0)
                                                                    else:
                                                                        var.get('result').put('contents', Js(False))
                                                                        return Js(0.0)
                                                                PyJs_do_key_a_29_._set_name('do_key_a')
                                                                return PyJs_do_key_a_29_
                                                            PyJs_anonymous_28_._set_name('anonymous')
                                                            var.put('do_key_a', PyJs_anonymous_28_(var.get('b$2'), var.get('result')))
                                                            @Js
                                                            def PyJs_anonymous_30_(PyJsArg_612432_, PyJsArg_622432_, result, this, arguments, var=var):
                                                                var = Scope({'a$2':PyJsArg_612432_, 'b$2':PyJsArg_622432_, 'result':result, 'this':this, 'arguments':arguments}, var)
                                                                var.registers(['a$2', 'b$2', 'result'])
                                                                @Js
                                                                def PyJs_do_key_b_31_(key, this, arguments, var=var):
                                                                    var = Scope({'key':key, 'this':this, 'arguments':arguments, 'do_key_b':PyJs_do_key_b_31_}, var)
                                                                    var.registers(['key'])
                                                                    if (var.get('a$2').callprop('hasOwnProperty', var.get('key')).neg() or var.get('caml_equal')(var.get('b$2').get(var.get('key')), var.get('a$2').get(var.get('key'))).neg()):
                                                                        var.get('result').put('contents', Js(False))
                                                                        return Js(0.0)
                                                                    else:
                                                                        return Js(0.0)
                                                                PyJs_do_key_b_31_._set_name('do_key_b')
                                                                return PyJs_do_key_b_31_
                                                            PyJs_anonymous_30_._set_name('anonymous')
                                                            var.put('do_key_b', PyJs_anonymous_30_(var.get('a$2'), var.get('b$2'), var.get('result')))
                                                            var.get('for_in')(var.get('a$2'), var.get('do_key_a'))
                                                            if var.get('result').get('contents'):
                                                                var.get('for_in')(var.get('b$2'), var.get('do_key_b'))
                                                            return var.get('result').get('contents')
                                                else:
                                                    return Js(False)
            pass
        PyJsHoisted_caml_equal_.func_name = 'caml_equal'
        var.put('caml_equal', PyJsHoisted_caml_equal_)
        @Js
        def PyJsHoisted_caml_equal_null_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if PyJsStrictNeq(var.get('y'),var.get(u"null")):
                return var.get('caml_equal')(var.get('x'), var.get('y'))
            else:
                return PyJsStrictEq(var.get('x'),var.get('y'))
        PyJsHoisted_caml_equal_null_.func_name = 'caml_equal_null'
        var.put('caml_equal_null', PyJsHoisted_caml_equal_null_)
        @Js
        def PyJsHoisted_caml_equal_undefined_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if PyJsStrictNeq(var.get('y'),var.get('undefined')):
                return var.get('caml_equal')(var.get('x'), var.get('y'))
            else:
                return PyJsStrictEq(var.get('x'),var.get('y'))
        PyJsHoisted_caml_equal_undefined_.func_name = 'caml_equal_undefined'
        var.put('caml_equal_undefined', PyJsHoisted_caml_equal_undefined_)
        @Js
        def PyJsHoisted_caml_equal_nullable_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('y')==var.get(u"null")):
                return PyJsStrictEq(var.get('x'),var.get('y'))
            else:
                return var.get('caml_equal')(var.get('x'), var.get('y'))
        PyJsHoisted_caml_equal_nullable_.func_name = 'caml_equal_nullable'
        var.put('caml_equal_nullable', PyJsHoisted_caml_equal_nullable_)
        @Js
        def PyJsHoisted_caml_notequal_(a, b, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b'])
            return var.get('caml_equal')(var.get('a'), var.get('b')).neg()
        PyJsHoisted_caml_notequal_.func_name = 'caml_notequal'
        var.put('caml_notequal', PyJsHoisted_caml_notequal_)
        @Js
        def PyJsHoisted_caml_greaterequal_(a, b, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b'])
            return (var.get('caml_compare')(var.get('a'), var.get('b'))>=Js(0.0))
        PyJsHoisted_caml_greaterequal_.func_name = 'caml_greaterequal'
        var.put('caml_greaterequal', PyJsHoisted_caml_greaterequal_)
        @Js
        def PyJsHoisted_caml_greaterthan_(a, b, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b'])
            return (var.get('caml_compare')(var.get('a'), var.get('b'))>Js(0.0))
        PyJsHoisted_caml_greaterthan_.func_name = 'caml_greaterthan'
        var.put('caml_greaterthan', PyJsHoisted_caml_greaterthan_)
        @Js
        def PyJsHoisted_caml_lessequal_(a, b, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b'])
            return (var.get('caml_compare')(var.get('a'), var.get('b'))<=Js(0.0))
        PyJsHoisted_caml_lessequal_.func_name = 'caml_lessequal'
        var.put('caml_lessequal', PyJsHoisted_caml_lessequal_)
        @Js
        def PyJsHoisted_caml_lessthan_(a, b, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'b'])
            return (var.get('caml_compare')(var.get('a'), var.get('b'))<Js(0.0))
        PyJsHoisted_caml_lessthan_.func_name = 'caml_lessthan'
        var.put('caml_lessthan', PyJsHoisted_caml_lessthan_)
        @Js
        def PyJsHoisted_caml_min_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('caml_compare')(var.get('x'), var.get('y'))<=Js(0.0)):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_min_.func_name = 'caml_min'
        var.put('caml_min', PyJsHoisted_caml_min_)
        @Js
        def PyJsHoisted_caml_max_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('caml_compare')(var.get('x'), var.get('y'))>=Js(0.0)):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_max_.func_name = 'caml_max'
        var.put('caml_max', PyJsHoisted_caml_max_)
        @Js
        def PyJsHoisted_caml_obj_set_tag_(prim, PyJsArg_7072696d2431_, this, arguments, var=var):
            var = Scope({'prim':prim, 'prim$1':PyJsArg_7072696d2431_, 'this':this, 'arguments':arguments}, var)
            var.registers(['prim', 'prim$1'])
            var.get('prim').put('tag', var.get('prim$1'))
            return Js(0.0)
        PyJsHoisted_caml_obj_set_tag_.func_name = 'caml_obj_set_tag'
        var.put('caml_obj_set_tag', PyJsHoisted_caml_obj_set_tag_)
        Js('use strict')
        var.put('Block', var.get('require')(Js('./block.js')))
        var.put('Caml_primitive', var.get('require')(Js('./caml_primitive.js')))
        var.put('Caml_builtin_exceptions', var.get('require')(Js('./caml_builtin_exceptions.js')))
        @Js
        def PyJs_anonymous_21_(o, foo, this, arguments, var=var):
            var = Scope({'o':o, 'foo':foo, 'this':this, 'arguments':arguments}, var)
            var.registers(['foo', 'x', 'o'])
            for PyJsTemp in var.get('o'):
                var.put('x', PyJsTemp)
                var.get('foo')(var.get('x'))
        PyJs_anonymous_21_._set_name('anonymous')
        var.put('for_in', PyJs_anonymous_21_)
        pass
        pass
        pass
        pass
        pass
        @Js
        def PyJs_anonymous_22_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x', 'k'])
            for PyJsTemp in var.get('y'):
                var.put('k', PyJsTemp)
                var.get('x').put(var.get('k'), var.get('y').get(var.get('k')))
            return Js(0.0)
        PyJs_anonymous_22_._set_name('anonymous')
        var.put('caml_update_dummy', PyJs_anonymous_22_)
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('caml_obj_block', var.get('caml_obj_block'))
        var.get('exports').put('caml_obj_dup', var.get('caml_obj_dup'))
        var.get('exports').put('caml_obj_truncate', var.get('caml_obj_truncate'))
        var.get('exports').put('caml_lazy_make_forward', var.get('caml_lazy_make_forward'))
        var.get('exports').put('caml_lazy_make', var.get('caml_lazy_make'))
        var.get('exports').put('caml_update_dummy', var.get('caml_update_dummy'))
        var.get('exports').put('caml_compare', var.get('caml_compare'))
        var.get('exports').put('caml_equal', var.get('caml_equal'))
        var.get('exports').put('caml_equal_null', var.get('caml_equal_null'))
        var.get('exports').put('caml_equal_undefined', var.get('caml_equal_undefined'))
        var.get('exports').put('caml_equal_nullable', var.get('caml_equal_nullable'))
        var.get('exports').put('caml_notequal', var.get('caml_notequal'))
        var.get('exports').put('caml_greaterequal', var.get('caml_greaterequal'))
        var.get('exports').put('caml_greaterthan', var.get('caml_greaterthan'))
        var.get('exports').put('caml_lessthan', var.get('caml_lessthan'))
        var.get('exports').put('caml_lessequal', var.get('caml_lessequal'))
        var.get('exports').put('caml_min', var.get('caml_min'))
        var.get('exports').put('caml_max', var.get('caml_max'))
        var.get('exports').put('caml_obj_set_tag', var.get('caml_obj_set_tag'))
    PyJs_anonymous_20_._set_name('anonymous')
    @Js
    def PyJs_anonymous_32_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['undefined_to_opt', 'valFromOption', 'exports', 'require', 'undefinedHeader', 'module', 'nullable_to_opt', 'some', 'null_to_opt', 'option_get', 'option_get_unwrap'])
        @Js
        def PyJsHoisted_some_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['block$1', 'nid', 'x', 'block'])
            if PyJsStrictEq(var.get('x'),var.get('undefined')):
                var.put('block', Js([var.get('undefinedHeader'), Js(0.0)]))
                var.get('block').put('tag', Js(256.0))
                return var.get('block')
            else:
                if (PyJsStrictNeq(var.get('x'),var.get(u"null")) and PyJsStrictEq(var.get('x').get('0'),var.get('undefinedHeader'))):
                    var.put('nid', ((var.get('x').get('1')+Js(1.0))|Js(0.0)))
                    var.put('block$1', Js([var.get('undefinedHeader'), var.get('nid')]))
                    var.get('block$1').put('tag', Js(256.0))
                    return var.get('block$1')
                else:
                    return var.get('x')
        PyJsHoisted_some_.func_name = 'some'
        var.put('some', PyJsHoisted_some_)
        @Js
        def PyJsHoisted_nullable_to_opt_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if (PyJsStrictEq(var.get('x'),var.get(u"null")) or PyJsStrictEq(var.get('x'),var.get('undefined'))):
                return var.get('undefined')
            else:
                return var.get('some')(var.get('x'))
        PyJsHoisted_nullable_to_opt_.func_name = 'nullable_to_opt'
        var.put('nullable_to_opt', PyJsHoisted_nullable_to_opt_)
        @Js
        def PyJsHoisted_undefined_to_opt_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if PyJsStrictEq(var.get('x'),var.get('undefined')):
                return var.get('undefined')
            else:
                return var.get('some')(var.get('x'))
        PyJsHoisted_undefined_to_opt_.func_name = 'undefined_to_opt'
        var.put('undefined_to_opt', PyJsHoisted_undefined_to_opt_)
        @Js
        def PyJsHoisted_null_to_opt_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if PyJsStrictEq(var.get('x'),var.get(u"null")):
                return var.get('undefined')
            else:
                return var.get('some')(var.get('x'))
        PyJsHoisted_null_to_opt_.func_name = 'null_to_opt'
        var.put('null_to_opt', PyJsHoisted_null_to_opt_)
        @Js
        def PyJsHoisted_valFromOption_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['depth', 'x'])
            if (PyJsStrictNeq(var.get('x'),var.get(u"null")) and PyJsStrictEq(var.get('x').get('0'),var.get('undefinedHeader'))):
                var.put('depth', var.get('x').get('1'))
                if PyJsStrictEq(var.get('depth'),Js(0.0)):
                    return var.get('undefined')
                else:
                    return Js([var.get('undefinedHeader'), ((var.get('depth')-Js(1.0))|Js(0.0))])
            else:
                return var.get('x')
        PyJsHoisted_valFromOption_.func_name = 'valFromOption'
        var.put('valFromOption', PyJsHoisted_valFromOption_)
        @Js
        def PyJsHoisted_option_get_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if PyJsStrictEq(var.get('x'),var.get('undefined')):
                return var.get('undefined')
            else:
                return var.get('valFromOption')(var.get('x'))
        PyJsHoisted_option_get_.func_name = 'option_get'
        var.put('option_get', PyJsHoisted_option_get_)
        @Js
        def PyJsHoisted_option_get_unwrap_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if PyJsStrictEq(var.get('x'),var.get('undefined')):
                return var.get('undefined')
            else:
                return var.get('valFromOption')(var.get('x')).get('1')
        PyJsHoisted_option_get_unwrap_.func_name = 'option_get_unwrap'
        var.put('option_get_unwrap', PyJsHoisted_option_get_unwrap_)
        Js('use strict')
        var.put('undefinedHeader', Js([]))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('nullable_to_opt', var.get('nullable_to_opt'))
        var.get('exports').put('undefined_to_opt', var.get('undefined_to_opt'))
        var.get('exports').put('null_to_opt', var.get('null_to_opt'))
        var.get('exports').put('valFromOption', var.get('valFromOption'))
        var.get('exports').put('some', var.get('some'))
        var.get('exports').put('option_get', var.get('option_get'))
        var.get('exports').put('option_get_unwrap', var.get('option_get_unwrap'))
    PyJs_anonymous_32_._set_name('anonymous')
    @Js
    def PyJs_anonymous_33_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['caml_nativeint_compare', 'exports', 'caml_int_min', 'caml_string_min', 'caml_string_max', 'caml_float_min', 'caml_bool_max', 'caml_bool_min', 'caml_int32_compare', 'caml_bytes_compare_aux', 'module', 'caml_int_compare', 'caml_bytes_equal', 'caml_nativeint_min', 'caml_int32_min', 'caml_nativeint_max', 'caml_float_max', 'require', 'caml_float_compare', 'caml_string_compare', 'caml_bool_compare', 'caml_bytes_compare', 'caml_int_max', 'caml_int32_max'])
        @Js
        def PyJsHoisted_caml_int_compare_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')<var.get('y')):
                return (-Js(1.0))
            else:
                if PyJsStrictEq(var.get('x'),var.get('y')):
                    return Js(0.0)
                else:
                    return Js(1.0)
        PyJsHoisted_caml_int_compare_.func_name = 'caml_int_compare'
        var.put('caml_int_compare', PyJsHoisted_caml_int_compare_)
        @Js
        def PyJsHoisted_caml_bool_compare_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if var.get('x'):
                if var.get('y'):
                    return Js(0.0)
                else:
                    return Js(1.0)
            else:
                if var.get('y'):
                    return (-Js(1.0))
                else:
                    return Js(0.0)
        PyJsHoisted_caml_bool_compare_.func_name = 'caml_bool_compare'
        var.put('caml_bool_compare', PyJsHoisted_caml_bool_compare_)
        @Js
        def PyJsHoisted_caml_float_compare_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if PyJsStrictEq(var.get('x'),var.get('y')):
                return Js(0.0)
            else:
                if (var.get('x')<var.get('y')):
                    return (-Js(1.0))
                else:
                    if ((var.get('x')>var.get('y')) or PyJsStrictEq(var.get('x'),var.get('x'))):
                        return Js(1.0)
                    else:
                        if PyJsStrictEq(var.get('y'),var.get('y')):
                            return (-Js(1.0))
                        else:
                            return Js(0.0)
        PyJsHoisted_caml_float_compare_.func_name = 'caml_float_compare'
        var.put('caml_float_compare', PyJsHoisted_caml_float_compare_)
        @Js
        def PyJsHoisted_caml_string_compare_(s1, s2, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'this':this, 'arguments':arguments}, var)
            var.registers(['s1', 's2'])
            if PyJsStrictEq(var.get('s1'),var.get('s2')):
                return Js(0.0)
            else:
                if (var.get('s1')<var.get('s2')):
                    return (-Js(1.0))
                else:
                    return Js(1.0)
        PyJsHoisted_caml_string_compare_.func_name = 'caml_string_compare'
        var.put('caml_string_compare', PyJsHoisted_caml_string_compare_)
        @Js
        def PyJsHoisted_caml_bytes_compare_aux_(s1, s2, _off, len, PyJsArg_646566_, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, '_off':_off, 'len':len, 'def':PyJsArg_646566_, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'def', 'off', 'a', 's2', '_off', 's1', 'b'])
            while Js(True):
                var.put('off', var.get('_off'))
                if (var.get('off')<var.get('len')):
                    var.put('a', var.get('s1').get(var.get('off')))
                    var.put('b', var.get('s2').get(var.get('off')))
                    if (var.get('a')>var.get('b')):
                        return Js(1.0)
                    else:
                        if (var.get('a')<var.get('b')):
                            return (-Js(1.0))
                        else:
                            var.put('_off', ((var.get('off')+Js(1.0))|Js(0.0)))
                            continue
                else:
                    return var.get('def')
            pass
        PyJsHoisted_caml_bytes_compare_aux_.func_name = 'caml_bytes_compare_aux'
        var.put('caml_bytes_compare_aux', PyJsHoisted_caml_bytes_compare_aux_)
        @Js
        def PyJsHoisted_caml_bytes_compare_(s1, s2, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'this':this, 'arguments':arguments}, var)
            var.registers(['s1', 'len1', 's2', 'len2'])
            var.put('len1', var.get('s1').get('length'))
            var.put('len2', var.get('s2').get('length'))
            if PyJsStrictEq(var.get('len1'),var.get('len2')):
                return var.get('caml_bytes_compare_aux')(var.get('s1'), var.get('s2'), Js(0.0), var.get('len1'), Js(0.0))
            else:
                if (var.get('len1')<var.get('len2')):
                    return var.get('caml_bytes_compare_aux')(var.get('s1'), var.get('s2'), Js(0.0), var.get('len1'), (-Js(1.0)))
                else:
                    return var.get('caml_bytes_compare_aux')(var.get('s1'), var.get('s2'), Js(0.0), var.get('len2'), Js(1.0))
        PyJsHoisted_caml_bytes_compare_.func_name = 'caml_bytes_compare'
        var.put('caml_bytes_compare', PyJsHoisted_caml_bytes_compare_)
        @Js
        def PyJsHoisted_caml_bytes_equal_(s1, s2, this, arguments, var=var):
            var = Scope({'s1':s1, 's2':s2, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'len1', 'b', 'off', 'a', 's1$1', 's2', 's2$1', 's1', '_off', 'len2'])
            var.put('len1', var.get('s1').get('length'))
            var.put('len2', var.get('s2').get('length'))
            if PyJsStrictEq(var.get('len1'),var.get('len2')):
                var.put('s1$1', var.get('s1'))
                var.put('s2$1', var.get('s2'))
                var.put('_off', Js(0.0))
                var.put('len', var.get('len1'))
                while Js(True):
                    var.put('off', var.get('_off'))
                    if PyJsStrictEq(var.get('off'),var.get('len')):
                        return Js(True)
                    else:
                        var.put('a', var.get('s1$1').get(var.get('off')))
                        var.put('b', var.get('s2$1').get(var.get('off')))
                        if PyJsStrictEq(var.get('a'),var.get('b')):
                            var.put('_off', ((var.get('off')+Js(1.0))|Js(0.0)))
                            continue
                        else:
                            return Js(False)
                pass
            else:
                return Js(False)
        PyJsHoisted_caml_bytes_equal_.func_name = 'caml_bytes_equal'
        var.put('caml_bytes_equal', PyJsHoisted_caml_bytes_equal_)
        @Js
        def PyJsHoisted_caml_bool_min_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if var.get('x'):
                return var.get('y')
            else:
                return var.get('x')
        PyJsHoisted_caml_bool_min_.func_name = 'caml_bool_min'
        var.put('caml_bool_min', PyJsHoisted_caml_bool_min_)
        @Js
        def PyJsHoisted_caml_int_min_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')<var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_int_min_.func_name = 'caml_int_min'
        var.put('caml_int_min', PyJsHoisted_caml_int_min_)
        @Js
        def PyJsHoisted_caml_float_min_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')<var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_float_min_.func_name = 'caml_float_min'
        var.put('caml_float_min', PyJsHoisted_caml_float_min_)
        @Js
        def PyJsHoisted_caml_string_min_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')<var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_string_min_.func_name = 'caml_string_min'
        var.put('caml_string_min', PyJsHoisted_caml_string_min_)
        @Js
        def PyJsHoisted_caml_nativeint_min_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')<var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_nativeint_min_.func_name = 'caml_nativeint_min'
        var.put('caml_nativeint_min', PyJsHoisted_caml_nativeint_min_)
        @Js
        def PyJsHoisted_caml_int32_min_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')<var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_int32_min_.func_name = 'caml_int32_min'
        var.put('caml_int32_min', PyJsHoisted_caml_int32_min_)
        @Js
        def PyJsHoisted_caml_bool_max_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if var.get('x'):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_bool_max_.func_name = 'caml_bool_max'
        var.put('caml_bool_max', PyJsHoisted_caml_bool_max_)
        @Js
        def PyJsHoisted_caml_int_max_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')>var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_int_max_.func_name = 'caml_int_max'
        var.put('caml_int_max', PyJsHoisted_caml_int_max_)
        @Js
        def PyJsHoisted_caml_float_max_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')>var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_float_max_.func_name = 'caml_float_max'
        var.put('caml_float_max', PyJsHoisted_caml_float_max_)
        @Js
        def PyJsHoisted_caml_string_max_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')>var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_string_max_.func_name = 'caml_string_max'
        var.put('caml_string_max', PyJsHoisted_caml_string_max_)
        @Js
        def PyJsHoisted_caml_nativeint_max_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')>var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_nativeint_max_.func_name = 'caml_nativeint_max'
        var.put('caml_nativeint_max', PyJsHoisted_caml_nativeint_max_)
        @Js
        def PyJsHoisted_caml_int32_max_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')>var.get('y')):
                return var.get('x')
            else:
                return var.get('y')
        PyJsHoisted_caml_int32_max_.func_name = 'caml_int32_max'
        var.put('caml_int32_max', PyJsHoisted_caml_int32_max_)
        Js('use strict')
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('caml_nativeint_compare', var.get('caml_int_compare'))
        var.put('caml_int32_compare', var.get('caml_int_compare'))
        var.get('exports').put('caml_bytes_compare', var.get('caml_bytes_compare'))
        var.get('exports').put('caml_bytes_equal', var.get('caml_bytes_equal'))
        var.get('exports').put('caml_int_compare', var.get('caml_int_compare'))
        var.get('exports').put('caml_bool_compare', var.get('caml_bool_compare'))
        var.get('exports').put('caml_float_compare', var.get('caml_float_compare'))
        var.get('exports').put('caml_nativeint_compare', var.get('caml_nativeint_compare'))
        var.get('exports').put('caml_string_compare', var.get('caml_string_compare'))
        var.get('exports').put('caml_int32_compare', var.get('caml_int32_compare'))
        var.get('exports').put('caml_bool_min', var.get('caml_bool_min'))
        var.get('exports').put('caml_int_min', var.get('caml_int_min'))
        var.get('exports').put('caml_float_min', var.get('caml_float_min'))
        var.get('exports').put('caml_string_min', var.get('caml_string_min'))
        var.get('exports').put('caml_nativeint_min', var.get('caml_nativeint_min'))
        var.get('exports').put('caml_int32_min', var.get('caml_int32_min'))
        var.get('exports').put('caml_bool_max', var.get('caml_bool_max'))
        var.get('exports').put('caml_int_max', var.get('caml_int_max'))
        var.get('exports').put('caml_float_max', var.get('caml_float_max'))
        var.get('exports').put('caml_string_max', var.get('caml_string_max'))
        var.get('exports').put('caml_nativeint_max', var.get('caml_nativeint_max'))
        var.get('exports').put('caml_int32_max', var.get('caml_int32_max'))
    PyJs_anonymous_33_._set_name('anonymous')
    @Js
    def PyJs_anonymous_34_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['uppercase_ascii', 'Caml_bytes', 'exports', 'compare', 'chr', 'require', 'uppercase', 'equal', 'module', 'lowercase', 'Caml_builtin_exceptions', 'lowercase_ascii', 'escaped'])
        @Js
        def PyJsHoisted_chr_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            if ((var.get('n')<Js(0.0)) or (var.get('n')>Js(255.0))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('Char.chr')]))
                raise PyJsTempException
            return var.get('n')
        PyJsHoisted_chr_.func_name = 'chr'
        var.put('chr', PyJsHoisted_chr_)
        @Js
        def PyJsHoisted_escaped_(c, this, arguments, var=var):
            var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['s$1', 'c', 'exit', 's'])
            var.put('exit', Js(0.0))
            if (var.get('c')>=Js(40.0)):
                if PyJsStrictNeq(var.get('c'),Js(92.0)):
                    var.put('exit', (Js(1.0) if (var.get('c')>=Js(127.0)) else Js(2.0)))
                else:
                    return Js('\\\\')
            else:
                if (var.get('c')>=Js(32.0)):
                    if (var.get('c')>=Js(39.0)):
                        return Js("\\'")
                    else:
                        var.put('exit', Js(2.0))
                else:
                    if (var.get('c')>=Js(14.0)):
                        var.put('exit', Js(1.0))
                    else:
                        while 1:
                            SWITCHED = False
                            CONDITION = (var.get('c'))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(8.0)):
                                SWITCHED = True
                                return Js('\\b')
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(9.0)):
                                SWITCHED = True
                                return Js('\\t')
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(10.0)):
                                SWITCHED = True
                                return Js('\\n')
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(11.0)):
                                SWITCHED = True
                                pass
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(12.0)):
                                SWITCHED = True
                                var.put('exit', Js(1.0))
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(13.0)):
                                SWITCHED = True
                                return Js('\\r')
                            SWITCHED = True
                            break
            while 1:
                SWITCHED = False
                CONDITION = (var.get('exit'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    var.put('s', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
                    var.get('s').put('0', Js(92.0))
                    var.get('s').put('1', ((Js(48.0)+((var.get('c')/Js(100.0))|Js(0.0)))|Js(0.0)))
                    var.get('s').put('2', ((Js(48.0)+(((var.get('c')/Js(10.0))|Js(0.0))%Js(10.0)))|Js(0.0)))
                    var.get('s').put('3', ((Js(48.0)+(var.get('c')%Js(10.0)))|Js(0.0)))
                    return var.get('Caml_bytes').callprop('bytes_to_string', var.get('s'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    var.put('s$1', Js([Js(0.0)]))
                    var.get('s$1').put('0', var.get('c'))
                    return var.get('Caml_bytes').callprop('bytes_to_string', var.get('s$1'))
                SWITCHED = True
                break
        PyJsHoisted_escaped_.func_name = 'escaped'
        var.put('escaped', PyJsHoisted_escaped_)
        @Js
        def PyJsHoisted_lowercase_(c, this, arguments, var=var):
            var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c'])
            if ((((var.get('c')>=Js(65.0)) and (var.get('c')<=Js(90.0))) or ((var.get('c')>=Js(192.0)) and (var.get('c')<=Js(214.0)))) or ((var.get('c')>=Js(216.0)) and (var.get('c')<=Js(222.0)))):
                return ((var.get('c')+Js(32.0))|Js(0.0))
            else:
                return var.get('c')
        PyJsHoisted_lowercase_.func_name = 'lowercase'
        var.put('lowercase', PyJsHoisted_lowercase_)
        @Js
        def PyJsHoisted_uppercase_(c, this, arguments, var=var):
            var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c'])
            if ((((var.get('c')>=Js(97.0)) and (var.get('c')<=Js(122.0))) or ((var.get('c')>=Js(224.0)) and (var.get('c')<=Js(246.0)))) or ((var.get('c')>=Js(248.0)) and (var.get('c')<=Js(254.0)))):
                return ((var.get('c')-Js(32.0))|Js(0.0))
            else:
                return var.get('c')
        PyJsHoisted_uppercase_.func_name = 'uppercase'
        var.put('uppercase', PyJsHoisted_uppercase_)
        @Js
        def PyJsHoisted_lowercase_ascii_(c, this, arguments, var=var):
            var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c'])
            if ((var.get('c')>=Js(65.0)) and (var.get('c')<=Js(90.0))):
                return ((var.get('c')+Js(32.0))|Js(0.0))
            else:
                return var.get('c')
        PyJsHoisted_lowercase_ascii_.func_name = 'lowercase_ascii'
        var.put('lowercase_ascii', PyJsHoisted_lowercase_ascii_)
        @Js
        def PyJsHoisted_uppercase_ascii_(c, this, arguments, var=var):
            var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c'])
            if ((var.get('c')>=Js(97.0)) and (var.get('c')<=Js(122.0))):
                return ((var.get('c')-Js(32.0))|Js(0.0))
            else:
                return var.get('c')
        PyJsHoisted_uppercase_ascii_.func_name = 'uppercase_ascii'
        var.put('uppercase_ascii', PyJsHoisted_uppercase_ascii_)
        @Js
        def PyJsHoisted_compare_(c1, c2, this, arguments, var=var):
            var = Scope({'c1':c1, 'c2':c2, 'this':this, 'arguments':arguments}, var)
            var.registers(['c1', 'c2'])
            return ((var.get('c1')-var.get('c2'))|Js(0.0))
        PyJsHoisted_compare_.func_name = 'compare'
        var.put('compare', PyJsHoisted_compare_)
        @Js
        def PyJsHoisted_equal_(c1, c2, this, arguments, var=var):
            var = Scope({'c1':c1, 'c2':c2, 'this':this, 'arguments':arguments}, var)
            var.registers(['c1', 'c2'])
            return PyJsStrictEq(((var.get('c1')-var.get('c2'))|Js(0.0)),Js(0.0))
        PyJsHoisted_equal_.func_name = 'equal'
        var.put('equal', PyJsHoisted_equal_)
        Js('use strict')
        var.put('Caml_bytes', var.get('require')(Js('./caml_bytes.js')))
        var.put('Caml_builtin_exceptions', var.get('require')(Js('./caml_builtin_exceptions.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('chr', var.get('chr'))
        var.get('exports').put('escaped', var.get('escaped'))
        var.get('exports').put('lowercase', var.get('lowercase'))
        var.get('exports').put('uppercase', var.get('uppercase'))
        var.get('exports').put('lowercase_ascii', var.get('lowercase_ascii'))
        var.get('exports').put('uppercase_ascii', var.get('uppercase_ascii'))
        var.get('exports').put('compare', var.get('compare'))
        var.get('exports').put('equal', var.get('equal'))
    PyJs_anonymous_34_._set_name('anonymous')
    @Js
    def PyJs_anonymous_35_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'curry_4', '_5', '__6', 'curry_6', '__5', 'Caml_array', '__1', '_1', '_7', 'curry_3', '__8', '_4', 'curry_5', '__3', 'curry_2', 'curry_8', 'curry_1', 'module', '_2', 'curry_7', 'require', '_3', 'app', '__4', '_6', '__2', '__7', '_8'])
        @Js
        def PyJsHoisted_app_(_f, _args, this, arguments, var=var):
            var = Scope({'_f':_f, '_args':_args, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'f', 'args', 'len', '_args', '_f', 'init_arity', 'd'])
            while Js(True):
                var.put('args', var.get('_args'))
                var.put('f', var.get('_f'))
                var.put('init_arity', var.get('f').get('length'))
                var.put('arity', (Js(1.0) if PyJsStrictEq(var.get('init_arity'),Js(0.0)) else var.get('init_arity')))
                var.put('len', var.get('args').get('length'))
                var.put('d', ((var.get('arity')-var.get('len'))|Js(0.0)))
                if PyJsStrictEq(var.get('d'),Js(0.0)):
                    return var.get('f').callprop('apply', var.get(u"null"), var.get('args'))
                else:
                    if (var.get('d')<Js(0.0)):
                        var.put('_args', var.get('Caml_array').callprop('caml_array_sub', var.get('args'), var.get('arity'), ((-var.get('d'))|Js(0.0))))
                        var.put('_f', var.get('f').callprop('apply', var.get(u"null"), var.get('Caml_array').callprop('caml_array_sub', var.get('args'), Js(0.0), var.get('arity'))))
                        continue
                    else:
                        @Js
                        def PyJs_anonymous_36_(f, args, this, arguments, var=var):
                            var = Scope({'f':f, 'args':args, 'this':this, 'arguments':arguments}, var)
                            var.registers(['f', 'args'])
                            @Js
                            def PyJs_anonymous_37_(x, this, arguments, var=var):
                                var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
                                var.registers(['x'])
                                return var.get('app')(var.get('f'), var.get('args').callprop('concat', Js([var.get('x')])))
                            PyJs_anonymous_37_._set_name('anonymous')
                            return PyJs_anonymous_37_
                        PyJs_anonymous_36_._set_name('anonymous')
                        return PyJs_anonymous_36_(var.get('f'), var.get('args'))
            pass
        PyJsHoisted_app_.func_name = 'app'
        var.put('app', PyJsHoisted_app_)
        @Js
        def PyJsHoisted_curry_1_(o, a0, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['a0', 'arity', 'o'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('o')(var.get('a0'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_38_(param, this, arguments, var=var):
                        var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param'])
                        return var.get('o')(var.get('a0'), var.get('param'))
                    PyJs_anonymous_38_._set_name('anonymous')
                    return PyJs_anonymous_38_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_39_(param, PyJsArg_706172616d2431_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param'])
                        return var.get('o')(var.get('a0'), var.get('param'), var.get('param$1'))
                    PyJs_anonymous_39_._set_name('anonymous')
                    return PyJs_anonymous_39_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_40_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param', 'param$2'])
                        return var.get('o')(var.get('a0'), var.get('param'), var.get('param$1'), var.get('param$2'))
                    PyJs_anonymous_40_._set_name('anonymous')
                    return PyJs_anonymous_40_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_41_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, PyJsArg_706172616d2433_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'param$3':PyJsArg_706172616d2433_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param', 'param$2', 'param$3'])
                        return var.get('o')(var.get('a0'), var.get('param'), var.get('param$1'), var.get('param$2'), var.get('param$3'))
                    PyJs_anonymous_41_._set_name('anonymous')
                    return PyJs_anonymous_41_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_42_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, PyJsArg_706172616d2433_, PyJsArg_706172616d2434_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'param$3':PyJsArg_706172616d2433_, 'param$4':PyJsArg_706172616d2434_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$2', 'param$4', 'param$1', 'param$3', 'param'])
                        return var.get('o')(var.get('a0'), var.get('param'), var.get('param$1'), var.get('param$2'), var.get('param$3'), var.get('param$4'))
                    PyJs_anonymous_42_._set_name('anonymous')
                    return PyJs_anonymous_42_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_43_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, PyJsArg_706172616d2433_, PyJsArg_706172616d2434_, PyJsArg_706172616d2435_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'param$3':PyJsArg_706172616d2433_, 'param$4':PyJsArg_706172616d2434_, 'param$5':PyJsArg_706172616d2435_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$2', 'param$4', 'param$5', 'param$1', 'param$3', 'param'])
                        return var.get('o')(var.get('a0'), var.get('param'), var.get('param$1'), var.get('param$2'), var.get('param$3'), var.get('param$4'), var.get('param$5'))
                    PyJs_anonymous_43_._set_name('anonymous')
                    return PyJs_anonymous_43_
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_1_.func_name = 'curry_1'
        var.put('curry_1', PyJsHoisted_curry_1_)
        @Js
        def PyJsHoisted__1_(o, a0, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a0', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(1.0)):
                return var.get('o')(var.get('a0'))
            else:
                return var.get('curry_1')(var.get('o'), var.get('a0'), var.get('arity'))
        PyJsHoisted__1_.func_name = '_1'
        var.put('_1', PyJsHoisted__1_)
        @Js
        def PyJsHoisted___1_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(1.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_44_(a0, this, arguments, var=var):
                    var = Scope({'a0':a0, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a0'])
                    return var.get('_1')(var.get('o'), var.get('a0'))
                PyJs_anonymous_44_._set_name('anonymous')
                return PyJs_anonymous_44_
        PyJsHoisted___1_.func_name = '__1'
        var.put('__1', PyJsHoisted___1_)
        @Js
        def PyJsHoisted_curry_2_(o, a0, a1, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['a0', 'arity', 'a1', 'o'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0')), Js([var.get('a1')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('o')(var.get('a0'), var.get('a1'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_45_(param, this, arguments, var=var):
                        var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('param'))
                    PyJs_anonymous_45_._set_name('anonymous')
                    return PyJs_anonymous_45_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_46_(param, PyJsArg_706172616d2431_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('param'), var.get('param$1'))
                    PyJs_anonymous_46_._set_name('anonymous')
                    return PyJs_anonymous_46_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_47_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param', 'param$2'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('param'), var.get('param$1'), var.get('param$2'))
                    PyJs_anonymous_47_._set_name('anonymous')
                    return PyJs_anonymous_47_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_48_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, PyJsArg_706172616d2433_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'param$3':PyJsArg_706172616d2433_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param', 'param$2', 'param$3'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('param'), var.get('param$1'), var.get('param$2'), var.get('param$3'))
                    PyJs_anonymous_48_._set_name('anonymous')
                    return PyJs_anonymous_48_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_49_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, PyJsArg_706172616d2433_, PyJsArg_706172616d2434_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'param$3':PyJsArg_706172616d2433_, 'param$4':PyJsArg_706172616d2434_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$2', 'param$4', 'param$1', 'param$3', 'param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('param'), var.get('param$1'), var.get('param$2'), var.get('param$3'), var.get('param$4'))
                    PyJs_anonymous_49_._set_name('anonymous')
                    return PyJs_anonymous_49_
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0'), var.get('a1')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_2_.func_name = 'curry_2'
        var.put('curry_2', PyJsHoisted_curry_2_)
        @Js
        def PyJsHoisted__2_(o, a0, a1, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a1', 'a0', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(2.0)):
                return var.get('o')(var.get('a0'), var.get('a1'))
            else:
                return var.get('curry_2')(var.get('o'), var.get('a0'), var.get('a1'), var.get('arity'))
        PyJsHoisted__2_.func_name = '_2'
        var.put('_2', PyJsHoisted__2_)
        @Js
        def PyJsHoisted___2_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(2.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_50_(a0, a1, this, arguments, var=var):
                    var = Scope({'a0':a0, 'a1':a1, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a1', 'a0'])
                    return var.get('_2')(var.get('o'), var.get('a0'), var.get('a1'))
                PyJs_anonymous_50_._set_name('anonymous')
                return PyJs_anonymous_50_
        PyJsHoisted___2_.func_name = '__2'
        var.put('__2', PyJsHoisted___2_)
        @Js
        def PyJsHoisted_curry_3_(o, a0, a1, a2, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a1', 'a0', 'o', 'a2'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0')), Js([var.get('a1'), var.get('a2')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1')), Js([var.get('a2')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_51_(param, this, arguments, var=var):
                        var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('param'))
                    PyJs_anonymous_51_._set_name('anonymous')
                    return PyJs_anonymous_51_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_52_(param, PyJsArg_706172616d2431_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('param'), var.get('param$1'))
                    PyJs_anonymous_52_._set_name('anonymous')
                    return PyJs_anonymous_52_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_53_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param', 'param$2'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('param'), var.get('param$1'), var.get('param$2'))
                    PyJs_anonymous_53_._set_name('anonymous')
                    return PyJs_anonymous_53_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_54_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, PyJsArg_706172616d2433_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'param$3':PyJsArg_706172616d2433_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param', 'param$2', 'param$3'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('param'), var.get('param$1'), var.get('param$2'), var.get('param$3'))
                    PyJs_anonymous_54_._set_name('anonymous')
                    return PyJs_anonymous_54_
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0'), var.get('a1'), var.get('a2')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_3_.func_name = 'curry_3'
        var.put('curry_3', PyJsHoisted_curry_3_)
        @Js
        def PyJsHoisted__3_(o, a0, a1, a2, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a1', 'a0', 'o', 'a2'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(3.0)):
                return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'))
            else:
                return var.get('curry_3')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('arity'))
        PyJsHoisted__3_.func_name = '_3'
        var.put('_3', PyJsHoisted__3_)
        @Js
        def PyJsHoisted___3_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(3.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_55_(a0, a1, a2, this, arguments, var=var):
                    var = Scope({'a0':a0, 'a1':a1, 'a2':a2, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a2', 'a1', 'a0'])
                    return var.get('_3')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'))
                PyJs_anonymous_55_._set_name('anonymous')
                return PyJs_anonymous_55_
        PyJsHoisted___3_.func_name = '__3'
        var.put('__3', PyJsHoisted___3_)
        @Js
        def PyJsHoisted_curry_4_(o, a0, a1, a2, a3, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0')), Js([var.get('a1'), var.get('a2'), var.get('a3')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1')), Js([var.get('a2'), var.get('a3')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2')), Js([var.get('a3')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_56_(param, this, arguments, var=var):
                        var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('param'))
                    PyJs_anonymous_56_._set_name('anonymous')
                    return PyJs_anonymous_56_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_57_(param, PyJsArg_706172616d2431_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('param'), var.get('param$1'))
                    PyJs_anonymous_57_._set_name('anonymous')
                    return PyJs_anonymous_57_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_58_(param, PyJsArg_706172616d2431_, PyJsArg_706172616d2432_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'param$2':PyJsArg_706172616d2432_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param', 'param$2'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('param'), var.get('param$1'), var.get('param$2'))
                    PyJs_anonymous_58_._set_name('anonymous')
                    return PyJs_anonymous_58_
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_4_.func_name = 'curry_4'
        var.put('curry_4', PyJsHoisted_curry_4_)
        @Js
        def PyJsHoisted__4_(o, a0, a1, a2, a3, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(4.0)):
                return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'))
            else:
                return var.get('curry_4')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('arity'))
        PyJsHoisted__4_.func_name = '_4'
        var.put('_4', PyJsHoisted__4_)
        @Js
        def PyJsHoisted___4_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(4.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_59_(a0, a1, a2, a3, this, arguments, var=var):
                    var = Scope({'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a3', 'a2', 'a1', 'a0'])
                    return var.get('_4')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'))
                PyJs_anonymous_59_._set_name('anonymous')
                return PyJs_anonymous_59_
        PyJsHoisted___4_.func_name = '__4'
        var.put('__4', PyJsHoisted___4_)
        @Js
        def PyJsHoisted_curry_5_(o, a0, a1, a2, a3, a4, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a4'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0')), Js([var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1')), Js([var.get('a2'), var.get('a3'), var.get('a4')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2')), Js([var.get('a3'), var.get('a4')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3')), Js([var.get('a4')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_60_(param, this, arguments, var=var):
                        var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('param'))
                    PyJs_anonymous_60_._set_name('anonymous')
                    return PyJs_anonymous_60_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_61_(param, PyJsArg_706172616d2431_, this, arguments, var=var):
                        var = Scope({'param':param, 'param$1':PyJsArg_706172616d2431_, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param$1', 'param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('param'), var.get('param$1'))
                    PyJs_anonymous_61_._set_name('anonymous')
                    return PyJs_anonymous_61_
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_5_.func_name = 'curry_5'
        var.put('curry_5', PyJsHoisted_curry_5_)
        @Js
        def PyJsHoisted__5_(o, a0, a1, a2, a3, a4, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a4'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(5.0)):
                return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'))
            else:
                return var.get('curry_5')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('arity'))
        PyJsHoisted__5_.func_name = '_5'
        var.put('_5', PyJsHoisted__5_)
        @Js
        def PyJsHoisted___5_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(5.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_62_(a0, a1, a2, a3, a4, this, arguments, var=var):
                    var = Scope({'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a3', 'a1', 'a0', 'a2', 'a4'])
                    return var.get('_5')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'))
                PyJs_anonymous_62_._set_name('anonymous')
                return PyJs_anonymous_62_
        PyJsHoisted___5_.func_name = '__5'
        var.put('__5', PyJsHoisted___5_)
        @Js
        def PyJsHoisted_curry_6_(o, a0, a1, a2, a3, a4, a5, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a5', 'a4'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0')), Js([var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1')), Js([var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2')), Js([var.get('a3'), var.get('a4'), var.get('a5')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3')), Js([var.get('a4'), var.get('a5')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4')), Js([var.get('a5')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_63_(param, this, arguments, var=var):
                        var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                        var.registers(['param'])
                        return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('param'))
                    PyJs_anonymous_63_._set_name('anonymous')
                    return PyJs_anonymous_63_
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_6_.func_name = 'curry_6'
        var.put('curry_6', PyJsHoisted_curry_6_)
        @Js
        def PyJsHoisted__6_(o, a0, a1, a2, a3, a4, a5, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a5', 'a4'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(6.0)):
                return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'))
            else:
                return var.get('curry_6')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('arity'))
        PyJsHoisted__6_.func_name = '_6'
        var.put('_6', PyJsHoisted__6_)
        @Js
        def PyJsHoisted___6_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(6.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_64_(a0, a1, a2, a3, a4, a5, this, arguments, var=var):
                    var = Scope({'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a3', 'a1', 'a0', 'a2', 'a5', 'a4'])
                    return var.get('_6')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'))
                PyJs_anonymous_64_._set_name('anonymous')
                return PyJs_anonymous_64_
        PyJsHoisted___6_.func_name = '__6'
        var.put('__6', PyJsHoisted___6_)
        @Js
        def PyJsHoisted_curry_7_(o, a0, a1, a2, a3, a4, a5, a6, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'a6':a6, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a5', 'a6', 'a4'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0')), Js([var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1')), Js([var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2')), Js([var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3')), Js([var.get('a4'), var.get('a5'), var.get('a6')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4')), Js([var.get('a5'), var.get('a6')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5')), Js([var.get('a6')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'))
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_7_.func_name = 'curry_7'
        var.put('curry_7', PyJsHoisted_curry_7_)
        @Js
        def PyJsHoisted__7_(o, a0, a1, a2, a3, a4, a5, a6, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'a6':a6, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a5', 'a6', 'a4'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(7.0)):
                return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'))
            else:
                return var.get('curry_7')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('arity'))
        PyJsHoisted__7_.func_name = '_7'
        var.put('_7', PyJsHoisted__7_)
        @Js
        def PyJsHoisted___7_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(7.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_65_(a0, a1, a2, a3, a4, a5, a6, this, arguments, var=var):
                    var = Scope({'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'a6':a6, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a3', 'a1', 'a0', 'a2', 'a5', 'a6', 'a4'])
                    return var.get('_7')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'))
                PyJs_anonymous_65_._set_name('anonymous')
                return PyJs_anonymous_65_
        PyJsHoisted___7_.func_name = '__7'
        var.put('__7', PyJsHoisted___7_)
        @Js
        def PyJsHoisted_curry_8_(o, a0, a1, a2, a3, a4, a5, a6, a7, arity, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'a6':a6, 'a7':a7, 'arity':arity, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a5', 'a6', 'a7', 'a4'])
            while 1:
                SWITCHED = False
                CONDITION = (var.get('arity'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0')), Js([var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1')), Js([var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2')), Js([var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3')), Js([var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(5.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4')), Js([var.get('a5'), var.get('a6'), var.get('a7')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5')), Js([var.get('a6'), var.get('a7')]))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(7.0)):
                    SWITCHED = True
                    return var.get('app')(var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6')), Js([var.get('a7')]))
                if True:
                    SWITCHED = True
                    return var.get('app')(var.get('o'), Js([var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7')]))
                SWITCHED = True
                break
        PyJsHoisted_curry_8_.func_name = 'curry_8'
        var.put('curry_8', PyJsHoisted_curry_8_)
        @Js
        def PyJsHoisted__8_(o, a0, a1, a2, a3, a4, a5, a6, a7, this, arguments, var=var):
            var = Scope({'o':o, 'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'a6':a6, 'a7':a7, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'a3', 'a1', 'a0', 'o', 'a2', 'a5', 'a6', 'a7', 'a4'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(8.0)):
                return var.get('o')(var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7'))
            else:
                return var.get('curry_8')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7'), var.get('arity'))
        PyJsHoisted__8_.func_name = '_8'
        var.put('_8', PyJsHoisted__8_)
        @Js
        def PyJsHoisted___8_(o, this, arguments, var=var):
            var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
            var.registers(['arity', 'o'])
            var.put('arity', var.get('o').get('length'))
            if PyJsStrictEq(var.get('arity'),Js(8.0)):
                return var.get('o')
            else:
                @Js
                def PyJs_anonymous_66_(a0, a1, a2, a3, a4, a5, a6, a7, this, arguments, var=var):
                    var = Scope({'a0':a0, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4, 'a5':a5, 'a6':a6, 'a7':a7, 'this':this, 'arguments':arguments}, var)
                    var.registers(['a3', 'a1', 'a0', 'a2', 'a5', 'a6', 'a7', 'a4'])
                    return var.get('_8')(var.get('o'), var.get('a0'), var.get('a1'), var.get('a2'), var.get('a3'), var.get('a4'), var.get('a5'), var.get('a6'), var.get('a7'))
                PyJs_anonymous_66_._set_name('anonymous')
                return PyJs_anonymous_66_
        PyJsHoisted___8_.func_name = '__8'
        var.put('__8', PyJsHoisted___8_)
        Js('use strict')
        var.put('Caml_array', var.get('require')(Js('./caml_array.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('app', var.get('app'))
        var.get('exports').put('curry_1', var.get('curry_1'))
        var.get('exports').put('_1', var.get('_1'))
        var.get('exports').put('__1', var.get('__1'))
        var.get('exports').put('curry_2', var.get('curry_2'))
        var.get('exports').put('_2', var.get('_2'))
        var.get('exports').put('__2', var.get('__2'))
        var.get('exports').put('curry_3', var.get('curry_3'))
        var.get('exports').put('_3', var.get('_3'))
        var.get('exports').put('__3', var.get('__3'))
        var.get('exports').put('curry_4', var.get('curry_4'))
        var.get('exports').put('_4', var.get('_4'))
        var.get('exports').put('__4', var.get('__4'))
        var.get('exports').put('curry_5', var.get('curry_5'))
        var.get('exports').put('_5', var.get('_5'))
        var.get('exports').put('__5', var.get('__5'))
        var.get('exports').put('curry_6', var.get('curry_6'))
        var.get('exports').put('_6', var.get('_6'))
        var.get('exports').put('__6', var.get('__6'))
        var.get('exports').put('curry_7', var.get('curry_7'))
        var.get('exports').put('_7', var.get('_7'))
        var.get('exports').put('__7', var.get('__7'))
        var.get('exports').put('curry_8', var.get('curry_8'))
        var.get('exports').put('_8', var.get('_8'))
        var.get('exports').put('__8', var.get('__8'))
    PyJs_anonymous_35_._set_name('anonymous')
    @Js
    def PyJs_anonymous_67_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'require', 'equal', 'module', 'min', 'max'])
        @Js
        def PyJsHoisted_equal_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            return PyJsStrictEq(var.get('x'),var.get('y'))
        PyJsHoisted_equal_.func_name = 'equal'
        var.put('equal', PyJsHoisted_equal_)
        Js('use strict')
        pass
        var.put('max', Js(2147483647.0))
        var.put('min', (-Js(2147483648.0)))
        var.get('exports').put('equal', var.get('equal'))
        var.get('exports').put('max', var.get('max'))
        var.get('exports').put('min', var.get('min'))
    PyJs_anonymous_67_._set_name('anonymous')
    @Js
    def PyJs_anonymous_68_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'require', 'unsafe_ceil', 'ceil_int', 'module', 'floor_int', 'random_int', 'ceil', 'Js_int', 'unsafe_floor', 'floor'])
        @Js
        def PyJsHoisted_unsafe_ceil_(prim, this, arguments, var=var):
            var = Scope({'prim':prim, 'this':this, 'arguments':arguments}, var)
            var.registers(['prim'])
            return var.get('Math').callprop('ceil', var.get('prim'))
        PyJsHoisted_unsafe_ceil_.func_name = 'unsafe_ceil'
        var.put('unsafe_ceil', PyJsHoisted_unsafe_ceil_)
        @Js
        def PyJsHoisted_ceil_int_(f, this, arguments, var=var):
            var = Scope({'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f'])
            if (var.get('f')>var.get('Js_int').get('max')):
                return var.get('Js_int').get('max')
            else:
                if (var.get('f')<var.get('Js_int').get('min')):
                    return var.get('Js_int').get('min')
                else:
                    return var.get('Math').callprop('ceil', var.get('f'))
        PyJsHoisted_ceil_int_.func_name = 'ceil_int'
        var.put('ceil_int', PyJsHoisted_ceil_int_)
        @Js
        def PyJsHoisted_unsafe_floor_(prim, this, arguments, var=var):
            var = Scope({'prim':prim, 'this':this, 'arguments':arguments}, var)
            var.registers(['prim'])
            return var.get('Math').callprop('floor', var.get('prim'))
        PyJsHoisted_unsafe_floor_.func_name = 'unsafe_floor'
        var.put('unsafe_floor', PyJsHoisted_unsafe_floor_)
        @Js
        def PyJsHoisted_floor_int_(f, this, arguments, var=var):
            var = Scope({'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f'])
            if (var.get('f')>var.get('Js_int').get('max')):
                return var.get('Js_int').get('max')
            else:
                if (var.get('f')<var.get('Js_int').get('min')):
                    return var.get('Js_int').get('min')
                else:
                    return var.get('Math').callprop('floor', var.get('f'))
        PyJsHoisted_floor_int_.func_name = 'floor_int'
        var.put('floor_int', PyJsHoisted_floor_int_)
        @Js
        def PyJsHoisted_random_int_(min, max, this, arguments, var=var):
            var = Scope({'min':min, 'max':max, 'this':this, 'arguments':arguments}, var)
            var.registers(['min', 'max'])
            return ((var.get('floor_int')((var.get('Math').callprop('random')*((var.get('max')-var.get('min'))|Js(0.0))))+var.get('min'))|Js(0.0))
        PyJsHoisted_random_int_.func_name = 'random_int'
        var.put('random_int', PyJsHoisted_random_int_)
        Js('use strict')
        var.put('Js_int', var.get('require')(Js('./js_int.js')))
        pass
        pass
        pass
        pass
        pass
        var.put('ceil', var.get('ceil_int'))
        var.put('floor', var.get('floor_int'))
        var.get('exports').put('unsafe_ceil', var.get('unsafe_ceil'))
        var.get('exports').put('ceil_int', var.get('ceil_int'))
        var.get('exports').put('ceil', var.get('ceil'))
        var.get('exports').put('unsafe_floor', var.get('unsafe_floor'))
        var.get('exports').put('floor_int', var.get('floor_int'))
        var.get('exports').put('floor', var.get('floor'))
        var.get('exports').put('random_int', var.get('random_int'))
    PyJs_anonymous_68_._set_name('anonymous')
    @Js
    def PyJs_anonymous_69_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'map', 'sub', 'Caml_primitive', 'Bytes', 'uppercase', 'rindex_opt', 'capitalize_ascii', 'iter', 'init', 'capitalize', 'unsafe_blits', 'trim', 'uppercase_ascii', 'Caml_bytes', 'rindex', 'rindex_from_opt', 'split_on_char', 'mapi', 'rindex_rec_opt', 'iteri', 'module', 'lowercase_ascii', 'contains_from', 'is_space', 'fill', 'index_rec_opt', 'copy', 'require', 'uncapitalize', 'index_from', 'Curry', 'index_from_opt', 'make', 'index', 'rindex_rec', 'rindex_from', 'Caml_builtin_exceptions', 'rcontains_from', 'ensure_ge', 'compare', 'index_opt', 'concat', 'equal', 'uncapitalize_ascii', 'lowercase', 'blit', 'contains', 'index_rec', 'escaped', 'sum_lengths'])
        @Js
        def PyJsHoisted_make_(n, c, this, arguments, var=var):
            var = Scope({'n':n, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'n'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('make', var.get('n'), var.get('c')))
        PyJsHoisted_make_.func_name = 'make'
        var.put('make', PyJsHoisted_make_)
        @Js
        def PyJsHoisted_init_(n, f, this, arguments, var=var):
            var = Scope({'n':n, 'f':f, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'n'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('init', var.get('n'), var.get('f')))
        PyJsHoisted_init_.func_name = 'init'
        var.put('init', PyJsHoisted_init_)
        @Js
        def PyJsHoisted_copy_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('copy', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_copy_.func_name = 'copy'
        var.put('copy', PyJsHoisted_copy_)
        @Js
        def PyJsHoisted_sub_(s, ofs, len, this, arguments, var=var):
            var = Scope({'s':s, 'ofs':ofs, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 'ofs', 's'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('sub', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s')), var.get('ofs'), var.get('len')))
        PyJsHoisted_sub_.func_name = 'sub'
        var.put('sub', PyJsHoisted_sub_)
        @Js
        def PyJsHoisted_ensure_ge_(x, y, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get('x')>=var.get('y')):
                return var.get('x')
            else:
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.concat')]))
                raise PyJsTempException
        PyJsHoisted_ensure_ge_.func_name = 'ensure_ge'
        var.put('ensure_ge', PyJsHoisted_ensure_ge_)
        @Js
        def PyJsHoisted_sum_lengths_(_acc, seplen, _param, this, arguments, var=var):
            var = Scope({'_acc':_acc, 'seplen':seplen, '_param':_param, 'this':this, 'arguments':arguments}, var)
            var.registers(['_param', 'tl', 'acc', 'hd', 'seplen', '_acc', 'param'])
            while Js(True):
                var.put('param', var.get('_param'))
                var.put('acc', var.get('_acc'))
                if var.get('param'):
                    var.put('tl', var.get('param').get('1'))
                    var.put('hd', var.get('param').get('0'))
                    if var.get('tl'):
                        var.put('_param', var.get('tl'))
                        var.put('_acc', var.get('ensure_ge')(((((var.get('hd').get('length')+var.get('seplen'))|Js(0.0))+var.get('acc'))|Js(0.0)), var.get('acc')))
                        continue
                    else:
                        return ((var.get('hd').get('length')+var.get('acc'))|Js(0.0))
                else:
                    return var.get('acc')
            pass
        PyJsHoisted_sum_lengths_.func_name = 'sum_lengths'
        var.put('sum_lengths', PyJsHoisted_sum_lengths_)
        @Js
        def PyJsHoisted_unsafe_blits_(dst, _pos, sep, seplen, _param, this, arguments, var=var):
            var = Scope({'dst':dst, '_pos':_pos, 'sep':sep, 'seplen':seplen, '_param':_param, 'this':this, 'arguments':arguments}, var)
            var.registers(['dst', '_pos', '_param', 'tl', 'pos', 'hd', 'seplen', 'sep', 'param'])
            while Js(True):
                var.put('param', var.get('_param'))
                var.put('pos', var.get('_pos'))
                if var.get('param'):
                    var.put('tl', var.get('param').get('1'))
                    var.put('hd', var.get('param').get('0'))
                    if var.get('tl'):
                        var.get('Caml_bytes').callprop('caml_blit_string', var.get('hd'), Js(0.0), var.get('dst'), var.get('pos'), var.get('hd').get('length'))
                        var.get('Caml_bytes').callprop('caml_blit_string', var.get('sep'), Js(0.0), var.get('dst'), ((var.get('pos')+var.get('hd').get('length'))|Js(0.0)), var.get('seplen'))
                        var.put('_param', var.get('tl'))
                        var.put('_pos', ((((var.get('pos')+var.get('hd').get('length'))|Js(0.0))+var.get('seplen'))|Js(0.0)))
                        continue
                    else:
                        var.get('Caml_bytes').callprop('caml_blit_string', var.get('hd'), Js(0.0), var.get('dst'), var.get('pos'), var.get('hd').get('length'))
                        return var.get('dst')
                else:
                    return var.get('dst')
            pass
        PyJsHoisted_unsafe_blits_.func_name = 'unsafe_blits'
        var.put('unsafe_blits', PyJsHoisted_unsafe_blits_)
        @Js
        def PyJsHoisted_concat_(sep, l, this, arguments, var=var):
            var = Scope({'sep':sep, 'l':l, 'this':this, 'arguments':arguments}, var)
            var.registers(['seplen', 'sep', 'l'])
            if var.get('l'):
                var.put('seplen', var.get('sep').get('length'))
                return var.get('Caml_bytes').callprop('bytes_to_string', var.get('unsafe_blits')(var.get('Caml_bytes').callprop('caml_create_bytes', var.get('sum_lengths')(Js(0.0), var.get('seplen'), var.get('l'))), Js(0.0), var.get('sep'), var.get('seplen'), var.get('l')))
            else:
                return Js('')
        PyJsHoisted_concat_.func_name = 'concat'
        var.put('concat', PyJsHoisted_concat_)
        @Js
        def PyJsHoisted_iter_(f, s, this, arguments, var=var):
            var = Scope({'f':f, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'i', 'i_finish', 's'])
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('s').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('Curry').callprop('_1', var.get('f'), var.get('s').callprop('charCodeAt', var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_iter_.func_name = 'iter'
        var.put('iter', PyJsHoisted_iter_)
        @Js
        def PyJsHoisted_iteri_(f, s, this, arguments, var=var):
            var = Scope({'f':f, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 'i', 'i_finish', 's'])
            #for JS loop
            var.put('i', Js(0.0))
            var.put('i_finish', ((var.get('s').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')<=var.get('i_finish')):
                try:
                    var.get('Curry').callprop('_2', var.get('f'), var.get('i'), var.get('s').callprop('charCodeAt', var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(0.0)
        PyJsHoisted_iteri_.func_name = 'iteri'
        var.put('iteri', PyJsHoisted_iteri_)
        @Js
        def PyJsHoisted_map_(f, s, this, arguments, var=var):
            var = Scope({'f':f, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 's'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('map', var.get('f'), var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_map_.func_name = 'map'
        var.put('map', PyJsHoisted_map_)
        @Js
        def PyJsHoisted_mapi_(f, s, this, arguments, var=var):
            var = Scope({'f':f, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['f', 's'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('mapi', var.get('f'), var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_mapi_.func_name = 'mapi'
        var.put('mapi', PyJsHoisted_mapi_)
        @Js
        def PyJsHoisted_is_space_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['switcher', 'param'])
            var.put('switcher', ((var.get('param')-Js(9.0))|Js(0.0)))
            if ((var.get('switcher')>Js(4.0)) or (var.get('switcher')<Js(0.0))):
                return PyJsStrictEq(var.get('switcher'),Js(23.0))
            else:
                return PyJsStrictNeq(var.get('switcher'),Js(2.0))
        PyJsHoisted_is_space_.func_name = 'is_space'
        var.put('is_space', PyJsHoisted_is_space_)
        @Js
        def PyJsHoisted_trim_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            if (PyJsStrictEq(var.get('s'),Js('')) or (var.get('is_space')(var.get('s').callprop('charCodeAt', Js(0.0))) or var.get('is_space')(var.get('s').callprop('charCodeAt', ((var.get('s').get('length')-Js(1.0))|Js(0.0))))).neg()):
                return var.get('s')
            else:
                return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('trim', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_trim_.func_name = 'trim'
        var.put('trim', PyJsHoisted_trim_)
        @Js
        def PyJsHoisted_escaped_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['needs_escape', 's'])
            @Js
            def PyJs_anonymous_70_(_i, this, arguments, var=var):
                var = Scope({'_i':_i, 'this':this, 'arguments':arguments}, var)
                var.registers(['match', 'i', 'switcher', '_i'])
                while Js(True):
                    var.put('i', var.get('_i'))
                    if (var.get('i')>=var.get('s').get('length')):
                        return Js(False)
                    else:
                        var.put('match', var.get('s').callprop('charCodeAt', var.get('i')))
                        if (var.get('match')>=Js(32.0)):
                            var.put('switcher', ((var.get('match')-Js(34.0))|Js(0.0)))
                            if ((var.get('switcher')>Js(58.0)) or (var.get('switcher')<Js(0.0))):
                                if (var.get('switcher')>=Js(93.0)):
                                    return Js(True)
                                else:
                                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                                    continue
                            else:
                                if ((var.get('switcher')>Js(57.0)) or (var.get('switcher')<Js(1.0))):
                                    return Js(True)
                                else:
                                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                                    continue
                        else:
                            return Js(True)
                pass
            PyJs_anonymous_70_._set_name('anonymous')
            var.put('needs_escape', PyJs_anonymous_70_)
            if var.get('needs_escape')(Js(0.0)):
                return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('escaped', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
            else:
                return var.get('s')
        PyJsHoisted_escaped_.func_name = 'escaped'
        var.put('escaped', PyJsHoisted_escaped_)
        @Js
        def PyJsHoisted_index_rec_(s, lim, _i, c, this, arguments, var=var):
            var = Scope({'s':s, 'lim':lim, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['lim', 'c', '_i', 's', 'i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')>=var.get('lim')):
                    PyJsTempException = JsToPyException(var.get('Caml_builtin_exceptions').get('not_found'))
                    raise PyJsTempException
                if PyJsStrictEq(var.get('s').callprop('charCodeAt', var.get('i')),var.get('c')):
                    return var.get('i')
                else:
                    var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                    continue
            pass
        PyJsHoisted_index_rec_.func_name = 'index_rec'
        var.put('index_rec', PyJsHoisted_index_rec_)
        @Js
        def PyJsHoisted_index_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('index_rec')(var.get('s'), var.get('s').get('length'), Js(0.0), var.get('c'))
        PyJsHoisted_index_.func_name = 'index'
        var.put('index', PyJsHoisted_index_)
        @Js
        def PyJsHoisted_index_rec_opt_(s, lim, _i, c, this, arguments, var=var):
            var = Scope({'s':s, 'lim':lim, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['lim', 'c', '_i', 's', 'i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')>=var.get('lim')):
                    return var.get('undefined')
                else:
                    if PyJsStrictEq(var.get('s').callprop('charCodeAt', var.get('i')),var.get('c')):
                        return var.get('i')
                    else:
                        var.put('_i', ((var.get('i')+Js(1.0))|Js(0.0)))
                        continue
            pass
        PyJsHoisted_index_rec_opt_.func_name = 'index_rec_opt'
        var.put('index_rec_opt', PyJsHoisted_index_rec_opt_)
        @Js
        def PyJsHoisted_index_opt_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('index_rec_opt')(var.get('s'), var.get('s').get('length'), Js(0.0), var.get('c'))
        PyJsHoisted_index_opt_.func_name = 'index_opt'
        var.put('index_opt', PyJsHoisted_index_opt_)
        @Js
        def PyJsHoisted_index_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', 'l'])
            var.put('l', var.get('s').get('length'))
            if ((var.get('i')<Js(0.0)) or (var.get('i')>var.get('l'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.index_from / Bytes.index_from')]))
                raise PyJsTempException
            return var.get('index_rec')(var.get('s'), var.get('l'), var.get('i'), var.get('c'))
        PyJsHoisted_index_from_.func_name = 'index_from'
        var.put('index_from', PyJsHoisted_index_from_)
        @Js
        def PyJsHoisted_index_from_opt_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', 'l'])
            var.put('l', var.get('s').get('length'))
            if ((var.get('i')<Js(0.0)) or (var.get('i')>var.get('l'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.index_from_opt / Bytes.index_from_opt')]))
                raise PyJsTempException
            return var.get('index_rec_opt')(var.get('s'), var.get('l'), var.get('i'), var.get('c'))
        PyJsHoisted_index_from_opt_.func_name = 'index_from_opt'
        var.put('index_from_opt', PyJsHoisted_index_from_opt_)
        @Js
        def PyJsHoisted_rindex_rec_(s, _i, c, this, arguments, var=var):
            var = Scope({'s':s, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', '_i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')<Js(0.0)):
                    PyJsTempException = JsToPyException(var.get('Caml_builtin_exceptions').get('not_found'))
                    raise PyJsTempException
                if PyJsStrictEq(var.get('s').callprop('charCodeAt', var.get('i')),var.get('c')):
                    return var.get('i')
                else:
                    var.put('_i', ((var.get('i')-Js(1.0))|Js(0.0)))
                    continue
            pass
        PyJsHoisted_rindex_rec_.func_name = 'rindex_rec'
        var.put('rindex_rec', PyJsHoisted_rindex_rec_)
        @Js
        def PyJsHoisted_rindex_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('rindex_rec')(var.get('s'), ((var.get('s').get('length')-Js(1.0))|Js(0.0)), var.get('c'))
        PyJsHoisted_rindex_.func_name = 'rindex'
        var.put('rindex', PyJsHoisted_rindex_)
        @Js
        def PyJsHoisted_rindex_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's'])
            if ((var.get('i')<(-Js(1.0))) or (var.get('i')>=var.get('s').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.rindex_from / Bytes.rindex_from')]))
                raise PyJsTempException
            return var.get('rindex_rec')(var.get('s'), var.get('i'), var.get('c'))
        PyJsHoisted_rindex_from_.func_name = 'rindex_from'
        var.put('rindex_from', PyJsHoisted_rindex_from_)
        @Js
        def PyJsHoisted_rindex_rec_opt_(s, _i, c, this, arguments, var=var):
            var = Scope({'s':s, '_i':_i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', '_i'])
            while Js(True):
                var.put('i', var.get('_i'))
                if (var.get('i')<Js(0.0)):
                    return var.get('undefined')
                else:
                    if PyJsStrictEq(var.get('s').callprop('charCodeAt', var.get('i')),var.get('c')):
                        return var.get('i')
                    else:
                        var.put('_i', ((var.get('i')-Js(1.0))|Js(0.0)))
                        continue
            pass
        PyJsHoisted_rindex_rec_opt_.func_name = 'rindex_rec_opt'
        var.put('rindex_rec_opt', PyJsHoisted_rindex_rec_opt_)
        @Js
        def PyJsHoisted_rindex_opt_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('rindex_rec_opt')(var.get('s'), ((var.get('s').get('length')-Js(1.0))|Js(0.0)), var.get('c'))
        PyJsHoisted_rindex_opt_.func_name = 'rindex_opt'
        var.put('rindex_opt', PyJsHoisted_rindex_opt_)
        @Js
        def PyJsHoisted_rindex_from_opt_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's'])
            if ((var.get('i')<(-Js(1.0))) or (var.get('i')>=var.get('s').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.rindex_from_opt / Bytes.rindex_from_opt')]))
                raise PyJsTempException
            return var.get('rindex_rec_opt')(var.get('s'), var.get('i'), var.get('c'))
        PyJsHoisted_rindex_from_opt_.func_name = 'rindex_from_opt'
        var.put('rindex_from_opt', PyJsHoisted_rindex_from_opt_)
        @Js
        def PyJsHoisted_contains_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's', 'l'])
            var.put('l', var.get('s').get('length'))
            if ((var.get('i')<Js(0.0)) or (var.get('i')>var.get('l'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.contains_from / Bytes.contains_from')]))
                raise PyJsTempException
            try:
                var.get('index_rec')(var.get('s'), var.get('l'), var.get('i'), var.get('c'))
                return Js(True)
            except PyJsException as PyJsTempException:
                PyJsHolder_65786e_38903962 = var.own.get('exn')
                var.force_own_put('exn', PyExceptionToJs(PyJsTempException))
                try:
                    if PyJsStrictEq(var.get('exn'),var.get('Caml_builtin_exceptions').get('not_found')):
                        return Js(False)
                    else:
                        PyJsTempException = JsToPyException(var.get('exn'))
                        raise PyJsTempException
                finally:
                    if PyJsHolder_65786e_38903962 is not None:
                        var.own['exn'] = PyJsHolder_65786e_38903962
                    else:
                        del var.own['exn']
                    del PyJsHolder_65786e_38903962
        PyJsHoisted_contains_from_.func_name = 'contains_from'
        var.put('contains_from', PyJsHoisted_contains_from_)
        @Js
        def PyJsHoisted_contains_(s, c, this, arguments, var=var):
            var = Scope({'s':s, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 's'])
            return var.get('contains_from')(var.get('s'), Js(0.0), var.get('c'))
        PyJsHoisted_contains_.func_name = 'contains'
        var.put('contains', PyJsHoisted_contains_)
        @Js
        def PyJsHoisted_rcontains_from_(s, i, c, this, arguments, var=var):
            var = Scope({'s':s, 'i':i, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'i', 's'])
            if ((var.get('i')<Js(0.0)) or (var.get('i')>=var.get('s').get('length'))):
                PyJsTempException = JsToPyException(Js([var.get('Caml_builtin_exceptions').get('invalid_argument'), Js('String.rcontains_from / Bytes.rcontains_from')]))
                raise PyJsTempException
            try:
                var.get('rindex_rec')(var.get('s'), var.get('i'), var.get('c'))
                return Js(True)
            except PyJsException as PyJsTempException:
                PyJsHolder_65786e_37015846 = var.own.get('exn')
                var.force_own_put('exn', PyExceptionToJs(PyJsTempException))
                try:
                    if PyJsStrictEq(var.get('exn'),var.get('Caml_builtin_exceptions').get('not_found')):
                        return Js(False)
                    else:
                        PyJsTempException = JsToPyException(var.get('exn'))
                        raise PyJsTempException
                finally:
                    if PyJsHolder_65786e_37015846 is not None:
                        var.own['exn'] = PyJsHolder_65786e_37015846
                    else:
                        del var.own['exn']
                    del PyJsHolder_65786e_37015846
        PyJsHoisted_rcontains_from_.func_name = 'rcontains_from'
        var.put('rcontains_from', PyJsHoisted_rcontains_from_)
        @Js
        def PyJsHoisted_uppercase_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('uppercase_ascii', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_uppercase_ascii_.func_name = 'uppercase_ascii'
        var.put('uppercase_ascii', PyJsHoisted_uppercase_ascii_)
        @Js
        def PyJsHoisted_lowercase_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('lowercase_ascii', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_lowercase_ascii_.func_name = 'lowercase_ascii'
        var.put('lowercase_ascii', PyJsHoisted_lowercase_ascii_)
        @Js
        def PyJsHoisted_capitalize_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('capitalize_ascii', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_capitalize_ascii_.func_name = 'capitalize_ascii'
        var.put('capitalize_ascii', PyJsHoisted_capitalize_ascii_)
        @Js
        def PyJsHoisted_uncapitalize_ascii_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('uncapitalize_ascii', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_uncapitalize_ascii_.func_name = 'uncapitalize_ascii'
        var.put('uncapitalize_ascii', PyJsHoisted_uncapitalize_ascii_)
        @Js
        def PyJsHoisted_split_on_char_(sep, s, this, arguments, var=var):
            var = Scope({'sep':sep, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['j', 'r', 'sep', 's', 'i'])
            var.put('r', Js(0.0))
            var.put('j', var.get('s').get('length'))
            #for JS loop
            var.put('i', ((var.get('s').get('length')-Js(1.0))|Js(0.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    if PyJsStrictEq(var.get('s').callprop('charCodeAt', var.get('i')),var.get('sep')):
                        var.put('r', Js([var.get('sub')(var.get('s'), ((var.get('i')+Js(1.0))|Js(0.0)), ((((var.get('j')-var.get('i'))|Js(0.0))-Js(1.0))|Js(0.0))), var.get('r')]))
                        var.put('j', var.get('i'))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            return Js([var.get('sub')(var.get('s'), Js(0.0), var.get('j')), var.get('r')])
        PyJsHoisted_split_on_char_.func_name = 'split_on_char'
        var.put('split_on_char', PyJsHoisted_split_on_char_)
        @Js
        def PyJsHoisted_uppercase_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('uppercase', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_uppercase_.func_name = 'uppercase'
        var.put('uppercase', PyJsHoisted_uppercase_)
        @Js
        def PyJsHoisted_lowercase_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('lowercase', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_lowercase_.func_name = 'lowercase'
        var.put('lowercase', PyJsHoisted_lowercase_)
        @Js
        def PyJsHoisted_capitalize_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('capitalize', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_capitalize_.func_name = 'capitalize'
        var.put('capitalize', PyJsHoisted_capitalize_)
        @Js
        def PyJsHoisted_uncapitalize_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('Caml_bytes').callprop('bytes_to_string', var.get('Bytes').callprop('uncapitalize', var.get('Caml_bytes').callprop('bytes_of_string', var.get('s'))))
        PyJsHoisted_uncapitalize_.func_name = 'uncapitalize'
        var.put('uncapitalize', PyJsHoisted_uncapitalize_)
        @Js
        def PyJsHoisted_equal_(prim, PyJsArg_7072696d2431_, this, arguments, var=var):
            var = Scope({'prim':prim, 'prim$1':PyJsArg_7072696d2431_, 'this':this, 'arguments':arguments}, var)
            var.registers(['prim', 'prim$1'])
            return PyJsStrictEq(var.get('prim'),var.get('prim$1'))
        PyJsHoisted_equal_.func_name = 'equal'
        var.put('equal', PyJsHoisted_equal_)
        Js('use strict')
        var.put('Bytes', var.get('require')(Js('./bytes.js')))
        var.put('Curry', var.get('require')(Js('./curry.js')))
        var.put('Caml_bytes', var.get('require')(Js('./caml_bytes.js')))
        var.put('Caml_primitive', var.get('require')(Js('./caml_primitive.js')))
        var.put('Caml_builtin_exceptions', var.get('require')(Js('./caml_builtin_exceptions.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('compare', var.get('Caml_primitive').get('caml_string_compare'))
        pass
        pass
        pass
        pass
        pass
        var.put('fill', var.get('Bytes').get('fill'))
        var.put('blit', var.get('Bytes').get('blit_string'))
        pass
        var.get('exports').put('make', var.get('make'))
        var.get('exports').put('init', var.get('init'))
        var.get('exports').put('copy', var.get('copy'))
        var.get('exports').put('sub', var.get('sub'))
        var.get('exports').put('fill', var.get('fill'))
        var.get('exports').put('blit', var.get('blit'))
        var.get('exports').put('concat', var.get('concat'))
        var.get('exports').put('iter', var.get('iter'))
        var.get('exports').put('iteri', var.get('iteri'))
        var.get('exports').put('map', var.get('map'))
        var.get('exports').put('mapi', var.get('mapi'))
        var.get('exports').put('trim', var.get('trim'))
        var.get('exports').put('escaped', var.get('escaped'))
        var.get('exports').put('index', var.get('index'))
        var.get('exports').put('index_opt', var.get('index_opt'))
        var.get('exports').put('rindex', var.get('rindex'))
        var.get('exports').put('rindex_opt', var.get('rindex_opt'))
        var.get('exports').put('index_from', var.get('index_from'))
        var.get('exports').put('index_from_opt', var.get('index_from_opt'))
        var.get('exports').put('rindex_from', var.get('rindex_from'))
        var.get('exports').put('rindex_from_opt', var.get('rindex_from_opt'))
        var.get('exports').put('contains', var.get('contains'))
        var.get('exports').put('contains_from', var.get('contains_from'))
        var.get('exports').put('rcontains_from', var.get('rcontains_from'))
        var.get('exports').put('uppercase', var.get('uppercase'))
        var.get('exports').put('lowercase', var.get('lowercase'))
        var.get('exports').put('capitalize', var.get('capitalize'))
        var.get('exports').put('uncapitalize', var.get('uncapitalize'))
        var.get('exports').put('uppercase_ascii', var.get('uppercase_ascii'))
        var.get('exports').put('lowercase_ascii', var.get('lowercase_ascii'))
        var.get('exports').put('capitalize_ascii', var.get('capitalize_ascii'))
        var.get('exports').put('uncapitalize_ascii', var.get('uncapitalize_ascii'))
        var.get('exports').put('compare', var.get('compare'))
        var.get('exports').put('equal', var.get('equal'))
        var.get('exports').put('split_on_char', var.get('split_on_char'))
    PyJs_anonymous_69_._set_name('anonymous')
    @Js
    def PyJs_anonymous_71_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['make$1', 'Id', 'Id$2', 'cmp$2', 'FocusId', 'exports', 'Belt_Set', '$$Map$1', 'convertParentToChild', 'fromArray', 'convertFocusToChild', 'toString', '$$Set$2', 'fromArray$1', 'make$4', 'convertFocusToParent', 'make$5', 'create$1', 'module', 'Make', 'toString$2', 'toString$1', 'Comparable$2', 'Belt_Id', 'ParentId', 'create', '$$Set$1', 'convertParentToFocus', 'require', '$$Map$2', 'make$2', 'cmp', 'make', 'Belt_Map', 'cmp$1', 'convertChildToFocus', 'Id$1', 'Comparable$1', '$$Map', 'Caml_obj', 'Comparable', 'fromArray$2', 'make$3', '$$Set', 'convertChildToParent', 'ChildId', 'create$2'])
        @Js
        def PyJsHoisted_Make_(PyJsArg_2473746172_, this, arguments, var=var):
            var = Scope({'$star':PyJsArg_2473746172_, 'this':this, 'arguments':arguments}, var)
            var.registers(['make$1', 'toString', 'Id', 'Comparable', 'cmp', '$$Set', 'make', 'fromArray', '$$Map', 'create', '$star'])
            @Js
            def PyJs_anonymous_72_(id, this, arguments, var=var):
                var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
                var.registers(['id'])
                return var.get('id')
            PyJs_anonymous_72_._set_name('anonymous')
            var.put('create', PyJs_anonymous_72_)
            @Js
            def PyJs_anonymous_73_(s, this, arguments, var=var):
                var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
                var.registers(['s'])
                return var.get('s')
            PyJs_anonymous_73_._set_name('anonymous')
            var.put('toString', PyJs_anonymous_73_)
            var.put('Id', Js({'create':var.get('create'),'toString':var.get('toString')}))
            var.put('cmp', var.get('Caml_obj').get('caml_compare'))
            var.put('Comparable', var.get('Belt_Id').callprop('MakeComparable', Js({'cmp':var.get('cmp')})))
            @Js
            def PyJs_anonymous_74_(param, this, arguments, var=var):
                var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                var.registers(['param'])
                return var.get('Belt_Map').callprop('make', var.get('Comparable'))
            PyJs_anonymous_74_._set_name('anonymous')
            var.put('make', PyJs_anonymous_74_)
            var.put('$$Map', Js({'make':var.get('make')}))
            @Js
            def PyJs_anonymous_75_(param, this, arguments, var=var):
                var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
                var.registers(['param'])
                return var.get('Belt_Set').callprop('make', var.get('Comparable'))
            PyJs_anonymous_75_._set_name('anonymous')
            var.put('make$1', PyJs_anonymous_75_)
            @Js
            def PyJs_anonymous_76_(vals, this, arguments, var=var):
                var = Scope({'vals':vals, 'this':this, 'arguments':arguments}, var)
                var.registers(['vals'])
                return var.get('Belt_Set').callprop('fromArray', var.get('vals'), var.get('Comparable'))
            PyJs_anonymous_76_._set_name('anonymous')
            var.put('fromArray', PyJs_anonymous_76_)
            var.put('$$Set', Js({'make':var.get('make$1'),'fromArray':var.get('fromArray')}))
            return Js({'Id':var.get('Id'),'create':var.get('create'),'toString':var.get('toString'),'Comparable':var.get('Comparable'),'$$Map':var.get('$$Map'),'$$Set':var.get('$$Set')})
        PyJsHoisted_Make_.func_name = 'Make'
        var.put('Make', PyJsHoisted_Make_)
        @Js
        def PyJsHoisted_create_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoisted_create_.func_name = 'create'
        var.put('create', PyJsHoisted_create_)
        @Js
        def PyJsHoisted_toString_(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('s')
        PyJsHoisted_toString_.func_name = 'toString'
        var.put('toString', PyJsHoisted_toString_)
        @Js
        def PyJsHoisted_make_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return var.get('Belt_Map').callprop('make', var.get('Comparable'))
        PyJsHoisted_make_.func_name = 'make'
        var.put('make', PyJsHoisted_make_)
        @Js
        def PyJsHoistedNonPyName(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return var.get('Belt_Set').callprop('make', var.get('Comparable'))
        PyJsHoistedNonPyName.func_name = 'make$1'
        var.put('make$1', PyJsHoistedNonPyName)
        @Js
        def PyJsHoisted_fromArray_(vals, this, arguments, var=var):
            var = Scope({'vals':vals, 'this':this, 'arguments':arguments}, var)
            var.registers(['vals'])
            return var.get('Belt_Set').callprop('fromArray', var.get('vals'), var.get('Comparable'))
        PyJsHoisted_fromArray_.func_name = 'fromArray'
        var.put('fromArray', PyJsHoisted_fromArray_)
        @Js
        def PyJsHoistedNonPyName(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoistedNonPyName.func_name = 'create$1'
        var.put('create$1', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('s')
        PyJsHoistedNonPyName.func_name = 'toString$1'
        var.put('toString$1', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return var.get('Belt_Map').callprop('make', var.get('Comparable$1'))
        PyJsHoistedNonPyName.func_name = 'make$2'
        var.put('make$2', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return var.get('Belt_Set').callprop('make', var.get('Comparable$1'))
        PyJsHoistedNonPyName.func_name = 'make$3'
        var.put('make$3', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(vals, this, arguments, var=var):
            var = Scope({'vals':vals, 'this':this, 'arguments':arguments}, var)
            var.registers(['vals'])
            return var.get('Belt_Set').callprop('fromArray', var.get('vals'), var.get('Comparable$1'))
        PyJsHoistedNonPyName.func_name = 'fromArray$1'
        var.put('fromArray$1', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoistedNonPyName.func_name = 'create$2'
        var.put('create$2', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(s, this, arguments, var=var):
            var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['s'])
            return var.get('s')
        PyJsHoistedNonPyName.func_name = 'toString$2'
        var.put('toString$2', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return var.get('Belt_Map').callprop('make', var.get('Comparable$2'))
        PyJsHoistedNonPyName.func_name = 'make$4'
        var.put('make$4', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return var.get('Belt_Set').callprop('make', var.get('Comparable$2'))
        PyJsHoistedNonPyName.func_name = 'make$5'
        var.put('make$5', PyJsHoistedNonPyName)
        @Js
        def PyJsHoistedNonPyName(vals, this, arguments, var=var):
            var = Scope({'vals':vals, 'this':this, 'arguments':arguments}, var)
            var.registers(['vals'])
            return var.get('Belt_Set').callprop('fromArray', var.get('vals'), var.get('Comparable$2'))
        PyJsHoistedNonPyName.func_name = 'fromArray$2'
        var.put('fromArray$2', PyJsHoistedNonPyName)
        @Js
        def PyJsHoisted_convertChildToParent_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoisted_convertChildToParent_.func_name = 'convertChildToParent'
        var.put('convertChildToParent', PyJsHoisted_convertChildToParent_)
        @Js
        def PyJsHoisted_convertParentToChild_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoisted_convertParentToChild_.func_name = 'convertParentToChild'
        var.put('convertParentToChild', PyJsHoisted_convertParentToChild_)
        @Js
        def PyJsHoisted_convertFocusToParent_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoisted_convertFocusToParent_.func_name = 'convertFocusToParent'
        var.put('convertFocusToParent', PyJsHoisted_convertFocusToParent_)
        @Js
        def PyJsHoisted_convertFocusToChild_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoisted_convertFocusToChild_.func_name = 'convertFocusToChild'
        var.put('convertFocusToChild', PyJsHoisted_convertFocusToChild_)
        @Js
        def PyJsHoisted_convertParentToFocus_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoisted_convertParentToFocus_.func_name = 'convertParentToFocus'
        var.put('convertParentToFocus', PyJsHoisted_convertParentToFocus_)
        @Js
        def PyJsHoisted_convertChildToFocus_(id, this, arguments, var=var):
            var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
            var.registers(['id'])
            return var.get('id')
        PyJsHoisted_convertChildToFocus_.func_name = 'convertChildToFocus'
        var.put('convertChildToFocus', PyJsHoisted_convertChildToFocus_)
        Js('use strict')
        var.put('Belt_Id', var.get('require')(Js('bs-platform/lib/js/belt_Id.js')))
        var.put('Belt_Map', var.get('require')(Js('bs-platform/lib/js/belt_Map.js')))
        var.put('Belt_Set', var.get('require')(Js('bs-platform/lib/js/belt_Set.js')))
        var.put('Caml_obj', var.get('require')(Js('bs-platform/lib/js/caml_obj.js')))
        pass
        pass
        pass
        var.put('Id', Js({'create':var.get('create'),'toString':var.get('toString')}))
        var.put('cmp', var.get('Caml_obj').get('caml_compare'))
        var.put('Comparable', var.get('Belt_Id').callprop('MakeComparable', Js({'cmp':var.get('cmp')})))
        pass
        var.put('$$Map', Js({'make':var.get('make')}))
        pass
        pass
        var.put('$$Set', Js({'make':var.get('make$1'),'fromArray':var.get('fromArray')}))
        var.put('FocusId', Js({'Id':var.get('Id'),'create':var.get('create'),'toString':var.get('toString'),'Comparable':var.get('Comparable'),'$$Map':var.get('$$Map'),'$$Set':var.get('$$Set')}))
        pass
        pass
        var.put('Id$1', Js({'create':var.get('create$1'),'toString':var.get('toString$1')}))
        var.put('cmp$1', var.get('Caml_obj').get('caml_compare'))
        var.put('Comparable$1', var.get('Belt_Id').callprop('MakeComparable', Js({'cmp':var.get('cmp$1')})))
        pass
        var.put('$$Map$1', Js({'make':var.get('make$2')}))
        pass
        pass
        var.put('$$Set$1', Js({'make':var.get('make$3'),'fromArray':var.get('fromArray$1')}))
        var.put('ChildId', Js({'Id':var.get('Id$1'),'create':var.get('create$1'),'toString':var.get('toString$1'),'Comparable':var.get('Comparable$1'),'$$Map':var.get('$$Map$1'),'$$Set':var.get('$$Set$1')}))
        pass
        pass
        var.put('Id$2', Js({'create':var.get('create$2'),'toString':var.get('toString$2')}))
        var.put('cmp$2', var.get('Caml_obj').get('caml_compare'))
        var.put('Comparable$2', var.get('Belt_Id').callprop('MakeComparable', Js({'cmp':var.get('cmp$2')})))
        pass
        var.put('$$Map$2', Js({'make':var.get('make$4')}))
        pass
        pass
        var.put('$$Set$2', Js({'make':var.get('make$5'),'fromArray':var.get('fromArray$2')}))
        var.put('ParentId', Js({'Id':var.get('Id$2'),'create':var.get('create$2'),'toString':var.get('toString$2'),'Comparable':var.get('Comparable$2'),'$$Map':var.get('$$Map$2'),'$$Set':var.get('$$Set$2')}))
        pass
        pass
        pass
        pass
        pass
        pass
        var.get('exports').put('Make', var.get('Make'))
        var.get('exports').put('FocusId', var.get('FocusId'))
        var.get('exports').put('ChildId', var.get('ChildId'))
        var.get('exports').put('ParentId', var.get('ParentId'))
        var.get('exports').put('convertChildToParent', var.get('convertChildToParent'))
        var.get('exports').put('convertParentToChild', var.get('convertParentToChild'))
        var.get('exports').put('convertFocusToParent', var.get('convertFocusToParent'))
        var.get('exports').put('convertFocusToChild', var.get('convertFocusToChild'))
        var.get('exports').put('convertParentToFocus', var.get('convertParentToFocus'))
        var.get('exports').put('convertChildToFocus', var.get('convertChildToFocus'))
    PyJs_anonymous_71_._set_name('anonymous')
    @Js
    def PyJs_anonymous_77_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['exports', 'PID', 'require', 'module', 'T', 'Path_immutable$KaroshibeeReTree'])
        Js('use strict')
        var.put('Path_immutable$KaroshibeeReTree', var.get('require')(Js('./paths/Path_immutable.bs.js')))
        var.put('T', Js({'empty':var.get('Path_immutable$KaroshibeeReTree').get('empty'),'size':var.get('Path_immutable$KaroshibeeReTree').get('size'),'fromList':var.get('Path_immutable$KaroshibeeReTree').get('fromList'),'fromPathToRootList':var.get('Path_immutable$KaroshibeeReTree').get('fromPathToRootList'),'fromRootToPathList':var.get('Path_immutable$KaroshibeeReTree').get('fromRootToPathList'),'moveUp':var.get('Path_immutable$KaroshibeeReTree').get('moveUp'),'moveDown':var.get('Path_immutable$KaroshibeeReTree').get('moveDown'),'parent':var.get('Path_immutable$KaroshibeeReTree').get('parent'),'root':var.get('Path_immutable$KaroshibeeReTree').get('root'),'pathToRoot':var.get('Path_immutable$KaroshibeeReTree').get('pathToRoot'),'pathFromRoot':var.get('Path_immutable$KaroshibeeReTree').get('pathFromRoot'),'eq':var.get('Path_immutable$KaroshibeeReTree').get('eq'),'append':var.get('Path_immutable$KaroshibeeReTree').get('append'),'toString':var.get('Path_immutable$KaroshibeeReTree').get('toString'),'removeElement':var.get('Path_immutable$KaroshibeeReTree').get('removeElement'),'concat':var.get('Path_immutable$KaroshibeeReTree').get('concat')}))
        var.put('PID', Js(0.0))
        var.get('exports').put('PID', var.get('PID'))
        var.get('exports').put('T', var.get('T'))
    PyJs_anonymous_77_._set_name('anonymous')
    @Js
    def PyJs_anonymous_78_(require, module, exports, this, arguments, var=var):
        var = Scope({'require':require, 'module':module, 'exports':exports, 'this':this, 'arguments':arguments}, var)
        var.registers(['$$String', 'exports', 'parent', 'Caml_option', 'empty', 'removeElement', 'toString', 'PID', 'fromList', 'fromRootToPathList', 'module', 'pathToRoot', 'size', 'moveUp', 'eq', 'require', 'root', 'Identity$KaroshibeeReTree', 'append', 'fromPathToRootList', 'Caml_obj', 'pathFromRoot', 'moveDown', 'Belt_Option', 'concat', 'Belt_List'])
        @Js
        def PyJsHoisted_empty_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param'])
            return Js({'pathUp':Js(0.0)})
        PyJsHoisted_empty_.func_name = 'empty'
        var.put('empty', PyJsHoisted_empty_)
        @Js
        def PyJsHoisted_size_(path, this, arguments, var=var):
            var = Scope({'path':path, 'this':this, 'arguments':arguments}, var)
            var.registers(['path'])
            return var.get('Belt_List').callprop('size', var.get('path').get('pathUp'))
        PyJsHoisted_size_.func_name = 'size'
        var.put('size', PyJsHoisted_size_)
        @Js
        def PyJsHoisted_fromList_(path, this, arguments, var=var):
            var = Scope({'path':path, 'this':this, 'arguments':arguments}, var)
            var.registers(['path'])
            @Js
            def PyJs_anonymous_79_(s, this, arguments, var=var):
                var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
                var.registers(['s'])
                return var.get('Identity$KaroshibeeReTree').get('ParentId').callprop('create', var.get('s'))
            PyJs_anonymous_79_._set_name('anonymous')
            return Js({'pathUp':var.get('Belt_List').callprop('map', var.get('path'), PyJs_anonymous_79_)})
        PyJsHoisted_fromList_.func_name = 'fromList'
        var.put('fromList', PyJsHoisted_fromList_)
        @Js
        def PyJsHoisted_fromRootToPathList_(path, this, arguments, var=var):
            var = Scope({'path':path, 'this':this, 'arguments':arguments}, var)
            var.registers(['path'])
            return var.get('fromList')(var.get('Belt_List').callprop('reverse', var.get('path')))
        PyJsHoisted_fromRootToPathList_.func_name = 'fromRootToPathList'
        var.put('fromRootToPathList', PyJsHoisted_fromRootToPathList_)
        @Js
        def PyJsHoisted_moveUp_(parents, this, arguments, var=var):
            var = Scope({'parents':parents, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'parents'])
            var.put('match', var.get('parents').get('pathUp'))
            return Js({'pathUp':(var.get('match').get('1') if var.get('match') else Js(0.0))})
        PyJsHoisted_moveUp_.func_name = 'moveUp'
        var.put('moveUp', PyJsHoisted_moveUp_)
        @Js
        def PyJsHoisted_moveDown_(parents, this, arguments, var=var):
            var = Scope({'parents':parents, 'this':this, 'arguments':arguments}, var)
            var.registers(['parents', 'n'])
            var.put('n', var.get('Belt_List').callprop('size', var.get('parents').get('pathUp')))
            return Js({'pathUp':var.get('Belt_Option').callprop('getWithDefault', var.get('Belt_List').callprop('take', var.get('parents').get('pathUp'), ((var.get('n')-Js(1.0))|Js(0.0))), Js(0.0))})
        PyJsHoisted_moveDown_.func_name = 'moveDown'
        var.put('moveDown', PyJsHoisted_moveDown_)
        @Js
        def PyJsHoisted_parent_(parents, this, arguments, var=var):
            var = Scope({'parents':parents, 'this':this, 'arguments':arguments}, var)
            var.registers(['match', 'parents'])
            var.put('match', var.get('parents').get('pathUp'))
            if var.get('match'):
                return var.get('Caml_option').callprop('some', var.get('match').get('0'))
        PyJsHoisted_parent_.func_name = 'parent'
        var.put('parent', PyJsHoisted_parent_)
        @Js
        def PyJsHoisted_root_(parents, this, arguments, var=var):
            var = Scope({'parents':parents, 'this':this, 'arguments':arguments}, var)
            var.registers(['parents', 'n'])
            var.put('n', var.get('Belt_List').callprop('size', var.get('parents').get('pathUp')))
            return var.get('Belt_List').callprop('get', var.get('parents').get('pathUp'), ((var.get('n')-Js(1.0))|Js(0.0)))
        PyJsHoisted_root_.func_name = 'root'
        var.put('root', PyJsHoisted_root_)
        @Js
        def PyJsHoisted_pathToRoot_(parents, this, arguments, var=var):
            var = Scope({'parents':parents, 'this':this, 'arguments':arguments}, var)
            var.registers(['parents'])
            return var.get('parents').get('pathUp')
        PyJsHoisted_pathToRoot_.func_name = 'pathToRoot'
        var.put('pathToRoot', PyJsHoisted_pathToRoot_)
        @Js
        def PyJsHoisted_pathFromRoot_(parents, this, arguments, var=var):
            var = Scope({'parents':parents, 'this':this, 'arguments':arguments}, var)
            var.registers(['parents'])
            return var.get('Belt_List').callprop('reverse', var.get('parents').get('pathUp'))
        PyJsHoisted_pathFromRoot_.func_name = 'pathFromRoot'
        var.put('pathFromRoot', PyJsHoisted_pathFromRoot_)
        @Js
        def PyJsHoisted_eq_(p1, p2, this, arguments, var=var):
            var = Scope({'p1':p1, 'p2':p2, 'this':this, 'arguments':arguments}, var)
            var.registers(['p2', 'p1'])
            return var.get('Belt_List').callprop('eq', var.get('p1').get('pathUp'), var.get('p2').get('pathUp'), var.get('Caml_obj').get('caml_equal'))
        PyJsHoisted_eq_.func_name = 'eq'
        var.put('eq', PyJsHoisted_eq_)
        @Js
        def PyJsHoisted_append_(parents, el, this, arguments, var=var):
            var = Scope({'parents':parents, 'el':el, 'this':this, 'arguments':arguments}, var)
            var.registers(['el', 'parents'])
            return Js({'pathUp':Js([var.get('el'), var.get('parents').get('pathUp')])})
        PyJsHoisted_append_.func_name = 'append'
        var.put('append', PyJsHoisted_append_)
        @Js
        def PyJsHoisted_toString_(parents, this, arguments, var=var):
            var = Scope({'parents':parents, 'this':this, 'arguments':arguments}, var)
            var.registers(['parents'])
            @Js
            def PyJs_anonymous_80_(p, this, arguments, var=var):
                var = Scope({'p':p, 'this':this, 'arguments':arguments}, var)
                var.registers(['p'])
                return var.get('Identity$KaroshibeeReTree').get('ParentId').callprop('toString', var.get('p'))
            PyJs_anonymous_80_._set_name('anonymous')
            return var.get('$$String').callprop('concat', Js(','), var.get('Belt_List').callprop('map', var.get('parents').get('pathUp'), PyJs_anonymous_80_))
        PyJsHoisted_toString_.func_name = 'toString'
        var.put('toString', PyJsHoisted_toString_)
        @Js
        def PyJsHoisted_removeElement_(parents, el, this, arguments, var=var):
            var = Scope({'parents':parents, 'el':el, 'this':this, 'arguments':arguments}, var)
            var.registers(['el', 'parents'])
            @Js
            def PyJs_anonymous_81_(pid, this, arguments, var=var):
                var = Scope({'pid':pid, 'this':this, 'arguments':arguments}, var)
                var.registers(['pid'])
                return var.get('Caml_obj').callprop('caml_notequal', var.get('pid'), var.get('el'))
            PyJs_anonymous_81_._set_name('anonymous')
            return Js({'pathUp':var.get('Belt_List').callprop('keep', var.get('parents').get('pathUp'), PyJs_anonymous_81_)})
        PyJsHoisted_removeElement_.func_name = 'removeElement'
        var.put('removeElement', PyJsHoisted_removeElement_)
        @Js
        def PyJsHoisted_concat_(parents, other, this, arguments, var=var):
            var = Scope({'parents':parents, 'other':other, 'this':this, 'arguments':arguments}, var)
            var.registers(['other', 'parents'])
            return Js({'pathUp':var.get('Belt_List').callprop('concat', var.get('parents').get('pathUp'), var.get('other').get('pathUp'))})
        PyJsHoisted_concat_.func_name = 'concat'
        var.put('concat', PyJsHoisted_concat_)
        Js('use strict')
        var.put('$$String', var.get('require')(Js('bs-platform/lib/js/string.js')))
        var.put('Caml_obj', var.get('require')(Js('bs-platform/lib/js/caml_obj.js')))
        var.put('Belt_List', var.get('require')(Js('bs-platform/lib/js/belt_List.js')))
        var.put('Belt_Option', var.get('require')(Js('bs-platform/lib/js/belt_Option.js')))
        var.put('Caml_option', var.get('require')(Js('bs-platform/lib/js/caml_option.js')))
        var.put('Identity$KaroshibeeReTree', var.get('require')(Js('../Identity.bs.js')))
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        var.put('PID', Js(0.0))
        var.put('fromPathToRootList', var.get('fromList'))
        var.get('exports').put('PID', var.get('PID'))
        var.get('exports').put('empty', var.get('empty'))
        var.get('exports').put('size', var.get('size'))
        var.get('exports').put('fromList', var.get('fromList'))
        var.get('exports').put('fromPathToRootList', var.get('fromPathToRootList'))
        var.get('exports').put('fromRootToPathList', var.get('fromRootToPathList'))
        var.get('exports').put('moveUp', var.get('moveUp'))
        var.get('exports').put('moveDown', var.get('moveDown'))
        var.get('exports').put('parent', var.get('parent'))
        var.get('exports').put('root', var.get('root'))
        var.get('exports').put('pathToRoot', var.get('pathToRoot'))
        var.get('exports').put('pathFromRoot', var.get('pathFromRoot'))
        var.get('exports').put('eq', var.get('eq'))
        var.get('exports').put('append', var.get('append'))
        var.get('exports').put('toString', var.get('toString'))
        var.get('exports').put('removeElement', var.get('removeElement'))
        var.get('exports').put('concat', var.get('concat'))
    PyJs_anonymous_78_._set_name('anonymous')
    @Js
    def PyJs_anonymous_82_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['r'])
        @Js
        def PyJsHoisted_r_(e, n, t, this, arguments, var=var):
            var = Scope({'e':e, 'n':n, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't', 'o', 'u', 'n', 'i'])
            @Js
            def PyJsHoisted_o_(i, f, this, arguments, var=var):
                var = Scope({'i':i, 'f':f, 'this':this, 'arguments':arguments}, var)
                var.registers(['f', 'c', 'a', 'i', 'p'])
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
                    def PyJs_anonymous_83_(r, this, arguments, var=var):
                        var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                        var.registers(['r', 'n'])
                        var.put('n', var.get('e').get(var.get('i')).get('1').get(var.get('r')))
                        return var.get('o')((var.get('n') or var.get('r')))
                    PyJs_anonymous_83_._set_name('anonymous')
                    var.get('e').get(var.get('i')).get('0').callprop('call', var.get('p').get('exports'), PyJs_anonymous_83_, var.get('p'), var.get('p').get('exports'), var.get('r'), var.get('e'), var.get('n'), var.get('t'))
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
    PyJs_anonymous_82_._set_name('anonymous')
    return PyJs_anonymous_82_()(Js({'1':Js([PyJs_anonymous_0_, Js({'./caml_option.js':Js(18.0),'./caml_primitive.js':Js(19.0),'./curry.js':Js(21.0),'./js_math.js':Js(23.0)})]),'2':Js([PyJs_anonymous_1_, Js({'./curry.js':Js(21.0)})]),'3':Js([PyJs_anonymous_2_, Js({'./belt_Array.js':Js(1.0),'./belt_SortArray.js':Js(9.0),'./caml_option.js':Js(18.0),'./curry.js':Js(21.0)})]),'4':Js([PyJs_anonymous_3_, Js({'./belt_MapDict.js':Js(5.0),'./curry.js':Js(21.0)})]),'5':Js([PyJs_anonymous_4_, Js({'./belt_internalAVLtree.js':Js(11.0),'./caml_option.js':Js(18.0),'./curry.js':Js(21.0)})]),'6':Js([PyJs_anonymous_7_, Js({'./caml_option.js':Js(18.0),'./curry.js':Js(21.0)})]),'7':Js([PyJs_anonymous_8_, Js({'./belt_SetDict.js':Js(8.0),'./curry.js':Js(21.0)})]),'8':Js([PyJs_anonymous_9_, Js({'./belt_internalAVLset.js':Js(10.0)})]),'9':Js([PyJs_anonymous_10_, Js({'./belt_Array.js':Js(1.0),'./curry.js':Js(21.0)})]),'10':Js([PyJs_anonymous_11_, Js({'./belt_SortArray.js':Js(9.0),'./caml_option.js':Js(18.0),'./curry.js':Js(21.0)})]),'11':Js([PyJs_anonymous_13_, Js({'./belt_SortArray.js':Js(9.0),'./caml_option.js':Js(18.0),'./curry.js':Js(21.0)})]),'12':Js([PyJs_anonymous_15_, Js({})]),'13':Js([PyJs_anonymous_16_, Js({'./caml_builtin_exceptions.js':Js(15.0),'./caml_bytes.js':Js(16.0),'./caml_primitive.js':Js(19.0),'./char.js':Js(20.0),'./curry.js':Js(21.0)})]),'14':Js([PyJs_anonymous_17_, Js({'./caml_builtin_exceptions.js':Js(15.0)})]),'15':Js([PyJs_anonymous_18_, Js({})]),'16':Js([PyJs_anonymous_19_, Js({'./caml_builtin_exceptions.js':Js(15.0)})]),'17':Js([PyJs_anonymous_20_, Js({'./block.js':Js(12.0),'./caml_builtin_exceptions.js':Js(15.0),'./caml_primitive.js':Js(19.0)})]),'18':Js([PyJs_anonymous_32_, Js({})]),'19':Js([PyJs_anonymous_33_, Js({})]),'20':Js([PyJs_anonymous_34_, Js({'./caml_builtin_exceptions.js':Js(15.0),'./caml_bytes.js':Js(16.0)})]),'21':Js([PyJs_anonymous_35_, Js({'./caml_array.js':Js(14.0)})]),'22':Js([PyJs_anonymous_67_, Js({})]),'23':Js([PyJs_anonymous_68_, Js({'./js_int.js':Js(22.0)})]),'24':Js([PyJs_anonymous_69_, Js({'./bytes.js':Js(13.0),'./caml_builtin_exceptions.js':Js(15.0),'./caml_bytes.js':Js(16.0),'./caml_primitive.js':Js(19.0),'./curry.js':Js(21.0)})]),'25':Js([PyJs_anonymous_71_, Js({'bs-platform/lib/js/belt_Id.js':Js(2.0),'bs-platform/lib/js/belt_Map.js':Js(4.0),'bs-platform/lib/js/belt_Set.js':Js(7.0),'bs-platform/lib/js/caml_obj.js':Js(17.0)})]),'26':Js([PyJs_anonymous_77_, Js({'./paths/Path_immutable.bs.js':Js(27.0)})]),'27':Js([PyJs_anonymous_78_, Js({'../Identity.bs.js':Js(25.0),'bs-platform/lib/js/belt_List.js':Js(3.0),'bs-platform/lib/js/belt_Option.js':Js(6.0),'bs-platform/lib/js/caml_obj.js':Js(17.0),'bs-platform/lib/js/caml_option.js':Js(18.0),'bs-platform/lib/js/string.js':Js(24.0)})])}), Js({}), Js([Js(26.0)]))
PyJs_LONG_84_()
pass


# Add lib to the module scope
Path = var.to_python()