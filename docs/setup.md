## Setting up your local environment

You need a computer which can run python 3.7, and preferably an IDE and debugger.
A good example is
[PyCharm, which is free for students](https://www.jetbrains.com/student/).

You may use a ***native*** python distribution (recommended for Mac/Linux) for
this course, or a ***docker***-based python workflow.  The latter may be
required on windows, depending on the pset.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Python](#python)
- [Pipenv](#pipenv)
- [Docker](#docker)
  - [Installation and setup](#installation-and-setup)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Python

You need a good base python installation and terminal/CLI.  Many IDE's provide
the latter, or you can use a system one.

Mac/Linux users can use the default system python if it is available on their
system or default package manager (just don't pip install anything there!).  Mac
users can also use [homebrew](https://brew.sh/) to install python 3.7. If,
however, your system does not provide the correct version of python, you should
use a conda distro as instructed below.  I do not recommend `pyenv`.

***Recommended on Windows***: You can use
[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
to create a base python environment, as well as using the shell in windows:

```bash
conda create -n py37 python=3.7
conda activate py37
pip install pipenv
pipenv install ...
```

### Pipenv

We will use [pipenv](https://pipenv.readthedocs.io/en/latest/) throughout the
course to build repeatable, fully specified python environments.  Pset 0 has no
normal package requirements, so you could get away without setting up pipenv,
but it would be a better idea to give it a shot now!

Instead of `pip install`-ing anything (eg, to run the test suite), use the
included [Pipfile](../Pipfile) to build a new virtual environment with your
project dependencies.

### Docker

This course will explore Docker, a containerization system, to help develop
within fully repeatable environments.  You may need to use docker immediately if
you are developing on Windows (the unittests use
[signals](https://docs.python.org/3.7/library/signal.html#signal.signal)).  You
should experiment with docker regardless, though it is not critical yet.

Older versions of Windows and Mac can install legacy Docker Toolbox or
[VirtualBox](https://www.virtualbox.org/) if necessary.

#### Installation and setup
You can install [Docker](https://docs.docker.com/install/) and
[Docker Compose](https://docs.docker.com/compose/install/) to get a fully
repeatable environment.  You can then [set up PyCharm to use your docker-compose
interpreter](https://www.jetbrains.com/help/pycharm/docker-compose.html), or do
things manually on the terminal via:

```bash
# If your Pipfile changes, or first time
docker-compose build

# Run python in the local directory
docker-compose run app python some_file.py

# Drop into an ipython shell in the container, if it is installed
docker-compose run app ipython

# Run unittests
docker-compose run app pytest
```

Docker is not strictly necessary to complete this initial set - just ensure you
can get it running and will be ready to dive into the concepts if necessary
later.
