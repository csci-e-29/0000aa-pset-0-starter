FROM python:3.7 AS base

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_SRC=/src \
    PIPENV_HIDE_EMOJIS=true \
    PIPENV_COLORBLIND=true \
    PIPENV_NOSPIN=true

RUN pip install pipenv

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --deploy --ignore-pipfile --dev

ENTRYPOINT ["pipenv", "run"]
