FROM python:latest

RUN pip3 install -r requirements.txt

ADD flask_api.py /

CMD [ "python3", "./flask_api.py" ]
