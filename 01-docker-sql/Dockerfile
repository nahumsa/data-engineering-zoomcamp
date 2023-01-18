FROM python:3.9

RUN pip install -U pip
RUN pip install pipenv

COPY [ "Pipfile", "./"]
COPY [ "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY [ingest_data.py, ingest_data.py]

ENTRYPOINT [ "python", "ingest_data.py" ]