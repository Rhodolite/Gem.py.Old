def actualize_module():
    import  sys, types, __builtin__


    from ByteCode import find__byte_code
    from ByteCode import BYTE_CODE__LOAD_CONSTANT
    from ByteCode import byte_code__load_constant
    from MemberDescriptor import DEFINITION_TYPE__ADDRESS, DEFINITION_TYPE__INTEGER, DEFINITION_TYPE__REFERENCE
    from MemberDescriptor import produce__single_thread__new_MemberDescriptor
    from Pack import calculate_offset, calculate_pack_size, pack_format__Object


    #
    #   Python types
    #
    #
    Function = actualize_module.__class__
    String   = str                                              #   builtin
    Method   = types.MethodType
    Tuple    = tuple


    #
    #   Python functions
    #
    character             = chr                                 #   builtin
    compare               = cmp                                 #   builtin
    enumerate             = __builtin__.enumerate               #   builtin
    flush_standard_output = sys.stdout.flush
    function_closure      = Function.func_closure.__get__
    function_code         = Function.func_code.__get__
    function_defaults     = Function.func_defaults.__get__
    function_globals      = Function.func_globals.__get__
    function_name         = Function.func_name.__get__
    intern_string         = intern                              #   builtin
    introspection         = dir                                 #   builtin
    iterate               = iter                                #   builtin
    ordinal               = ord
    length                = len                                 #   builtin
    sorted                = __builtin__.sorted
    sum                   = __builtin__.sum
    python_modules        = sys.modules


    #
    #   Code: Object
    #       code_argument_count             integer
    #       code_number_locals              integer
    #       code_stack_size                 int eger
    #       code_flags                      integer
    #       code_byte_code                  String*
    #       code_constants                  Tuple*
    #       code_global_names               Tuple*
    #       code_local_names                Tuple*
    #       code_free_variables             Tuple*          - variables from nested function
    #       code_cell_variables             Tuple*          - variables to nested functions
    #       code_filename                   String*
    #       code_name                       String*
    #       code_first_line_number          integer
    #       code_line_number_table          String*
    #       code_zombie_frame               void*
    #
    Code = function_code(actualize_module).__class__

    offset__Code__argumemt_count    = calculate_offset(pack_format__Object, 'i')
    offset__Code__number_locals     = calculate_offset(pack_format__Object + 'i', 'i')
    offset__Code__stack_size        = calculate_offset(pack_format__Object + 'ii', 'i')
    offset__Code__flags             = calculate_offset(pack_format__Object + 'iii', 'i')
    offset__Code__byte_code         = calculate_offset(pack_format__Object + 'iiii', 'P')
    offset__Code__constants         = calculate_offset(pack_format__Object + 'iiiiP', 'P')
    offset__Code__global_names      = calculate_offset(pack_format__Object + 'iiiiPP', 'P')
    offset__Code__local_names       = calculate_offset(pack_format__Object + 'iiiiPPP', 'P')
    offset__Code__free_variables    = calculate_offset(pack_format__Object + 'iiiiPPPP', 'P')
    offset__Code__cell_variables    = calculate_offset(pack_format__Object + 'iiiiPPPPP', 'P')
    offset__Code__filename          = calculate_offset(pack_format__Object + 'iiiiPPPPPP', 'P')
    offset__Code__name              = calculate_offset(pack_format__Object + 'iiiiPPPPPPP', 'P')
    offset__Code__first_line_number = calculate_offset(pack_format__Object + 'iiiiPPPPPPPP', 'i')
    offset__Code__line_number_table = calculate_offset(pack_format__Object + 'iiiiPPPPPPPPi', 'P')
    offset__Code__zombie_frame      = calculate_offset(pack_format__Object + 'iiiiPPPPPPPPiP', 'P')

    assert calculate_pack_size(pack_format__Object + 'iiiiPPPPPPPPiPP') == Code.__basicsize__


    new_Code_MemberDescriptor = Method(produce__single_thread__new_MemberDescriptor(), Code)


    def new_Code_AddressDescriptor(member_name, offset):
        return new_Code_MemberDescriptor(member_name, DEFINITION_TYPE__ADDRESS, offset)


    def new_Code_IntegerDescriptor(member_name, offset):
        return new_Code_MemberDescriptor(member_name, DEFINITION_TYPE__INTEGER, offset)


    def new_Code_ReferenceDescriptor(member_name, offset):
        return new_Code_MemberDescriptor(member_name, DEFINITION_TYPE__REFERENCE, offset)


    slot__Code__argument_count    = new_Code_IntegerDescriptor  ('argument_count',    offset__Code__argumemt_count)
    slot__Code__number_locals     = new_Code_IntegerDescriptor  ('number_locals',     offset__Code__number_locals)
    slot__Code__stack_size        = new_Code_IntegerDescriptor  ('stack_size',        offset__Code__stack_size)
    slot__Code__flags             = new_Code_IntegerDescriptor  ('flags',             offset__Code__flags)
    slot__Code__byte_code         = new_Code_ReferenceDescriptor('byte_code',         offset__Code__byte_code)
    slot__Code__constants         = new_Code_ReferenceDescriptor('constants',         offset__Code__constants)
    slot__Code__global_names      = new_Code_ReferenceDescriptor('global_names',      offset__Code__global_names)
    slot__Code__local_names       = new_Code_ReferenceDescriptor('local_names',       offset__Code__local_names)
    slot__Code__free_variables    = new_Code_ReferenceDescriptor('free_variables',    offset__Code__free_variables)
    slot__Code__cell_variables    = new_Code_ReferenceDescriptor('cell_variables',    offset__Code__cell_variables)
    slot__Code__filename          = new_Code_ReferenceDescriptor('filename',          offset__Code__filename)
    slot__Code__name              = new_Code_ReferenceDescriptor('name',              offset__Code__name)
    slot__Code__first_line_number = new_Code_IntegerDescriptor  ('first_line_number', offset__Code__first_line_number)
    slot__Code__line_number_table = new_Code_ReferenceDescriptor('line_number_table', offset__Code__line_number_table)
    slot__Code__zombie_frame      = new_Code_AddressDescriptor  ('zombie_frame',      offset__Code__zombie_frame)

    fetch__Code__argument_count    = slot__Code__argument_count   .__get__
    fetch__Code__number_locals     = slot__Code__number_locals    .__get__
    fetch__Code__stack_size        = slot__Code__stack_size       .__get__
    fetch__Code__flags             = slot__Code__flags            .__get__
    fetch__Code__byte_code         = slot__Code__byte_code        .__get__
    fetch__Code__constants         = slot__Code__constants        .__get__
    fetch__Code__global_names      = slot__Code__global_names     .__get__
    fetch__Code__local_names       = slot__Code__local_names      .__get__
    fetch__Code__cell_variables    = slot__Code__cell_variables   .__get__
    fetch__Code__free_variables    = slot__Code__free_variables   .__get__
    fetch__Code__filename          = slot__Code__filename         .__get__
    fetch__Code__name              = slot__Code__name             .__get__
    fetch__Code__first_line_number = slot__Code__first_line_number.__get__
    fetch__Code__line_number_table = slot__Code__line_number_table.__get__
    fetch__Code__zombie_frame      = slot__Code__zombie_frame    .__get__

    list_0                = [0]


    def line(format, *arguments):
        print (format % arguments   if arguments else   format)

        flush_standard_output()


    constant_code__cache  = []
    append__constant_code = constant_code__cache.append
    find__constant_code   = constant_code__cache.__getitem__
    length__constant_code = constant_code__cache.__len__


    def conjure__constant_code(i):
        while length__constant_code() <= i:
            append__constant_code(intern_string(BYTE_CODE__LOAD_CONSTANT + character(i & 0xFF) + character(i >> 8)))

        return find__constant_code(i)


    constant_code__0 = conjure__constant_code(0)
        

    def x():
        return 5
        return 2 + 3.2


    x_code          = function_code(x)
    constants       = fetch__Code__constants(x_code)
    total_constants = length(constants)

    byte_code     = fetch__Code__byte_code(x_code)
    iterate_bytes = iterate(byte_code)
    next_byte     = iterate_bytes.next
    use_constants = list_0 * total_constants

    for c in iterate_bytes:
        b = find__byte_code(c)


        if b.has_argument:
            v = ordinal(next_byte()) + ordinal(next_byte()) * 256

            if b is byte_code__load_constant:
                use_constants[v] = 1

                line('load constant   #%d (%r)', v, constants[v])
                continue

            line('%-15s %d', b.name, v)
            continue

        line('%1s', b.name)

    total__use_constants = sum(use_constants)

    line('    constants: %r', constants)
    line('use_constants: %r', use_constants)
    line('total_constants: %d', total__use_constants)

    if total__use_constants is 0:
        new_constants = ()
    elif total__use_constants is 1:
        if total_constants is 1:
            new_constants = constants
        else:
            for [i, v] in enumerate(use_constants):
                if v is 1:
                    new_constants    = ((constants[i],))
                    use_constants[i] = constant_code__0
                    break
    else:
        assert 0

    line('new_constants: %r', new_constants)
    line('use_constants: %r', use_constants)


    def compare_constants(t, that):
        return (
               compare(type(t), type(that))
            or compare(t,       that)
        )


    if use_constant_0 is 0:
        total_constants = length(constants) - 1

        if total_constants is 0:
            new_constants = (())
        elif total_constants is 1:
            new_constants = ((constants[1],))
        else:
            iterate_constants = iterate(constants)
            iterate_constants.next()

            new_constants = Tuple(sorted(iterate_constants, compare_constants))

            next_constant = iterate(constants).next

            next_constant()

            for v in new_constants:
                if v is not next_constant():
                    break
            else:
                pass
    else:
        new_constants = Tuple(sorted(constants, compare_constants))

    line('new_constants: %r', new_constants)


    if 7:
        import dis

        dis.dis(x)



if 0:
    import dis

    dis.dis(actualize_module)


actualize_module()


del actualize_module
