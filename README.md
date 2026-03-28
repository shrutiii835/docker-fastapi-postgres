# 🚀 Dockerized FastAPI + PostgreSQL

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

A **production-ready** FastAPI application with PostgreSQL, fully containerized using Docker and Docker Compose.

## ✨ Features

- Modern **FastAPI** with automatic Swagger UI (`/docs`)
- Optimized **multi-stage Dockerfile** (small & secure image)
- Non-root user + health checks
- Multi-container setup with persistent PostgreSQL
- Clean architecture and best practices

## 🛠 Quick Start

```bash
docker compose up --build -d
Access:

API → http://localhost:8000
Swagger Docs → http://localhost:8000/docs
Health Check → http://localhost:8000/health

📁 Project Structure
(See full structure in repository)
🛡️ Technologies

Python 3.12 + FastAPI
SQLAlchemy + PostgreSQL
Docker + Docker Compose
Uvicorn

Production Practices

Multi-stage builds
Non-root container user
Layer caching
.dockerignore
Service health checks
Restart policies

Made as a learning project to demonstrate Docker + DevOps skills.
