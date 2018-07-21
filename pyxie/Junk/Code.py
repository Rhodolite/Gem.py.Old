def actualize_module():
    import  sys, __builtin__


    #
    #   Python types
    #
    #
    Function = actualize_module.__class__
    String   = str                                              #   builtin


    #
    #   Python functions
    #
    flush_standard_output = sys.stdout.flush
    function_closure      = Function.func_closure.__get__
    function_code         = Function.func_code.__get__
    function_defaults     = Function.func_defaults.__get__
    function_globals      = Function.func_globals.__get__
    function_name         = Function.func_name.__get__
    intern_string         = intern                              #   builtin
    introspection         = dir                                 #   builtin
    iterate               = iter                                #   builtin
    length                = len                                 #   builtin
    python_modules        = sys.modules


    #
    #   Code
    #
    Code = function_code(actualize_module).__class__

    code_argument_count    = Code.co_argcount.__get__
    code_cell_vars         = Code.co_cellvars.__get__
    code_constants         = Code.co_consts.__get__
    code_filename          = Code.co_filename.__get__
    code_first_line_number = Code.co_firstlineno.__get__
    code_flags             = Code.co_flags.__get__
    code_free_variables    = Code.co_freevars.__get__
    code_global_names      = Code.co_names.__get__
    code_line_number_table = Code.co_lnotab.__get__
    code_name              = Code.co_name.__get__
    code_number_locals     = Code.co_nlocals.__get__
    code_stack_size        = Code.co_stacksize.__get__
    code_variable_names    = Code.co_varnames.__get__
    code_virtual_code      = Code.co_code.__get__


    def line(format, *arguments):
        print (format % arguments   if arguments else   format)

        flush_standard_output()


    def x(a, b):
        line('x(%r, %r)')
        return

        c = 2 + G + H

        def d():
            return c + code_name

        return d

    x_code = function_code(x)

    line('   argument count:  %r', code_argument_count(x_code))
    line('    number locals:  %r', code_number_locals(x_code))
    line('       stack size:  %r', code_stack_size(x_code))
    line('            flags:  %r', code_flags(x_code))
    line('     virtual code:  %r', code_virtual_code(x_code))
    line('        constants:  %r', code_constants(x_code))
    line('     global names:  %r', code_global_names(x_code))
    line('   variable names:  %r', code_variable_names(x_code))
    line('         filename:  %r', code_filename(x_code))
    line('             name:  %r', code_name(x_code))
    line('first line number:  %r', code_first_line_number(x_code))
    line('line number table:  %r', code_line_number_table(x_code))
    line('   free variables:  %r', code_free_variables(x_code))
    line('        cell vars:  %r', code_cell_vars(x_code))

    constants = code_constants(x_code)

    def add(a, b): return a  + b

    mine_1 = add('y', 'z')
    mine_2 = intern(add('y', 'z'))

    line('mine_1: %x', id(mine_1))
    line('mine_2: %x', id(mine_2))
    line('intern(mine_1): %x', id(intern(mine_1)))

    constants = (None, mine_1, 2, constants[3])

    y_code = Code(
                 code_argument_count(x_code),
                 code_number_locals(x_code),
                 code_stack_size(x_code),
                 code_flags(x_code),
                 code_virtual_code(x_code),
                 constants,
                 code_global_names(x_code),
                 code_variable_names(x_code),
                 code_filename(x_code),
                 code_name(x_code),
                 code_first_line_number(x_code),
                 code_line_number_table(x_code),
                 code_free_variables(x_code),
                 code_cell_vars(x_code),
             )

    line('constants[1]: %x', id(constants[1]))

    assert code_constants(y_code) is constants

    y = Function(
            y_code,
            function_globals(x),
            function_name(x),
            function_defaults(x),
            function_closure(x),
        )

    y(3, 5)

    #
    #   In the following '==', means it did not take our input value, but rewrote it
    #
    assert  code_argument_count(x_code)    is  code_argument_count(y_code)
    assert  code_number_locals(x_code)     is  code_number_locals(y_code)
    assert  code_stack_size(x_code)        is  code_stack_size(y_code)
    assert  code_flags(x_code)             is  code_flags(y_code)
    assert  code_virtual_code(x_code)      is  code_virtual_code(y_code)
    assert  code_constants(x_code)         is  code_constants(y_code)
    assert  code_global_names(x_code)      ==  code_global_names(y_code)
    assert  code_variable_names(x_code)    ==  code_variable_names(y_code)
    assert  code_filename(x_code)          is  code_filename(y_code)
    assert  code_name(x_code)              is  code_name(y_code)
    assert  code_first_line_number(x_code) is  code_first_line_number(y_code)
    assert  code_line_number_table(x_code) is  code_line_number_table(y_code)
    assert  code_free_variables(x_code)    ==  code_free_variables(y_code)
    assert  code_cell_vars(x_code)         ==  code_cell_vars(y_code)


actualize_module()
