#
#   Copyright (c) 2017-2018 Joy Diamond.  All rights reserved.
#
__import__('Boot').boot()

def line(format, *args):
    print format % args


def main():
    if 0:
        from Pattern import make_match_function

        joy_match = make_match_function('[Aa](m)i(?P<what>t)\Z')
    else:
        import _sre

        joy_match = _sre.compile(
            None,#'[Aa](m)i(?P<what>t)\\Z',
            0,
            [
                17, 9, 4, 4, 4, 19, 65, 19, 97, 0, 15, 6, 19, 65, 19, 97, 0, 21, 0, 19, 109,
                21, 1, 19, 105, 21, 2, 19, 116, 21, 3, 6, 7, 1,
            ],
            2,
            {'what': 2},
            ((None, None, 'what')),
        ).match

    m = joy_match('Joy')

    print m.group(0, 1, 2)
