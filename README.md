# Enterprise Integration APIs

A **FastAPI** backend providing APIs for **Users**, **Orders**, and **Health Check**, designed for integration with **WSO2 API Manager** and documented via **OpenAPI**.

---

## Features

- RESTful APIs for Users and Orders  
- Health check endpoint for monitoring  
- Modular, versioned route structure (`v1`)  
- OpenAPI documentation (`.yaml` files) compatible with WSO2  
- Clean separation: **routes**, **services**, **models**

---

## Tech Stack

- **Backend:** FastAPI, Python 3.11+  
- **Server:** Uvicorn  
- **API Management:** WSO2 API Manager 4.3.0  
- **Database:** Placeholder/fake DB (can integrate with real DB)  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vipunsanjana/integration-enterprise-api-fastapi-wso2
cd integration-enterprise-api-fastapi-wso2
````

2. Create & activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Server

```bash
python -m app.main
```

Swagger UI: `http://localhost:9000/docs`
ReDoc: `http://localhost:9000/redoc`

---

## API Endpoints

| Module | Endpoint               | Method | Description        |
| ------ | ---------------------- | ------ | ------------------ |
| Users  | `/api/v1/users`        | GET    | Get all users      |
| Users  | `/api/v1/users`        | POST   | Create a new user  |
| Orders | `/api/v1/orders`       | GET    | Get all orders     |
| Orders | `/api/v1/orders`       | POST   | Create a new order |
| Health | `/api/v1/health/check` | GET    | API health check   |

---

## OpenAPI Specs

OpenAPI YAML files are in the `OpenAPI/` folder:

* `user-api.yaml`
* `order-api.yaml`
* `health-api.yaml`

These can be imported into WSO2 API Manager for API deployment or testing.

---

## Project Structure

```
.
├── OpenAPI/
├── health-api.yaml
├── order-api.yaml
├── user-api.yaml
├── venv/
├── wso2am-4.3.0/
│   ├── backup/
│   ├── bin/
│   ├── dbscripts/
│   ├── diagnostics-tool/
│   ├── lib/
│   ├── repository/
│   ├── resources/
│   ├── solr/
│   ├── tmp/
│   ├── updates/
│   ├── INSTALL.txt
│   ├── LICENSE.txt
│   ├── README.txt
│   ├── release-notes.html
│   └── XMLInputFactory.properties
├── .gitignore
├── README.md
├── requirements.txt
└── app/
    ├── __pycache__/
    ├── api/
    │   ├── __pycache__/
    │   ├── v1/routes/
    │   │   ├── __pycache__/
    │   │   └── api.py
    │   ├── health.py
    │   ├── order.py
    │   ├── user.py
    │   └── __init__.py
    ├── core/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── db/
    │   │   ├── __pycache__/
    │   │   ├── __init__.py
    │   │   └── fake_db.py
    │   ├── models/
    │   │   ├── __pycache__/
    │   │   ├── __init__.py
    │   │   ├── order.py
    │   │   └── user.py
    │   └── services/
    │       ├── __pycache__/
    │       ├── __init__.py
    │       ├── order_service.py
    │       └── user_service.py
    ├── __init__.py
    └── main.py

```

---
