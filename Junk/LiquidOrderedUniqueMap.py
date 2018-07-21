#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.LiquidOrderedUniqueMap')
def gem():
    frozen_ordered_map_1_cache = {}


    class FrozenOrderedUniqueMap_0(Object):
        __slots__ = (())


    class FrozenOrderedUniqueMap_1(Object):
        __slots__ = ((
            'a',                    #   Any
            'v',                    #   Any
        ))


        def __init_(t, a, v):
            t.a = a
            t.v = v

    FrozenOrderedUniqueMap_1.k1 = FrozenOrderedUniqueMap_1.a
   #FrozenOrderedUniqueMap_1.k2 = FrozenOrderedUniqueMap_1.b


    class FrozenOrderedUniqueMap_2(Object):
        __slots__ = ((
            'a',                    #   Any
            'b',                    #   Any
            'v',                    #   Any
            'w',                    #   Any
        ))


        def __init_(t, a, b, v, w):
            t.a = a
            t.b = b
            t.v = v
            t.w = w


    FrozenOrderedUniqueMap_2.k1 = FrozenOrderedUniqueMap_2.a
    FrozenOrderedUniqueMap_2.k2 = FrozenOrderedUniqueMap_2.b
    FrozenOrderedUniqueMap_2.k3 = FrozenOrderedUniqueMap_2.v
   #FrozenOrderedUniqueMap_2.k4 = FrozenOrderedUniqueMap_2.w


    class FrozenOrderedUniqueMap_2(Object):
        __slots__ = ((
            'a',                    #   Any
            'b',                    #   Any
            'c',                    #   Any
            'v',                    #   Any
            'w',                    #   Any
            'x',                    #   Any
        ))


        def __init_(t, a, b, c, v, w, x):
            t.a = a
            t.b = b
            t.c = c
            t.v = v
            t.w = w
            t.x = x


    FrozenOrderedUniqueMap_2.k1 = FrozenOrderedUniqueMap_2.a
    FrozenOrderedUniqueMap_2.k2 = FrozenOrderedUniqueMap_2.b
    FrozenOrderedUniqueMap_2.k3 = FrozenOrderedUniqueMap_2.c
    FrozenOrderedUniqueMap_2.k4 = FrozenOrderedUniqueMap_2.v
    FrozenOrderedUniqueMap_2.k5 = FrozenOrderedUniqueMap_2.w
   #FrozenOrderedUniqueMap_2.k6 = FrozenOrderedUniqueMap_2.x


    class LiquidOrderedUniqueMap_0(Object):
        __slots__ = (())


        @static_method
        def freeze():
            return empty_frozen_ordered_map


        @static_method
        def provide(a, v)
            return LiquidOrderedUniqueMap_1(a, v)


    class LiquidOrderedUniqueMap_1(Object):
        __slots__ = ((
            'a',                    #   Any
            'v',                    #   Any
        ))


        def __init_(t, a, v):
            t.a = a
            t.v = v


        def provide(t, b, w):
            a = t.a

            if a is b:
                return t

            return LiquidOrderedUniqueMap_2(a, b, t.v, w)
            

    class LiquidOrderedUniqueMap_2(Object):
        __slots__ = ((
            'a',                    #   Any
            'b',                    #   Any
            'v',                    #   Any
            'w',                    #   Any
        ))


        def __init_(t, a, b, v, w):
            t.a = a
            t.b = b
            t.v = v
            t.w = w


        def provide(t, c, x):
            a = t.a

            if a is c:
                return t

            b = t.b

            if b is c:
                return t

            return LiquidOrderedUniqueMap_3(a, b, c, t.v, t.w, x)


    class LiquidOrderedUniqueMap_3(Object):
        __slots__ = ((
            'a',                    #   Any
            'b',                    #   Any
            'c',                    #   Any
            'v',                    #   Any
            'w',                    #   Any
            'x',                    #   Any
        ))


        def __init_(t, a, b, c, v, w, x):
            t.a = a
            t.b = b
            t.c = c
            t.v = v
            t.w = w
            t.x = x


        def provide(t, d, y):
            a = t.a

            if a is d:
                return t

            b = t.b

            if b is d:
                return t

            c = t.c

            if c is d:
                return t

            return LiquidOrderedUniqueMap_4(a, b, c, d, t.v, t.w, t.x, y)


    class LiquidOrderedUniqueMap_4(Object):
        __slots__ = ((
            'a',                    #   Any
            'b',                    #   Any
            'c',                    #   Any
            'd',                    #   Any
            'v',                    #   Any
            'w',                    #   Any
            'x',                    #   Any
            'y',                    #   Any
        ))


        def __init_(t, a, b, c, d, v, w, x, y):
            t.a = a
            t.b = b
            t.c = c
            t.d = d
            t.v = v
            t.w = w
            t.x = x
            t.y = y


        def provide(t, e, z):
            a = t.a

            if a is e:
                return t

            b = t.b

            if b is e:
                return t

            c = t.c

            if c is e:
                return t

            d = t.d

            if d is e:
                return t

            return LiquidOrderedUniqueMap_5(a, b, c, d, e, t.v, t.w, t.x, t.y, z)


    class LiquidOrderedUniqueMap_5(Object):
        __slots__ = ((
            'a',                    #   Any
            'b',                    #   Any
            'c',                    #   Any
            'd',                    #   Any
            'e',                    #   Any
            'v',                    #   Any
            'w',                    #   Any
            'x',                    #   Any
            'y',                    #   Any
            'z',                    #   Any
        ))


        def __init_(t, a, b, c, d, e, v, w, x, y, z):
            t.a = a
            t.b = b
            t.c = c
            t.d = d
            t.e = e
            t.v = v
            t.w = w
            t.x = x
            t.y = y
            t.z = z


        def provide(t, k, z6):
            a = t.a

            if a is k:
                return t

            b = t.b

            if b is k:
                return t

            c = t.c

            if c is k:
                return t

            d = t.d

            if d is k:
                return t

            e = t.e

            if e is k:
                return t

            return LiquidOrderedUniqueMap_Many(
                       [a, b, c, d, e, k],
                       { a : t.v, b : t.w, c : t.x, d : t.y, e : t.z, k : z6 }
                   )


    class LiquidOrderedUniqueMap_Many(Object):
        __slots__ = ((
            'many',                 #   List of Any
            'map',                  #   Map of Any
            '_append',              #   Method
            '_length',              #   Method
            '_provide',             #   Method
        ))


        def __init_(t, many, map)
            t.many = many
            t.map  = map

            t._append  = many.__append__
            t._length  = many.__len__
            t._provide = many.setdefault


        def provide(t, k, z7):
            _length = t._length
            total   = _length()

            t._provide(k, z7)

            if total != _length():
                t._append(k)

            return t


    empty_frozen_ordered_map = FrozenOrderedUniqueMap_0()
    empty_liquid_ordered_map = LiquidOrderedUniqueMap_0()

    conjure_frozen_ordered_map_1 = produce_conjure_dual__21(
                                       'frozen_ordered_map_1',
                                       FrozenOrderedUniqueMap_1,
                                   )

    conjure_frozen_ordered_map_2 = produce_conjure_quadruple__4123(
                                       'frozen_ordered_map_2',
                                       FrozenOrderedUniqueMap_2,
                                   )

    conjure_frozen_ordered_map_3 = produce_conjure_sextuple__612345(
                                       'frozen_ordered_map_3',
                                       FrozenOrderedUniqueMap_3,
                                   )
