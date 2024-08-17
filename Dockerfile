FROM python:3.12-slim AS requirements-stage

WORKDIR /tmp

RUN pip install --no-cache-dir poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

###########

FROM python:3.12-slim

ENV PORT=8000
WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN apt-get -y update && apt-get -y upgrade \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code


EXPOSE ${PORT}
CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT}"]

