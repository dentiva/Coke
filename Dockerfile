FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./

EXPOSE 8000

# Railway sets $PORT, default to 8000 for local
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
