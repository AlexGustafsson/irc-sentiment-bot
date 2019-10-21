FROM python:3-alpine

RUN mkdir -p /var/www
COPY src /var/www/

RUN python -m pip install -r /var/www/requirements.txt

CMD ["python", "/var/www/index.py"]
