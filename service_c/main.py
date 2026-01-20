# service_c เป็น API Gateway
# client จะเรียก service นี้โดยตรง

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/users")
def get_users():
    # ส่ง REST request ไปยัง service_b
    response = requests.get("http://service_b:8000/users")

    # ส่ง response กลับไปให้ client
    return response.json()
