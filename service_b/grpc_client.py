# ไฟล์นี้เป็น gRPC client
# ใช้เรียก service_a ผ่าน gRPC

import grpc
import user_pb2
import user_pb2_grpc


def get_user(user_id: int):
    # เชื่อมต่อไปยัง gRPC server ของ service_a
    channel = grpc.insecure_channel("service_a:50051")

    # สร้าง stub สำหรับเรียก method
    stub = user_pb2_grpc.UserServiceStub(channel)

    # ส่ง gRPC request
    response = stub.GetUser(user_pb2.UserRequest(id=user_id))

    # แปลง response เป็น dict เพื่อส่งต่อแบบ REST
    return {
        "id": response.id,
        "name": response.name,
        "email": response.email
    }
