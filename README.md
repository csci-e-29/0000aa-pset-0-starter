# Pset 0

***Please review*** 'General Pset Instructions' on Canvas prior to starting this
assignment!

Replace the below with your own build badges:

[![Build Status](https://travis-ci.com/lisanmejia/0000aa-pset-0-starter.svg?branch=develop)](https://travis-ci.com/lisanmejia/0000aa-pset-0-starter)

[![Maintainability](https://api.codeclimate.com/v1/badges/ad08644cfce1f677cd48/maintainability)](https://codeclimate.com/github/lisanmejia/0000aa-pset-0-starter/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/ad08644cfce1f677cd48/test_coverage)](https://codeclimate.com/github/lisanmejia/0000aa-pset-0-starter/test_coverage)

## Objectives

* Demonstrate mastery of basic python syntax (functions, classes, etc)
* Track development history with Git/GitHub
* Set up a CI/CD pipeline using Travis-CI to hold ourselves accountable
* Measure code quality with testing and Code Climate
* Build a working and repeatable Python environment

### Submission Checklist

* Build badges updated above
* Code passes tests in Travis on Master Branch
* Address any major code quality issues on Code Climate
* Code is auto formatted with [black](https://black.readthedocs.io/en/stable/)
* You have added relevant test cases and suites
* The deploy submits your assignment and answers quiz ahead of the deadline
* Complete peer review (after submission deadline)

This problem set is designed to be solvable with minimal prep work - you should
be able to complete it with your own prior knowledge and limited external
research beyond the provided tutorials. If it proves too challenging, please
discuss with the teaching staff whether you should consider delaying enrollment
in this course.

**Please complete this Pset before class begins** if possible.  The refund drop
date is very early in the semester.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Problems](#problems)
  - [Build badges](#build-badges)
  - [Pyramid](#pyramid)
  - [Fibonacci](#fibonacci)
    - [A better solution](#a-better-solution)
    - [Generalizing](#generalizing)
  - [Submit!](#submit)
- [Other grading aspects](#other-grading-aspects)
  - [Testing Quality](#testing-quality)
    - [Test Coverage](#test-coverage)
  - [Python Quality](#python-quality)
  - [Git History](#git-history)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Problems

### Build badges

Update the build badges at the top of this README, using markdown templates for
your master branch.

See [Travis](https://docs.travis-ci.com/user/status-images) and [Code
Climate](https://docs.codeclimate.com/docs/overview#badges) instructions. You
may add multiple if you'd like for various branches (eg, a 'develop' branch),
but only one for master is required.

### Pyramid

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

### Fibonacci

The Fibonacci sequence, `f(i)`, is defined as `(0, 1, 1, 2, 3, 5, 8, ...)` where
the `i`th number is the sum of the two proceeding numbers, with `f(0) == 0` and
`f(1) == 1`.  A common implementation of the function adds the result of
calling itself on a smaller number, i.e.:

```python
def f(i):
    return f(i - 1) + f(i - 2)
```

with appropriate handling of the edge cases.

#### A better solution

What is the value of `f(100000)`? (NB: for brevity, you will work with the last
eight digits of your answer.)

Note that the common implementation will not work! Your code should execute very
quickly (do not remove the timeouts in the unittests!).  Describe any changes
you made in terms of scaling, time/memory tradeoffs, etc, and ensure your
working function is committed.

Implement your solution in `optimized_fibonacci` within
[fibonacci.py](fibonacci.py).

#### Generalizing

We can think of this sequence as a special case of a class of sequences where
the `i`th number is the sum of the previous `n` numbers in the sequence, with
the first `n` numbers defined arbitrarily.  That is, the Fibonacci sequence is
a special instance where `n=2` with the first numbers `(0, 1)`.

Design a class where the Fibonacci sequence is an instance (eg, `fib =
SummableSequence(...)`). Now, create a new sequence instance where `n=3` and the
initial values are `(5, 7, 11)`; return the value of `new_seq(100000)`.  E.g.:

```python
class SummableSequence(object):

    def __init__(self, *initial):
        ...

    def __call__(self, i):
        ...


if __name__ == '__main__':
    ...
    new_seq = SummableSequence(5, 7, 11)
    print(last_8(new_seq(100000)))
```

***Make sure you apply your learnings from `optimized_fibonacci` to this
class!*** We want this to be an efficient solution as well.

Continue the implementation in [fibonacci.py](fibonacci.py).

### Submit!

Note the `deploy` in your [.travis.yml](.travis.yml).  After your tests
successfully run in CI, this will run [submit.py](submit.py) to submit your
assignment and answer the quiz on Canvas.  Note that the submit script must pull
questions from the quiz, parse the question, and run the appropriate code - you
should not have any hard-coded responses where code can run.  Eg, you will
import your fibonacci functions and run them based on the quiz input.

You can run the submit script manually from your machine if necessary to develop
it (or also see Canvas for a test quiz and assignment), but you should ensure
your final submission is via CI/CD.

You will need to provide the approprate environment variables and Canvas token
to your Travis environment - ***DO NOT COMMIT THESE SECRETS TO THE CODE BASE***.
See Canvas and Travis docs for information.  You can get Canvas ID's usually by
inspecting the URL of an assignment or quiz.  Eg, when on an assignment page,
the URL is:

`https://canvas.harvard.edu/courses/{course_id}/assignments/{assignment_id}`

Deployments should run before the deadline.  However, if there is a substantial
build queue, we will forgive late deployments if the ***commit*** was pushed
before the deadline.

Sometimes, people like to work from their own private repos and Travis accounts,
to allow for more builds and less build queue.  This is fine.  You must,
however, push your code back to the classroom org - the final submission link
must be in our org (even if the build is not).  Point the build badge where you
want, and push your code to the classroom org before peer review and grading
begins.

## Other grading aspects

These will be recurring standards for every problem set.  Please see rubrics in
Canvas for up to date details.

### Testing Quality

Take a look at the file [test_pset.py](test_pset.py).  It has unittests you can
run with `python3 -m unittest` or `pytest`.  They all should pass!  Do not
remove the existing test methods, but you are expected to add new ones to ensure
your code is working properly.  Deciding exactly what tests to add, and how much
coverage you need to achieve, is a decision you must make yourself for every
pset - we will grade partially on whether or not you identify appropriate test
cases.

Try to ensure (the right) tests pass before you commit and merge/push new code
on your master branch! This will help minimize the number of builds on the CI
server.  That is, ***test locally*** first before committing, pushing, or
merging to master.  This is good practice in general and will help with the
shared resources.

#### Test Coverage

Travis/Code Climate will report overall test coverage if set up correctly; try
to cover every major function and clause you write.  Travis will also display
an output of coverage on the terminal.

To help with your own development, you can use tools which show you exactly
which lines are covered, eg:

* [Run tests with coverage in Pycharm](https://www.jetbrains.com/help/pycharm/running-test-with-coverage.html)
* Generate an html report directly with `pytest --cov-report html` then `open htmlcov/index.html`

### Python Quality

We will comment on your overall quality of documentation, commenting,
appropriate variable names, usage of higher-level code, etc.  Be sure to look at
Code Climate reports to help you improve.

### Git History

Git commits should be logically structured, follow a branching model, etc.  Do
not commit irrelevant files to the VCS (eg, anything under `__pycache__` or your
editor/IDE configurations).  Never `git add *` or `git commit -a`!  They lump
all your changes together; you want each commit to be a logical bit of history
that captures what was done and why in a cohesive unit.
