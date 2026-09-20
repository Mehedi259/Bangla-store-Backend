<div align="center">

# 🐍 Bangla Store — Django REST API Backend

**The backend API powering the Bangla Store eCommerce platform.**

[![Django](https://img.shields.io/badge/Django-5+-092E20?style=for-the-badge&logo=django)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3+-ff1709?style=for-the-badge)](https://www.django-rest-framework.org)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)](https://docker.com)

</div>

---

## ✨ API Overview

| Endpoint | Methods | Description |
|---|---|---|
| `/api/products/` | GET, POST | List all products / Create new product |
| `/api/products/{id}/` | GET, PUT, DELETE | Single product CRUD |
| `/api/products/upload/` | POST | Upload a product/category image file |
| `/api/products/categories/` | GET, POST | List all categories / Create category |
| `/api/products/categories/{id}/` | GET, PUT, DELETE | Single category CRUD |
| `/api/orders/` | GET, POST | List all orders / Create new order |
| `/api/orders/{id}/` | GET, PUT, DELETE | Single order CRUD (update status etc.) |
| `/api/dashboard/stats/` | GET | Dashboard statistics (revenue, orders, customers, products) |
| `/api/dashboard/sales-overview/` | GET | Monthly sales data for charts |

---

## 🛠️ Tech Stack

- **Framework**: [Django 5+](https://djangoproject.com)
- **API**: Django REST Framework (DRF)
- **Database**: SQLite (development) — can be swapped for PostgreSQL in production
- **File Serving**: Django's `MEDIA_ROOT` for uploaded images
- **Server**: Gunicorn (production)

---

## 📁 Project Structure

```
Bangla-store-Backend/
├── config/               # Django project settings & URLs
│   ├── settings.py       # Main settings (CORS, ALLOWED_HOSTS, MEDIA, etc.)
│   └── urls.py           # Root URL config
├── products/             # Products & Categories app
│   ├── models.py         # Product, Category models
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views (incl. FileUploadView for images)
│   └── urls.py           # Products URL routes
├── orders/               # Orders app
│   ├── models.py         # Order model
│   ├── serializers.py    # Order serializer
│   ├── views.py          # Order API views
│   └── urls.py           # Order URL routes
├── dashboard/            # Dashboard stats app
│   ├── views.py          # Stats & sales overview views
│   └── urls.py           # Dashboard URL routes
├── manage.py
├── requirements.txt
└── Dockerfile
```

---

## 🚀 Getting Started (Local Development)

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/Mehedi259/Bangla-store-Backend.git
cd Bangla-store-Backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`.

---

## 🔑 Key Configuration Notes

### CORS
CORS is enabled for all origins (`CORS_ALLOW_ALL_ORIGINS = True`) to allow requests from the frontend and admin panel.

### Media Files
Uploaded images are stored in the `media/` directory. The backend serves them at `/media/`.

### Allowed Hosts
`ALLOWED_HOSTS = ['*']` is configured to allow the VPS server to serve requests.

---

## 🔗 Related Repositories

| Repo | Description |
|---|---|
| [Bangla-store](https://github.com/Mehedi259/Bangla-store) | Customer-facing frontend |
| [Bangla-store-Admin](https://github.com/Mehedi259/Bangla-store-Admin) | Admin dashboard |

---

## 📄 Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for full deployment instructions.
