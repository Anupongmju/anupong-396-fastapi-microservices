Project: anupong-396-fastapi-microservices

This project demonstrates 3 FastAPI microservices
using RESTful API and gRPC for inter-service communication.

Services:
- service_a: gRPC Server (User data provider)
- service_b: gRPC Client + REST API
- service_c: API Gateway (REST)

The goal of this project is to show how REST and gRPC can work
together in a microservices system.

Run the project:
docker-compose up --build

Test:
http://localhost:8000/users
