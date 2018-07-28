#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@module('Beryl.Ask')
def module():
    require_module('Capital.IO')


    from Capital import input


    @share
    def ask(question, answer):
        response = input(question + arrange(' [%s]  ', answer)   if answer else   question + '  ')

        return (response) or (answer)
