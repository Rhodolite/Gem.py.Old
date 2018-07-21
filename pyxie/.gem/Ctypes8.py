def actualize_module():
    import _ctypes, os, sys


    #
    #   Types
    #
    String = str                                        #   Built in


    #
    #   Functions
    #
    calculate_pack_size   = struct.calcsize
    flush_standard_output = sys.stdout.flush
    object_address        = id                          #   Built in


    #
    #   Values
    #
    none = None                                         #   Built in



    #
    #   C functions
    #
    c_alignment             = _ctypes.alignment
    #C_Pointer               = _ctypes.POINTER          #   Creates a type, so starts with capital 'C'
    C_SimpleCData           = _ctypes._SimpleCData
    c_size_of               = _ctypes.sizeof
    #c_delete_cached_pointer = _ctypes._pointer_type_cache.__delitem__


    #
    #   C Values
    #
    def arrange(format, *arguments):
        return (format % arguments   if arguments else   format)


    def line(format, *arguments):
        print (format % arguments   if arguments else   format)

        flush_standard_output()


    #
    #   Simple C Types
    #
    class c_integer(C_SimpleCData):
        _type_ = 'i'


    class c_long(C_SimpleCData):
        _type_ = 'l'


    class c_pointer_python_object(C_SimpleCData):
        _type_ = 'O'


    class c_size_type(C_SimpleCData):
        _type_ = 'L'


    class c_void_p(C_SimpleCData):
        _type_ = 'P'


    #C_Pointer_Long = C_Pointer(c_long)
    #c_delete_cached_pointer(c_long)


    if __debug__:
        class c_character(C_SimpleCData):
            _type_ = 'c'


        def verify_SimpleCData(meta, size, alignment, pack_type = none):
            assert (c_size_of(meta) is size) and (c_alignment(meta) is alignment)
            assert calculate_pack_size('c' + ((pack_type) or (meta._type_))) is size + alignment

        verify_SimpleCData(c_character,              1, 1)
        verify_SimpleCData(c_integer,                4, 4)
        verify_SimpleCData(c_long,                   8, 8)
        verify_SimpleCData(c_pointer_python_object,  8, 8, 'P')
        verify_SimpleCData(c_size_type,              8, 8)
        verify_SimpleCData(c_void_p,                 8, 8)

        #assert c_size_of(C_Pointer_Long) is c_alignment_of(C_Pointer_Long) is 8


    def align__Character(offset):
        v = offset

        return ((offset, v + 1))


    def align__Integer(offset):
        v = (offset + 3) & ~3

        return ((v, v + 4))


    def align__Long(offset):
        v = (offset + 7) & ~7

        return ((v, v + 8))


    align__Size_Type = align_Pointer = align__Long


    #
    #   Pointers to Functions
    #
    C_Pointer_Function                  = _ctypes.CFuncPtr
    FUNCTION_FLAG__CALLING_CONVENTION_C = _ctypes.FUNCFLAG_CDECL
    FUNCTION_FLAG__PYTHON_API           = _ctypes.FUNCFLAG_PYTHONAPI

    FUNCTION_FLAG__CALLING_CONVENTION__PYTHON_API = FUNCTION_FLAG__CALLING_CONVENTION_C| FUNCTION_FLAG__PYTHON_API

    def make_Pointer_Function(arguments, return_type):
        class PointerFunction(C_Pointer_Function):
            _argtypes_ = arguments
            _restype_  = return_type
            _flags_    = FUNCTION_FLAG__CALLING_CONVENTION__PYTHON_API

            def __repr__(t):
                return arrange('<C_PointerFunction(%s) -> %s @%#x>',
                               ','.join(v.__name__   for v in t._argtypes_),
                               t._restype_.__name__,
                               object_address(t))

                      

        if __debug__:
            PointerFunction.__name__ = arrange('C_Pointer_Function__%s__returns__%s',
                                               '__'.join(v.__name__   for v in arguments),
                                               return_type.__name__)

        return PointerFunction


    c_cast3 = make_Pointer_Function(
                  ((c_void_p, c_pointer_python_object, c_pointer_python_object)),
                  c_pointer_python_object
              )(_ctypes._cast_addr)


    def c_cast(object, c_type):
        return c_cast3(object, object, type)


    import c0

    PyBuffer_FromMemory = make_Pointer_Function(
                             (c_void_p, c_size_type),
                             c_pointer_python_object
                          )( (('PyBuffer_FromMemory', c0.pythonapi)) )

    line('PyBuffer_FromMemory: %r', PyBuffer_FromMemory)
    #PyBuffer_FromMemory = c0.pythonapi.PyBuffer_FromMemory


    hello = 'Hello 77'
    x = PyBuffer_FromMemory(hello, 20)

    line('x: %r', x)


actualize_module()

del actualize_module
