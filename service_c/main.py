# API Gateway
# Receives client request and forwards to service_b

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/users")
def get_users():
    # Call service_b REST API
    response = requests.get("http://service_b:8000/users")
    return response.json()
