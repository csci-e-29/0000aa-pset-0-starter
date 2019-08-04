#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    raise NotImplementedError()


def optimized_fibonacci(f):
    raise NotImplementedError()


class SummableSequence(object):
    def __init__(self, n, initial):
        raise NotImplementedError()

    def __call__(self, i):
        raise NotImplementedError()


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(3, (5, 7, 11))
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
