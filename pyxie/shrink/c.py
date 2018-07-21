import gc

def coalese_simple_attribute(name):
    """This sample implementation of __coalese__.attribute does not use the
    name argument.  This argument is for other more complex implementations
    coalese objects."""

    return value


def coalese_identity_decorator(f):
    """This identity decorator does no decorating, it is returned by a
    coalese operator to avoid any decorating."""

    return f


if __debug__:
    class CoallaseResult(object):
        __slots__ = (
            '__doc__',          #   String
            'name',             #   String
            'attribute',        #   Function | Method
            'decorate',         #   Function | Method
            'value',            #   Any
        )


        def __init__(self, name, documentation, value):
            self.__doc__   = documentation
            self.name      = name
            self.attribute = coalese_simple_attribute
            self.decorate  = coalese_identity_decorator
            self.value     = value


        def __repr__(self):
            return '<__coalase__ result for %r>' % self.value


    make_coalese = CoallaseResult
else:
    ModuleType = type(gc)           #   Same as ModuleType from types.py

    #
    #   A quick & efficient way to implement 'CoalaseResult' without a class
    #
    #   One issue is its representation is something like '<module 'none_coalese' (built-in)>'
    #   instead of the more readable return value of 'CoallaseResult.__repr__'
    #
    def make_coalese(name, documentation, value):
        """This reuses a module as quick & efficient way to have a singleton object
        that has three attributes"""

        def attribute(name):
            return value

        module = ModuleType(name)

        module.__doc__   = documentation
        module.attribute = coalese_simple_attribute
        module.decorate  = coalese_identity_decorator
        module.value     = value

        return module


#
#   NOTE: Horrible "hack" to do:
#
#       None.__coalese__ = make_coalese(
#               'none__coalese',
#               """This is the return type from None.__coalese__""",
#               None,
#           )
#
#   (Only being used here to create a "quick reference" implementation).
#
gc.get_referents(type(None).__dict__)[0]['__coalese__'] = make_coalese(
        'none_coalese',
        """This is the return type from None.__coalese__""",
        None,
    )


#
#   The same for boolean, but with a conditional return from '___coalese__'
#
#       False   - coaleses
#       True    - does not coalese
#
false_coalese = make_coalese(
        'false_coalese',
        """This is the return type from False.__coalese__""",
        False,
    )

@property
def boolean_coalese(self):
    """This is the bool.__coalese__ property"""

    if self is False:
        return false_coalese

    #return none    - True does not coalese


gc.get_referents(bool.__dict__)[0]['__coalese__'] = boolean_coalese


#
#   The same for integers:
#
#       0              - coaleses
#       Other inteters - do not coalese
#
zero_coalese = make_coalese(
        'zero_coalese',
        """This is the return type from (0).__coalese__""",
        0,
    )

@property
def integer_coalese(self):
    """This is the int.__coalese__ property"""

    if self is 0:
        return zero_coalese

    #return none    - All non-zero values do not coalese


gc.get_referents(int.__dict__)[0]['__coalese__'] = integer_coalese


#
#   Demo
#
print 'None.__coalese__', None.__coalese__
print 'False.__coalese__', False.__coalese__
print 'True.__coalese__', True.__coalese__
print '(0).__coalese__', (0).__coalese__
print '(7).__coalese__', (7).__coalese__
