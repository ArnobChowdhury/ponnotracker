# 🌊 Ponno Tracker

Inventory and order management system with a FastAPI backend and Next.js frontend.

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose installed.
- `gunicorn` and `uvicorn` added to `backend/requirements.txt`.

---

## 🛠️ Development Environment

In development, we use `docker-compose.override.yml` to enable hot-reloading for both the backend (FastAPI) and frontend (Next.js).

1. **Start the environment:**

   ```bash
   docker compose up --build
   ```

   _Note: Docker Compose automatically merges `docker-compose.yml` and `docker-compose.override.yml`._

2. **Access the services:**
   - Backend API: http://localhost:8000
   - Frontend App: http://localhost:3000
   - Glitchtip: http://localhost:8001

---

## 🏗️ Production Environment

The production setup uses `docker-compose.prod.yml`. It disables hot-reloading, uses Gunicorn as a process manager for the API, and enforces health checks for all services.

1. **Start the production stack:**

   ```bash
   docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
   ```

2. **Key differences in Production:**
   - **Backend:** Runs via Gunicorn with 4 worker threads.
   - **Restart Policy:** Containers are set to `always` restart on failure.
   - **Volumes:** Code is baked into the images; local host volumes are not mounted.
