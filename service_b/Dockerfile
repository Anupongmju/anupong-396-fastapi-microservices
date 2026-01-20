FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn grpcio grpcio-tools

# Generate gRPC code
RUN python -m grpc_tools.protoc \
    -I./proto \
    --python_out=. \
    --grpc_python_out=. \
    ./proto/user.proto

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
