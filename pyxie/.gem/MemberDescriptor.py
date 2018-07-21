def actualize_module():
    from C_Types import GarbageCollection_Track, GarbageCollection_MemoryAllocate, PythonBuffer_FromReadWriteMemory
    from Pack import calculate_pack_size
    from Pack import offset__Buffer__buffer_base
    from Pack import offset__Buffer__buffer_pointer
    from Pack import offset__ExtendedMemberDescriptor__MemberDefinition
    from Pack import offset__MemberDescriptor__member_definition
    from Pack import offset__MemberDescriptor__member_name
    from Pack import offset__MemberDescriptor__member_type
    from Pack import offset__Object__object_type
    from Pack import offset__Object__reference_count
    from Pack import offset__Property__property_get
    from Pack import offset__String__string_buffer
    from Pack import Packer
    from Pack import pack_format__MemberDescriptor
    from Pack import offset__Slice__step

    import os, sys, types


    flush_standard_output = sys.stdout.flush
    Function              = type(actualize_module)
    iterate               = iter
    length                = len
    MemberDescriptor      = type(Function.func_globals)
    Module                = type(sys)
    none                  = None
    Property              = property

    
    Buffer         = buffer
    Object         = object
    object_address = id
    Method         = types.MethodType
    Slice          = slice
    String         = str
    intern_string  = intern


    function_defaults = Function.func_defaults.__get__


    def arrange(format, *arguments):
        return (format % arguments   if arguments else   format)


    def line(format, *arguments):
        print (format % arguments   if arguments else   format)

        flush_standard_output()



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
    DEFINITION_TYPE__REFERENCE          = 16        #   ObjectExtended
    DEFINITION_TYPE__LONG_LONG          = 17
    DEFINITION_TYPE__UNSIGNED_LONG_LONG = 18
    DEFINITION_TYPE__SIZE_TYPE          = 19


    pack__ExtendedMemberDescriptor      = Packer(pack_format__MemberDescriptor + 'PiLiP')
    pack_into__ExtendedMemberDescriptor = pack__ExtendedMemberDescriptor.pack_into
    size__ExtendedMemberDescriptor      = pack__ExtendedMemberDescriptor.size


    pointer_size = calculate_pack_size('P')


    if calculate_pack_size('l') == pointer_size:
        DEFINITION_TYPE__ADDRESS = DEFINITION_TYPE__LONG
    else:
        assert 0, "Don't know what the integral type is the same length (%d) as a pointer" % pointer_size


    #
    #   "Hackito Ero Sum", Part I
    #
    #   Constraints:
    #       Allocate as little as possible between 'GarbageCollection_MemoryAllocate' & 'GarbageCollection_Track'
    #       (to hopefully avoid exceptions that we can't handle)
    #
    #       NOTE: Using Python Exception handlign around this is totally useless, as the only exception should be
    #             "Out of Memory" and an exception handler would not work as it would need to allocate memory
    #             to do the exception handling.
    #
    #   Therefore:
    #       First, We preallocate 'hacker1' as our read/write buffer.
    #
    #           Now, therefore, to change 'hacker1', we need:
    #               We preallocate 'hacker2' as the read/write buffer into hacker1.
    #               This allows us to use 'pack_into__Buffer__pointer_size' to rewrite where hacker1 points to.
    #
    #       Secondly we preallcoate 'hackito_ergo_sum' as property in order to do three reference count manipulations:
    #
    #           1.  Store 'Object' & 'member_name' inside a property (this increments their reference counts)
    #           2.  Then wipe them (replace with 0; then deallcoating the property will not decrement their reference counts).
    #
    #           3.  Store the address of our object inside the property (using up its reference count that was initialized above)
    #           4.  Then extract it an object from the proeprty
    #           5.  Later, when the property is deallocated, it will decrement the reference count of our object.
    #
    #       NOTE:
    #           By setting the .fget member to NULL ('None' means NULL for property members), we avoid the special behavior of
    #           'property' where it sets its .__doc__ member to the value of .fget.__doc__
    #
    packer__Buffer__pointer_size    = Packer('PL')
    pack_into__Buffer__pointer_size = packer__Buffer__pointer_size.pack_into

    hacker1 = PythonBuffer_FromReadWriteMemory(0, 0)        #   Fake address & size, repalced below using hacker2
    hacker2 = PythonBuffer_FromReadWriteMemory(
                  object_address(hacker1) + offset__Buffer__buffer_pointer,
                  packer__Buffer__pointer_size.size,
              )

    packer__Property__get_set_delete    = Packer('PPP')
    pack_into__Property__get_set_delete = packer__Property__get_set_delete.pack_into
    size__Property__get_set_delete      = packer__Property__get_set_delete.size

    address__MemberDescriptor = object_address(MemberDescriptor)


    def new_MemberDescriptor(member_type, member_name, definition_type, definition_offset, definition_flags = 0):
        member_name = intern_string(member_name)

        hackito_ergo_sum               = Property(none, member_type, member_name)
        address__hackito_ergo_sum__get = object_address(hackito_ergo_sum) + offset__Property__property_get

        address__member_type     = object_address(member_type)
        address__member_name     = object_address(member_name)
        address__definition_name = address__member_name + offset__String__string_buffer


        #
        #   "Hackito Ero Sum", Part II.
        #
        #       As per above, we want to do steps 1-6 as quickly as possible with as little memory allocation as possible
        #       (to avoid exeptions; so no operations other than the required one '+' is done between steps 1-6):
        #
        #       1.  GarbageCollection_MemoryAllocate: Allocate the memory & store in 'address'
        #
        #       2.  Point 'hacker1' at 'address'
        #
        #       3.  Store the data for the ExtendedMemberDescriptor at adress
        #
        #           A.  (Out reference count of ourself is now 1, but nothing points to this objecdt)
        #
        #           B.  (Our reference counts are one too low for 'Object' & 'member_name')
        #
        #       4.  Point 'hacker1' at 'hackito_ergo_sum' (the .fget, .fset & .fdel members)
        #
        #       5.  Overwrite 'hackito_ergo_sum' (the .fget, .fset & .fdel members):
        #
        #           A.  Store address in 'hackito_ergo_sum.fget'
        #               This fixes the refernece to our object from step 3A.
        #
        #           B.  Wipe 'hackito_ergo_sum.fset' ('Object') & 'hackito_ergo_sum.fdel' ('member_name').
        #               This fixes the refernece count issue from step 3B
        #
        #       6.  GarbageCollection_Track: Now track our object properly
        #
        #   This finishes the hack & we can find our object in 'hackito_ergo_sum.fget'
        #
        address = GarbageCollection_MemoryAllocate(size__ExtendedMemberDescriptor)

        #   2. Point 'hacker1' at 'address'
        pack_into__Buffer__pointer_size(hacker2, 0, address, size__ExtendedMemberDescriptor)

        #   3.  Store the data for the ExtendedMemberDescriptor at adress
        pack_into__ExtendedMemberDescriptor(
            hacker1,
            0,

            1,                              #   L = reference_count           : size_t
            address__MemberDescriptor,      #   P = object_type               : PythonTypeObject*
            address__member_type,           #   P = member_type               : PythonTypeObject*
            address__member_name,           #   P = member_name               : PythonStringObject*
            address + offset__ExtendedMemberDescriptor__MemberDefinition,
                                            #   P = member_definition_address : PythonMemberDefinition*
            address__definition_name,       #   P = definition_name : char*
            definition_type,                #   i = definition_type : int
            definition_offset,              #   L = offset          : size_t
            definition_flags,               #   i = flags           : int
            0,                              #   P = documentation   : char*
        )

        #   4.  Point 'hacker1' at 'hackito_ergo_sum' (the .fget, .fset & .fdel members)
        pack_into__Buffer__pointer_size(hacker2, 0, address__hackito_ergo_sum__get, size__Property__get_set_delete)

        #   5.  Overwrite 'hackito_ergo_sum' (the .fget, .fset & .fdel members):
        pack_into__Property__get_set_delete(
            hacker1,
            0,

            address,            #   P: .fget -- convert adress to ojbect (taking its reference count)
            0,                  #   P: .fset -- wipe out Object (thus "transferring" its reference count to our object)
            0,                  #   P: .fdel -- wipe out member_name (thus "transferring" its reference count to our object)
        )

        GarbageCollection_Track(address)


        #
        #   "Hackito Ergo Sum", Part III
        #
        #   NOTE:
        #       A more traditional approach (instead of using 'hackito_ergo_sum' for reference count manipulation) would be:
        #
        #           C_Types.pythonapi.Py_IncRef(Object)
        #           C_Types.pythonapi.Py_IncRef(Object)
        #
        #           GarbageCollection_Track(address)
        #
        #           return C_Types.cast(address, C_Types.Pointer_PythonObject).value
        #
        #       However this is (1) Boring; (2) more expensive in having to create & use more C_Types points, functions, cast, etc.
        #
        #   Summary:
        #       Our method is (1) More elegant; (2) Quicker; (3) Allocates less memory, reducing the chance of an exception;
        #       but (4) Hackish.
        #
        return hackito_ergo_sum.fget


    store__Buffer__buffer_base__as__address = new_MemberDescriptor(
                                                  Buffer, 'buffer_base', DEFINITION_TYPE__ADDRESS,
                                                  offset__Buffer__buffer_base,
                                              ).__set__

    slot__Buffer__buffer_base = new_MemberDescriptor(
                                    Buffer, 'buffer_base', DEFINITION_TYPE__REFERENCE,
                                    offset__Buffer__buffer_base,
                                )
    load__Buffer__buffer_base   = slot__Buffer__buffer_base.__get__
    delete__Buffer__buffer_base = slot__Buffer__buffer_base.__delete__

    store__Buffer__buffer_pointer = new_MemberDescriptor(
                                        Buffer, 'buffer_pointer', DEFINITION_TYPE__ADDRESS,
                                        offset__Buffer__buffer_pointer,
                                    ).__set__

    store__MemberDescriptor__member_type = new_MemberDescriptor(
                                               MemberDescriptor, 'member_type', DEFINITION_TYPE__REFERENCE,
                                               offset__MemberDescriptor__member_type,
                                           ).__set__


    store__MemberDescriptor__member_name = new_MemberDescriptor(
                                               MemberDescriptor, 'member_name', DEFINITION_TYPE__REFERENCE,
                                               offset__MemberDescriptor__member_name,
                                           ).__set__

    #
    #   Here is a multi-threaded safe versio of new_MemberDescriptornew_MemberDescriptor, using our new descriptors
    #
    #   For comments, see the code above.
    #
    #-------------------------------------
    #
    #   def new_MemberDescriptor(member_type, member_name, definition_type, definition_offset, definition_flags = 0):
    #       member_name = intern_string(member_name)
    #
    #       address__member_type     = object_address(member_type)
    #       address__member_name     = object_address(member_name)
    #       address__definition_name = address__member_name + offset__String__string_buffer
    #
    #       hacker  = PythonBuffer_FromReadWriteMemory(0, size__ExtendedMemberDescriptor)
    #       address = GarbageCollection_MemoryAllocate(size__ExtendedMemberDescriptor)
    #
    #       store__Buffer__buffer_pointer(hacker, address)
    #
    #       pack_into__ExtendedMemberDescriptor(
    #           hacker,
    #           0,
    #
    #           1,
    #           address__MemberDescriptor,
    #           0,
    #           0,
    #           address + offset__ExtendedMemberDescriptor__MemberDefinition,
    #           address__definition_name,
    #           definition_type,
    #           definition_offset,
    #           definition_flags,
    #           0,
    #       )
    #
    #       store__Buffer__buffer_base__as__address(hacker, address)
    #
    #       r = load__Buffer__buffer_base(hacker)
    #
    #       store__MemberDescriptor__member_type(r, member_type)
    #       store__MemberDescriptor__member_name(r, member_name)
    #
    #       GarbageCollection_Track(address)
    #
    #       #delete__Buffer__buffer_base(hacker)        - not needed, done automaticallyb when 'hacker' goes out of scope
    #
    #       return r
    #


    #
    #   Here, on a per thread basis, we can call produce__single_thread__new_MemberDescriptor to create a
    #   'new_MemberDescriptor' function that allocates desriptors for us.
    #
    #   Each thread has its own 'hacker' -- since this can't be shared between threads
    #
    @export
    def produce__single_thread__new_MemberDescriptor():
        #
        #   Fake address.  Replaced below using store__Buffer__buffer_pointer
        #
        hacker = PythonBuffer_FromReadWriteMemory(0, size__ExtendedMemberDescriptor)


        def new_MemberDescriptor(member_type, member_name, definition_type, definition_offset, definition_flags = 0):
            member_name = intern_string(member_name)

            address__member_type     = object_address(member_type)
            address__member_name     = object_address(member_name)
            address__definition_name = address__member_name + offset__String__string_buffer

            address = GarbageCollection_MemoryAllocate(size__ExtendedMemberDescriptor)

            store__Buffer__buffer_pointer(hacker, address)

            pack_into__ExtendedMemberDescriptor(
                hacker,
                0,

                1,
                address__MemberDescriptor,
                0,
                0,
                address + offset__ExtendedMemberDescriptor__MemberDefinition,
                address__definition_name,
                definition_type,
                definition_offset,
                definition_flags,
                0,
            )

            store__Buffer__buffer_base__as__address(hacker, address)

            r = load__Buffer__buffer_base(hacker)

            store__MemberDescriptor__member_type(r, member_type)
            store__MemberDescriptor__member_name(r, member_name)

            GarbageCollection_Track(address)

            delete__Buffer__buffer_base(hacker)

            return r


        return new_MemberDescriptor


    export(
        'DEFINITION_TYPE__ADDRESS',   DEFINITION_TYPE__ADDRESS,
        'DEFINITION_TYPE__INTEGER',   DEFINITION_TYPE__INTEGER,
        'DEFINITION_TYPE__REFERENCE', DEFINITION_TYPE__REFERENCE,
    )


actualize_module()


del actualize_module
