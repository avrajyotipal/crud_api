# Student Management API

A backend REST API for managing student records using **FastAPI, Python, SQLAlchemy, SQLite, and Pydantic**.

This project demonstrates how to build a clean CRUD-based REST API with request validation, database persistence, dependency injection, appropriate HTTP status codes, and automatically generated Swagger API documentation.

---

## 📌 Project Overview

The **Student Management API** allows users to create, retrieve, update, and delete student records.

Each student contains:

- Student ID
- Name
- Email
- Age
- Course

The application uses **SQLite** as the database, making it lightweight and easy to run locally without requiring an external database server.

FastAPI automatically generates interactive API documentation through Swagger UI, making it easy to test all endpoints.

---

## 🚀 Features

- Create a new student
- Retrieve all students
- Retrieve a student by ID
- Update an existing student
- Delete a student
- Pydantic request validation
- Email validation
- Age validation
- Duplicate email prevention
- Proper HTTP status codes
- SQLAlchemy ORM integration
- SQLite database
- FastAPI dependency injection
- Automatic Swagger documentation
- Clean separation of API, schema, model, database, and CRUD logic

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI application server |
| Pydantic | Request/data validation |
| SQLAlchemy | ORM and database interaction |
| SQLite | Database |
| Swagger UI | Interactive API documentation |

---

## 📂 Project Structure

```text
student_management_api/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
├── .gitignore
└── students.db
```

### File Description

#### `main.py`

Contains the FastAPI application and API endpoints.

Responsible for:

- Creating the FastAPI application
- Defining routes
- Handling HTTP requests
- Returning HTTP responses
- Handling API exceptions
- Creating database tables

---

#### `database.py`

Responsible for the SQLite database configuration.

It contains:

- SQLite connection URL
- SQLAlchemy engine
- Database session
- Database dependency

Example:

```python
DATABASE_URL = "sqlite:///./students.db"
```

---

#### `models.py`

Contains the SQLAlchemy database model.

The `Student` model represents the `students` table in SQLite.

---

#### `schemas.py`

Contains Pydantic schemas used for:

- Request validation
- Response serialization
- Email validation
- Age validation
- Field length validation

---

#### `crud.py`

Contains the database CRUD operations:

- Create
- Read
- Update
- Delete

Keeping these operations separate from `main.py` makes the application easier to maintain.

---

#### `requirements.txt`

Contains the Python dependencies required to run the project.

---

#### `students.db`

SQLite database file automatically created when the application starts.

> The database file should normally be excluded from Git using `.gitignore`.

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/student-management-api.git
```

Move into the project directory:

```bash
cd student-management-api
```

---

## 2. Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the dependencies manually:

```bash
pip install fastapi uvicorn sqlalchemy pydantic[email]
```

---

# ▶️ Running the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will start at:

```text
http://127.0.0.1:8000
```

You should see output similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to:

- View available endpoints
- Inspect request schemas
- Enter request data
- Execute API calls
- View API responses
- Test validation errors
- Test different HTTP status codes

---

## ReDoc

FastAPI also provides ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 🔌 API Endpoints

The application provides the following endpoints:

| Method | Endpoint | Description | Success Status |
|---|---|---|---|
| POST | `/students` | Create student | `201 Created` |
| GET | `/students` | Get all students | `200 OK` |
| GET | `/students/{student_id}` | Get student by ID | `200 OK` |
| PUT | `/students/{student_id}` | Update student | `200 OK` |
| DELETE | `/students/{student_id}` | Delete student | `204 No Content` |

---

# 1️⃣ Create Student

### Endpoint

```http
POST /students
```

### Request Body

```json
{
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "age": 23,
    "course": "FastAPI"
}
```

### Successful Response

**Status: `201 Created`**

```json
{
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "age": 23,
    "course": "FastAPI",
    "id": 1
}
```

The student is stored permanently in the SQLite database.

---

# 2️⃣ Get All Students

### Endpoint

```http
GET /students
```

### Successful Response

**Status: `200 OK`**

```json
[
    {
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "age": 23,
        "course": "FastAPI",
        "id": 1
    },
    {
        "name": "Priya Singh",
        "email": "priya@gmail.com",
        "age": 24,
        "course": "Python",
        "id": 2
    }
]
```

---

# 3️⃣ Get Student by ID

### Endpoint

```http
GET /students/{student_id}
```

### Example

```http
GET /students/1
```

### Successful Response

**Status: `200 OK`**

```json
{
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "age": 23,
    "course": "FastAPI",
    "id": 1
}
```

### Student Not Found

If the requested student doesn't exist:

**Status: `404 Not Found`**

```json
{
    "detail": "Student not found"
}
```

---

# 4️⃣ Update Student

### Endpoint

```http
PUT /students/{student_id}
```

### Example

```http
PUT /students/1
```

### Request Body

```json
{
    "name": "Rahul Kumar",
    "email": "rahul.kumar@gmail.com",
    "age": 24,
    "course": "Advanced FastAPI"
}
```

### Successful Response

**Status: `200 OK`**

```json
{
    "name": "Rahul Kumar",
    "email": "rahul.kumar@gmail.com",
    "age": 24,
    "course": "Advanced FastAPI",
    "id": 1
}
```

---

# 5️⃣ Delete Student

### Endpoint

```http
DELETE /students/{student_id}
```

### Example

```http
DELETE /students/1
```

### Successful Response

**Status: `204 No Content`**

The student is permanently removed from the SQLite database.

If the student doesn't exist:

**Status: `404 Not Found`**

```json
{
    "detail": "Student not found"
}
```

---

# ✅ Pydantic Validation

The project uses Pydantic to validate incoming student data before it reaches the database.

The following rules are applied.

| Field | Validation |
|---|---|
| `name` | Required, 2–100 characters |
| `email` | Required, valid email format |
| `age` | Required, between 16 and 100 |
| `course` | Required, 2–100 characters |

Example:

```json
{
    "name": "A",
    "email": "invalid-email",
    "age": 10,
    "course": ""
}
```

This request fails validation.

FastAPI returns:

```text
422 Unprocessable Entity
```

---

# 🔐 Duplicate Email Validation

Email addresses are configured as unique in the database.

For example, if the following student already exists:

```json
{
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "age": 23,
    "course": "FastAPI"
}
```

Attempting to create another student using:

```json
{
    "name": "Another Student",
    "email": "rahul@gmail.com",
    "age": 25,
    "course": "Python"
}
```

will return:

```text
409 Conflict
```

with:

```json
{
    "detail": "Student with this email already exists"
}
```

---

# 🌐 HTTP Status Codes

The API uses appropriate HTTP status codes.

| Status Code | Meaning | Usage |
|---|---|---|
| `200` | OK | Successful GET/PUT |
| `201` | Created | Student successfully created |
| `204` | No Content | Student successfully deleted |
| `404` | Not Found | Student doesn't exist |
| `409` | Conflict | Duplicate email |
| `422` | Unprocessable Entity | Pydantic validation failure |

---

# 🗄️ Database

This project uses SQLite.

The database URL is:

```python
DATABASE_URL = "sqlite:///./students.db"
```

When the application starts, SQLAlchemy executes:

```python
Base.metadata.create_all(bind=engine)
```

This creates the required database table if it doesn't already exist.

No separate database server is required.

---

# 🧩 Application Architecture

The project follows a simple layered architecture:

```text
                   Client
                     │
                     ▼
              FastAPI Endpoint
                     │
                     ▼
             Pydantic Schema
              Data Validation
                     │
                     ▼
               CRUD Layer
                     │
                     ▼
              SQLAlchemy ORM
                     │
                     ▼
                 SQLite
                     │
                     ▼
              students.db
```

### Request Flow

For example, when creating a student:

```text
POST /students
       │
       ▼
StudentCreate
       │
       ▼
Pydantic Validation
       │
       ▼
create_student()
       │
       ▼
SQLAlchemy
       │
       ▼
SQLite
       │
       ▼
StudentResponse
       │
       ▼
JSON Response
```

---

# 🧠 FastAPI Concepts Demonstrated

This project demonstrates several important FastAPI concepts.

### 1. Path Parameters

```python
@app.get("/students/{student_id}")
```

`student_id` is extracted from the URL.

---

### 2. Request Body

```python
def create_student_api(
    student: StudentCreate
):
```

FastAPI automatically reads and validates the JSON request body.

---

### 3. Pydantic Models

```python
class StudentCreate(BaseModel):
```

Used for validating incoming API data.

---

### 4. Response Models

```python
response_model=StudentResponse
```

Controls the structure of the API response.

---

### 5. Dependency Injection

```python
db: Session = Depends(get_db)
```

FastAPI automatically provides a database session to the endpoint.

---

### 6. HTTP Exceptions

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

Used to return meaningful API errors.

---

### 7. SQLAlchemy ORM

Instead of writing raw SQL queries, the application uses Python objects and SQLAlchemy.

For example:

```python
db.query(Student).all()
```

retrieves all students.

---

# 🧪 Testing the API

The easiest way to test the project is through Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Recommended testing sequence:

```text
1. POST /students
        ↓
2. GET /students
        ↓
3. GET /students/{student_id}
        ↓
4. PUT /students/{student_id}
        ↓
5. GET /students/{student_id}
        ↓
6. DELETE /students/{student_id}
        ↓
7. GET /students/{student_id}
```

You should also test error scenarios:

```text
Invalid email
Invalid age
Missing required fields
Non-existent student ID
Duplicate email
Invalid student ID
```

---

# 🧪 Example Test Data

You can use the following records while testing.

### Student 1

```json
{
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "age": 23,
    "course": "FastAPI"
}
```

### Student 2

```json
{
    "name": "Priya Singh",
    "email": "priya@gmail.com",
    "age": 24,
    "course": "Python"
}
```

### Student 3

```json
{
    "name": "Amit Verma",
    "email": "amit@gmail.com",
    "age": 22,
    "course": "Data Science"
}
```

---

# 🔍 Example Validation Failure

Request:

```json
{
    "name": "A",
    "email": "abc",
    "age": 12,
    "course": ""
}
```

Expected result:

```text
422 Unprocessable Entity
```

This demonstrates that invalid data is rejected before being inserted into the database.

---

# 🔄 CRUD Operations

The project implements the complete CRUD lifecycle.

```text
CREATE
   │
   └── POST /students

READ
   │
   ├── GET /students
   └── GET /students/{student_id}

UPDATE
   │
   └── PUT /students/{student_id}

DELETE
   │
   └── DELETE /students/{student_id}
```

---

# 🔒 Security Considerations

This project is intended as a learning and portfolio project.

For a production application, additional security features would be required, such as:

- Authentication
- Authorization
- JWT tokens
- API keys or OAuth2
- Rate limiting
- HTTPS
- Secure configuration management
- Database migrations
- Structured logging
- Exception handling
- Input sanitization
- Production database such as PostgreSQL

---

# 🚧 Future Improvements

The current application provides basic CRUD functionality. It can be extended with:

### API Improvements

- `PATCH /students/{student_id}` for partial updates
- Pagination
- Sorting
- Search by student name
- Filter by course
- Filter by age
- Student enrollment history

### Backend Improvements

- Service layer
- Repository pattern
- Global exception handlers
- Structured logging
- Database migrations with Alembic
- Automated tests with Pytest

### Security

- JWT authentication
- Role-based authorization
- API key authentication
- Rate limiting

### Deployment

The application could eventually be deployed using:

```text
FastAPI
   │
   ▼
Docker
   │
   ▼
Cloud Platform
   │
   ▼
PostgreSQL
```

---

# 🐳 Docker Support

A future version of this project can be containerized using Docker.

Example architecture:

```text
Client
  │
  ▼
FastAPI Container
  │
  ▼
Database
```

For production deployments, PostgreSQL would generally be a better choice than SQLite.

---

# 📊 Learning Outcomes

After completing this project, you should understand:

- How FastAPI applications are structured
- How REST APIs work
- CRUD operations
- HTTP methods
- HTTP status codes
- Path parameters
- Request bodies
- Pydantic validation
- Response models
- Dependency injection
- SQLAlchemy ORM
- SQLite integration
- Database sessions
- Exception handling
- Swagger API documentation

---

# 🎯 Project Goals

The primary goal of this project is to gain practical experience building a backend API rather than simply learning FastAPI syntax.

The project demonstrates the complete flow:

```text
Client Request
      ↓
FastAPI
      ↓
Pydantic Validation
      ↓
CRUD Logic
      ↓
SQLAlchemy
      ↓
SQLite
      ↓
API Response
```

---

# 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/<your-username>`


---

# 📄 License

This project is intended for educational and portfolio purposes.

You may modify and extend the project for your own learning and development.