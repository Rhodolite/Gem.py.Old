#
#   Copyright (c) 2017-2018 Joy Diamnod & Mike Zhukovskiy.  All rights reserved.
#
def boot(module_name):
    def execute(f):
        return f()

    return execute


@boot('Boot')
def boot():
    from sys     import path    as module_path
    from os.path import abspath as path_absolute, join as path_join

    path_0 = module_path[0]

    module_path.insert(0, path_absolute(path_join(path_0, '../')))
    module_path.insert(1, path_absolute(path_join(path_0, '../../Gem')))


    import Gem


@gem('Beryl.Main')
def gem():
    require_gem('Beryl.BerylAnswer')


    @share
    def main(arguments):
        answers = BerylAnswer()

        answers.load_answers__if_exists()
        answers.ask_four_questions()
        answers.write_contribution_agreement()
