def actualize_module():
    import  ctypes, sys, __builtin__, struct, types


    #
    #   Python types
    #
    #
    Buffer    = buffer
    Integer   = int
    Function  = actualize_module.__class__
    FrozenSet = frozenset                                       #   Builtin
    Method    = types.MethodType
    NoneType  = type(None)                                      #   Builtin
    Object    = object                                          #   builtin
    String    = str                                             #   builtin
    Type      = type                                            #   builtin


    None_or_String = FrozenSet([NoneType, String])


    #
    #   Python functions
    #
    delete_attribute      = delattr
    flush_standard_output = sys.stdout.flush
    function_closure      = Function.func_closure.__get__
    function_code         = Function.func_code.__get__
    function_defaults     = Function.func_defaults.__get__
    function_globals      = Function.func_globals.__get__
    function_name         = Function.func_name.__get__
    hash                  = __builtin__.hash
    intern_string         = intern                              #   builtin
    introspection         = dir                                 #   builtin
    iterate               = iter                                #   builtin
    length                = len                                 #   builtin
    maximum               = max
    object_address        = id
    pack                  = struct.pack
    python_modules        = sys.modules
    reference_count       = sys.getrefcount


    #
    #   Python values
    #
    none = None                                             #   builtin


    #
    #   Code
    #
    Code = function_code(actualize_module).__class__

    code__argument_count    = Code.co_argcount.__get__
    code__cell_vars         = Code.co_cellvars.__get__
    code__constants         = Code.co_consts.__get__
    code__filename          = Code.co_filename.__get__
    code__first_line_number = Code.co_firstlineno.__get__
    code__flags             = Code.co_flags.__get__
    code__free_variables    = Code.co_freevars.__get__
    code__global_names      = Code.co_names.__get__
    code__line_number_table = Code.co_lnotab.__get__
    code__name              = Code.co_name.__get__
    code__number_locals     = Code.co_nlocals.__get__
    code__stack_size        = Code.co_stacksize.__get__
    code__variable_names    = Code.co_varnames.__get__
    code__virtual_code      = Code.co_code.__get__


    def arrange(format, *arguments):
        return (format % arguments   if arguments else   format)


    def line(format, *arguments):
        print (format % arguments   if arguments else   format)

        flush_standard_output()

    #
    #   C Types
    #
    C_Boolean           = ctypes.c_bool
    C_Character         = ctypes.c_char
    C_Character_Pointer = ctypes.c_char_p
    C_Integer           = ctypes.c_int
    C_Long              = ctypes.c_long
    C_Python_Function   = ctypes.PYFUNCTYPE
    C_Size_Type         = ctypes.c_size_t
    C_Structure         = ctypes.Structure
    C_Pointer_Void      = ctypes.c_void_p

    #
    #   C functions
    #
    c_alignment   = ctypes.alignment
    c_cast        = ctypes.cast
    c_memory_move = ctypes.memmove
    c_memory_set  = ctypes.memset
    c_size_of     = ctypes.sizeof
    c_string_at   = ctypes.string_at
    C_Pointer     = ctypes.POINTER            #   Creates a type, so starts with capital 'C'


    #
    #   Values
    #
    c_python_api         = ctypes.pythonapi
    c_pointer_type_cache = ctypes._pointer_type_cache


    #
    #   Derived C Types
    #
    C_Pointer_Integer    = C_Pointer(C_Integer)
    C_Pointer_Long       = C_Pointer(C_Long)
    C_Pointer__Size_Type = C_Pointer(C_Size_Type)


    #
    #   C_PythonMemberDefinition
    #
    class C_PythonMemberDefinition(C_Structure):
        __slots__ = (())

    C_Pointer_PythonMemberDefinition = C_Pointer(C_PythonMemberDefinition)

    DEFINITION_FLAGS__READ_WRITE            = 0
    DEFINITION_FLAGS__READ_ONLY             = 1
    DEFINITION_FLAGS__READ_RESTRICTED       = 2
    DEFINITION_FLAGS__WRITE_RESTRICTED      = 4
    DEFINITION_FLAGS__READ_WRITE_RESTRICTED = DEFINITION_FLAGS__READ_RESTRICTED | DEFINITION_FLAGS__WRITE_RESTRICTED

    DEFINITION_TYPE__SHORT              = 0
    DEFINITION_TYPE__INTEGER            = 1
    DEFINITION_TYPE__LONG               = 2
    DEFINITION_TYPE__FLOAT              = 3
    DEFINITION_TYPE__DOUBLE             = 4
    DEFINITION_TYPE__STRING             = 5
    DEFINITION_TYPE__OBJECT             = 6
    DEFINITION_TYPE__CHARACTER          = 7
    DEFINITION_TYPE__BYTE               = 8
    DEFINITION_TYPE__UNSIGNED_BYTE      = 9
    DEFINITION_TYPE__UNSIGNED_SHORT     = 10
    DEFINITION_TYPE__UNSIGNED_INTEGER   = 11
    DEFINITION_TYPE__UNSIGNED_LONG      = 12
    DEFINITION_TYPE__STRING_IN_PLACE    = 13
    DEFINITION_TYPE__BOOLEAN            = 14
    #DEFINITION_TYPE__15                = 15
    DEFINITION_TYPE__OBJECT_EXTENDED    = 16
    DEFINITION_TYPE__LONG_LONG          = 17
    DEFINITION_TYPE__UNSIGNED_LONG_LONG = 18
    DEFINITION_TYPE__SIZE_TYPE          = 19


    lookup_member_flags = {
        DEFINITION_FLAGS__READ_WRITE            : intern_string('READ_WRITE'),
        DEFINITION_FLAGS__READ_ONLY             : intern_string('READ_ONLY'),
        DEFINITION_FLAGS__READ_RESTRICTED       : intern_string('READ_RESTRICTED'),
        DEFINITION_FLAGS__WRITE_RESTRICTED      : intern_string('WRITE_RESTRICTED'),
        DEFINITION_FLAGS__READ_WRITE_RESTRICTED : intern_string('READ_AND_WRITE_RESTRICTED'),
    }.get


    lookup_member_type = {
        DEFINITION_TYPE__SHORT              : intern_string('SHORT'),
        DEFINITION_TYPE__INTEGER            : intern_string('INTEGER'),
        DEFINITION_TYPE__LONG               : intern_string('LONG'),
        DEFINITION_TYPE__FLOAT              : intern_string('FLOAT'),
        DEFINITION_TYPE__DOUBLE             : intern_string('DOUBLE'),
        DEFINITION_TYPE__STRING             : intern_string('STRING'),
        DEFINITION_TYPE__OBJECT             : intern_string('OBJECT'),
        DEFINITION_TYPE__CHARACTER          : intern_string('CHARACTER'),
        DEFINITION_TYPE__BYTE               : intern_string('BYTE'),
        DEFINITION_TYPE__UNSIGNED_BYTE      : intern_string('UNSIGNED_BYTE'),
        DEFINITION_TYPE__UNSIGNED_SHORT     : intern_string('UNSIGNED_SHORT'),
        DEFINITION_TYPE__UNSIGNED_INTEGER   : intern_string('UNSIGNED_INTEGER'),
        DEFINITION_TYPE__UNSIGNED_LONG      : intern_string('UNSIGNED_LONG'),
        DEFINITION_TYPE__STRING_IN_PLACE    : intern_string('STRING_IN_PLACE'),
        DEFINITION_TYPE__BOOLEAN            : intern_string('BOOLEAN'),

        DEFINITION_TYPE__OBJECT_EXTENDED    : intern_string('OBJECT_EXTENDED'),
        DEFINITION_TYPE__LONG_LONG          : intern_string('LONG_LONG'),
        DEFINITION_TYPE__UNSIGNED_LONG_LONG : intern_string('UNSIGNED_LONG_LONG'),
        DEFINITION_TYPE__SIZE_TYPE          : intern_string('SIZE_TYPE'),
    }.get


    #
    #   More: Sizes & Alignment
    #
    alignment__Pointer_Void = c_alignment(C_Pointer_Void)
    size__Pointer_Void      = c_size_of  (C_Pointer_Void)

    use_pointers = 0
    use_shift    = 0

    if (
            (
                   size__Pointer_Void
                is c_size_of(C_Pointer_PythonMemberDefinition)
                is c_size_of(C_Pointer_Long)
                is c_size_of(C_Pointer__Size_Type)
            )
        and (
                   alignment__Pointer_Void
                is c_alignment(C_Pointer_PythonMemberDefinition)
                is c_alignment(C_Pointer_Long)
                is c_alignment(C_Pointer__Size_Type)
            )
    ):
        alignment__Long    = c_alignment(C_Long)
        alignment_m1__Long = alignment__Long - 1
        size__Long         = c_size_of(C_Long)
        mask__Long         = ~alignment_m1__Long

        if size__Long is size__Pointer_Void:
            C_Pointer_Address        = C_Pointer_Long
            DEFINITION_TYPE__ADDRESS = DEFINITION_TYPE__LONG

            alignment_m1__Character = c_alignment(C_Character) - 1
            mask__Character         = ~alignment_m1__Character
            size__Character         = c_size_of  (C_Character)

            alignment__Integer    = c_alignment(C_Integer)
            alignment_m1__Integer = alignment__Integer
            mask__Integer         = ~alignment_m1__Integer
            size__Integer         = c_size_of  (C_Integer)

            alignment__Pointer    = alignment__Pointer_Void
            alignment_m1__Pointer = alignment__Pointer - 1
            mask__Pointer         = ~alignment_m1__Pointer
            size__Pointer         = size__Pointer_Void

            alignment__Size_Type    = c_alignment(C_Size_Type)
            alignment_m1__Size_Type = alignment__Size_Type - 1
            mask__Size_Type         = ~alignment_m1__Size_Type
            size__Size_Type         = c_size_of  (C_Size_Type)


            def align__Character(offset):
                v = (offset + alignment_m1__Character) & mask__Character

                return ((v, v + size__Character))


            def align__Integer(offset):
                v = (offset + alignment_m1__Integer) & mask__Integer

                return ((v, v + size__Integer))


            def align__Long(offset):
                v = (offset + alignment_m1__Long) & mask__Long

                return ((v, v + size__Long))


            def align__Pointer(offset):
                v = (offset + alignment_m1__Pointer) & mask__Pointer

                return ((v, v + size__Pointer))


            def align__Size_Type(offset):
                v = (offset + alignment_m1__Size_Type) & mask__Size_Type

                return ((v, v + size__Size_Type))


            use_pointers = 7

            if (
                    alignment__Integer      is size__Integer
                and alignment__Long         is size__Long
                and alignment__Size_Type    is size__Size_Type
                and alignment__Pointer_Void is size__Pointer
            ):
                get_shift = { 1 : 0, 2 : 1, 4 : 2, 8 : 3, 16 : 4 }.get

                shift__Integer   = get_shift(size__Integer)
                shift__Long      = get_shift(size__Long)
                shift__Size_Type = get_shift(size__Size_Type)
                shift__Pointer   = get_shift(size__Pointer)

                if (
                        shift__Integer   is not none
                    and shift__Long      is not none
                    and shift__Size_Type is not none
                    and shift__Pointer   is not none
                ):
                    use_shift = 7

    use_structure = (0   if use_pointers is 7 else   7)
    use_structure = 7
    #use_shift     = 0


    if use_shift is 7:
        pointer__address   = c_cast(size__Pointer, C_Pointer_Address)
        pointer__integer   = c_cast(size__Integer, C_Pointer_Integer)
        pointer__long      = c_cast(size__Long,    C_Pointer_Long)
        pointer__size_type = c_cast(size__Pointer, C_Pointer__Size_Type)


        def peek_address(address, offset):
            return pointer__address[(address + offset >> shift__Pointer) - 1]


        def peek_integer(address, offset):
            return pointer__integer[(address + offset >> shift__Integer) - 1]


        def peek_long(address, offset):
            return pointer__long[(address + offset >> shift__Long) - 1]


        #
        #   Returns: Integer | Long
        #
        #       'ctypes' returns a Long: If sufficiently small (usually) convert to Integer
        #
        def peek_size_type(address, offset):
            return Integer(pointer__size_type[(address + offset >> shift__Size_Type) - 1])


        def poke_address(address, offset, value):
            pointer__address[(address + offset >> shift__Pointer) - 1] = value


        def poke_integer(address, offset, value):
            pointer__integer[(address + offset >> shift__Integer) - 1] = value


        def poke_size_type(address, offset, value):
            pointer__size_type[(address + offset >> shift__Size_Type) - 1] = value


        def build__peek_address__and__poke_address(address):
            def peek():
                return pointer__address[(address >> shift__Pointer) - 1]


            def poke(value):
                pointer__address[(address >> shift__Pointer) - 1] = value


            return ((peek, poke))


    elif use_pointers is 7:
        def peek_address(address, offset):
            return c_cast(address + offset, C_Pointer_Address)[0]


        def peek_integer(address, offset):
            return c_cast(address + offset, C_Pointer_Integer)[0]


        def peek_long(address, offset):
            return c_cast(address + offset, C_Pointer_Long)[0]


        #
        #   Returns: Integer | Long
        #
        #       'ctypes' returns a Long: If sufficiently small (usually) convert to Integer
        #
        def peek_size_type(address, offset):
            return Integer(c_cast(address + offset, C_Pointer__Size_Type)[0])


        def poke_address(address, offset, value):
            c_cast(address + offset, C_Pointer_Address)[0] = value


        def poke_integer(address, offset, value):
            c_cast(address + offset, C_Integer)[0] = value


        def poke_size_type(address, offset, value):
            c_cast(address + offset, C_Size_Type)[0] = value


        def build__peek_address__and__poke_address(address):
            pointer_address = c_cast(address, C_Pointer_Address)

            return ((
                       Method(pointer_address.__getitem__, 0),
                       Method(pointer_address.__setitem__, 0)
                   ))


    if __debug__:
        def peek_string(address, offset):
            v = peek_address(address, offset)

            assert v is not 0

            return c_string_at(v)
    else:
        def peek_string(address, offset):
            return c_string_at(peek_address(address, offset))


    if 0:
        def peek_address_and_string(address, offset = 0):
            v = peek_address(address, offset)

            assert v is not 0

            return (( v, c_string_at(v) ))


    def peek_string_or_none(address, offset):
        v = peek_address(address, offset)

        if v is 0:
            return none

        return c_string_at(v)


    #
    #
    #
    class ReferenceObject(Object):
        __slots__ = (('reference',))


    #
    #   Create pointer__reference_object__object
    #
    reference_object     = ReferenceObject()
    reference_descriptor = ReferenceObject.reference
    get_reference        = Method(reference_descriptor.__get__,    reference_object)
    delete_reference     = Method(reference_descriptor.__delete__, reference_object)
    save_reference       = Method(reference_descriptor.__set__,    reference_object)

    if use_pointers is 7:
        address__reference_object = object_address(reference_object)

        [offset__Object__reference_count, next]             = align__Size_Type(0)
        [offset__Object__type, unaligned_size__Object_type] = align__Pointer(next)

        [offset__VariableObject__size, unaligned_size__VariableObject] = align__Size_Type(unaligned_size__Object_type)

        [offset__String__hash, next]  = align__Long(unaligned_size__VariableObject)
        [offset__String__state, next] = align__Integer(next)
        [offset__String__string, J]   = align__Character(next)

        [offset__ReferenceObject__object, next] = align__Pointer(unaligned_size__Object_type)

        [scan_reference, overwrite_reference] = build__peek_address__and__poke_address(
                                                    address__reference_object + offset__ReferenceObject__object,
                                                )


        wipe_reference = Method(overwrite_reference, 0)


        #
        #   Convert an address to a python object (second routine also decrements the reference count of the object).
        #
        def address_to_object(address):
            overwrite_reference(address)

            r = get_reference()

            wipe_reference()

            return r


        def address_to_object_and_steal_reference(address):
            overwrite_reference(address)

            r = get_reference()

            #
            #   'delete' will steal the reference.  This is safe (i.e.: object will not be deleted) since 'r' is storing
            #   an extra reference.
            #
            delete_reference()

            return r


        def peek_object(address, offset):
            return address_to_object(peek_address(address, offset))


        def poke_object(address, offset, object):
            save_reference(object)              #   Increment reference count
            wipe_reference()                    #   And lose track of this object (so reference count increments)

            poke_address(address, offset, object_address(object))


        def poke_object__no_reference(address, offset, object):
            poke_address(address, offset, object_address(object))
            


        #
        #   Since reference_object.reference is uninitialized, its value is 0 which means 'NULL'.
        #
        assert peek_size_type(address__reference_object, offset__Object__reference_count) is 4
        assert peek_object   (address__reference_object, offset__Object__type)            is ReferenceObject
        assert scan_reference()                                                           is 0

        if __debug__:
            string_object         = 'hello 77'
            address_string_object = object_address(string_object)

            assert peek_size_type(address_string_object, offset__Object__reference_count) is reference_count(string_object) - 1 
            assert peek_object   (address_string_object, offset__Object__type)            is String
            assert peek_size_type(address_string_object, offset__VariableObject__size)    is 8
            assert hash(string_object) == peek_long(address_string_object, offset__String__hash)    #  call hash' first
            assert 0 <= peek_integer(address_string_object, offset__String__state) <= 2
            assert c_string_at(address_string_object + offset__String__string) == string_object


    #
    #   PythonMemberDescriptor:
    #       reference_count:    size_t                      #   Inherited from PythonObject
    #       type:               PythonTypeObject*           #   Inherited from PythonObject
    #       member_type:        PythonTypeObject*
    #       member_name:        PythonStringObject*
    #       member_definition:  PythonMemberDefinition*
    #
    #   PythonMemberDefinition:
    #       name:               char const*
    #       type:               int
    #       offset:             size_t
    #       flags:              int
    #       documentation:      char const*
    #
    MemberDescriptor = type(reference_descriptor)

    if use_pointers is 7:
        #
        #   PythonMemberDescriptor
        #
        [offset__PythonMemberDescriptor__member_type, next] = align__Pointer(unaligned_size__Object_type)
        [offset__PythonMemberDescriptor__member_name, next] = align__Pointer(next)
        [offset__PythonMemberDescriptor__member_definition, unaligned_size__PythonMemberDescriptor] = align__Pointer(next)

        member_descriptor_address = object_address(reference_descriptor)

        assert (
                   peek_size_type(member_descriptor_address, offset__Object__reference_count)
                == reference_count(reference_descriptor) - 1
            )
        assert peek_object(member_descriptor_address, offset__Object__type) is MemberDescriptor
        assert (
                   peek_object(member_descriptor_address, offset__PythonMemberDescriptor__member_type)
                is reference_descriptor.__objclass__
                is ReferenceObject
            )
        assert (
                   peek_object(member_descriptor_address, offset__PythonMemberDescriptor__member_name)
                is reference_descriptor.__name__
            )

        member_definition_address = peek_address(
                                        member_descriptor_address, offset__PythonMemberDescriptor__member_definition
                                    )

        #
        #   PythonMemberDefinition
        #
        [offset__PythonMemberDefinition__name,          next] = align__Pointer(0)
        [offset__PythonMemberDefinition__type,          next] = align__Integer(next)
        [offset__PythonMemberDefinition__offset,        next] = align__Size_Type(next)
        [offset__PythonMemberDefinition__flags,         next] = align__Integer(next)
        [offset__PythonMemberDefinition__documentation, next] = align__Pointer(next)


        alignment__PythonMemberDefinition      = maximum(alignment__Pointer_Void, alignment__Integer, alignment__Size_Type)
        alignment_m1__PythonMemberDefinition   = alignment__PythonMemberDefinition - 1
        mask__PythonMemberDefinition           = ~alignment_m1__PythonMemberDefinition
        size__PythonMemberDefinition           = (next + alignment_m1__PythonMemberDefinition) & mask__PythonMemberDefinition
        unaligned_size__PythonMemberDefinition = next


        def align__PythonMemberDefinition(offset):
            v = (offset + alignment_m1__PythonMemberDefinition) & mask__PythonMemberDefinition

            return ((v, v + size__PythonMemberDefinition))


        assert peek_string   (member_definition_address, offset__PythonMemberDefinition__name)    == reference_descriptor.__name__
        assert peek_integer  (member_definition_address, offset__PythonMemberDefinition__type)   is 16
        assert peek_size_type(member_definition_address, offset__PythonMemberDefinition__offset) == offset__ReferenceObject__object
        assert peek_integer  (member_definition_address, offset__PythonMemberDefinition__flags)         is 0
        assert peek_address  (member_definition_address, offset__PythonMemberDefinition__documentation) is 0


        if use_structure is 7:
            C_PythonMemberDefinition._fields_ = ((
                                                    (('name',   C_Character_Pointer)),
                                                    (('type',   C_Integer)),
                                                    (('offset', C_Size_Type)),            #  Converts to Python Long
                                                    (('flags',  C_Integer)),
                                                    (('doc',    C_Character_Pointer)),
                                                ))

            member_definition = c_cast(member_definition_address, C_Pointer_PythonMemberDefinition).contents

            assert member_definition.name   == reference_descriptor.__name__
            assert member_definition.type   is 16
            assert member_definition.offset == offset__ReferenceObject__object
            assert member_definition.flags  is 0
            assert member_definition.doc    is none


    #
    #   Use 'c_cast' to force the creation of a NEW function pointer, so we don't share it with any
    #   other code by mistake.
    #
    GarbageCollection_MemoryAllocate = c_cast(
                                           c_python_api._PyObject_GC_Malloc,
                                           C_Python_Function(C_Pointer_Void, C_Size_Type),
                                       )
    GarbageCollection_Track          = c_cast(c_python_api.PyObject_GC_Track, C_Python_Function(none, C_Pointer_Void))

    [adjust__PythonMemberDefinition, J] = align__PythonMemberDefinition(unaligned_size__PythonMemberDescriptor)
    unaligned_adjust__name_buffer       = adjust__PythonMemberDefinition + unaligned_size__PythonMemberDefinition
    [adjust__name_buffer,            J] = align__Character(unaligned_adjust__name_buffer)


    def dump_MemberDescriptor(member_descriptor):
        assert member_descriptor.__class__ is MemberDescriptor

        member_descriptor_address = object_address(member_descriptor)
        member_definition_address = peek_address(
                                        member_descriptor_address, offset__PythonMemberDescriptor__member_definition
                                    )

        assert peek_object(member_descriptor_address, offset__Object__type) is MemberDescriptor
        assert peek_string(member_definition_address, offset__PythonMemberDefinition__name) == member_descriptor.__name__

        member_type  = peek_integer(member_definition_address, offset__PythonMemberDefinition__type)
        member_flags = peek_integer(member_definition_address, offset__PythonMemberDefinition__flags)

        line('=== Dump of MemberDescriptor ===')
        line('  references:  %d', peek_size_type(member_descriptor_address, offset__Object__reference_count))
        line(' member_type:  %r', peek_object(member_descriptor_address, offset__PythonMemberDescriptor__member_type))
        line(' member_name:  %r', peek_object(member_descriptor_address, offset__PythonMemberDescriptor__member_name))

        line('            definition_type:  %r (%s)', member_type, lookup_member_type(member_type, '?'))

        line('          definition_offset:  %r',
             peek_size_type(member_definition_address, offset__PythonMemberDefinition__offset))

        line('           definition_flags:  %r (%s)', member_flags, lookup_member_flags(member_flags, '?'))

        line('   definition_documentation:  %r',
             peek_string_or_none(member_definition_address, offset__PythonMemberDefinition__documentation))


    if 0:
        dump_MemberDescriptor(Code.co_names)


    def new_MemberDescriptor(member_type, member_name, definition_type, offset, flags = 0, documentation = none):
        if __debug__:
            assert type(documentation) in None_or_String
        else:
            documentation = none

        member_name = intern_string(member_name)
        size        = (
                          unaligned_adjust__name_buffer    if documentation is none else
                          adjust__name_buffer + size__Character * (length(documentation) + 1)
                      )

        member_descriptor_address = GarbageCollection_MemoryAllocate(size)
        member_definition_address = member_descriptor_address + adjust__PythonMemberDefinition

        c_memory_set(member_descriptor_address, 0, size)

        if 0:
            line('new_MemberDescriptor: %s.%s %s @%d %s %s: allocate %d => %#x, %#x',
                 member_type, member_name, lookup_member_type(definition_type), offset, lookup_member_flags(flags),
                 (
                    'none'   if documentation is none else
                    arrange('%r<%d>', documentation, size__Character * (length(documentation) + 1))
                 ),
                 size, member_descriptor_address, member_definition_address)


        #
        #   PythonMemberDescriptor
        #
        poke_size_type           (member_descriptor_address, offset__Object__reference_count, 1)
        poke_object__no_reference(member_descriptor_address, offset__Object__type, MemberDescriptor)
        poke_object              (member_descriptor_address, offset__PythonMemberDescriptor__member_type, member_type)
        poke_object              (member_descriptor_address, offset__PythonMemberDescriptor__member_name, member_name)

        poke_address(
            member_descriptor_address,
            offset__PythonMemberDescriptor__member_definition,
            member_definition_address,
        )


        #
        #   PythonMemberDefinition
        #
        poke_address(
            member_definition_address,
            offset__PythonMemberDefinition__name,
            object_address(member_name) + offset__String__string
        )

        poke_integer  (member_definition_address, offset__PythonMemberDefinition__type,   definition_type)
        poke_size_type(member_definition_address, offset__PythonMemberDefinition__offset, offset)
        poke_integer  (member_definition_address, offset__PythonMemberDefinition__flags,  flags)

        if documentation is none:
            poke_address(member_definition_address, offset__PythonMemberDefinition__documentation, 0)

            assert size == adjust__PythonMemberDefinition + offset__PythonMemberDefinition__documentation + 8
        else:
            buffer_address = member_descriptor_address + adjust__name_buffer

            poke_address(
                member_definition_address,
                offset__PythonMemberDefinition__documentation,
                buffer_address,
            )

            c_memory_move(
                buffer_address,
                object_address(documentation) + offset__String__string,
                size__Character * (length(documentation) + 1),
            )

            assert buffer_address + size__Character * (length(documentation) + 1) - member_descriptor_address == size


        #
        #   It's not clear if its ok to use 'GarbageCollection_Track' if the refernece count is zero
        #   (what would happen if another thread did garbage collection and saw this object with no reference count??):
        #
        #       Therefore, above, the reference count is initialized to '1'.  And we use 'address_to_object_and_steal_reference'
        #       below, which will "steal" out refernece count of 1 -- and "return" the object with a reference count of 1
        #       (i.e.: without incrementing it to 2).
        #   
        #
        GarbageCollection_Track(member_descriptor_address)

        return address_to_object_and_steal_reference(member_descriptor_address)


    def copy_MemberDescriptor(t, flags = 0, documentation = none):
        t__member_definition_address = peek_address(object_address(t), offset__PythonMemberDescriptor__member_definition)

        return new_MemberDescriptor(
                   t.__objclass__,
                   t.__name__,
                   peek_address(t__member_definition_address, offset__PythonMemberDefinition__type),
                   peek_address(t__member_definition_address, offset__PythonMemberDefinition__offset),
                   flags,
                   documentation
               )

    if __debug__:
        Object__reference_count = new_MemberDescriptor(
                                      Object,
                                      'reference_count',
                                      DEFINITION_TYPE__SIZE_TYPE,
                                      offset__Object__reference_count,
                                      0,
                                      'Read/Write Object.reference_count',
                                  )

        Object__object_type = new_MemberDescriptor(
                                  Object,
                                  'object_type',
                                  DEFINITION_TYPE__OBJECT,
                                  offset__Object__type,
                                  0,
                                  'Read/Write Object.object_type',
                              )

        assert Object__reference_count.__get__(reference_object) == reference_count(reference_object)
        assert Object__object_type    .__get__(reference_object) is ReferenceObject


    PythonMemberDescriptor__member_type = new_MemberDescriptor(
                                              MemberDescriptor,
                                              'member_type',
                                              DEFINITION_TYPE__OBJECT,
                                              offset__PythonMemberDescriptor__member_type,
                                              0,
                                              'Read/Write Object.member_type',
                                          )
    PythonMemberDescriptor__member_name = new_MemberDescriptor(
                                              MemberDescriptor,
                                              'member_name',
                                              DEFINITION_TYPE__OBJECT,
                                              offset__PythonMemberDescriptor__member_name,
                                              0,
                                              'Read/Write Object.member_name',
                                          )
    PythonMemberDescriptor__member_definition = new_MemberDescriptor(
                                                    MemberDescriptor,
                                                    'member_definition',
                                                    DEFINITION_TYPE__ADDRESS,
                                                    offset__PythonMemberDescriptor__member_definition,
                                                    0,
                                                    'Read/Write Object.member_definition',
                                                )
    adjusted__PythonMemberDefinition__name = new_MemberDescriptor(
                                                 MemberDescriptor,
                                                 'definition_name',
                                                 DEFINITION_TYPE__ADDRESS,
                                                 adjust__PythonMemberDefinition + offset__PythonMemberDefinition__name,
                                                 0,
                                                 'Read/Write MemberDescriptor.MemberDefinition.name',
                                             )
    adjusted__PythonMemberDefinition__type = new_MemberDescriptor(
                                                 MemberDescriptor,
                                                 'definition_type',
                                                 DEFINITION_TYPE__INTEGER,
                                                 adjust__PythonMemberDefinition + offset__PythonMemberDefinition__type,
                                                 0,
                                                 'Read/Write MemberDescriptor.MemberDefinition.type',
                                             )
    adjusted__PythonMemberDefinition__offset = new_MemberDescriptor(
                                                   MemberDescriptor,
                                                   'definition_offset',
                                                   DEFINITION_TYPE__SIZE_TYPE,
                                                   (
                                                         adjust__PythonMemberDefinition
                                                       + offset__PythonMemberDefinition__offset
                                                   ),
                                                   0,
                                                   'Read/Write MemberDescriptor.MemberDefinition.offset',
                                               )
    adjusted__PythonMemberDefinition__flags = new_MemberDescriptor(
                                                  MemberDescriptor,
                                                  'definition_flags',
                                                  DEFINITION_TYPE__INTEGER,
                                                  (
                                                        adjust__PythonMemberDefinition
                                                      + offset__PythonMemberDefinition__flags
                                                  ),
                                                  0,
                                                  'Read/Write MemberDescriptor.MemberDefinition.flags',
                                              )
    adjusted__PythonMemberDefinition__documentation = new_MemberDescriptor(
                                                          MemberDescriptor,
                                                          'definition_flags',
                                                          DEFINITION_TYPE__ADDRESS,
                                                          (
                                                                adjust__PythonMemberDefinition
                                                              + offset__PythonMemberDefinition__documentation
                                                          ),
                                                          0,
                                                          'Read/Write MemberDescriptor.MemberDefinition.flags',
                                                      )
    assert PythonMemberDescriptor__member_type.__get__(reference_descriptor) is ReferenceObject
    assert PythonMemberDescriptor__member_name.__get__(reference_descriptor) == 'reference'

    store__PythonMemberDescriptor__member_type             = PythonMemberDescriptor__member_type            .__set__
    store__PythonMemberDescriptor__member_name             = PythonMemberDescriptor__member_name            .__set__
    store__PythonMemberDescriptor__member_definition       = PythonMemberDescriptor__member_definition      .__set__
    store__adjusted__PythonMemberDefinition__name          = adjusted__PythonMemberDefinition__name         .__set__
    store__adjusted__PythonMemberDefinition__type          = adjusted__PythonMemberDefinition__type         .__set__
    store__adjusted__PythonMemberDefinition__offset        = adjusted__PythonMemberDefinition__offset       .__set__
    store__adjusted__PythonMemberDefinition__flags         = adjusted__PythonMemberDefinition__flags        .__set__
    store__adjusted__PythonMemberDefinition__documentation = adjusted__PythonMemberDefinition__documentation.__set__


    if __debug__:
        #
        #   Rewrite this function now using the new descriptors instead of 'poke_*' functions
        #
        def new_MemberDescriptor(member_type, member_name, definition_type, offset, flags = 0, documentation = none):
            assert type(documentation) in None_or_String

            member_name = intern_string(member_name)
            size        = (
                              unaligned_adjust__name_buffer    if documentation is none else
                              adjust__name_buffer + size__Character * (length(documentation) + 1)
                          )

            member_descriptor_address = GarbageCollection_MemoryAllocate(size)
            member_definition_address = member_descriptor_address + adjust__PythonMemberDefinition

            c_memory_set(member_descriptor_address, 0, size)

            if 1:
                line('new_MemberDescriptor: %s.%s %s @%d %s %s: allocate %d => %#x, %#x',
                     member_type, member_name, lookup_member_type(definition_type), offset, lookup_member_flags(flags),
                     (
                        'none'   if documentation is none else
                        arrange('%r<%d>', documentation, size__Character * (length(documentation) + 1))
                     ),
                     size, member_descriptor_address, member_definition_address)


            #
            #   PythonMemberDescriptor
            #
            #       Before we can use a descriptor, we have to at least have a 'object_type'.
            #
            #       Also for safety make sure we should also have a reference count (not strictly neccessary but it feels
            #       wrong to manipulate an object without a reference count).
            #
            poke_size_type(member_descriptor_address, offset__Object__reference_count, 1)
            poke_object   (member_descriptor_address, offset__Object__type, MemberDescriptor)

            r = address_to_object_and_steal_reference(member_descriptor_address)

            store__PythonMemberDescriptor__member_type      (r, member_type)
            store__PythonMemberDescriptor__member_name      (r, member_name)
            store__PythonMemberDescriptor__member_definition(r, member_definition_address)

            store__adjusted__PythonMemberDefinition__name   (r, object_address(member_name) + offset__String__string)
            store__adjusted__PythonMemberDefinition__type   (r, definition_type)
            store__adjusted__PythonMemberDefinition__offset (r, offset)
            store__adjusted__PythonMemberDefinition__flags  (r, flags)

            if documentation is not none:
                buffer_address = member_descriptor_address + adjust__name_buffer

                store__adjusted__PythonMemberDefinition__documentation(r, buffer_address)

                c_memory_move(
                    buffer_address,
                    object_address(documentation) + offset__String__string,
                    size__Character * (length(documentation) + 1),
                )

                assert buffer_address + size__Character * (length(documentation) + 1) - member_descriptor_address == size


            GarbageCollection_Track(member_descriptor_address)

            return r
    else:
        #
        #   Same as debug version, but ignore 'documentation'
        #
        def new_MemberDescriptor(member_type, member_name, definition_type, offset, flags = 0, documentation = none):
            member_name = intern_string(member_name)

            member_descriptor_address = GarbageCollection_MemoryAllocate(unaligned_adjust__name_buffer)

            c_memory_set(member_descriptor_address, 0, unaligned_adjust__name_buffer)

            poke_size_type(member_descriptor_address, offset__Object__reference_count, 1)
            poke_object   (member_descriptor_address, offset__Object__type, MemberDescriptor)

            r = address_to_object_and_steal_reference(member_descriptor_address)

            store__PythonMemberDescriptor__member_type(r, member_type)
            store__PythonMemberDescriptor__member_name(r, member_name)

            store__PythonMemberDescriptor__member_definition(
                r,
                member_descriptor_address + adjust__PythonMemberDefinition,
            )

            store__adjusted__PythonMemberDefinition__name  (r, object_address(member_name) + offset__String__string)
            store__adjusted__PythonMemberDefinition__type  (r, definition_type)
            store__adjusted__PythonMemberDefinition__offset(r, offset)
            store__adjusted__PythonMemberDefinition__flags (r, flags)

            GarbageCollection_Track(member_descriptor_address)

            return r


    address__MemberDescriptor = object_address(MemberDescriptor)


    def new_MemberDescriptor(member_type, member_name, definition_type, offset, flags = 0, documentation = none):
        assert type(documentation) in None_or_String

        member_name = intern_string(member_name)
        size        = (
                          unaligned_adjust__name_buffer    if documentation is none else
                          adjust__name_buffer + size__Character * (length(documentation) + 1)
                      )

        member_descriptor_address = GarbageCollection_MemoryAllocate(size)
        member_definition_address = member_descriptor_address + adjust__PythonMemberDefinition

        if 1:
            line('new_MemberDescriptor: %s.%s %s @%d %s %s: allocate %d => %#x, %#x',
                 member_type, member_name, lookup_member_type(definition_type), offset, lookup_member_flags(flags),
                 (
                    'none'   if documentation is none else
                    arrange('%r<%d>', documentation, size__Character * (length(documentation) + 1))
                 ),
                 size, member_descriptor_address, member_definition_address)

        if documentation is none:
            packed = pack(
                         'LPPPPPiLiP',
                         1,                              #   L = reference_count           : size_t
                         address__MemberDescriptor,      #   P = object_type               : PythonTypeObject*
                         object_address(member_type),    #   P = member_type               : PythonTypeObject*
                         object_address(member_name),    #   P = member_name               : PythonStringObject*
                         member_definition_address,      #   P = member_definition_address : PythonMemberDefinition*
                         object_address(member_name) + offset__String__string,      #   P = definition_name : char*
                         definition_type,                                           #   i = definition_type : int
                         offset,                                                    #   L = offset          : size_t
                         flags,                                                     #   i = flags           : int
                         0,                                                         #   P = documetnation   : char*
                     )
        else:
            packed = pack(
                         'LPPPPPiLiP' + String(length(documentation) + 1) + 's',
                         1,                              #   L = reference_count           : size_t
                         address__MemberDescriptor,      #   P = object_type               : PythonTypeObject*
                         object_address(member_type),    #   P = member_type               : PythonTypeObject*
                         object_address(member_name),    #   P = member_name               : PythonStringObject*
                         member_definition_address,      #   P = member_definition_address : PythonMemberDefinition*
                         object_address(member_name) + offset__String__string,      #   P = definition_name : char*
                         definition_type,                                           #   i = definition_type : int
                         offset,                                                    #   L = offset          : size_t
                         flags,                                                     #   i = flags           : int
                         member_descriptor_address + adjust__name_buffer,           #   P = documetnation   : char*
                         documentation,                                             #   #s = documentation  : char[#]
                     )

        line('packed: %d: %r', length(packed), packed)

        assert length(packed) == size

        c_memory_move(member_descriptor_address, object_address(packed) + offset__String__string, size)

        GarbageCollection_Track(member_descriptor_address)

        return r


    if 1:
        store__Code__global_names = copy_MemberDescriptor(Code.co_names, 0, 'Read/Write Code.global_names')

        #
        #   Verify that result of copy_MemberDescriptor is an object with a reference count of 1
        #
        assert peek_size_type(object_address(store__Code__global_names), offset__Object__reference_count) is 1

        dump_MemberDescriptor(store__Code__global_names)

        store__Code__global_names = none

    #
    #   Cleanup
    #
    del c_pointer_type_cache[C_PythonMemberDefinition]

    if __debug__:
        for k in C_PythonMemberDefinition.__dict__.keys():
            if k == '__module__':
                continue

            delete_attribute(C_PythonMemberDefinition, k)

        class Zap(Object):
            __slots__ = ((
                'name',
            ))


            def __init__(t, name):
                t.name = name


            def __del__(t):
                line('Zapping %s', t.name)


        C_PythonMemberDefinition.zap = Zap('C_PythonMemberDefinition')

        del C_Pointer_PythonMemberDefinition, C_PythonMemberDefinition
        del member_definition

        import gc
        gc.collect()

        line('=== Collected, DONE ===')


actualize_module()
