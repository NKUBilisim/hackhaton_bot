FROM python:3.4-jessie
COPY public_transport_service ./public_transport_service
WORKDIR ./public_transport_service
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python","base.py"]