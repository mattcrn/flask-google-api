FROM python:3.6
RUN apt-get update -y
COPY ./app /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]