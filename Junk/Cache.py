    #
    #   NOTE:
    #       This is really 'produce_triple_cache' with 'k3' set to 'none' for key searches
    #       {The invisible it not use in initializing members, which are intiailized "Meta(k1, k2)"}
    #
    @export
    @privileged
    def produce_dual_cache__12N(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_dual__12N(k1, k2):
            first = lookup(k1, absent)
            
            if first.__class__ is Map:
                second = first.get(k2, absent)

                if second.__class__ is Map:
                    return (second.get(none)) or (second.setdefault(none, Meta(k1, k2)))

                if second.k3 is none:
                    assert type(second) is Meta

                    return second

                r = Meta(k1, k2)

                first[k2] = (r   if second is absent else   { second.k3 : second, none : r })

                return r

            if first.k2 is k2:
                if first.k3 is none:
                    assert type(first) is Meta

                    return first

                r = Meta(k1, k2)

                store(k1, { first.k2 : { first.k3 : first, none : r } })

                return r

            r = Meta(k1, k2)

            store(k1, (r   if first is absent else   { first.k2 : first, k2 : r }))

            return r


        if __debug__:
            conjure_dual__12N.__name__ = intern_arrange('conjure_%s__12N', name)

        return conjure_dual__12N


    @export
    @privileged
    def produce_quadruple_cache(
            name,
            Meta,

            cache  = absent,
            lookup = absent,
            store  = absent,
    ):
        if cache is absent:
            cache = {}

        if lookup is absent:
            lookup = cache.get

        if store is absent:
            store = cache.__setitem__


        def conjure_quadruple(kq1, kq2, kq3, kq4):
            first = lookup(kq1, absent)

            if first.__class__ is Map:
                second = first.get(kq2, absent)

                if second.__class__ is Map:
                    third = first.get(kq3, absent)

                    if third.__class__ is Map:
                        return (
                                      third.get(kq4)
                                   or third.setdefault(kq4, Meta(kq1, kq2, kq3, kq4))
                               )

                    if third.kq4 is kq4:
                        return third

                    r = Meta(kq1, kq2, kq3, kq4)

                    second[kq3] = (r   if third is absent else   { third.kq4 : third, kq4 : r })

                    return r

                if second.kq3 is kq3:
                    if second.kq4 is kq4:
                        return second

                    r = Meta(kq1, kq2, kq3, kq4)

                    first[kq2] = { kq3 : { second.kq4 : second, kq4 : r } }

                    return r

                r = Meta(kq1, kq2, kq3, kq4)

                first[kq2] = (r   if second is absent else   { second.kq3 : second, kq3 : r })

                return r

            if first.kq2 is kq2:
                if first.kq3 is kq3:
                    if first.kq4 is kq4:
                        return first

                    r = Meta(kq1, kq2, kq3, kq4)

                    store(kq1, { kq2 : { kq3 : { first.kq4 : first, kq4 : r } } })

                    return r

                r = Meta(kq1, kq2, kq3, kq4)

                store(kq1, { kq2 : { first.kq3 : first, kq3 : r } })

                return r

            r = Meta(kq1, kq2, kq3, kq4)

            store(kq1, (r   if first is absent else   { first.kq2 : first, kq2 : r }))

            return r


        if __debug__:
            conjure_quadruple.__name__ = intern_arrange('conjure_%s', name)

        return conjure_quadruple
