FROM python:3.9.0

RUN pip install pandas sqlalchemy requests

WORKDIR /app

copy pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]