#!/usr/bin/env python3


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    return int(str(some_int)[-8:])


def optimized_fibonacci(f):
    """Fast (non-recursive) implementation of Fibonacci
    Returns the nth number in the Fibonacci sequence, given input n
    :param int f: the number
    :rtype: int
    """
    a = 0
    b = 1
    if f < 2:
        return f
    else:
        for i in range(1, f):
            c = a + b
            a = b
            b = c
        return b


class SummableSequence(object):
    def __init__(self, *initial):
        """Creates a SummableSequence object, akin to Fibonacci but with any abitrary number of feed values instead of just two as used by Fibonacci
        :the list of given (integer) parameters
        """
        self.prompt_list = list(initial)

    def __call__(self, i):
        """Returns the nth number in the SummableSequence, given input n
        :param int i: place in the sequence
        :rtype: int
        """
        n = len(self.prompt_list)
        if i <= 0:
            return 0
        elif i <= n:
            return self.prompt_list[i - 1]
        else:
            running_list = self.prompt_list[:]
            for j in range(n - 1, i):
                running_sum = sum(running_list)
                for k in range(n - 1):
                    running_list[k] = running_list[k + 1]
                running_list[-1] = running_sum
            return running_sum


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
