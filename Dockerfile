FROM python:3.8-alpine

LABEL maintainer="dipti.bagal@gslab.com"

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./App.py" ]
