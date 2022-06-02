FROM python:3.10.2-slim-buster

RUN apt-get update -qy
RUN apt-get install curl -qy

# install poetry
RUN pip install poetry
RUN poetry config virtualenvs.in-project true

ADD pyproject.toml /pyproject.toml
RUN poetry install

