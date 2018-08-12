# Pset 0

This pset is mandatory but ungraded - you will get full credit for a complete
submission, but will receive full feedback.  "Grades" will be returned before
the drop date.

**Please complete this Pset before class begins** if possible.

The questions are designed to be solvable with minimal prep work - you should be
able to complete them with your own prior knowledge and limited external
research. If they prove too challenging, please discuss with the teaching staff
whether you should consider delaying enrollment in this course.

## Setting up your environment

You need a computer which can run python 3, and preferably an IDE and debugger.
A good example is
[PyCharm, which is free for students](https://www.jetbrains.com/student/).

You can install [Docker](https://docs.docker.com/install/) and
[Docker Compose](https://docs.docker.com/compose/install/) to get a fully
repeatable environment.  You can then [set up PyCharm to use your docker-compose
interpreter](https://www.jetbrains.com/help/pycharm/docker-compose.html), or do
things manually on the terminal via:

```bash
# If your requirements.txt changes, or first time
docker-compose build

# Run python in the local directory
docker-compose run app python some_file.py

# Drop into an ipython shell in the container
docker-compose run app ipython
```

You may commit any python files you wish, but do NOT commit a Jupyter notebook.
You may commit and run code like this:

```python
# some_file.py

def f(x):
    return x

if __name__ == '__main__':
    print('f(10) is:', f(10))
```

## Grading standards and mechanics

You will submit your problem via editing this repository and pushing your code
to Github Classroom before the deadline.

Please ensure that this README is visibly accurate on GitHub after your final
submission.

This is a Markdown file which allows for easy writing of rich text.  Many
editors and IDEs will display a rendered version of this text for easy reading.
Please read more about
[GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/)
for style and syntax references.

###  Submissions
Some problems will require code, and some will be textual.  For the latter, you
should enter your answers inline in this file below the heading.  All code which
supports an answer must be committed and referred to from this file.

In addition to the answers you provide, we will subjectively grade you on the
overall quality of your submission - stylistic consistency, readability, design,
documentation, commenting, appropriate commit history, etc.  Treat this
assignment as if it were a collaborative project in a real working environment.

For example, regarding git history, we do not want to see a single commit with
all of your work.  You should have an appropriate amount of history with
consistent and logically isolated commits, minimal 'undo' commits, no
unnecessary files added, etc.

Grading breakdown:

1. Problems: 80 points
2. Overall python quality assessment: 10 points
3. Overall git history/etc quality assessment: 10 points

## Problems (80 points)

### Python project (10 points)

Describe a Python project that you have been involved in. Provide details. For
example, how did you design a data structure or algorithm? How did yor approach
error handling, modular design, etc?

### Importing (10 points)

What is the difference between the following statements? When would you prefer
each? *(NB: the package is irrelevant)*

```python
import urllib
from urllib import request
import urllib.request
```

### Trees (10 points)

Read the code below, but do ***not*** run it - evaluate it by sight or on paper
only.  What is the output of the program? Explain the different between
`print_all_1()` and `print_all_2()`.

```python
class Node(object):
  def __init__(self, name):
    self._children = []
    self.name = name

  def __repr__(self):
    return "<Node '{}'>".format(self.name)

  def append(self, *args, **kwargs):
    self._children.append(*args, **kwargs)

  def print_all_1(self):
    print(self)
    for child in self._children:
      child.print_all_1()

  def print_all_2(self):
    def generator(obj):
      all = [obj,]
      while all:
        next = all.pop(0)
        all.extend(next._children)
        yield next

    for node in generator(self):
      print(node)

root = Node("root")
child1 = Node("child1")
child2 = Node("child2")
child3 = Node("child3")
child4 = Node("child4")
child5 = Node("child5")
child6 = Node("child6")

root.append(child1)
root.append(child2)
child1.append(child3)
child1.append(child4)
child2.append(child5)
child2.append(child6)

root.print_all_1()
root.print_all_2()
```

### Pyramid (15 points)

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

Print a pyramid of height 10

### Fibonacci (25 points)

The Fibonacci sequence, `f(i)`, is defined as `(0, 1, 1, 2, 3, 5, 8, …)` where
the `i`th number is the sum of the two proceeding numbers, with `f(0) == 0` and
`f(1) == 1`.  A common implementation of the function adds the result of
calling itself on a smaller number, i.e.:

```python
def f(i):
    return f(i - 1) + f(i - 2)
```

with appropriate handling of the edge cases.

#### Naive implementation (5 points)

Describe the pros and cons of this implementation.  How does it scale as `i`
gets large?

#### What is the value of `f(100000)` (10 points)?

Note: the common implementation may not work! Your code should
execute very quickly.  Describe any changes you made in terms of scaling,
time/memory tradeoffs, etc, and ensure your working function is committed.

#### Generalizing (10 points)

We can think of this sequence as a special case of a class of sequences where
the `i`th number is the sum of the previous `n` numbers in the sequence, with
the first `n` numbers defined arbitrarily.   That is, the Fibonacci sequence is
a special instance where `n=2` with the first numbers `(0, 1)`.

Design a class where the Fibonacci sequence is an instance (you can use the
common implementation logic - we don’t need to scale right now!). Now, create a
new sequence instance where `n=3` and the initial values are `(5, 7, 11)`;
return the value of `new_seq(20)`.  E.g.:

```python
class SummableSequence(object):

    def __init__(self, n, initial):
        ...

    def __call__(self, i):
        ...


if __name__ == '__main__':
    fib = SummableSequence(2, (0, 1))
    assert fib(6) == 8

    new_seq = SummableSequence(3, (5, 7, 11))
    print(new_seq(20))
```

### Feedback (10 points)

#### How many hours did this assignment take? (2 points)

#### What did you find interesting? Challenging? Tedious? (8 points)

## Python Quality (10 points)
Notes from TA may go here

## Git History (10 points)
Notes from TA may go here

## Total Grade
Notes from TA may go here
