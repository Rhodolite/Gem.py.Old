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
    function_name         = Function.func_name.__get__
    intern_string         = intern                              #   builtin
    introspection         = dir                                 #   builtin
    iterate               = iter                                #   builtin
    length                = len                                 #   builtin
    python_modules        = sys.modules


    #
    #   Wipe out '__main__' from the system.
    #
    #   It's scope remains active though, due to the link on the topmost frame stack:
    #
    #       Therefore, we reuse main's scope for our own purposes :)
    #
    Gem__name          = intern_string('Gem')
    main               = python_modules.pop('__main__')
    Gem                = python_modules.pop(Gem__name)
    privileged_scope   = main.__dict__
    provide_privileged = privileged_scope.setdefault

    main.__name__ = main.__doc__ = Gem__name

    if __debug__:
        NameError          = __builtin__.NameError
        restricted_scope   = Gem.__dict__
        provide_restricted = restricted_scope.setdefault

        Gem.__doc__ = intern_string('Restricted Gem')           #   Not needed, will be 'zapped'


        def make_change_globals(scope):
            def change_globals(f):
                return Function(
                           function_code(f),
                           scope,
                           function_name(f),
                           function_defaults(f),
                           function_closure(f),
                       )

            return change_globals


        #
        #   1   make_change_globals
        #           A temporarily privileged function that makes [temporarily privileged] functions
        #           to change functions from privileged or restricted
        #           (this funtion loses its privileges when Gem.__builtins__ is changed later on)
        #
        #   2.  temporary_privileged:
        #           A temporarily privileged function to change a function to privileged
        #           (this funtion loses it privileges when Gem.__builtins__ is changed later on)
        # 
        #   3.  make_change_globals:
        #           Using 'temporary_privileged': 'make_change_globals' is changed to be a [permenant]
        #           privileged funtion.  Now 'make_change_globals' will produce [permentant] privileged functions.
        #
        #   4.  privileged & restricted
        #           Using [the rewritten 'make_change_globals' that produces permenantly privileged funtions]
        #           the functions 'privileged' & 'restricted' are created.  These functions will remain
        #           privileged, and change other functions to be either privileged or restricted.
        #
        temporary_privileged = make_change_globals(privileged_scope)
        make_change_globals  = temporary_privileged(make_change_globals)
        privileged           = make_change_globals(privileged_scope)
        restricted           = make_change_globals(restricted_scope)


        #
        #   Now that we have a 'privileged' & 'restricted' functions, we can make the Gem
        #   scope a restricted scope.
        #
        #       1.  Get rid of the Gem module, replacing it with the main module.
        #
        #       2.  Set the buildins for the restricted scope
        #
        #   This affects 'temporary_privileged' which will no longer be privileged (although on this
        #   stack frame it is still privileged due to how CPython caches '__builtins__')
        #
        @restricted
        def line(format, *arguments):
            print (format % arguments   if arguments else   format)

            flush_standard_output()


        line('before')

        for [k, v] in restricted_scope.iteritems():
            if v is  __builtin__:
                line('  %s: __buitin__', k)
            elif v is  __builtin__.__dict__:
                line('  %s: __buitin__.__dict__', k)
            else:
                line('  %s: %s', k, v)

        Gem = main


        line('after')


        for [k, v] in restricted_scope.iteritems():
            if v is  __builtin__:
                line('  %s: __buitin__', k)
            elif v is  __builtin__.__dict__:
                line('  %s: __buitin__.__dict__', k)
            else:
                line('  %s: %s', k, v)


        provide_restricted('__builtins__', { intern_string(AssertionError.__name__) : AssertionError })


        @restricted
        def raise_NameError(format, *arguments):
            message = (format % arguments   if arguments else   format)

            raise NameError(message)


        @restricted
        def attempt_export(name, exporting):
            previous = provide_restricted(name, provide_privileged(name, exporting))

            if previous is not exporting:
                raise_NameError("Gem.%s already exists (value: %r): can't export %r also",
                                name, previous, exporting)

            return exporting


        @restricted
        def export(f, *arguments):
            if f.__class__ is Function:
                assert length(arguments) is 0

                name = function_name(f)

                return attempt_export(name, restricted(f))
                            
            if length(arguments) is 0:
                attempt_export(f.__name__, f)
                return

            argument_iterator = iterate(arguments)
            next_argument     = argument_iterator.next

            assert f.__class__ is String

            attempt_export(f, next_argument())

            for v in argument_iterator:
                if v.__class__ is String:
                    attempt_export(v, next_argument())
                    continue

                attempt_export(v.__name__, v)


        export = export(export)


        @export
        def export_privileged(f):
            return attempt_export(function_name(f), privileged(f))
    else:
        Gem         = main
        Gem.__doc__ = intern_string('Gem Scope')

        restricted_scope = privileged_scope


        def export_privileged(f):
            name = function_name(f)

            return provide_privileged(
                       name,
                       Function(
                           function_code(f),
                           privileged_scope,
                           name,
                           function_defaults(f),
                           function_closure(f),
                       ),
                   )


        export_privileged = export_privileged(export_privileged)


        @export_privileged
        def export(f, *arguments):
            if f.__class__ is Function:
                name = function_name(f)

                return provide_privileged(
                           name,
                           Function(
                               function_code(f),
                               privileged_scope,
                               name,
                               function_defaults(f),
                               function_closure(f),
                           ),
                       )
                            
            if length(arguments) is 0:
                return provide_privileged(f.__name__, f)

            argument_iterator = iterate(arguments)
            next_argument     = argument_iterator.next

            assert f.__class__ is String

            provide_privileged(f, next_argument())

            for v in argument_iterator:
                if v.__class__ is String:
                    provide_privileged(v, next_argument())
                else:
                    provide_privileged(v.__name__, f)


    #
    #   Since 'Gem' was popped off python_moduels, earlier, we now store an interned key 'Gem' ...
    #   (If we had not popped it off, the previous [non-interned] key is kept)
    #
    Gem__name = intern_string('Gem')
    python_modules[Gem__name] = Gem.__name__ = Gem__name

    Gem.__path__ = [sys.path.pop(0)]

    export(
        'globals',      globals,            #   Builtin
        'sorted_list',  sorted,             #   Builtin
    )


    @restricted
    def line(format, *arguments):
        print (format % arguments   if arguments else   format)
        flush_standard_output()


    @restricted
    def make_boot3():
        #
        #   'boot3' has to be defined here, so that 'boot2' does not see it &
        #   use a variable from a nested scope.
        #
        def boot3():
            del main.__package__, main.boot3

            line('main: %s', introspection(main))
            line('main.__builtins__: %s', main.__builtins__)
            line('main.__doc__: %r', main.__doc__)
            line('main.__file__: %r', main.__file__)
            line('main.__name__: %r', main.__name__)

            assert 0, 'incomplete'

        main.boot3 = boot3


    make_boot3()



    #
    #   Since this is called as follows:
    #
    #       exec __import__('Gem')
    #
    #   This must not have use any variables from a nested scope (i.e.: actualize_module)
    #
    def boot2():
        try:
            main = boot3()
            main()
        except:
            import sys

            [e_type, e, traceback] = sys.exc_info()

            if e_type is SystemExit:        #   Builtin
                raise

            #
            #   Use 'traceback.tb_next' to remove ourselves from the stack trace
            #
            try:
                __import__('traceback').print_exception(e_type, e, traceback.tb_next)
            finally:
                e_type = value = tb = 0

            sys.exit(1)


    python_modules[Gem__name] = function_code(boot2)


actualize_module()
