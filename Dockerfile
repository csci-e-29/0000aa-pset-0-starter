FROM python:3.6

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir ipython
RUN pip install --no-cache-dir -r requirements.txt