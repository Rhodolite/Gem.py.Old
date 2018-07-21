#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Gem.Horde')
def gem():
    #
    #   Horde:
    #
    #       Liquid (modifiable)
    #       Map (Associative Array)
    #       Unordered
    #       Key must not include absent
    #
    #   .inject
    #   .lookup
    #   .provide
    #       Use == for comparing keys
    #
    #       All the verbs here do NOT have an 'is' inside them.
    #
    #   .glimpse
    #   .insert
    #   .provision
    #       Unique Keys: Use 'is' for comparing keys
    #
    #       NOTE: All the verbs here have an 'is' inside them.
    #


    map__lookup  = Map.get
    map__provide = Map.setdefault
    map__store   = Map.__setitem__


    class Horde_0(Object):
        __slots__ = (())


        is_horde = true
        k1       = absent
        k2       = absent


        @static_method
        def glimpse(k):
            return none


        @static_method
        def items_sorted_by_key():
            return (())


        lookup = glimpse



    class Horde_1(Object):
        __slots__ = ((
            'a',                        #   Any
            'v',                        #   Any
        ))


        is_horde = true
        k1       = absent
        k2       = absent


        def __init__(t, a, v):
            assert a is not absent

            t.a = a
            t.v = v


        if 0:
            def glimpse(t, k):
                if t.a is k: return t.v

                assert k is not absent

                return none


            def inject(t, b, w):
                assert t.a != b

                return Horde_23(t.a, b, t.v, w)


        def items_sorted_by_key(t):
            return (( ((t.a, t.v)), ))


        if 0:
            def lookup(t, k):
                if t.a == k: return t.v

                assert k is not absent

                return none


            def insert(t, b, w):
                assert t.a is not b

                return Horde_23(t.a, b, t.v, w)


            def provide(t, b, w):
                a = t.a
                if a == b: return t

                return Horde_23(a, b, t.v, w)


        def provision(t, b, w):
            a = t.a
            if a is b: return t

            return Horde_23(a, b, t.v, w)


    class Horde_23(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Absent | Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Vacant | Any
        ))


        is_horde = true
        k1       = absent
        k2       = absent


        def __init__(t, a, b, v, w):
            assert (a is not b) and (a is not absent) and (b is not absent)

            t.a = a
            t.b = b
            t.c = absent
            t.v = v
            t.w = w


        if 0:
            def glimpse(t, k):
                if t.a is k: return t.v
                if t.b is k: return t.w

                assert k is not absent

                if t.c is k: return t.x

                return none


            def inject(t, d, y):
                assert (t.a != d) and (t.b != d) and (t.c != d)

                c = t.c

                if c is absent:
                    t.c = d
                    t.x = y
                    return t

                return create_horde_4567(t.a, t.b, c, d, t.v, t.w, t.x, y)


            def insert(t, d, y):
                assert (t.a is not d) and (t.b is not d) and (t.c is not d)

                c = t.c

                if c is absent:
                    t.c = d
                    t.x = y
                    return t

                return create_horde_4567(t.a, t.b, c, d, t.v, t.w, t.x, y)


        def items_sorted_by_key(t):
            a = t.a
            b = t.b
            c = t.c

            nub = a.nub

            av = ((a, t.v))
            bw = ((b, t.w))
            ka = nub(a)
            kb = nub(b)


            if c is absent:
                if ka < kb:
                    return ((av, bw))

                return ((bw, av))

            cx = ((c, t.x))
            kc = nub(c)

            if ka < kb:
                if kb < kc:
                    return ((av, bw, cx))

                if ka < kc:
                    return ((av, cx, bw))

                return ((cx, av, bw))

            if ka < kc:
                return ((bw, av, cx))

            if kb < kc:
                return ((bw, cx, av))

            return ((cx, bw, av))


        if 0:
            def lookup(t, k):
                if t.a == k: return t.v
                if t.b == k: return t.w

                assert k is not absent

                if t.c == k: return t.x

                return none


            def provide(t, d, y):
                a = t.a
                if a == d: return t

                b = t.b
                if b == d: return t

                c = t.c
                if c == d: return t

                assert d is not absent

                if c is absent:
                    t.c = d
                    t.x = y
                    return t

                return create_horde_4567(a, b, c, d, t.v, t.w, t.x, y)


        def provision(t, d, y):
            a = t.a
            if a is d: return t

            b = t.b
            if b is d: return t

            c = t.c
            if c is d: return t

            assert d is not absent

            if c is absent:
                t.c = d
                t.x = y
                return t

            return create_horde_4567(a, b, c, d, t.v, t.w, t.x, y)


        def provision_dual_k1(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1: return t.v

            b = t.b
            if b is k1: return t.w

            c = t.c
            if c is k1: return t.x

            r = Meta(k1, k2)

            if c is absent:
                t.c = k1
                t.x = r
                return r

            displace(k2, create_horde_4567(a, b, c, k1, t.v, t.w, t.x, r))

            return r


        def provision_dual_k2(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2: return t.v

            b = t.b
            if b is k2: return t.w

            c = t.c
            if c is k2: return t.x

            r = Meta(k1, k2)

            if c is absent:
                t.c = k2
                t.x = r
                return r

            displace(k1, create_horde_4567(a, b, c, k2, t.v, t.w, t.x, r))

            return r


    class Horde_4567(Object):
        __slots__ = ((
            'a',                        #   Any
            'b',                        #   Any
            'c',                        #   Any
            'd',                        #   Any
            'e',                        #   Absent | Any
            'e6',                       #   Absent | Vacant | Any
            'e7',                       #   Absent | Vacant | Any
            'v',                        #   Any
            'w',                        #   Any
            'x',                        #   Any
            'y',                        #   Any
            'z',                        #   Any
            'z6',                       #   Any
            'z7',                       #   Any
        ))


        is_horde = true
        k1       = absent
        k2       = absent


        if 0:
            def glimpse(t, k):
                if t.a is k:        return t.v
                if t.b is k:        return t.w
                if t.c is k:        return t.x
                if t.d is k:        return t.y

                assert k is not absent

                e = t.e
                if e is k:          return t.z
                if e is absent:     return none

                e6 = t.e6
                if e6 is k:         return t.z6
                if e6 is absent:    return none

                if t.e7 is k:       return t.z7

                return none


            def inject(t, e8, z8):
                assert (t.a != e8) and (t.b != e8) and (t.c != e8) and (t.d != e8)
                assert e8 is not absent

                e = t.e
                if e is absent:
                    t.e  = e8
                    t.z  = z8
                    t.e6 = absent
                    return t
                assert t.e != e8

                e6 = t.e6
                if e6 is absent:
                    t.e6 = e8
                    t.z6 = z8
                    t.e7 = absent
                    return t
                assert t.e6 != e8

                e7 = t.e7
                if e7 is absent:
                    t.e7 = e8
                    t.z7 = z8
                    t.e8 = absent
                    return t
                assert t.e7 != e8

                return create_horde_many(t.a, t.b, t.c, t.d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


            def insert(t, e8, z8):
                assert (t.a is not e8) and (t.b is not e8) and (t.c is not e8) and (t.d is not e8)
                assert e8 is not absent

                e = t.e
                if e is absent:
                    t.e  = e8
                    t.z  = z8
                    t.e6 = absent
                    return t
                assert t.e is not e8

                e6 = t.e6
                if e6 is absent:
                    t.e6 = e8
                    t.z6 = z8
                    t.e7 = absent
                    return t
                assert t.e6 is not e8

                e7 = t.e7
                if e7 is absent:
                    t.e7 = e8
                    t.z7 = z8
                    return t
                assert t.e7 is not e8

                return create_horde_many(t.a, t.b, t.c, t.d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def items_sorted_by_key(t):
            a   = t.a
            nub = a.nub

            r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y))]

            e = t.e

            if e is absent:
                r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y))]
            else:
                r = [((a, t.v)), ((t.b, t.w)), ((t.c, t.x)), ((t.d, t.y))]

                r.append( ((e, t.z)) )

                e6 = t.e6

                if e6 is not absent:
                    r.append( ((e6, t.z6)) )

                    e7 = t.e7

                    if e7 is not absent:
                        r.append( ((e7, t.z7)) )


            if nub is 0:
                def key(pair):
                    return pair[0]
            else:
                def key(pair):
                    return nub(pair[0])


            return sorted_list(r, key = key)


        if 0:
            def lookup(t, k):
                if t.a == k:        return t.v
                if t.b == k:        return t.w
                if t.c == k:        return t.x
                if t.d == k:        return t.y

                assert k is not absent

                e = t.e
                if e == k:          return t.z
                if e is absent:     return none

                e6 = t.e6
                if e6 == k:         return t.z6
                if e6 is absent:    return none

                if t.e7 == k:       return t.z7

                return none


            def provide(t, e8, z8):
                a = t.a
                if a == e8: return t

                b = t.b
                if b == e8: return t

                c = t.c
                if c == e8: return t

                d = t.d
                if d == e8: return t

                assert e8 is not absent

                e = t.e
                if e == e8: return t
                if e is absent:
                    t.e  = e8
                    t.z  = z8
                    t.e6 = absent
                    return t

                e6 = t.e6
                if e6 == e8: return t
                if e6 is absent:
                    t.e6 = e8
                    t.z6 = z8
                    t.e7 = absent
                    return t

                e7 = t.e7
                if e7 == e8: return t
                if e7 is absent:
                    t.e7 = e8
                    t.z7 = z8
                    return t

                return create_horde_many(a, b, c, d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def provision(t, e8, z8):
            a = t.a
            if a is e8: return t

            b = t.b
            if b is e8: return t

            c = t.c
            if c is e8: return t

            d = t.d
            if d is e8: return t

            assert e8 is not absent

            e = t.e
            if e is e8: return t
            if e is absent:
                t.e  = e8
                t.z  = z8
                t.e6 = absent
                return t

            e6 = t.e6
            if e6 is e8: return t
            if e6 is absent:
                t.e6 = e8
                t.z6 = z8
                t.e7 = absent
                return t

            e7 = t.e7
            if e7 is e8: return t
            if e7 is absent:
                t.e7 = e8
                t.z7 = z8
                return t

            return create_horde_many(a, b, c, d, e, e6, e7, e8, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, z8)


        def provision_dual_k1(t, displace, Meta, k1, k2):
            a = t.a
            if a is k1:     return t.v

            b = t.b
            if b is k1:     return t.w

            c = t.c
            if c is k1:     return t.x

            d = t.d
            if d is k1:     return t.y

            e = t.e
            if e is k1:     return t.z
            if e is absent:
                t.e  = k1
                t.e6 = absent
                t.z  = r = Meta(k1, k2)
                return r

            e6 = t.e6
            if e6 is k1:    return t.z6
            if e6 is absent:
                t.e6 = k1
                t.e7 = absent
                t.z6 = r = Meta(k1, k2)
                return r

            e7 = t.e7
            if e7 is k1:    return t.z7

            r = Meta(k1, k2)

            if e7 is absent:
                t.e7 = k1
                t.z7 = Meta(k1, k2)
                return r

            displace(k2, create_horde_many(a, b, c, d, e, e6, e7, k1, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


        def provision_dual_k2(t, displace, Meta, k1, k2):
            a = t.a
            if a is k2:     return t.v

            b = t.b
            if b is k2:     return t.w

            c = t.c
            if c is k2:     return t.x

            d = t.d
            if d is k2:     return t.y

            e = t.e
            if e is k2:     return t.z
            if e is absent:
                t.e  = k2
                t.e6 = absent
                t.z  = r = Meta(k1, k2)
                return r

            e6 = t.e6
            if e6 is k2:    return t.z6
            if e6 is absent:
                t.e6 = k2
                t.e7 = absent
                t.z6 = r = Meta(k1, k2)
                return r

            e7 = t.e7
            if e7 is k2:    return t.z7

            r = Meta(k1, k2)

            if e7 is absent:
                t.e7 = k2
                t.z7 = Meta(k1, k2)
                return r

            displace(k1, create_horde_many(a, b, c, d, e, e6, e7, k2, t.v, t.w, t.x, t.y, t.z, t.z6, t.z7, r))

            return r


    class Horde_Many(Map):
        __slots__ = (())


        is_horde = true
        k1       = absent
        k2       = absent


        glimpse = map__lookup
        lookup  = map__lookup


        def inject(t, k, v):
            assert map__lookup(t, k) is none

            map__store(t, k, v)
            return t


        insert = inject


        if is_python_2:
            def items_sorted_by_key(t):
                keys  = t.keys()
                value = t.__getitem__

                for k in sorted_list(keys, key = keys[0].nub):
                    yield (( k, value(k) ))
        else:
            def items_sorted_by_key(t):
                keys  = List(t.keys())
                value = t.__getitem__

                for k in sorted_list(keys, key = keys[0].nub):
                    yield (( k, value(k) ))


        if 0:
            def provide(t, k, v):
                map__provide(t, k, v)
                return t


        def provision(t, k, v):
            map__provide(t, k, v)
            return t


        def provision_dual_k1(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k1)) or (map__provide(t, k1, Meta(k1, k2)))


        def provision_dual_k2(t, _displace, Meta, k1, k2):
            return (map__lookup(t, k2)) or (map__provide(t, k2, Meta(k1, k2)))


    empty_horde = Horde_0()


    new_Horde_1    = Method(Object.__new__, Horde_1)
    new_Horde_23   = Method(Object.__new__, Horde_23)
    new_Horde_4567 = Method(Object.__new__, Horde_4567)
    new_Horde_Many = Method(Map   .__new__, Horde_Many)


    def create_horde_1(a, v):
        assert a is not absent

        t = new_Horde_1()

        t.a = a
        t.v = v

        return t


    @export
    def create_horde_23(a, b, v, w):
        assert (a is not absent) and (a is not b) and (b is not absent)

        t = new_Horde_23()

        t.a = a
        t.b = b
        t.c = absent
        t.v = v
        t.w = w

        return t


    def create_horde_4567(a, b, c, d, v, w, x, y):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d)
        assert (b is not absent) and (b is not c) and (b is not d)
        assert (c is not absent) and (c is not d)
        assert d is not absent

        t = new_Horde_4567()

        t.a = a
        t.b = b
        t.c = c
        t.d = d
        t.e = absent
        t.v = v
        t.w = w
        t.x = x
        t.y = y

        return t


    def create_horde_many(a, b, c, d, e, e6, e7, e8, v, w, x, y, z, z6, z7, z8):
        assert (a is not absent) and (a is not b) and (a is not c) and (a is not d) and (a is not e)
        assert (a is not e6) and (a is not e7) and (a is not e8)
        assert (b is not absent) and (b is not c) and (b is not d) and (b is not e) and (b is not e6)
        assert (b is not e7) and (b is not e8)
        assert (c is not absent) and (c is not d) and (c is not e) and (c is not e6) and (c is not e7)
        assert (c is not e8)
        assert (d is not absent) and (d is not e) and (d is not e6) and (d is not e7) and (d is not e8)
        assert (e is not absent) and (e is not e6) and (e is not e7) and (e is not e8)
        assert (e6 is not absent) and (e6 is not e7) and (e6 is not e8)
        assert (e7 is not absent) and (e7 is not e8)
        assert e8 is not absent

        t = new_Horde_Many()

        t[a]  = v
        t[b]  = w
        t[c]  = x
        t[d]  = y
        t[e]  = z
        t[e6] = z6
        t[e7] = z7
        t[e8] = z8

        return t


    Horde_0.provision = Horde_0.provide = Horde_0.inject = Horde_0.insert = static_method(create_horde_1)

    export(
        'empty_horde',      empty_horde
    )
