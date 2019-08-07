## Showing your work!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [CI/CD](#cicd)
- [Git mechanics](#git-mechanics)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

It is not enough to run code in a Jupyter notebook, or even an ipython shell,
and paste the answer into Canvas.  These problem sets will be designed to rerun
your work and validate it through "continuous integration and 'deployment.'"

You may commit any python files you wish, but do NOT commit a Jupyter notebook.
The general pattern for showing work looks like this:

```python
# some_file.py

def f(x):
    return x

if __name__ == '__main__':
    # Canvas asks for the value of f(10)
    print('f(10) is:', f(10))
```

### CI/CD
Take a look at the file [.travis.yml](../.travis.yml).  When you push a commit
to github, [Travis CI](https://travis-ci.com/) will run your code in a number
of ways.  It will first run the unittests via `pytest`, and, if
those succeed, will progress to the 'Answers' stage of the build.  Note in
the file how it invokes your runnables:

```yaml

jobs:
  include:
    - stage: test
      script: pytest
    - stage: answers
      script: python fibonacci.py
```

After you push your code, you will see a few indicators on GitHub that you
can click through to see the status of the build.  Click on the "Commits" tab
and then notice the red checks etc:

![](../img/commits.png)

You can click through the details or navigate directly to your Travis page,
which will have a url like so [PLEASE REPLACE your link!]:

[https://travis-ci.com/csci-e-29/2019sp-pset-0-gorlins/](https://travis-ci.com/csci-e-29/2019sp-pset-0-gorlins/)

You will add a build badge (see below) to make it even more explicit.  The
teaching staff will look at your answers as 'deployed' via Travis to validate
your submissions to Canvas.

***NB***: We have limited concurrent builds.  Depending on how many students
are submitting code simultaneously, your job may hang in 'pending' mode for a
while.  The teaching staff will monitor and upgrade our build plan if necessary.

### Git mechanics

If you have never used Git or Github before, please see the supplemental
tutorials section in Canvas or go through some Github tutorials.  Git has a
steep learning curve.  Ask for help in Piazza if necessary.

Your answers will only run on the master branch.  Since shared computing
resources on the CI/CD environment are limited, please try to minimize the
commits to master - try using a git branching model, and only 'release' work to
master that is intended to be 'production ready' (eg fully answers one of the
problems). You may merge to master multiple times - at the pset deadline, github
will tag the latest master commit.  We will explore branching and release models
like this more formally throughout the course.

Try to avoid rapid small changes to master (eg don't edit directly on github!)
without running tests yourself to ensure they pass.

You may also add `[skip ci]` in your git message to instruct travis not to run
tests for a commit.  Only do so for code that doesn't need testing - eg editing
this README, or docstrings, etc.
