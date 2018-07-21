#
#   Keywords in expressions: if, else, lambda, or, and, not,
#

def tokenizer():
    import __builtin__
    import cStringIO
    import re
    import sys
    import types


    #
    #   Python Types
    #
    Exception = __builtin__.Exception
    Map       = dict
    Method    = types.MethodType
    Object    = object
    Slice     = slice
    String    = str
    Type      = type
    Tuple     = tuple


    #
    #   Python functions
    #
    intern_string   = intern
    compile_pattern = re.compile
    portray         = repr
    object__new     = Object.__new__
    sorted_list     = sorted


    #
    #   Python values
    #
    make_StringIO   = cStringIO.StringIO
    length          = len
    none            = __builtin__.None
    false           = __builtin__.False
    standard_output = sys.stdout
    true            = __builtin__.True
    slice_all       = slice(None)


    write_standard_output = standard_output.write
    flush_standard_output = standard_output.flush


    def arrange(format, *arguments):
        return format % arguments


    def iterate_values_sorted_by_keys(mapping):
        for k in sorted_list(mapping.keys()):
            yield ((k, mapping[k]))


    def line(format, *arguments):
        print (format % arguments   if arguments else   format)
        flush_standard_output()


    def partial(format, *arguments):
        write_standard_output(format % arguments   if arguments else   format)


    def make_match_function(pattern):
        return compile_pattern(pattern).match


    def make_StringOutput():
        return make_StringIO()


    def raise_error(format, *arguments):
        error = format % arguments

        raise Exception(error)


    def dump_tokens(header):
        dump_ContinueLine()
        dump_EndLine()
        dump_MultiLine()
        dump_continue_line()

        line('=== %s: lines: %d; tokens: %d; continue_tokens: %d ===',
             header, length(line_list), length(token_list), length(continue_token_list))

        for v in line_list:
            partial(v.show())

        line('===')

        for v in token_list:
            partial(v.show())

        for v in continue_token_list:
            partial(v.show())

        line('')
        line('===')


    line_match = make_match_function(r'(.*)(\r\n?|\n|\Z)')


    def incomplete():
        dump_tokens('incomplete')

        partial('%s', current_line)

        if index == 0:
            line('^')
        else:
            line('%*c^', index, ' ')

        raise_error('#%d: incomplete for %r', line_number, current_line)


    def continue_incomplete(continue_line, index):
        dump_tokens('incomplete')

        partial('%s', continue_line)

        if index == 0:
            line('^')
        else:
            line('%*c^', index, ' ')

        raise_error('#%d: incomplete for %r', line_number, continue_line)




    symbol_pattern         = r'([A-Z_a-z][0-9A-Z_a-z]*)'
    operator_pattern       = (
                                   r'([%,:=]|\.(?![0-9])|(?:and|i[fn]|else|lambda|not|or)(?![0-9A_Z_a-z]))'
                                 + r'(?: +(?![#\r\n]|\Z))?'
                             )
    open_operator_pattern  = r'([(\[{]) *(?:#.*)?(\r\n?|\n)?'
    newline_pattern        = r'(?:#.*)?(\r\n?|\n)'

    nested1_operator_pattern       = r'([(*,\[{]|\.(?![0-9])) *(?:#.*)?(\r\n?|\n)?'
    nested1_close_operator_pattern = r'([)\]}])'

    nested7_operator_pattern       = r'([()*,\[\]{}]) *(?:#.*)?(\r\n?|\n)?'

    double_quote_middle_pattern = r'(?:[ !$-&(-\[\]-~]|\.)*'
    single_quote_middle_pattern = r'(?:[ -&(-\[\]-~]|\.)*'


    first_match = make_match_function(
                         r' *(?:'
                       +      r'(\r\n?|\n)'                                                 #   newline
                       +     r'|('
                       +         r'def|class|for|import|in|print|raise|return'
                       +      r')(?![0-9A_Z_a-z]) *'                                        #   keyword
                       +     r'|' + symbol_pattern                                          #   symbol
                       +     r'|#.*(\r\n?|\n)?'                                             #   comment
                       +   r')'
                       + r'|'
                  )

    middle_match = make_match_function(
                         r' *(?:'
                       +             operator_pattern               #   operator
                       +      r'|' + symbol_pattern                 #   symbol
                       +      r'|' + open_operator_pattern          #   open_operator, open_operator_newline
                       +      r'|' + newline_pattern                #   newline
                       +    r')'
                       + r'|'
                   )

    nested1_match = make_match_function(
                          symbol_pattern                                #   symbol
                        + r'| *(?:'
                        +             nested1_operator_pattern          #   operator, operator_newline
                        +      r'|' + nested1_close_operator_pattern    #   close_operator
                        +    r')'
                        + r'|'
                    )

    nested7_match = make_match_function(
                          symbol_pattern                                #   symbol
                        + r'| *(?:'
                        +             nested7_operator_pattern          #   operator, operator_newline
                        +    r')'
                        + r'|'
                    )

    continue7_match = make_match_function(
                           r' *(?:'
                         +      r"('" + single_quote_middle_pattern + r"')"     #   single_quote
                        +      r'|' +  nested7_operator_pattern                 #   operator, operator_newline
                         +   r')'
                         + r'|'
                      )


    def show_keyword(t):
        if t.name[-1] in '\r\n':
            return arrange('<%r>', t.name)

        return arrange('<%s>', t.name)


    show_operator = show_keyword


    class BeginContinueOrEndLineBase(Object):
        __slots__ = ((
            'tokens',                   #   Tuple of Token*
            'nesting',                  #   Integer
        ))


        def __init__(t, tokens, nesting):
            assert (type(tokens) is Tuple) and (length(tokens) >= 1)

            for v in tokens[:-1]:
                if type(v) is BlankLine or v.total_newlines:
                    line('OOPS: v.is_newline')
                    incomplete()

            assert tokens[-1].total_newlines

            t.tokens  = tokens
            t.nesting = nesting


        def __repr__(t):
            last = t.tokens[-1].show()

            if last[-1] == '\n':
                return arrange('<%s %s; nesting %d>',
                               t.__class__.__name__,
                               ''.join(v.show()   for v in t.tokens[:-1]) + last[:-1],
                               t.nesting)

            assert last[-3] == '\n'

            return arrange('<%s %s; nesting %d>',
                           t.__class__.__name__,
                           ''.join(v.show()   for v in t.tokens[:-1]) + last[:-3] + last[-2:],
                           t.nesting)


        def show(t):
            last = t.tokens[-1].show()

            if last[-1] == '\n':
                return arrange('[%s; nesting %d]\n',
                               ''.join(v.show()   for v in t.tokens[:-1]) + last[:-1],
                               t.nesting)

            assert last[-3] == '\n'

            return arrange('[%s; nesting %d]\n',
                           ''.join(v.show()   for v in t.tokens[:-1]) + last[:-3] + last[-2:],
                           t.nesting)


    class BeginLine(BeginContinueOrEndLineBase):
        __slots__ = (())


    class ContinueLine(BeginContinueOrEndLineBase):
        __slots__ = (())


    class EndLine(BeginContinueOrEndLineBase):
        __slots__ = (())


    class MultiLine(Object):
        __slots__ = ((
            'tokens',                   #   Tuple of Token*
            'total_newlines',           #   Integer
        ))


        def __init__(t, tokens, total_newlines):
            assert (type(tokens) is Tuple) and (length(tokens) >= 1)

            for v in tokens[:-1]:
                if type(v) is BlankLine or v.is_newline:
                    line('OOPS: v.is_newline')
                    incomplete()

            assert tokens[-1].is_newline

            t.tokens         = tokens
            t.total_newlines = total_newlines


        def __repr__(t):
            last = t.tokens[-1].show()

            assert last[-1] == '\n'

            return arrange('<%s %s; #%d>',
                           t.__class__.__name__,
                           ''.join(v.show()   for v in t.tokens[:-1]) + last[:-1],
                           t.total_newlines)


        def show(t):
            last = t.tokens[-1].show()

            assert last[-1] == '\n'

            return arrange('[%s; #%d]\n',
                           ''.join(v.show()   for v in t.tokens[:-1]) + last[:-1],
                           t.total_newlines)


    class BlankLine(Object):
        __slots__ = ((
            'name',
        ))


        def __init__(t, name):
            t.name = name


        def show(t):
            return arrange('[%r]\n', t.name)


    class TokenLine(Object):
        __slots__ = ((
            'tokens',                   #   Tuple of Token*
        ))


        def __init__(t, tokens):
            assert (type(tokens) is Tuple) and (length(tokens) >= 2)

            for v in tokens[:-1]:
                if type(v) is BlankLine or v.is_newline:
                    line('OOPS: v.is_newline')
                    incomplete()

            assert tokens[-1].is_newline

            t.tokens = tokens


        def __repr__(t):
            return arrange('<TokenLine %s>', ''.join(v.show()   for v in t.tokens)[:-1])


        def show(t):
            return arrange('[%s]\n', ''.join(v.show()   for v in t.tokens)[:-1])




    class TokenBase(Object):
        __slots__ = ((
            'name',
        ))


        adjust_nesting     = 0
        is_newline         = False
        is_token_pair      = False
        is_valid           = True
        total_newlines     = 0


        def __init__(t, name):
            t.name = name


        def __repr__(t):
            return arrange('<Token %r>', t.name)


    class Colon(TokenBase):
        __slots__ = (())
        show      = show_operator


    class Comma(TokenBase):
        __slots__ = (())
        show      = show_operator


    class Dot(TokenBase):
        __slots__ = (())
        show      = show_operator


    class EqualSign(TokenBase):
        __slots__ = (())
        show      = show_operator


    class Indentation(TokenBase):
        __slots__ = ((
            'indented',                 #   Integer+
        ))


        def __init__(t, name, indented):
            t.name     = name
            t.indented = indented


        def __repr__(t):
            return arrange('<Indentation +%d>', t.indented)

        def show(t):
            return arrange('{%d}', t.indented)


    class KeywordClass(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class KeywordDefine(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class KeywordFor(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class KeywordImport(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class KeywordIn(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class KeywordPrint(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class KeywordRaise(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class KeywordReturn(TokenBase):
        __slots__ = (())
        show      = show_keyword


    class LeftParenthesis(TokenBase):
        __slots__        = (())
        adjust_nesting   = 1
        show             = show_operator


    class NewlineToken(TokenBase):
        __slots__      = (())
        is_newline     = True
        total_newlines = 1


        def show(t):
            return arrange('{%r}\n', t.name)


    class PrefixAtom(TokenBase):
        __slots__ = ((
            'atom',                     #   SingleQuote
        ))


        def __init__(t, name, atom):
            t.name = name
            t.atom = atom


        show = show_operator


    class RightParenthesis(TokenBase):
        __slots__         = (())
        adjust_nesting    = -1
        show              = show_operator


    class SingleQuote(TokenBase):
        __slots__ = (())
        show      = show_operator


    class Star(TokenBase):
        __slots__ = (())
        show      = show_operator


    class Symbol(TokenBase):
        __slots__ = (())

        def show(t):
            return arrange('$%s', t.name)


    class TokenEmpty(TokenBase):
        __slots__ = (())


        is_valid = False


        def __init__(t):
            t.name = ''


        def show(t):
            return '<empty-token>'


        def __repr__(t):
            return '<TokenEmpty>'


    class TokenPair(Object):
        __slots__ = ((
            'a',                #   Indentation
            'b',                #   Token*
        ))


        is_token_pair = True


        def __init__(t, a, b):
            t.a = a
            t.b = b


        def __repr__(t):
            return arrange('<Pair %s %s>', t.a, t.b)


    double_quote_portray_pattern = r'(?:[ !$-&(-\[\]-~]|\[ -mo-qs-~])*'
    single_quote_portray_pattern = r'(?:[ -&(-\[\]-~]|\[ -mo-qs-~])*'

    start_portray_match = make_match_function(
                                r'(?:'
                              +    r"(')" + single_quote_portray_pattern
                              +   r'|"' + double_quote_portray_pattern
                              + r')'
                              + r'(?:\\r\\n|\\[rn])'
                          )

    continue_portray_1_match = make_match_function(
                                     double_quote_portray_pattern
                                   + r"(?:(')|\\r\\n|\\[rn])"
                               )

    continue_portray_2_match = make_match_function(
                                     single_quote_portray_pattern
                                   + r'(?:(")|\\r\\n|\\[rn])'
                               )


    def newline__show(t):
        s = portray(t.name)
        m = start_portray_match(s)
        r = '{' + m.group() + '\n'

        if m.start(1) is 0:
            while 7 is 7:
                m = continue_portray_1_match(s, m.end())

                if m.start(1) is not -1:
                    return r + m.group() + '}'

                r += m.group() + '\n'

        while 7 is 7:
            m = continue_portray_2_match(s, m.end())

            if m.start(1) is not -1:
                return r + m.group() + '}'

            r += m.group() + '\n'


    #
    #   Create an instance of class just like 'meta':
    #
    #       1.  Class is nameed '%sNewline'
    #       2.  Class has an extra 'total_newlines' member
    #       3.  Class has a '.show' method to display the newlines
    #
    #   Also, when creating the in stance, we bypass the constructor (TokenBase.__init__) and just
    #   initialize the new instance directly (Since we are the only place that constructors these
    #   instances, and it's a tiny bit faster).
    #
    def new_TokenNewline(meta, name, total_newlines):
        meta_newline = lookup_meta_newline(meta)

        if meta_newline is none:
            assert meta.__base__  is TokenBase
            assert meta.__slots__ is (())

            mapping              = meta.__dict__.copy()
            mapping['__slots__'] = (('name', 'total_newlines'))
            mapping['show']      = newline__show

            meta_newline = provide_meta_newline(
                               meta,
                               Type(
                                   arrange('%sNewline', meta.__name__),
                                   ((TokenBase,)),
                                   mapping,
                               ),
                           )

            del meta_newline.__slots__

        r                = object__new(meta_newline)
        r.name           = name
        r.total_newlines = total_newlines

        return r


    keyword_map =  {
        '%'      : Comma,
        '('      : LeftParenthesis,
        ')'      : RightParenthesis,
        '*'      : Star,
        ','      : Comma,
        '.'      : Dot,
        ':'      : Colon,
        '='      : EqualSign,
        'class'  : KeywordClass,
        'def'    : KeywordDefine,
        'for'    : KeywordFor,
        'import' : KeywordImport,
        'in'     : KeywordIn,
        'print'  : KeywordPrint,
        'raise'  : KeywordRaise,
        'return' : KeywordReturn,
    }

    find_keyword = keyword_map.__getitem__
    is_keyword   = keyword_map.__contains__


    def continue_tokenize(last_token, nesting):
        append_token(last_token)
        provide_line(current_line, BeginLine(tupalize_tokens(), nesting))

        continue_line_number = line_number
        total_newlines       = 1

        while continue_line_number < last_line_number:
            continue_line    = all_lines[continue_line_number]

            continue_line_number += 1

            continue_index   = 0

            level_1 = lookup_continue_line(nesting)

            if level_1 is not none:
                previous = level_1.get(continue_line)

                if previous is not none:
                    continue_incomplete(continue_line, continue_index)

                    extend_tokens(previous.tokens)
                    continue

            nesting_start = nesting

            if nesting <= 1:
                continue_incomplete(continue_line, continue_index)

            m = continue7_match(continue_line)

            [single_quote, operator, operator_newline] = m.groups()

            if single_quote is not none:
                start = m.start(1)

                if start is 0:
                    append_continue_token(
                        lookup_token(single_quote) or provide_token(single_quote, SingleQuote(single_quote))
                    )
                else:
                    s = m.group()

                    append_continue_token(
                           lookup_token(s)
                        or provide_token(
                               s,
                               PrefixAtom(
                                   s,
                                   (
                                          lookup_token(single_quote)
                                       or provide_token(single_quote, SingleQuote(single_quote))
                                   ),
                               ),
                          ),
                    )

                continue_index = m.end()

            elif operator is not none:
                if operator_newline is not none:
                    continue_incomplete(continue_line, continue_index)

                meta = find_keyword(operator)

                append_continue_token(
                    lookup_token(operator) or provide_token(operator, meta(operator)),
                )

                nesting += meta.adjust_nesting

                continue_index = m.end()
            else:
                continue_incomplete(continue_line, continue_index)

            while 7 is 7:
                if nesting is 0:
                    while 7 is 7:
                        m = middle_match(continue_line, continue_index)
                        s = m.group()

                        line('continue_tokenize; middle_match: %r', s)

                        token = lookup_token(s)

                        if token is not none:
                            if not token.is_valid:
                                line('token: %r', token)
                                incomplete()

                            append_continue_token(token)

                            assert type(token_list[-1]) is not BlankLine

                            if token.is_newline:
                                extend_tokens_with_continue_tokens()

                                if level_1 is none:
                                    store_continue_line(
                                        nesting_start,
                                        {
                                            continue_line:
                                                new_EndLine(tupalize_continue_token(), nesting_start - nesting),
                                        },
                                    )
                                else:
                                    level_1[continue_line] = new_EndLine(
                                                                 tupalize_continue_token(), nesting_start - nesting,
                                                             )

                                zap_continue_tokens()


                                append_line(new_MultiLine(tupalize_tokens(), total_newlines + 1))
                                zap_tokens()

                                return continue_line_number

                            index = m.end()
                            continue_incomplete(continue_line, continue_index)

                        continue_incomplete(continue_line, continue_index)

                    if continue_index is -1:
                        break
                elif nesting is 1:
                    while 7 is 7:
                        m = nested1_match(continue_line, continue_index)
                        s = m.group()

                        token = lookup_nested1(s)

                        if token is not none:
                            if token.total_newlines is not 0:
                                continue_incomplete(continue_line, continue_index)

                            append_continue_token(token)
                            continue_index = m.end()

                            if token.adjust_nesting is 0:
                                continue

                            nesting += token.adjust_nesting
                            break

                        continue_incomplete(continue_line, continue_index)

                    if continue_index is -1:
                        break
                else:
                    while 7 is 7:
                        m = nested7_match(continue_line, continue_index)
                        s = m.group()

                        token = lookup_nested7(s)

                        if token is not none:
                            continue_incomplete(continue_line, continue_index)

                        [symbol, operator, operator_newline] = m.groups()

                        if symbol is not none:
                            continue_incomplete(continue_line, continue_index)

                        if operator is not none:
                            if operator_newline is none:
                                continue_incomplete(continue_line, continue_index)

                            meta = find_keyword(operator)

                            if meta.adjust_nesting is not 0:
                                continue_incomplete(continue_line, continue_index)

                            append_continue_token(
                                provide_nested7(
                                    s,
                                    lookup_token(s) or provide_token(s, new_TokenNewline(meta, s, 1))
                                )
                            )

                            extend_tokens_with_continue_tokens()

                            if level_1 is none:
                                store_continue_line(
                                    nesting_start,
                                    {
                                        continue_line:
                                            new_ContinueLine(tupalize_continue_token(), nesting_start - nesting),
                                    },
                                )
                            else:
                                level_1[continue_line] = new_ContinueLine(
                                                             tupalize_continue_token(), nesting_start - nesting,
                                                         )

                            zap_continue_tokens()

                            continue_index = -1
                            total_newlines += 1
                            break

                        continue_incomplete(continue_line, continue_index)

                    if continue_index is -1:
                        break

        incomplete()

        many_tokens = tupalize_tokens()
        zap_tokens()

        append_line(
               lookup_multiline(many_tokens)
            or conjure_multiline(
                   many_tokens,
                   MultiLine(many_tokens, 1),
               )
        )

        return line_number


    def make_lookup_and_provide():
        cache = {}

        return ((cache.get, cache.setdefault))


    def make_dump_lookup_provide_and_store(name):
        cache = {}

        def dump():
            line('===  Dump of %s Map ===', name)

            for [k, v] in iterate_values_sorted_by_keys(cache):
                if type(v) is Map:
                    line('  %r:', k)

                    for [k2, w] in iterate_values_sorted_by_keys(v):
                        display_1 = portray(k2)
                        display_2 = portray(w)

                        if 4 + length(display_1) + 3 + length(display_2) >= 100:
                            line('    %s:', display_1)
                            line('      %s', display_2)
                        else:
                            line('    %s:  %s', display_1, display_2)
                else:
                    line('  %r:  %r', k, v)

            line('===')


        return ((dump, cache.get, cache.setdefault, cache.__setitem__))


    [
            dump_ContinueLine, lookup_ContinueLine,  provide_ContinueLine, store_ContinueLine
    ] = make_dump_lookup_provide_and_store('ContinueLine')

    [
            dump_EndLine, lookup_EndLine, provide_EndLine, store_EndLine
    ] = make_dump_lookup_provide_and_store('EndLine')

    [
            dump_MultiLine, lookup_MultiLine, provide_MultiLine, store_MultiLine
    ] = make_dump_lookup_provide_and_store('MultiLine')

    [
            dump_continue_line, lookup_continue_line, provide_continue_line, store_continue_line,
    ] = make_dump_lookup_provide_and_store('continue_line')

    [lookup_first,         provide_first]         = make_lookup_and_provide()
    [lookup_meta_newline,  provide_meta_newline]  = make_lookup_and_provide()
    [lookup_indentation,   provide_indentation]   = make_lookup_and_provide()
    [lookup_line,          provide_line]          = make_lookup_and_provide()
    [lookup_newline,       provide_newline]       = make_lookup_and_provide()
    [lookup_open_operator, provide_open_operator] = make_lookup_and_provide()
    [lookup_token,         provide_token]         = make_lookup_and_provide()
    [lookup_nested1,       provide_nested1]       = make_lookup_and_provide()
    [lookup_nested7,       provide_nested7]       = make_lookup_and_provide()


    def make_new_XLine(meta, lookup_XLine, provide_XLine, store_XLine):
        def new_XLine(tokens, nesting):
            level_1 = lookup_XLine(nesting)

            if level_1 is none:
                return provide_XLine(nesting, meta(tokens, nesting))

            if type(level_1) is Map:
                level_2 = level_1.get(tokens)

                if level_2 is not none:
                    return level_2

                level_1[tokens] = r = meta(tokens, nesting)

                return r

            if level_1.tokens == tokens:
                return level_1

            r = meta(tokens, nesting)

            store_XLine(nesting, {level_1.tokens : level_1, tokens : r})

            return r


        return new_XLine


    new_ContinueLine = make_new_XLine(
                           ContinueLine, lookup_ContinueLine, provide_ContinueLine, store_ContinueLine,
                       )

    new_EndLine = make_new_XLine(EndLine, lookup_EndLine, provide_EndLine, store_EndLine)

    new_MultiLine = make_new_XLine(MultiLine, lookup_MultiLine, provide_MultiLine, store_MultiLine)



    provide_token('', TokenEmpty())

    continue_token_list     = []
    append_continue_token   = continue_token_list.append
    tupalize_continue_token = Method(Tuple, continue_token_list)
    zap_continue_tokens     = Method(continue_token_list.__delitem__, slice_all)

    token_list      = []
    extend_tokens   = token_list.extend
    append_token    = token_list.append
    tupalize_tokens = Method(Tuple, token_list)
    zap_tokens      = Method(token_list.__delitem__, slice_all)

    extend_tokens_with_continue_tokens = Method(extend_tokens, continue_token_list)

    line_list       = []
    append_line     = line_list.append

    all_data         = open('/home/joy/pyxie/.gem/Tokenizer.py').read()
    all_lines        = all_data.splitlines(True)
    last_line_number = length(all_lines) - 1

    line_number = 0

    while line_number < last_line_number:
        current_line = all_lines[line_number]
        index        = 0

        line_number += 1

        token_line = lookup_line(current_line)

        if token_line is not none:
            append_line(token_line)
            continue

        m     = first_match(current_line)
        s     = m.group()
        token = lookup_first(s)

        #line('lookup_first(%r): %s', s, token)

        if token is not none:
            if token.is_token_pair:
                assert type(token.a) is not BlankLine
                assert type(token.b) is not BlankLine

                append_token(token.a)
                append_token(token.b)

                index = m.end()
            elif token.is_valid:
                assert not token.is_newline

                append_token(token)

                index = m.end()

                #if token.is_newline:
                #    continue
            else:
                incomplete()
        else:
            [newline, keyword, symbol, comment] = m.groups()

            if (newline is not none) or (comment is not none):
                assert keyword is symbol is none

                append_line(provide_line(s, BlankLine(intern_string(s))))
                continue

            if keyword is not none:
                meta  = find_keyword(keyword)
                start = m.start(2)

                #line('index: %d, meta: %s, start: %d', index, meta, start)

                if start == index:
                    append_token(provide_first(s, lookup_token(s) or provide_token(s, meta(s))))

                    assert type(token_list[-1]) is not BlankLine
                else:
                    indented    = start - index
                    indentation = (
                                         lookup_indentation(indented)
                                      or provide_indentation(indented, Indentation(s[index:start], indented))
                                  )

                    name = current_line[start:m.end()]
                    b    = lookup_token(name) or provide_token(name, meta(name))

                    append_token(indentation)
                    append_token(b)

                    assert type(token_list[-1]) is not BlankLine

                    provide_first(s, TokenPair(indentation, b))

            elif symbol is not none:
                start = m.start(3)

                if start == index:
                    if is_keyword(s):
                        incomplete()

                    append_token(provide_first(s, lookup_token(s) or Symbol(s)))

                    assert type(token_list[-1]) is not BlankLine
                else:
                    indented    = start - index
                    indentation = (
                                         lookup_indentation(indented)
                                      or provide_indentation(indented, Indentation(s[index:start], indented))
                                  )

                    name = current_line[start:m.end()]

                    if is_keyword(name):
                        incomplete()

                    b = lookup_token(name) or provide_token(name, Symbol(name))

                    append_token(indentation)
                    append_token(b)

                    assert type(token_list[-1]) is not BlankLine

                    provide_first(s, TokenPair(indentation, b))

            else:
                incomplete()

            index = m.end()


        while 7 is 7:
            m = middle_match(current_line, index)
            s = m.group()

            #line('middle_match: %r', s)

            token = lookup_token(s)

            if token is not none:
                if not token.is_valid:
                    line('token: %r', token)
                    incomplete()

                append_token(token)

                assert type(token_list[-1]) is not BlankLine

                if token.is_newline:
                    append_line(provide_line(current_line, TokenLine(tupalize_tokens())))
                    zap_tokens()
                    break

                index = m.end()

                if token.adjust_nesting:
                    incomplete()

                continue

            [operator, symbol, open_operator, open_operator_newline, newline] = m.groups()

            if operator is not none:
                append_token(provide_token(s, find_keyword(operator)(s)))
                index = m.end()
                continue

                incomplete()

            if symbol is not none:
                if m.start(1) == index:
                    append_token(provide_token(symbol, Symbol(symbol)))
                else:
                    append_token(
                        provide_token(
                           s,
                           PrefixAtom(
                               s,
                               (
                                      lookup_token(symbol)
                                   or provide_token(symbol, Symbol(symbol))
                               ),
                           ),
                        ),
                    )

                index = m.end()
                continue

            if open_operator is not none:
                assert open_operator_newline is none

                append_token(
                       lookup_open_operator(s)
                    or provide_open_operator(s, find_keyword(open_operator)(s))
                )

                index = m.end()

                while 7 is 7:
                    m = nested1_match(current_line, index)
                    s = m.group()

                    #line('nested1_match: %r', s)

                    token = lookup_nested1(s)

                    if token is not none:
                        if token.adjust_nesting is -1:
                            append_token(token)
                            index = m.end()
                            break

                        assert token.adjust_nesting is 0

                        if token.is_valid:
                            append_token(token)

                            assert type(token_list[-1]) is not BlankLine

                            index = m.end()
                            continue

                        line('token: %r', token)
                        incomplete()

                    [symbol, operator, operator_newline, close_operator] = m.groups()

                    if symbol is not none:
                        assert operator is operator_newline is close_operator is none

                        append_token(provide_nested1(s, lookup_token(s) or provide_token(s, Symbol(s))))
                        index = m.end()
                        continue

                    if operator is not none:
                        assert close_operator is none

                        if operator_newline is none:
                            append_token(
                                provide_nested1(
                                    s,
                                    lookup_token(s) or provide_token(s, find_keyword(operator)(s))
                                ),
                            )


                            index = m.end()
                            continue

                        meta = find_keyword(operator)

                        if meta.adjust_nesting is 1:
                            line_number = continue_tokenize(
                                              provide_nested1(
                                                  s,
                                                  lookup_token(s) or provide_token(s, new_TokenNewline(meta, s, 1)),
                                              ),
                                              2,
                                          )

                            index = -1
                            break

                        assert meta.adjust_nesting is 0

                        line_number = continue_tokenize(
                                          provide_nested1(
                                              s,
                                              new_TokenNewline(meta, s, 1),
                                          ),
                                          1,
                                      )

                        index = -1
                        break

                    if close_operator is not none:
                        assert operator_newline is none

                        meta = find_keyword(close_operator)

                        append_token(provide_nested1(s, meta(s)))
                        index = m.end()
                        break

                    incomplete()

                if index is -1:
                    break

                continue

            if newline is not none:
                append_token(provide_token(s, NewlineToken(s)))
                append_line(provide_line(current_line, TokenLine(tupalize_tokens())))
                zap_tokens()
                break

            incomplete()
