"""
Module with some functions
"""


def new_add(arg_1, arg_2):
    """
    Compute sum of two numbers

    Parameters
    ----------
    arg_1 : int or float
        First arg
    arg_2 : int or float
        Second arg

    Returns
    -------
    int
        Sum of two args

    """
    return arg_1 + arg_2


def new_pow(arg_1, arg_2):
    """
    Compute pow of two numbers

    Parameters
    ----------
    arg_1 : int or float
        First arg
    arg_2 : int or float
        Second arg

    Returns
    -------
    int
        Pow

    """
    return arg_1 ** arg_2


def get_dict():
    return {
        "abc": 1020,
        "bcd": 3040,
        "ced": 5060,
        "dfg": 0,
        "eas": 1111111111,
        "wdd": 556,
    }
