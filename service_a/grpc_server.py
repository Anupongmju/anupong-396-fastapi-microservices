# ไฟล์นี้ทำหน้าที่เป็น gRPC Server
# service_a จะให้ข้อมูล user ผ่าน gRPC

import grpc
from concurrent import futures

# import code ที่ generate จาก proto
import user_pb2
import user_pb2_grpc


# สร้าง class ที่ implement gRPC service
class UserService(user_pb2_grpc.UserServiceServicer):

    # ฟังก์ชันนี้จะถูกเรียกเมื่อมี gRPC request เข้ามา
    def GetUser(self, request, context):
        # สร้าง response กลับไปให้ client
        return user_pb2.UserResponse(
            id=request.id,
            name="Anupong Mabunrueang",
            email="anupong@example.com"
        )


def serve():
    # สร้าง gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # ผูก service เข้ากับ server
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

    # เปิด port สำหรับ gRPC
    server.add_insecure_port("[::]:50051")

    # เริ่มทำงาน
    server.start()
    print("service_a (gRPC Server) running on port 50051")

    # รอรับ request ตลอดเวลา
    server.wait_for_termination()
