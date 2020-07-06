FROM python:3

ADD requirements.txt /requirements.txt

RUN apt-get update &&
    && pyvenv /venv \
    && /venv/bin/pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt"

RUN mkdir /code/
WORKDIR /code/
ADD . /code/

# Add any custom, static environment variables needed by Django or your settings file here:
ENV FLASK_APP=app.py

EXPOSE 5000
ENTRYPOINT ["/venv/bin/flask", "run"]
