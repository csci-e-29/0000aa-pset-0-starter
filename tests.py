import signal
from contextlib import contextmanager
from time import sleep, time
from unittest import TestCase, main

from fibonacci import SummableSequence, optimized_fibonacci

try:
    # Absent on Windows, trigger AttributeError
    signal.alarm

    def _timeout(signum, frame):
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
        finally:
            signal.alarm(0)

except AttributeError:

    @contextmanager
    def timeout(seconds=1, message="Timeout!"):
        t0 = time()
        yield
        if time() - t0 > seconds:
            raise TimeoutError(message)


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
        ss = SummableSequence(2, (0, 1))
        for n in range(0, 50, 5):
            with timeout(message="Timeout running f({})".format(n)):
                self.assertEqual(ss(n), optimized_fibonacci(n))


class TestTimeout(TestCase):
    def test_timeout(self):
        with self.assertRaises(TimeoutError):
            with timeout():
                sleep(2)




if __name__ == '__main__':
    main()
