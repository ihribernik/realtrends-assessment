FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:$PYTHONPATH
RUN mkdir /code
WORKDIR /code
COPY dev-requirements.txt /code
COPY requirements.txt /code
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install -r dev-requirements.txt
COPY . /code/