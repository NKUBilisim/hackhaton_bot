FROM python
COPY location .
WORKDIR location
RUN pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python","add_to_cor.py"]