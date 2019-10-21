FROM python:3-alpine

WORKDIR /app
COPY src /app
COPY requirements.txt /app

RUN python -m pip install -r /app/requirements.txt

CMD ["python", "/app/index.py"]
