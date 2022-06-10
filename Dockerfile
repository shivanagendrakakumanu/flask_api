FROM python:latest

ADD flask_api.py /

ADD requirements.txt /

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "./flask_api.py" ]
