# Simple API Project

This project demonstrates a simple backend API built using modern technologies and follows best practices for development.

## Technology Stack

- **FastAPI**: High-performance API framework.
- **SQLAlchemy**: ORM for database operations.
- **PostgreSQL**: Database engine.
- **Docker Compose**: Container orchestration.

---

## Features

- RESTful API endpoints.
- CRUD operations for managing data.
- Integrated with PostgreSQL database.
- Dockerized setup for easy deployment.

---

## Project Structure

```
.
├── app
│   ├── config                            # Configuration files (e.g., database setup, settings)
│   ├── internal                          # Application logic (features/modules)
│   │   ├── app
│   │   │   └── product                   # Product-related features
│   │   │       ├── handler               # Request handlers (Controllers)
│   │   │       ├── repository            # Data access logic (DAO/Repositories)
│   │   │       └── service               # Business logic layer (use cases)
│   │   ├── dto                           # Data Transfer Objects (schemas for validation)
│   │   └── model                             # SQLAlchemy models (entities)
│   ├── router                            # API routing (FastAPI routers)
│   └── main.py                           # Entry point for the FastAPI application
├── docker-compose.yml                    # Docker Compose configuration for container orchestration
├── requirements.txt                      # Python dependencies
└── README.md                             # Project documentation
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application manually using Uvicorn:
   ```bash
   uvicorn app.main:app --host localhost --port 8001
   ```
   
---

## Example Endpoints

| Method | Endpoint       | Description          |
|--------|----------------|----------------------|
| GET    | /product       | Retrieve all items  |
| POST   | /product       | Create a new item   |
| GET    | /product/{id}  | Retrieve an item    |
| PUT    | /product/{id}  | Update an item      |
| DELETE | /product/{id}  | Delete an item      |

---
