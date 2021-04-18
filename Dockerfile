FROM python:alpine3.7

COPY App.py /app

COPY requirements.txt /app

EXPOSE 9090

ENTRYPOINT [ "python" ]

CMD [ "App.py" ]