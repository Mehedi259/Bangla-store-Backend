# 🚀 Deployment Guide — Bangla Store Backend (Django API)

This document describes how the Bangla Store Django REST API is deployed to the production server.

---

## 🖥️ Production Environment

| Detail | Value |
|---|---|
| **Server IP** | `167.233.34.127` |
| **API Base URL** | `http://167.233.34.127:8000/api/` |
| **Port** | `8000` |
| **Deployment Method** | Docker + Docker Compose |
| **WSGI Server** | Gunicorn |
| **Database** | SQLite (file: `db.sqlite3`) |
| **Server OS** | Linux (VPS) |

---

## 🐳 Docker Setup

The backend is containerized using a single-stage `Dockerfile`:

- Uses `python:3.11-slim` base image.
- Installs all dependencies from `requirements.txt` + `gunicorn`.
- Runs `gunicorn` binding to `0.0.0.0:8000`.

---

## 📦 Deployment Steps

### 1. SSH into the Server

```bash
ssh root@167.233.34.127
```

### 2. Navigate to the project directory

```bash
cd /opt/website/Bangla-store-Backend
```

### 3. Pull the latest code

```bash
git pull origin main
```

### 4. Apply database migrations (if models changed)

```bash
docker compose exec backend python manage.py migrate
```

### 5. Rebuild and restart the container

```bash
docker compose build backend
docker compose up -d backend
```

---

## 🔄 Quick Deploy from Local (rsync)

```bash
# Sync local backend code to the server (excluding venv and pycache)
rsync -avz --exclude='venv/' --exclude='__pycache__/' --exclude='*.pyc' --exclude='db.sqlite3' \
  /Users/mehedihasanmridul/Backend/Bangla-store-Backend/ \
  root@167.233.34.127:/opt/website/Bangla-store-Backend/

# Rebuild and restart
ssh root@167.233.34.127 'cd /opt/website/Bangla-store-Backend && docker compose build backend && docker compose up -d backend'
```

---

## 🗄️ Database

The project uses **SQLite** for simplicity. The database file `db.sqlite3` is stored on the server and is **not version-controlled** (excluded via `.gitignore`).

> ⚠️ **Warning**: Do not delete the `db.sqlite3` file on the server as it contains all production data (products, categories, orders).

### Running Migrations

```bash
# Inside the container
docker compose exec backend python manage.py migrate

# Or directly on the server if venv is available
python manage.py migrate
```

---

## 📸 Media Files

Uploaded images (product and category images) are stored in the `media/` directory on the server. This directory is mounted as a Docker volume to persist data across container restarts.

---

## 🌐 API Endpoints Reference

| Endpoint | Methods | Description |
|---|---|---|
| `/api/products/` | GET, POST | Products |
| `/api/products/{id}/` | GET, PUT, DELETE | Single product |
| `/api/products/upload/` | POST | Image file upload |
| `/api/products/categories/` | GET, POST | Categories |
| `/api/products/categories/{id}/` | GET, PUT, DELETE | Single category |
| `/api/orders/` | GET, POST | Orders |
| `/api/orders/{id}/` | GET, PUT, DELETE | Single order |
| `/api/dashboard/stats/` | GET | Dashboard statistics |
| `/api/dashboard/sales-overview/` | GET | Monthly sales chart |

---

## 🔗 Related Services

| Service | URL |
|---|---|
| **Customer Frontend** | `http://167.233.34.127:3000` |
| **Admin Dashboard** | `http://167.233.34.127:3001` |
