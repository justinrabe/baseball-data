FROM python:3.9.0

RUN pip install pandas sqlalchemy requests

WORKDIR /app

copy main.py main.py

ENTRYPOINT ["python", "main.py"]