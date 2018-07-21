def parser():
    import __builtin__
    import cStringIO
    import re
    import sys


    #
    #   Python Types
    #
    Exception = __builtin__.Exception
    Object    = object
    String    = str


    #
    #   Python functions
    #
    compile_pattern = re.compile


    #
    #   Python values
    #
    make_StringIO   = cStringIO.StringIO
    length          = len
    none            = __builtin__.None
    false           = __builtin__.False
    standard_output = sys.stdout
    true            = __builtin__.True


    def make_match_function(pattern):
        return compile_pattern(pattern).match


    def make_StringOutput():
        return make_StringIO()


    def line(format, *arguments):
        print format % arguments


    def raise_error(format, *arguments):
        error = format % arguments

        raise Exception(error)


    class Parser(Object):
        __slots__ = ((
            'all_data',                 #   String+
            'all_lines',                #   List of String+
            'line_number',              #   Integer
            'last_line_number',         #   Integer
        ))

        
        def __init__(t, all_data, all_lines):
            t.all_data         = all_data
            t.all_lines        = all_lines = all_data.split()
            t.line_number      = 0
            t.last_line_number = length(all_lines) - 1


    class LineParser(Object):
        __slots__ = ((
            'match',            #   BuiltinFunctionOrMethod
            'parser',           #   Function
        ))


        def __init__(t, match, parser):
            t.match  = match
            t.parser = parser


        def attempt(t, s):
            m = t.match(s)

            if m is not none:
                append_tree(t.parser(m))
                return true

            return false


    def line_parser(pattern):
        def line_parser(f):
            return LineParser(make_match_function(pattern), f)


        return line_parser


    group_assign_pattern            = r'( *= *)'
    group_comma_pattern             = r'( *, *)'
    group_colon_pattern             = r'( *:)'
    group_comment_pattern           = r'(#.*)'
    group_dot_pattern               = r'( *\. *)'
    group_indentation_pattern       = r'( +)'
    group_left_parenthesis_pattern  = r'( *\( *)'
    group_name_pattern              = r'([A-Z_a-z][0-9A-Z_a-z]*)'
    group_newline_pattern           = r'(\n)\Z'
    group_percent_pattern           = r'( *% *)'
    group_right_parenthesis_pattern = r'( *\))'
    group_star_pattern              = r'( *\* *)'
    group_whitespace_pattern        = r'( *)'


    @line_parser(group_newline_pattern)
    def blank_line(m):
        [newline] = m.groups()

        return BlankLine(newline)


    @line_parser(group_whitespace_pattern + group_comment_pattern + group_newline_pattern)
    def comment_line(m):
        [indentation, comment, newline] = m.groups()

        return CommentLine(indentation, comment, newline)


    @line_parser(
          r'( *)(class +)'
        + group_name_pattern
        + group_left_parenthesis_pattern
        + group_name_pattern
        + group_right_parenthesis_pattern
        + group_colon_pattern
        + group_newline_pattern
    )
    def class_header(m):
        [
            indentation, keyword, name,
                left_parenthesis, first, right_parenthesis,
                colon, newline,
        ] = m.groups()


        return ClassHeader(
                   indentation,
                   keyword,
                   Symbol(name),
                   FunctionArguments_One(left_parenthesis, Symbol(first), right_parenthesis),
                   colon,
                   newline,
               )


    @line_parser(
          r'( *)(def +)'
        + group_name_pattern
        + group_left_parenthesis_pattern
        + r'(?:'
        +     group_name_pattern
        +     r'(?:' + group_comma_pattern + group_name_pattern + r')?'
        +     r'(?:' + group_comma_pattern + group_name_pattern + r')?'
        +     r'(?:' + group_comma_pattern + group_star_pattern + group_name_pattern + r')?'
        + r')?'
        + group_right_parenthesis_pattern
        + r'(:)'
        + group_newline_pattern
    )
    def function_header(m):
        [
            indentation, keyword, name,
                left_parenthesis,
                    first, first_comma,
                    second, second_comma,
                    third, third_comma,
                    star, star_name,
                right_parenthesis,
                colon, newline,
        ] = m.groups()

        if first is none:
            arguments = FunctionArguments_Blank(left_parenthesis, right_parenthesis)
        elif second is none:
            if star is none:
                arguments = FunctionArguments_One(
                                left_parenthesis,
                                Symbol(first),
                                right_parenthesis,
                            )
            else:
                arguments = FunctionArguments_Two(
                                left_parenthesis,
                                Symbol(first),
                                third_comma,
                                FunctionArguments_Star(star, star_name),
                                right_parenthesis,
                            )
        elif third is none:
            assert star is none

            arguments = FunctionArguments_Two(
                            left_parenthesis,
                            Symbol(first), first_comma,
                            Symbol(second),
                            right_parenthesis,
                        )
        else:
            assert star is none

            arguments = FunctionArguments_Three(
                            left_parenthesis,
                            Symbol(first), first_comma,
                            Symbol(second), second_comma,
                            Symbol(third),
                            right_parenthesis,
                        )



        return FunctionHeader(
                   indentation,
                   keyword,
                   Symbol(name),
                   arguments,
                   colon,
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + group_name_pattern
        + group_left_parenthesis_pattern
        + group_name_pattern
        + group_dot_pattern
        + group_name_pattern
        + group_left_parenthesis_pattern
        + group_name_pattern
        + group_right_parenthesis_pattern
        + group_right_parenthesis_pattern
        + group_newline_pattern
    )
    def nested_function_call(m):
        [
                indentation,
                left, left_parenthesis_1,
                left_dot, dot, right_dot, left_parenthesis_2,
                last_name,
                right_parenthesis_2,
                right_parenthesis_1,
                newline,
        ] = m.groups()


    #                append_tree(t.parser(m))
        return StatementExpression(
                   indentation,
                   ExpressionFunctionCall(
                       Symbol(left),
                       ExpressionFunctionArguments_One(
                           left_parenthesis_1,
                           ExpressionFunctionCall(
                               ExpressionDot(Symbol(left_dot), dot, right_dot),
                               ExpressionFunctionArguments_One(
                                   left_parenthesis_2,
                                   Symbol(last_name),
                                   right_parenthesis_2,
                               ),
                           ),
                           right_parenthesis_1,
                       ),
                   ),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + r'(if +)'
        + group_name_pattern
        + r'( *is +not +)'
        + group_name_pattern
        + group_colon_pattern
        + group_newline_pattern
    )
    def statement_if_header(m):
        [indentation, keyword, left, is_not, right, colon, newline] = m.groups()

        return StatementIfHeader(
                   indentation,
                   keyword,
                   ExpressionBinary(Symbol(left), is_not, Symbol(right)),
                   colon,
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + r'(import +)'
        + group_name_pattern
        + group_newline_pattern
    )
    def statement_import(m):
        [indentation, keyword, name, newline] = m.groups()

        return StatementImport(indentation, keyword, Symbol(name), newline)


    @line_parser(
          group_indentation_pattern
        + group_name_pattern
        + group_assign_pattern
        + group_name_pattern
        + group_percent_pattern
        + group_name_pattern
        + group_newline_pattern
    )
    def assign_binary_expression(m):
        [
                indentation, left_side, equal_sign,
                left_binary, percent, right_binary,
                newline,
        ] = m.groups()

        return StatementAssign(
                   indentation,
                   Symbol(left_side),
                   equal_sign,
                   ExpressionBinary(Symbol(left_binary), percent, Symbol(right_binary)),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + group_name_pattern
        + group_dot_pattern
        + group_name_pattern
        + group_assign_pattern
        + group_name_pattern
        + group_newline_pattern
    )
    def assign_left_dot_member(m):
        [indentation, left_side, dot, member, equal_sign, value, newline] = m.groups()

        return StatementAssign(
                   indentation,
                   ExpressionDot(Symbol(left_side), dot, member),
                   equal_sign,
                   Symbol(value),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + group_name_pattern
        + group_assign_pattern
        + group_name_pattern
        + group_newline_pattern
    )
    def assign_name(m):
        [indentation, left_side, equal_sign, name, newline] = m.groups()

        return StatementAssign(
                   indentation,
                   Symbol(left_side),
                   equal_sign,
                   Symbol(name),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + group_name_pattern
        + group_assign_pattern
        + group_name_pattern
        + group_dot_pattern
        + group_name_pattern
        + group_newline_pattern
    )
    def assign_right_dot_member(m):
        [indentation, left_side, equal_sign, left_dot, dot, right_dot, newline] = m.groups()

        return StatementAssign(
                   indentation,
                   Symbol(left_side),
                   equal_sign,
                   ExpressionDot(Symbol(left_dot), dot, right_dot),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + group_name_pattern
        + group_assign_pattern
        + group_name_pattern
        + group_dot_pattern
        + group_name_pattern
        + group_left_parenthesis_pattern
        + group_name_pattern
        + group_right_parenthesis_pattern
        + group_newline_pattern
    )
    def assign_method_call(m):
        [
                indentation, left_side, equal_sign,
                left_dot, dot, right_dot,
                left_parenthesis, first, right_parenthesis,
                newline,
        ] = m.groups()

        return StatementAssign(
                   indentation,
                   Symbol(left_side),
                   equal_sign,
                   ExpressionFunctionCall(
                       ExpressionDot(Symbol(left_dot), dot, right_dot),
                       ExpressionFunctionArguments_One(
                           left_parenthesis, Symbol(first), right_parenthesis,
                       ),
                   ),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + group_name_pattern
        + group_assign_pattern
        + group_left_parenthesis_pattern
        + group_left_parenthesis_pattern
        + group_newline_pattern
    )
    def start_assign_slots(m):
        [
                indentation, left_side, equal_sign,
                left_parenthesis_1, left_parenthesis_2, newline,
        ] = m.groups()

        return StatementStartAssignSlots(
                   indentation,
                   Symbol(left_side),
                   equal_sign,
                   left_parenthesis_1,
                   left_parenthesis_2,
                   newline,
               )

    @line_parser(
          group_indentation_pattern
        + r"('[A-Z_a-z][0-9A-Z_a-z]*')"
        + group_comma_pattern
        + group_whitespace_pattern
        + group_comment_pattern
        + group_newline_pattern
    )
    def slot_definition(m):
        [indentation, quoted_name, comma, whitespace, comment, newline] = m.groups()

        return SlotDefinition(
                   indentation,
                   quoted_name,
                   comma,
                   whitespace,
                   comment,
                   newline,
               )

    @line_parser(
          group_indentation_pattern
        + group_right_parenthesis_pattern
        + group_right_parenthesis_pattern
        + group_newline_pattern
    )
    def end_assign_slots(m):
        [indentation, right_parenthesis_1, right_parenthesis_2, newline] = m.groups()

        return StatementEndAssignSlots(
                   indentation,
                   right_parenthesis_1,
                   right_parenthesis_2,
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + r'(print +)'
        + group_name_pattern
        + group_percent_pattern
        + group_name_pattern
        + group_newline_pattern
    )
    def print_expression(m):
        [indentation, keyword, left_name, percent, right_name, newline] = m.groups()

        return StatementPrintExpression(
                   indentation,
                   keyword,
                   ExpressionBinary(Symbol(left_name), percent, Symbol(right_name)),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + r'(return +)'
        + group_name_pattern
        + group_left_parenthesis_pattern
        + group_name_pattern
        + group_right_parenthesis_pattern
        + group_dot_pattern
        + group_name_pattern
        + group_newline_pattern
    )
    def return_compile_pattern(m):
        [
            indentation, keyword, function_name,
                left_parenthesis, function_argument, right_parenthesis,
                dot, name, newline
        ] = m.groups()

        return StatementReturnExpression(
                   indentation,
                   keyword,
                   ExpressionDot(
                       ExpressionFunctionCall(
                           Symbol(function_name),
                           ExpressionFunctionArguments_One(
                               left_parenthesis, Symbol(function_argument), right_parenthesis,
                           ),
                       ),
                       dot,
                       name,
                   ),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + r'(raise +)'
        + group_name_pattern
        + group_left_parenthesis_pattern
        + group_name_pattern
        + group_right_parenthesis_pattern
        + group_newline_pattern
    )
    def raise_function_call(m):
        [
                indentation, keyword, function_name,
                left_parenthesis, first, right_parenthesis,
                newline
        ] = m.groups()

        return StatementRaiseExpression(
                   indentation,
                   keyword,
                   ExpressionFunctionCall(
                       Symbol(function_name),
                       ExpressionFunctionArguments_One(
                           left_parenthesis, Symbol(first), right_parenthesis,
                       ),
                   ),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + r'(return +)'
        + group_name_pattern
        + group_left_parenthesis_pattern
        + group_right_parenthesis_pattern
        + group_newline_pattern
    )
    def return_function_call(m):
        [
            indentation, keyword, function_name,
                left_parenthesis, right_parenthesis,
                newline
        ] = m.groups()

        return StatementReturnExpression(
                   indentation,
                   keyword,
                   ExpressionFunctionCall(
                       Symbol(function_name),
                       ExpressionFunctionArguments_Blank(
                           left_parenthesis, right_parenthesis,
                       ),
                   ),
                   newline,
               )


    @line_parser(
          group_indentation_pattern
        + r'(return +)'
        + group_name_pattern
        + group_newline_pattern
    )
    def return_name(m):
        [indentation, keyword, name, newline] = m.groups()

        return StatementReturnExpression(indentation, keyword, Symbol(name), newline)


    tree_many   = []
    append_tree = tree_many.append


    class BaseTree(Object):
        __slots__ = (())


        def __str__(t):
            f = make_StringIO()

            t.write(f)

            r = f.getvalue()

            f.close()

            return r


    class BlankLine(BaseTree):
        __slots__ = ((
            'newline'
        ))


        def __init__(t, newline):
            t.newline   = newline


        def write(t, w):
            w.write(t.newline)


    class ClassHeader(BaseTree):
        __slots__ = ((
            'indentation',
            'keyword',
            'name',
            'arguments',
            'colon',
            'newline'
        ))


        def __init__(t, indentation, keyword, name, arguments, colon, newline):
            t.indentation = indentation
            t.keyword     = keyword
            t.name        = name
            t.arguments   = arguments
            t.colon       = colon
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.keyword)
            t.name.write(w)
            t.arguments.write(w)
            w.write(t.colon + t.newline)


    class CommentLine(BaseTree):
        __slots__ = ((
            'indentation',
            'comment',
            'newline'
        ))


        def __init__(t, indentation, comment, newline):
            t.indentation = indentation
            t.comment     = comment
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.comment + t.newline)


    class ExpressionBinary(BaseTree):
        __slots__ = ((
            'left',
            'dot',
            'right',
        ))


        def __init__(t, left, dot, right):
            t.left  = left
            t.dot   = dot
            t.right = right


        def write(t, w):
            t.left.write(w)
            w.write(t.dot)
            t.right.write(w)


    class ExpressionDot(BaseTree):
        __slots__ = ((
            'left',
            'dot',
            'right',
        ))


        def __init__(t, left, dot, right):
            t.left  = left
            t.dot   = dot
            t.right = right


        def write(t, w):
            t.left.write(w)
            w.write(t.dot + t.right)


    class ExpressionFunctionArguments_Blank(BaseTree):
        __slots__ = ((
            'left_parenthesis',
            'right_parenthesis',
        ))


        def __init__(t, left_parenthesis, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.right_parenthesis = right_parenthesis


        def write(t, w):
            w.write(t.left_parenthesis + t.right_parenthesis)


    class ExpressionFunctionArguments_One(BaseTree):
        __slots__ = ((
            'left_parenthesis',
            'first',
            'right_parenthesis',
        ))


        def __init__(t, left_parenthesis, first, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.first             = first
            t.right_parenthesis = right_parenthesis


        def write(t, w):
            w.write(t.left_parenthesis)
            t.first.write(w)
            w.write(t.right_parenthesis)


    class ExpressionFunctionCall(BaseTree):
        __slots__ = ((
            'left',
            'arguments',
        ))


        def __init__(t, left, arguments):
            t.left      = left
            t.arguments = arguments


        def write(t, w):
            t.left.write(w)
            t.arguments.write(w)


    class FunctionArguments_Blank(BaseTree):
        __slots__ = ((
            'left_parenthesis',
            'right_parenthesis',
        ))


        def __init__(t, left_parenthesis, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.right_parenthesis = right_parenthesis


        def write(t, w):
            w.write(t.left_parenthesis + t.right_parenthesis)


    class FunctionArguments_One(BaseTree):
        __slots__ = ((
            'left_parenthesis',
            'first',
            'right_parenthesis',
        ))


        def __init__(t, left_parenthesis, first, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.first             = first
            t.right_parenthesis = right_parenthesis


        def write(t, w):
            w.write(t.left_parenthesis)
            t.first.write(w)
            w.write(t.right_parenthesis)


    class FunctionArguments_Star(BaseTree):
        __slots__ = ((
            'star',
            'name',
        ))


        def __init__(t, star, name):
            t.star = star
            t.name = name


        def write(t, w):
            w.write(t.star + t.name)


    class FunctionArguments_Two(BaseTree):
        __slots__ = ((
            'left_parenthesis',
            'first',
            'first_comma',
            'second',
            'right_parenthesis',
        ))


        def __init__(t, left_parenthesis, first, first_comma, second, right_parenthesis):
            t.left_parenthesis  = left_parenthesis
            t.first             = first
            t.first_comma       = first_comma
            t.second            = second
            t.right_parenthesis = right_parenthesis


        def write(t, w):
            w.write(t.left_parenthesis)
            t.first.write(w)
            w.write(t.first_comma)
            t.second.write(w)
            w.write(t.right_parenthesis)


    class FunctionArguments_Three(BaseTree):
        __slots__ = ((
            'left_parenthesis',
            'first',
            'first_comma',
            'second',
            'second_comma',
            'third',
            'right_parenthesis',
        ))


        def __init__(
                t, left_parenthesis,
                first, first_comma, second, second_comma, third,
                right_parenthesis,
        ):
            t.left_parenthesis  = left_parenthesis
            t.first             = first
            t.first_comma       = first_comma
            t.second            = second
            t.second_comma      = second_comma
            t.third             = third
            t.right_parenthesis = right_parenthesis


        def write(t, w):
            w.write(t.left_parenthesis)
            t.first.write(w)
            w.write(t.first_comma)
            t.second.write(w)
            w.write(t.second_comma)
            t.third.write(w)
            w.write(t.right_parenthesis)


    class FunctionHeader(BaseTree):
        __slots__ = ((
            'indentation',
            'keyword',
            'name',
            'arguments',
            'colon',
            'newline'
        ))


        def __init__(t, indentation, keyword, name, arguments, colon, newline):
            t.indentation = indentation
            t.keyword     = keyword
            t.name        = name
            t.arguments   = arguments
            t.colon       = colon
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.keyword)
            t.name.write(w)
            t.arguments.write(w)
            w.write(t.colon + t.newline)


    class SlotDefinition(BaseTree):
        __slots__ =((
           'indentation',
           'quoted_name',
           'comma',
           'whitespace',
           'comment',
           'newline',
        ))


        def __init__(t, indentation, quoted_name, comma, whitespace, comment, newline):
            t.indentation = indentation
            t.quoted_name = quoted_name
            t.comma       = comma
            t.whitespace  = whitespace
            t.comment     = comment
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.quoted_name + t.comma + t.whitespace + t.comment + t.newline)

      
    class StatementAssign(BaseTree):
        __slots__ = ((
            'indentation',
            'left',
            'equal',
            'right',
            'newline'
        ))


        def __init__(t, indentation, left, equal, right, newline):
            t.indentation = indentation
            t.left        = left
            t.equal       = equal
            t.right       = right
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation)
            t.left.write(w)
            w.write(t.equal)
            t.right.write(w)
            w.write(t.newline)


    class StatementExpression(BaseTree):
        __slots__ = ((
            'indentation',
            'expression',
            'newline'
        ))


        def __init__(t, indentation, expression, newline):
            t.indentation = indentation
            t.expression  = expression
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation)
            t.expression.write(w)
            w.write(t.newline)


    class StatementIfHeader(BaseTree):
        __slots__ = ((
            'indentation',
            'keyword',
            'expression',
            'colon',
            'newline'
        ))


        def __init__(t, indentation, keyword, expression, colon, newline):
            t.indentation = indentation
            t.keyword     = keyword
            t.expression  = expression
            t.colon       = colon
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.keyword)
            t.expression.write(w)
            w.write(t.colon + t.newline)


    class StatementImport(BaseTree):
        __slots__ = ((
            'indentation',
            'keyword',
            'name',
            'newline'
        ))


        def __init__(t, indentation, keyword, name, newline):
            t.indentation = indentation
            t.keyword     = keyword
            t.name        = name
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.keyword)
            t.name.write(w)
            w.write(t.newline)


    class StatementPrintExpression(BaseTree):
        __slots__ = ((
            'indentation',
            'keyword',
            'expression',
            'newline'
        ))


        def __init__(t, indentation, keyword, expression, newline):
            t.indentation = indentation
            t.keyword     = keyword
            t.expression  = expression
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.keyword)
            t.expression.write(w)
            w.write(t.newline)


    class StatementRaiseExpression(BaseTree):
        __slots__ = ((
            'indentation',
            'keyword',
            'expression',
            'newline'
        ))


        def __init__(t, indentation, keyword, expression, newline):
            t.indentation = indentation
            t.keyword     = keyword
            t.expression  = expression
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.keyword)
            t.expression.write(w)
            w.write(t.newline)


    class StatementReturnExpression(BaseTree):
        __slots__ = ((
            'indentation',
            'keyword',
            'expression',
            'newline'
        ))


        def __init__(t, indentation, keyword, expression, newline):
            t.indentation = indentation
            t.keyword     = keyword
            t.expression  = expression
            t.newline     = newline


        def write(t, w):
            w.write(t.indentation + t.keyword)
            t.expression.write(w)
            w.write(t.newline)


    class StatementEndAssignSlots(BaseTree):
        __slots__ = ((
            'indentation',
            'right_parenthesis_1',
            'right_parenthesis_2',
            'newline'
        ))


        def __init__(t, indentation, right_parenthesis_1, right_parenthesis_2, newline):
            t.indentation         = indentation
            t.right_parenthesis_1 = right_parenthesis_1
            t.right_parenthesis_2 = right_parenthesis_2
            t.newline             = newline


        def write(t, w):
            w.write(t.indentation + t.right_parenthesis_1 + t.right_parenthesis_2 + t.newline)


    class StatementStartAssignSlots(BaseTree):
        __slots__ = ((
            'indentation',
            'left',
            'equal',
            'left_parenthesis_1',
            'left_parenthesis_2',
            'newline'
        ))


        def __init__(
                t, indentation, left, equal, left_parenthesis_1, left_parenthesis_2, newline,
        ):
            t.indentation        = indentation
            t.left               = left
            t.equal              = equal
            t.left_parenthesis_1 = left_parenthesis_1
            t.left_parenthesis_2 = left_parenthesis_2
            t.newline            = newline


        def write(t, w):
            w.write(t.indentation)
            t.left.write(w)
            w.write(t.equal + t.left_parenthesis_1 + t.left_parenthesis_2 + t.newline)


    class Symbol(BaseTree):
        __slots__ = ((
            'name',
        ))


        def __init__(t, name):
            t.name = name


        def write(t, w):
            w.write(t.name)


    all_data   = open('/home/joy/pyxie/.gem/Parser.py').read()
    data_lines = all_data.splitlines(True)


    for s in data_lines:
        for v in ((
                assign_binary_expression,
                assign_left_dot_member,
                assign_method_call,
                assign_name,
                assign_right_dot_member,
                blank_line,
                class_header,
                comment_line,
                end_assign_slots,
                function_header,
                nested_function_call,
                print_expression,
                raise_function_call,
                return_compile_pattern,
                return_function_call,
                return_name,
                slot_definition,
                start_assign_slots,
                statement_if_header,
                statement_import,
        )):
            if v.attempt(s):
                break
        else:
            for v in tree_many:
                v.write(standard_output)

            raise_error('%r', s)
