FROM python:3.8.0-slim-buster

WORKDIR /code

COPY requirements.txt .
COPY src ./src

RUN pip install --upgrade -v pip
RUN pip install -r requirements.txt

WORKDIR /code/src

CMD [ "python", "./app.py" ]
