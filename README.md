# Pset 0

Replace these with your own build badges!

[![Build Status](https://travis-ci.com/csci-e-29-dev/pset-0-starter.svg?token=aaaaa&branch=master)](https://travis-ci.com/csci-e-29-dev/pset-0-starter)

[![Maintainability](https://api.codeclimate.com/v1/badges/aaaaa/maintainability)](https://codeclimate.com/repos/aaaaa/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/aaaaa/test_coverage)](https://codeclimate.com/repos/aaaaa/test_coverage)

## Objectives

* Build a working and repeatable Python environment
* Track development history with Git/GitHub
* Measure code quality with testing and Code Climate
* Set up a CI/CD pipeline using Travis-CI to hold ourselves accountable
This problem set is designed to be solvable with minimal prep work - you should
be able to complete it with your own prior knowledge and limited external
research beyond the provided tutorials. If it proves too challenging, please
discuss with the teaching staff whether you should consider delaying enrollment
in this course.

**Please complete this Pset before class begins** if possible.  Feedback will be
returned before the drop date.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Preamble](#preamble)
  - [Setting up your local environment](#setting-up-your-local-environment)
  - [Setting up your cloud environment](#setting-up-your-cloud-environment)
  - [Grading standards and mechanics](#grading-standards-and-mechanics)
  - [Showing your work!](#showing-your-work)
- [Problems (25 points)](#problems-25-points)
  - [Build badges (5 points)](#build-badges-5-points)
  - [Pyramid (5 points)](#pyramid-5-points)
  - [Fibonacci (15 points)](#fibonacci-15-points)
    - [A better solution (5 points)](#a-better-solution-5-points)
    - [Generalizing (10 points)](#generalizing-10-points)
- [Other grading aspects (40 points)](#other-grading-aspects-40-points)
  - [Testing Quality (20 points)](#testing-quality-20-points)
  - [Python Quality (10 points)](#python-quality-10-points)
  - [Git History (10 points)](#git-history-10-points)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Preamble

### Setting up your local environment

[Setup notes](docs/setup.md)

### Setting up your cloud environment

[Cloud notes](docs/cloud.md)

### Grading standards and mechanics

[Grading notes](docs/grading.md)

### Showing your work!

[Proof notes](docs/work.md)

## Problems (25 points)

### Build badges (5 points)

Update the build badges at the top of this README, using markdown templates for
your master branch.

See [Travis](https://docs.travis-ci.com/user/status-images) and [Code
Climate](https://docs.codeclimate.com/docs/overview#badges) instructions. You
may add multiple if you'd like for various branches (eg, a 'develop' branch),
but only one for master is required.

### Pyramid (5 points)

Write a program that outputs an isosceles pyramid of variable height to the
terminal using the example characters.  For example, a pyramid of height 2 would
look like:

```
-=-
===
```

While a pyramid of height 3 would look like:

```
--=--
-===-
=====
```

Implement the function `print_pyramid` in [pyramid.py](pyramid.py) and print a
pyramid of height 10.

### Fibonacci (15 points)

The Fibonacci sequence, `f(i)`, is defined as `(0, 1, 1, 2, 3, 5, 8, ...)` where
the `i`th number is the sum of the two proceeding numbers, with `f(0) == 0` and
`f(1) == 1`.  A common implementation of the function adds the result of
calling itself on a smaller number, i.e.:

```python
def f(i):
    return f(i - 1) + f(i - 2)
```

with appropriate handling of the edge cases.


#### A better solution (5 points)

What is the value of `f(100000)`?

Note that the common implementation will not work! Your code should execute very
quickly (do not remove the timeouts in the unittests!).  Describe any changes
you made in terms of scaling, time/memory tradeoffs, etc, and ensure your
working function is committed.

Implement your solution in `optimized_fibonacci` within
[fibonacci.py](fibonacci.py).

#### Generalizing (10 points)

We can think of this sequence as a special case of a class of sequences where
the `i`th number is the sum of the previous `n` numbers in the sequence, with
the first `n` numbers defined arbitrarily.   That is, the Fibonacci sequence is
a special instance where `n=2` with the first numbers `(0, 1)`.

Design a class where the Fibonacci sequence is an instance. Now, create a
new sequence instance where `n=3` and the initial values are `(5, 7, 11)`;
return the value of `new_seq(100000)`.  E.g.:

```python
class SummableSequence(object):

    def __init__(self, n, initial):
        ...

    def __call__(self, i):
        ...


if __name__ == '__main__':
    ...
    new_seq = SummableSequence(3, (5, 7, 11))
    print(last_8(new_seq(100000)))
```

***Make sure you apply your learnings from `optimized_fibonacci` to this
class!*** We want this to be an efficient solution as well.

Continue the implementation in [fibonacci.py](fibonacci.py).

## Other grading aspects (40 points)

### Testing Quality (20 points)

Take a look at the file [tests.py](tests.py).  It has unittests you can run with
`python3 -m unittest` or `pytest`.  They all should pass!  Do not touch the
existing test methods, but you can add new ones to ensure your code is working
properly.  Try to ensure tests pass before you commit and push new code on your
master branch! This will help minimize the number of builds on the CI server.

#### Test Coverage

Travis/Code Climate will report overall test coverage; try to cover every major
function and clause you write.

Some tools will show you exactly which lines are covered, eg:

* [Run tests with coverage in Pycharm](https://www.jetbrains.com/help/pycharm/running-test-with-coverage.html)
* Generate an html report directly with `pytest --cov-report html` then `open htmlcov/index.html`

### Python Quality (10 points)

We will comment on your overall quality of documentation, commenting,
appropriate variable names, usage of higher-level code, etc.  Be sure to look
at Code Climate reports to help you improve.

### Git History (10 points)

Git commits should be logically structured, follow a branching model, etc.  Do
not commit irrelevant files to the VCS (eg, anything under `__pycache__` or your
editor/IDE configurations).  Never `git add *` or `git commit -a`!  They lump
all your changes together; you want each commit to be a logical bit of history
that captures what was done and why in a cohesive unit.
