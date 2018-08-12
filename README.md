# Pset 0

This pset is mandatory but ungraded - you will get full credit for a complete
submission, but will receive full feedback.  "Grades" will be returned before
the drop date.

**Please complete this Pset before class begins** if possible.

The questions are designed to be solvable with minimal prepwork - you should be
able to complete them with your own experience and limited external research.
If they prove too challenging, please discuss with the teaching staff whether
you should consider delaying enrollment in this course.

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

### Feedback (10 points)

#### How many hours did this assignment take? (2 points)

#### What did you find interesting? Challenging? Tedious? (8 points)