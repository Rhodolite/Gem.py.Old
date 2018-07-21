#
#   Smaller version of ctypes.py
#
def actualize_module():
    import _ctypes, os, sys


    iterate = iter
    length  = len
    Module                = type(sys)
    
    none    = None
    String  = str


    if __debug__:
        object_address = id


        def arrange(format, *arguments):
            return (format % arguments   if arguments else   format)


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


    C_SimpleCData = _ctypes._SimpleCData


    if 0:
        class C_Integer(C_SimpleCData):
            _type_ = 'i'


        class C_Long(C_SimpleCData):
            _type_ = 'l'


    class C_Pointer_PythonObject(C_SimpleCData):
        _type_ = 'O'


    class C_Size_Type(C_SimpleCData):
        _type_ = 'L'


    class C_Pointer_Void(C_SimpleCData):
        _type_ = 'P'


    #
    #   Pointer to function
    #
    C_Pointer_Function                  = _ctypes.CFuncPtr
    FUNCTION_FLAG__CALLING_CONVENTION_C = _ctypes.FUNCFLAG_CDECL
    FUNCTION_FLAG__PYTHON_API           = _ctypes.FUNCFLAG_PYTHONAPI

    FUNCTION_FLAG__CALLING_CONVENTION__PYTHON_API = FUNCTION_FLAG__CALLING_CONVENTION_C | FUNCTION_FLAG__PYTHON_API

    def make_Pointer_PythonFunction(arguments, return_type):
        class PointerPythonFunction(C_Pointer_Function):
            _argtypes_ = arguments
            _restype_  = return_type
            _flags_    = FUNCTION_FLAG__CALLING_CONVENTION__PYTHON_API

            if __debug__:
                def __repr__(t):
                    return arrange('<C_Pointer_PythonFunction(%s) -> %s @%#x>',
                                   ','.join(v.__name__   for v in t._argtypes_),
                                   t._restype_.__name__,
                                   object_address(t))

                      

        if __debug__:
            PointerPythonFunction.__name__ = arrange('C_Pointer_PythonFunction__%s__returns__%s',
                                                     '__'.join(v.__name__   for v in arguments),
                                                     'NoneType'   if return_type is none else   return_type.__name__)

        return PointerPythonFunction


    #
    #   pythonapi
    #
    pythonapi         = Module('pythonapi')
    borrow_handle     = (os.name in (('nt', 'ce')) )
    pythonapi._handle = (
                            sys.dllhandle    if borrow_handle else
                            _ctypes.dlopen(
                                (
                                    arrange('libpython%d.%d.dll', sys.version_info[0], sys.version_info[1])
                                        if sys.platform == 'cygwin' else
                                            None
                                ),
                                _ctypes.RTLD_LOCAL,
                            )
                        )

    PythonBuffer_FromReadWriteMemory = make_Pointer_PythonFunction(
                                           ((C_Pointer_Void, C_Size_Type)),
                                           C_Pointer_PythonObject
                                       )( (('PyBuffer_FromReadWriteMemory', pythonapi)) )

    GarbageCollection_MemoryAllocate = make_Pointer_PythonFunction(
                                           ((C_Size_Type,)),
                                           C_Pointer_Void,
                                       )( (('_PyObject_GC_Malloc', pythonapi)) )
    GarbageCollection_Track          = make_Pointer_PythonFunction(
                                           ((C_Pointer_Void,)),
                                           none,
                                       )( (('PyObject_GC_Track', pythonapi)) )


    if not borrow_handle:
        _ctypes.dlclose(pythonapi._handle)

    del pythonapi

    if 0:
        c_cast3 = make_Pointer_PythonFunction(
                      ((C_Pointer_Void, C_Pointer_PythonObject, C_Pointer_PythonObject)),
                      C_Pointer_PythonObject
                  )(_ctypes._cast_addr)


        def c_cast(c_object, c_type):
            return c_cast3(c_object, c_object, c_type)



    export(
        'GarbageCollection_MemoryAllocate',     GarbageCollection_MemoryAllocate,
        'GarbageCollection_Track',              GarbageCollection_Track,
        'PythonBuffer_FromReadWriteMemory',     PythonBuffer_FromReadWriteMemory,
    )


actualize_module()


del actualize_module
