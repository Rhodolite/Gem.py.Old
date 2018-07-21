def actualize_module():
    import struct


    Buffer           = buffer
    Code             = type(actualize_module.func_code)
    Function         = type(actualize_module)
    MemberDescriptor = type(Function.func_globals)
    Module           = type(struct)
    Object           = object
    Packer           = struct.Struct
    Property         = property
    Slice            = slice
    String           = str

    calculate_pack_size = struct.calcsize
    iterate             = iter
    length              = len
    none                = None
    object_address      = id
    

    provide_global = globals().setdefault


    def export(f, *arguments):
        if length(arguments) is 0:
            previous = provide_global(f.__name__, f)

            assert previous is f

            return f

        argument_iterator = iterate(arguments)
        next_argument     = argument_iterator.next

        assert f.__class__ is String

        w = next_argument()

        previous = provide_global(f, w)

        assert previous is w

        for v in argument_iterator:
            if v.__class__ is String:
                w        = next_argument()
                previous = provide_global(v, w)

                assert previous is w
                continue

            previous = (v.__name__, v)

            assert previous is v


    @export
    def calculate_offset(prefix, last):
        return calculate_pack_size(prefix + last) - calculate_pack_size(last)


    #
    #   Object
    #       reference_count: size_t
    #       object_type:     Object*
    #
    offset__Object__reference_count  = 0 
    offset__Object__object_type      = calculate_offset('L', 'P')
    pack_format__Object              = 'LP'


    assert calculate_pack_size(pack_format__Object) == Object.__basicsize__


    #
    #   VariableObject: Object
    #       extra_length: size_t
    #
    offset__Object__extra_length    = calculate_offset(pack_format__Object, 'L')
    pack_format__VariableObject     = pack_format__Object + 'L'


    #
    #   Buffer: Object
    #       buffer_base:      Object*
    #       buffer_pointer:   void*
    #       buffer_size:      size_t
    #       buffer_offset:    size_t
    #       buffer_read_only: integer
    #       buffer_hash;      long
    #
    offset__Buffer__buffer_base      = calculate_offset(pack_format__Object, 'P')
    offset__Buffer__buffer_pointer   = calculate_offset(pack_format__Object + 'P', 'P')
    #offset__Buffer__buffer_size      = calculate_offset(pack_format__Object + 'PP', 'L')
    #offset__Buffer__buffer_offset    = calculate_offset(pack_format__Object + 'PPL', 'L')
    #offset__Buffer__buffer_read_only = calculate_offset(pack_format__Object + 'PPLL', 'i')
    #offset__Buffer__buffer_hash      = calculate_offset(pack_format__Object + 'PPLLi', 'l')

    assert calculate_pack_size(pack_format__Object + 'PPLLil') == Buffer.__basicsize__


    #
    #   Code: Object
    #       code_argumemt_count             integer
    #       code_number_locals              integer
    #       code_stack_size                 int eger
    #       code_flags                      integer
    #       code_byte_code                  String*
    #       code_constants                  None* | Tuple*
    #       code_global_names               None* | Tuple*
    #       code_variable_names             None* | Tuple*
    #       code_cell_variables             None* | Tuple*
    #       code_free_variables             None* | Tuple*
    #       code_filename                   String*
    #       code_name                       String*
    #       code_first_line_number          integer
    #       code_line_number_table          String*
    #       code_zombie_frame               void*
    #
    offset__Code__code_argumemt_count    = calculate_offset(pack_format__Object, 'i')
    offset__Code__code_number_locals     = calculate_offset(pack_format__Object + 'i', 'i')
    offset__Code__code_stack_size        = calculate_offset(pack_format__Object + 'ii', 'i')
    offset__Code__code_flags             = calculate_offset(pack_format__Object + 'iii', 'i')
    offset__Code__code_byte_code         = calculate_offset(pack_format__Object + 'iiii', 'P')
    offset__Code__code_constants         = calculate_offset(pack_format__Object + 'iiiiP', 'P')
    offset__Code__code_global_names      = calculate_offset(pack_format__Object + 'iiiiPP', 'P')
    offset__Code__code_variable_names    = calculate_offset(pack_format__Object + 'iiiiPPP', 'P')
    offset__Code__code_cell_variables    = calculate_offset(pack_format__Object + 'iiiiPPPP', 'P')
    offset__Code__code_free_variables    = calculate_offset(pack_format__Object + 'iiiiPPPPP', 'P')
    offset__Code__code_filename          = calculate_offset(pack_format__Object + 'iiiiPPPPPP', 'P')
    offset__Code__code_name              = calculate_offset(pack_format__Object + 'iiiiPPPPPPP', 'P')
    offset__Code__code_first_line_number = calculate_offset(pack_format__Object + 'iiiiPPPPPPPP', 'i')
    offset__Code__code_line_number_table = calculate_offset(pack_format__Object + 'iiiiPPPPPPPPi', 'P')
    offset__Code__code_zombie_frame      = calculate_offset(pack_format__Object + 'iiiiPPPPPPPPiP', 'P')

    assert calculate_pack_size(pack_format__Object + 'iiiiPPPPPPPPiPP') == Code.__basicsize__


    #
    #   Function: Object
    #       function_code:                  Object*
    #       function_globals:               Object*
    #       function_defaults:              Object*
    #       function_closure:               Object*
    #       function_documentation:         Object*
    #       function_name:                  Object*
    #       function_map:                   Object*
    #       function_weak_reference_list:   Object*
    #       function_module:                Object*
    #
    #offset__Function__function_code                = calculate_offset(pack_format__Object, 'P')
    #offset__Function__function_globals             = calculate_offset(pack_format__Object + 'P', 'P')
    #offset__Function__function_defaults            = calculate_offset(pack_format__Object + 'PP', 'P')
    #offset__Function__function_closure             = calculate_offset(pack_format__Object + 'PPP', 'P')
    #offset__Function__function_documentation       = calculate_offset(pack_format__Object + 'PPPP', 'P')
    #offset__Function__function_name                = calculate_offset(pack_format__Object + 'PPPPP', 'P')
    #offset__Function__function_map                 = calculate_offset(pack_format__Object + 'PPPPPP', 'P')
    #offset__Function__function_weak_reference_list = calculate_offset(pack_format__Object + 'PPPPPPP', 'P')
    #offset__Function__function_module              = calculate_offset(pack_format__Object + 'PPPPPPPP', 'P')

    assert calculate_pack_size(pack_format__Object + 'PPPPPPPPP') == Function.__basicsize__


    #
    #   MemberDescriptor: Object
    #       member_type:        Type*
    #       member_name:        String*
    #       member_definition:  MemberDefinition*
    #
    offset__MemberDescriptor__member_type       = calculate_offset(pack_format__Object, 'P')
    offset__MemberDescriptor__member_name       = calculate_offset(pack_format__Object + 'P', 'P')
    offset__MemberDescriptor__member_definition = calculate_offset(pack_format__Object + 'PP', 'P')
    pack_format__MemberDescriptor               = pack_format__Object + 'PPP'

    assert calculate_pack_size(pack_format__MemberDescriptor) == MemberDescriptor.__basicsize__

    offset__ExtendedMemberDescriptor__MemberDefinition = calculate_offset(pack_format__MemberDescriptor, 'P')


    #
    #   MemberDefinition:
    #       name:               char const*
    #       type:               int
    #       offset:             size_t
    #       flags:              int
    #       documentation:      char const*
    #
    #   ExtendedMemberDescriptor: MemberDescriptor
    #       extended_definition: MemberDefinition
    #


    #
    #   Function: Object
    #       function_code: Object*
    #       function_globals: Object*
    #       function_defaults: Object*
    #       function_closure: Object*
    #       function_documentation: Object*
    #       function_name: Object*
    #       function_map: Object*
    #       function_weak_reference_list: Object*
    #       function_module: Object*
    #
    #offset__Function__function_code                = calculate_offset(pack_format__Object, 'P')
    #offset__Function__function_globals             = calculate_offset(pack_format__Object + 'P', 'P')
    #offset__Function__function_defaults            = calculate_offset(pack_format__Object + 'PP', 'P')
    #offset__Function__function_closure             = calculate_offset(pack_format__Object + 'PPP', 'P')
    #offset__Function__function_documentation       = calculate_offset(pack_format__Object + 'PPPP', 'P')
    #offset__Function__function_name                = calculate_offset(pack_format__Object + 'PPPPP', 'P')
    #offset__Function__function_map                 = calculate_offset(pack_format__Object + 'PPPPPP', 'P')
    #offset__Function__function_weak_reference_list = calculate_offset(pack_format__Object + 'PPPPPPP', 'P')
    #offset__Function__function_module              = calculate_offset(pack_format__Object + 'PPPPPPPP', 'P')

    assert calculate_pack_size(pack_format__Object + 'PPPPPPPPP') == Function.__basicsize__


    #
    #   Property: Object
    #       property_get:           Object*
    #       property_set:           Object*
    #       property_delete:        Object*
    #       property_documentation: Object*
    #       documentation_from_get: int
    #
    offset__Property__property_get           = calculate_offset(pack_format__Object, 'P')
    #offset__Property__property_set           = calculate_offset(pack_format__Object + 'P', 'P')
    #offset__Property__property_delete        = calculate_offset(pack_format__Object + 'PP', 'P')
    #offset__Property__property_documentation = calculate_offset(pack_format__Object + 'PPP', 'P')
    #offset__Property__documentation_from_get = calculate_offset(pack_format__Object + 'PPPP', 'i')

    assert calculate_offset(pack_format__Object + 'PPPPi', 'P') == Property.__basicsize__

    #
    #   Slice: Object
    #       start:      Object*
    #       stop:       Object*
    #       step:       Object*
    #
    #offset__Slice__start = calculate_offset(pack_format__Object, 'P')
    #offset__Slice__stop  = calculate_offset(pack_format__Object + 'P', 'P')
    offset__Slice__step  = calculate_offset(pack_format__Object + 'PP', 'P')

    assert calculate_pack_size(pack_format__Object + 'PPP') == Slice.__basicsize__


    #
    #   String: VariableObject
    #       string_hash:   long
    #       string_state:  integer
    #       string_buffer: character[...]
    #
    offset__String__string_hash   = calculate_offset(pack_format__VariableObject, 'l')
    offset__String__string_state  = calculate_offset(pack_format__VariableObject + 'l', 'i')
    offset__String__string_buffer = calculate_offset(pack_format__VariableObject + 'li', 'c')

    assert calculate_offset(pack_format__VariableObject + 'lic', 'P') == String.__basicsize__


    export(
        'calculate_pack_size',                                  calculate_pack_size,
        'offset__Buffer__buffer_base',                          offset__Buffer__buffer_base,
        'offset__Buffer__buffer_pointer',                       offset__Buffer__buffer_pointer,
        'offset__ExtendedMemberDescriptor__MemberDefinition',   offset__ExtendedMemberDescriptor__MemberDefinition,
        'offset__MemberDescriptor__member_definition',          offset__MemberDescriptor__member_definition,
        'offset__MemberDescriptor__member_name',                offset__MemberDescriptor__member_name,
        'offset__MemberDescriptor__member_type',                offset__MemberDescriptor__member_type,
        'offset__Object__object_type',                          offset__Object__object_type,
        'offset__Object__reference_count',                      offset__Object__reference_count,
        'offset__Property__property_get',                       offset__Property__property_get,
        'offset__Slice__step',                                  offset__Slice__step,
        'offset__String__string_buffer',                        offset__String__string_buffer,
        'Packer',                                               Packer,
        'pack_format__MemberDescriptor',                        pack_format__MemberDescriptor,
        'pack_format__Object',                                  pack_format__Object,
    )


actualize_module()


del actualize_module
