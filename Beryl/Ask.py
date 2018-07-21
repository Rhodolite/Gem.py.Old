#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@gem('Beryl.Ask')
def gem():
    require_gem('Gem.IO')


    from Gem import input


    @share
    def ask(question, answer):
        response = input(question + arrange(' [%s]  ', answer)   if answer else   question + '  ')

        return (response) or (answer)
