FROM ubuntu:bionic

RUN apt update && \
    apt install -y python3-pip python3-dev

COPY ./requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app

RUN pip3 install -r requirements.txt

COPY ./access /usr/src/app

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]
