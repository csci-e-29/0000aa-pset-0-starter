# pset-0-starter

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
