#
#   Copyright (c) 2017 Joy Diamond.  All rights reserved.
#
@export
def catch_ImportError():
    return CatchException(ImportError)
