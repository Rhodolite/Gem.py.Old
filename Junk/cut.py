def conjure_unique_triple(k1, k2, k3):
    first = lookup(k1, absent)

    if first.k2 is k2:
        if first.k3 is k3:
            return first

        r = Meta(k1, k2, k3)

        store(k1, create_herd_1(k2, create_herd_2(first.k3, k3, first, r)))

        return r

    if not first.is_herd:
        r = Meta(k1, k2, k3)

        store(k1, (r   if first is absent else   create_herd_2(first.k2, k2, first, r)))

        return r

    skip = 0#first.skip

    if skip is 0:
        second = first.glimpse(k2, absent)

        if second.k3 is k3:
            return second

        if not second.is_herd:
            r = Meta(k1, k2, k3)

            if second is absent:
                first__2 = first.insert(k2, r)

                if first is not first__2:
                    store(k1, first__2)
            else:
                first.displace(k2, create_herd_2(second.k3, k3, second, r))

            return r

        r = second.glimpse(k3)

        if r is not none:
            assert r.k3 is k3

            return r

        r = Meta(k1, k2, k3)

        second__2 = second.insert(k3, r)

        if second is not second__2:
            first.displace(k2, second__2)

        return r

    assert 0, 'incomplete'

    if skip is k2:
        r = first.glimpse(k3)

        if r is not none:
            assert (r.k2 is k2) and (r.k3 is k3)

            return r

        r = Meta(k1, k2, k3)

        first__2 = first.insert(k3, r)

        if first is not first__2:
            assert first__2.skip is k2

            store(k1, first__2)

        return r

    r = Meta(k1, k2, k3)

    store(k1, create_herd_2(skip, k2, first.remove_skip(), r))

    return r
