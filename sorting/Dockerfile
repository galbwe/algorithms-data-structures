FROM python:3.7.3-alpine

ENV PYTHONPATH /sorting/src

WORKDIR /sorting

COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install -r requirements.txt

COPY . .

CMD pytest
