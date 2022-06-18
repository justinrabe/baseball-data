FROM python:3.9.0

RUN pip install pandas sqlalchemy requests

WORKDIR  /app
COPY main.python
ENTRYPOINT ["python", "main.py"]