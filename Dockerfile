FROM python:3.7

MAINTAINER eu "iklobato1@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]