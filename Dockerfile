FROM python:3.11-slim

WORKDIR /simple-crud-api

COPY . .

COPY eu-central-1-bundle.pem /certs/eu-central-1-bundle.pem

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]