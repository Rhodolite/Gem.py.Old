    #
    #   Proof that main scope is on the frame stack
    #
    main_scope = find_object_by_address(main_scope_address)

    if main_scope:
        line('found main_scope: %d: %s', references(main_scope), main_scope.keys())

        for v in links_to_me(main_scope):
            line('  %s', v)
none = None


def line(format, *args):
    print format % args


import imp

def find_module(name):
    line('find_module: %s', name)

    if name == 'Gem.xyz':
        return Gem_loader


def load_module(name):
    [f, pathname, description] = imp.find_module(name[4:], __path__)

    if 1:
        line('found: %s, %s, %s', f, pathname, description)

    try:
        imp.load_module(name, f, pathname, description)
    finally:
        f.close()

    return sys.modules[name]


Gem_loader = Module('Gem.Loader')
Gem_loader.__file__    = 'Gem'
Gem_loader.find_module = find_module
Gem_loader.load_module = load_module

sys.path_importer_cache[path0] = Gem_loader
import Gem.xyz
reload(Gem.xyz)

assert 0, 'done'

    class PyObject(C_Structure):
        __slots__ = (())


    C_Pointer_PyObject             = C_Pointer(PyObject)
    C_Structure_Pointer__alignment = c_alignment(C_Pointer_PyObject)
    C_Structure_Pointer__size      = c_size_of(C_Pointer_PyObject)


    if 1:
        PyObject._fields_ = ((
                                 (('object_reference_count', C_Size_Type)),
                                 (('object_type',            C_Pointer_PyObject)),
                            ))


    assert C_PyMemberDefinition.name.offset   is 0
    assert C_PyMemberDefinition.type.offset   is PyMemberDefinition__type__offset
    assert C_PyMemberDefinition.offset.offset is PyMemberDefinition__offset__offset
    assert C_PyMemberDefinition.flags.offset  is PyMemberDefinition__offset__flags
    assert C_PyMemberDefinition.doc.offset    is PyMemberDefinition__offset__documentation

    assert c_size_of(C_PyMemberDefinition) is PyMemberDefinition__size

    if 0:
        line('type(member_descriptor),size: %r, %r', type(member_descriptor), MemberDescriptor.__basicsize__)
        line('size: %d, c_size: %d', member_definition.__sizeof__(), c_size_of(member_definition))
        line('C_PyMemberDefinition.name: %s', C_PyMemberDefinition.name.offset)
        line('C_PyMemberDefinition.type: %s', C_PyMemberDefinition.type.offset)
        line('C_PyMemberDefinition.offset: %s', C_PyMemberDefinition.offset.offset)
        line('C_PyMemberDefinition.flags: %s', C_PyMemberDefinition.flags.offset)
        line('C_PyMemberDefinition.doc: %s', C_PyMemberDefinition.doc.offset)


    line('0,%d,%d,%d,%d %d,%d,%d,%d,%d %d',
         offset__Object__type,
         offset__PyMemberDescriptor__member_type,
         offset__PyMemberDescriptor__member_name,
         offset__PyMemberDescriptor__member_definition,

         adjusted__PyMemberDefinition__name,
         adjusted__PyMemberDefinition__type,
         adjusted__PyMemberDefinition__offset,
         adjusted__PyMemberDefinition__flags,
         adjusted__PyMemberDefinition__documentation,
         
         adjust__name_buffer)

    #
    #   cast
    #
    c_cast3 = make_Pointer_PythonFunction(
                  ((C_Pointer_Void, C_Pointer_PythonObject, C_Pointer_PythonObject)),
                  C_Pointer_PythonObject
              )(_ctypes._cast_addr)


    def c_cast(object, c_type):
        return c_cast3(object, object, type)


    if 0:
        store__Object__reference_count = new_MemberDescriptor(
                                             Object, 'reference_count', DEFINITION_TYPE__SIZE_TYPE,
                                             offset__Object__reference_count,
                                         ).__set__

        store__Object__object_type__as_address = new_MemberDescriptor(
                                                     Object, 'object_type__as_address', DEFINITION_TYPE__ADDRESS, 
                                                     offset__Object__object_type,
                                                 ).__set__

        store__MemberDescriptor__member_type__as_address = new_MemberDescriptor(
                                                               MemberDescriptor,
                                                               'member_type__as_address',
                                                               DEFINITION_TYPE__ADDRESS,
                                                               offset__MemberDescriptor__member_type,
                                                           ).__set__

        store__MemberDescriptor__member_name__as_address = new_MemberDescriptor(
                                                               MemberDescriptor,
                                                               'member_name__as_address',
                                                               DEFINITION_TYPE__ADDRESS,
                                                               offset__MemberDescriptor__member_name,
                                                           ).__set__

        slot__MemberDescriptor__member_definition = new_MemberDescriptor(
                                                        MemberDescriptor, 'member_definition', DEFINITION_TYPE__ADDRESS,
                                                        offset__MemberDescriptor__member_definition,
                                                    )

        store__MemberDescriptor__member_definition = slot__MemberDescriptor__member_definition.__set__

    if 0:
        new_MemberDescriptor = produce__single_thread__new_MemberDescriptor()

        slot__Slice__step = new_MemberDescriptor(
                                Slice, 'step', DEFINITION_TYPE__OBJECT_EXTENDED,
                                offset__Slice__step
                            )

        class Zap(Object):
            __slots__ = ((
                'name',
            ))


            def __init__(t, name):
                t.name = name


            def __del__(t):
                line('Zapping %s', t.name)


        s1 = Slice(1, Zap('1'))
        s2 = Slice(2, Zap('2'), s1)

        #slot__Slice__step.__set__(s1, ((s2, Zap)) )

        Zap.s1 = s1





    x_code = function_code(x)

    line('   argument count:  %r', fetch__Code__argument_count(x_code))
    line('    number locals:  %r', fetch__Code__number_locals(x_code))
    line('       stack size:  %r', fetch__Code__stack_size(x_code))
    line('            flags:  %r', fetch__Code__flags(x_code))
    line('     virtual code:  %r', fetch__Code__byte_code(x_code))
    line('        constants:  %r', fetch__Code__constants(x_code))
    line('     global names:  %r', fetch__Code__global_names(x_code))
    line('   variable names:  %r', fetch__Code__local_names(x_code))
    line('   free variables:  %r', fetch__Code__free_variables(x_code))
    line('        cell vars:  %r', fetch__Code__cell_variables(x_code))
    line('         filename:  %r', fetch__Code__filename(x_code))
    line('             name:  %r', fetch__Code__name(x_code))
    line('first line number:  %r', fetch__Code__first_line_number(x_code))
    line('line number table:  %r', fetch__Code__line_number_table(x_code))
    line('     zombie frame:  %r', fetch__Code__zombie_frame(x_code))

    constants = fetch__Code__constants(x_code)

    y_code = Code(
                 fetch__Code__argument_count(x_code),
                 fetch__Code__number_locals(x_code),
                 fetch__Code__stack_size(x_code),
                 fetch__Code__flags(x_code),
                 fetch__Code__byte_code(x_code),
                 fetch__Code__constants(x_code),
                 fetch__Code__global_names(x_code),
                 fetch__Code__local_names(x_code),
                 fetch__Code__filename(x_code),
                 fetch__Code__name(x_code),
                 fetch__Code__first_line_number(x_code),
                 fetch__Code__line_number_table(x_code),
                 fetch__Code__free_variables(x_code),
                 fetch__Code__cell_variables(x_code),
             )

    y = Function(
            y_code,
            function_globals(x),
            function_name(x),
            function_defaults(x),
            function_closure(x),
        )

    y()

    #
    #   In the following '==', means it did not take our input value, but rewrote it
    #
    assert  fetch__Code__argument_count(x_code)    is  fetch__Code__argument_count(y_code)
    assert  fetch__Code__number_locals(x_code)     is  fetch__Code__number_locals(y_code)
    assert  fetch__Code__stack_size(x_code)        is  fetch__Code__stack_size(y_code)
    assert  fetch__Code__flags(x_code)             is  fetch__Code__flags(y_code)
    assert  fetch__Code__byte_code(x_code)         is  fetch__Code__byte_code(y_code)
    assert  fetch__Code__constants(x_code)         is  fetch__Code__constants(y_code)
    assert  fetch__Code__global_names(x_code)      ==  fetch__Code__global_names(y_code)
    assert  fetch__Code__local_names(x_code)       ==  fetch__Code__local_names(y_code)
    assert  fetch__Code__cell_variables(x_code)    ==  fetch__Code__cell_variables(y_code)
    assert  fetch__Code__free_variables(x_code)    ==  fetch__Code__free_variables(y_code)
    assert  fetch__Code__filename(x_code)          is  fetch__Code__filename(y_code)
    assert  fetch__Code__name(x_code)              is  fetch__Code__name(y_code)
    assert  fetch__Code__first_line_number(x_code) is  fetch__Code__first_line_number(y_code)
    assert  fetch__Code__line_number_table(x_code) is  fetch__Code__line_number_table(y_code)
