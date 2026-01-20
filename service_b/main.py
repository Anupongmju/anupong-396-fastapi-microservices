# FastAPI app for service_b
# Acts as REST API that calls gRPC service

from fastapi import FastAPI
from grpc_client import get_user

app = FastAPI()


@app.get("/users")
def read_users():
    # Call gRPC service to get user data
    user = get_user(1)
    return [user]
