FROM python:3.8-alpine
COPY ./requirements.txt /system73/requirements.txt

WORKDIR /system73

RUN pip install -r requirements.txt

COPY . /system73

ENTRYPOINT [ "python" ]

CMD ["app.py" ]