# service_b เป็น FastAPI service
# ทำหน้าที่เป็นตัวกลางระหว่าง REST และ gRPC

from fastapi import FastAPI
from grpc_client import get_user

app = FastAPI()


@app.get("/users")
def read_users():
    # รับ REST request จาก service_c
    # เรียก gRPC ไปยัง service_a
    user = get_user(1)

    # ส่งผลลัพธ์กลับเป็น REST response
    return [user]
