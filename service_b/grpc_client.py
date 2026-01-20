# gRPC client used to communicate with service_a

import grpc
import user_pb2
import user_pb2_grpc


def get_user(user_id: int):
    # Connect to service_a gRPC server
    channel = grpc.insecure_channel("service_a:50051")
    stub = user_pb2_grpc.UserServiceStub(channel)

    # Send request
    response = stub.GetUser(user_pb2.UserRequest(id=user_id))

    # Return as dictionary
    return {
        "id": response.id,
        "name": response.name,
        "email": response.email
    }
