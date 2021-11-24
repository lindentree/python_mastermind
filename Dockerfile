FROM python:3.10-slim-bullseye

WORKDIR /code

COPY . /code/

RUN pip install pipenv

ENV PYTHONPATH /code

RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "/code/main.py"]