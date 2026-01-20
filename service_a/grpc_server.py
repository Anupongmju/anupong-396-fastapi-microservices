# gRPC server for service_a
# This service provides user data via gRPC

import grpc
from concurrent import futures
import time

# Import generated classes (generated at runtime)
import user_pb2
import user_pb2_grpc


class UserService(user_pb2_grpc.UserServiceServicer):
    # Implement GetUser RPC method
    def GetUser(self, request, context):
        # Simulated user data
        return user_pb2.UserResponse(
            id=request.id,
            name="Anupong Mabunrueang",
            email="anupong@example.com"
        )


def serve():
    # Create gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register service
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

    # Listen on port 50051
    server.add_insecure_port("[::]:50051")
    server.start()

    print("gRPC Server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
