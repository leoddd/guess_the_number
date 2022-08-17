FROM python:3.9-alpine

COPY . /app/
WORKDIR /app/
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "./app.py"]
CMD ["python3", "./app.py"]
