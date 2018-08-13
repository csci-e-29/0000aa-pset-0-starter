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

    # Check to ensure we agree with basic Fibonacci
    fib = SummableSequence(2, (0, 1))
    assert fib(6) == 8

    # Actual HW answer
    new_seq = SummableSequence(3, (5, 7, 11))
    print('new_seq(20):', new_seq(20))
