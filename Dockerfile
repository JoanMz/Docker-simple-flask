FROM python:3.11.9-alpine3.19
WORKDIR /app
COPY ./app/app.py /app
COPY ./app/models.py /app
COPY ./app/requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN mkdir /app/Data
CMD ["python3", "/app/app.py"]
EXPOSE 5000
