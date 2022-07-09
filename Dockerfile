FROM python:3.9.0

RUN pip install pandas sqlalchemy requests

copy pipeline.py
ENTRYPOINT ["bash"]