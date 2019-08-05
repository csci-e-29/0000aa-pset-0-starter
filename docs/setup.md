## Setting up your environment

You need a computer which can run python 3.7, and preferably an IDE and debugger.
A good example is
[PyCharm, which is free for students](https://www.jetbrains.com/student/).

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Docker](#docker)
  - [Installation and setup](#installation-and-setup)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Docker
This course will explore Docker, a containerization system, to help develop
within fully repeatable environments.  You may need to use docker immediately
if you are developing on Windows (the unittests use [signals](https://docs.python.org/3.7/library/signal.html#signal.signal)).  You
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

# Drop into an ipython shell in the container
docker-compose run app ipython

# Run unittests
docker-compose run app pytest
```

Docker is not strictly necessary to complete this initial set - just ensure you
can get it running and will be ready to dive into the concepts.
