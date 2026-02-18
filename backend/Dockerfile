FROM python:3.9-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Gunakan Gunicorn untuk production server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]