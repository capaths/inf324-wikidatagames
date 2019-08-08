import os

from app import app

PROD = os.environ.get("ENV") == "prod"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080 if PROD else 8081)
