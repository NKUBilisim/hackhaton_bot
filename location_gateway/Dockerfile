FROM python
COPY location ./location
WORKDIR ./location
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python","addr_to_cor.py"]
