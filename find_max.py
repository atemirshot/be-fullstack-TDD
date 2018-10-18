def get_max(a, b):
    return b if a < b else a

def get_max_without_arguments():
    raise TypeError('There must be an arguments')



def get_max_with_one_argument(a):
    return a



def get_max_with_many_arguments(*args):
    first = args[0]
    for i in args:
        if i>first:
            first=i
    return first

def get_max_with_one_or_more_arguments(first, *args):
    result = 0
    for arg in (first,) + args:
        if arg > result:
            result = arg
    return result



def get_max_bounded(*args, low, high):
    res = 0
    for arg in args:
        if arg > res and low < arg < high:
            res = arg
    return res


def make_max(*, low, high):
    def inner(first, *args):
        result = 0

        for arg in (first,) + args:
            if arg > result and low < arg < high:
                result = arg
        return result

   
    return inner
