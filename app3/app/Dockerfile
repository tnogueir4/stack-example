FROM python:3.8-slim-buster

RUN mkdir /app

ADD . /app

WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENV FLASK_APP=main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]