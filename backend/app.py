import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

# Menggunakan host 'redis' yang nanti didefinisikan di docker-compose
redis_host = os.environ.get('REDIS_HOST', 'redis')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def home():
    try:
        # Increment counter visits
        count = r.incr('hits')
    except redis.ConnectionError:
        count = "Redis connection failed"
    
    return jsonify({
        "message": "Halo dari ini pesan dari Backend!",
        "visits": count,
        "hostname": os.getenv("HOSTNAME", "local")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)