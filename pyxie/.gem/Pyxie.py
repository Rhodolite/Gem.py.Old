@make_module
def make_module():
    import gc, sys


    @gem
    def line(format, *arguments):
        print format % arguments


    #
    #   Python types
    #
    Code      = line.func_code.__class__
    Function  = line.__class__
    FrozenSet = frozenset                   #   builtin
    Module    = sys.__class__
    Map       = sys.modules.__class__
    Object    = object                  #   builtin
    String    = str


    #
    #   Functions
    #
    address_of      = id                    #   builtin
    links_to_me     = gc.get_referrers
    i_link_to       = gc.get_referents
    get_objects     = gc.get_objects
    reference_count = sys.getrefcount
    type            = __builtins__.type      #   builtin; effectivly a function


    #
    #   Values
    #
    none           = None                         #   builtin


    @gem
    def oops():
        0/0


    known_function_modules = FrozenSet(['codecs', 'encodings', 'encodings.utf_8'])

    known_modules = FrozenSet([
                         '__builtin__',
                         '_codecs', 'codecs',
                         'encodings', 'encodings.aliases', 'encodings.utf_8',
                         'exceptions',
                         'gc',
                         'signal', 'sys',
                         'time',
                         '_warnings',
                         'zipimport',
                    ])



    @gem
    def print_unknown_modules():
        for v in sorted_list(
                     v
                        for v in get_objects()
                           if (type(v) is Module) and (v.__name__ not in known_modules)
        ):
            line('%d: %s', reference_count(v), v)




    @gem
    def print_unknown_functions():
        for v in sorted_list(
                    v
                        for v in get_objects()
                           if (
                                   type(v) is Function
                               and v.__module__ not in known_function_modules
                           )
            ):
                line('%d: Function %s.%s', reference_count(v), v.__module__, v.__name__)


        
    @export_diamond
    def main():
        if 0:
            print_unknown_modules()
            print_unknown_functions()

            for v in get_objects():
                if type(v) is Map:
                    if '__module__' in v:
                        line('%d: Map.__module__: %s', reference_count(v), v['__module__'])
                        continue

                    if '__doc__' in v:
                        line('%d: Map.__doc__: %r', reference_count(v), v['__doc__'])
                        continue
                        
                    line('%d: Map.keys: %s', reference_count(v), v.keys())

            def find_object_by_address(address):
                for v in get_objects():
                    if address_of(v) == address:
                        return v


        from Tokenizer import tokenizer

        tokenizer()
