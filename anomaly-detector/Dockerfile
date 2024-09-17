FROM python:3.11-slim

WORKDIR /src/app

COPY ../../deucalion-ad .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
