import signal
from contextlib import contextmanager
from unittest import TestCase, main

from fibonacci import SummableSequence, optimized_fibonacci


def _timeout(signum, frame):
    print('Signal handler called with signal', signum)
    raise TimeoutError()


signal.signal(signal.SIGALRM, _timeout)


@contextmanager
def timeout(seconds=1, message="Timeout!"):
    # NB: doesn't work on windows
    signal.alarm(seconds)
    try:
        yield
    except TimeoutError:
        raise TimeoutError(message)
    signal.alarm(0)


def raw_fib(n):
    if n < 2:
        return n
    return raw_fib(n-1) + raw_fib(n - 2)


class FibTests(TestCase):

    def test_fibonnacci(self):
        for n, expected in [
            # Check progressively more complex values, see if time out
            (0, 0), (1, 1), (6, 8),
            (10, 55),
            (15, 610),
            (20, 6765), (30, 832040), (40, 102334155), (100, 354224848179261915075),
        ]:
            with timeout(message="Timeout running f({})".format(n)):
                self.assertEqual(optimized_fibonacci(n), expected)

    def test_summable(self):
        with timeout():
            ss = SummableSequence(2, (0, 1))
            self.assertEqual(ss(9), optimized_fibonacci(9))


if __name__ == '__main__':
    main()
