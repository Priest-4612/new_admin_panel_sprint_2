FROM python:3.7-slim

WORKDIR /app
COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r ./requirements.txt --no-cache-dir
COPY ./app ./app
RUN ls -al
RUN ls -al app
CMD ["gunicorn", "config.wsgi:application", "--bind", "0:8000" ]
