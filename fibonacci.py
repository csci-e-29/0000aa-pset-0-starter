#!/usr/bin/env python3


def optimized_fibonacci(f):
    raise NotImplementedError()


class SummableSequence(object):

    def __init__(self, n, initial):
        raise NotImplementedError()

    def __call__(self, i):
        raise NotImplementedError()


if __name__ == '__main__':

    print('f(100000):', optimized_fibonacci(100000))

    new_seq = SummableSequence(3, (5, 7, 11))
    print('new_seq(20):', new_seq(20))
