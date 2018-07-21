character     = chr
Object        = object
intern_string = intern


class ByteCode(Object):
    __slots__ = ((
        'name',
        'has_argument',
    ))


    def __init__(t, name, has_argument = 0, load_constant = 0):
        t.name          = name
        t.has_argument  = has_argument


byte_code__load_constant = ByteCode('load constant', has_argument = 1)
BYTE_CODE__LOAD_CONSTANT = character(100)


find__byte_code = {
    character(83)  : ByteCode('return'),
    character(100) : byte_code__load_constant
}.__getitem__


