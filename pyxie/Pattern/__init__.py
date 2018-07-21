def make():
    from    Pattern.sre_compile         import compile


    def make_match_function(pattern):
        return compile(pattern, 0).match


    return [make_match_function]


[make_match_function] = make()


del __builtins__, make
