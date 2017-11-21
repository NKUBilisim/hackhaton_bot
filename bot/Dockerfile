FROM python:3.4-jessie
COPY bot_service ./bot_service
WORKDIR ./bot_service
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python","base.py"]