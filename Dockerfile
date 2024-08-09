FROM registry.hub.docker.com/library/python:3.12-slim-bookworm AS requirements-stage

WORKDIR /tmp

# hadolint ignore=DL3013
RUN pip install --no-cache-dir poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

###########

FROM registry.hub.docker.com/library/python:3.12-slim-bookworm

ENV PORT=11111
WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN apt-get -y update && apt-get -y upgrade \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /EdOrg/src

EXPOSE ${PORT}
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT}"]

