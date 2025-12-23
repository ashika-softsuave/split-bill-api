# split-bill-api
Split Bill API (FastAPI)
🎯 Project Objective

This project implements a simple Split Bill backend API using FastAPI.
The goal is to understand how to expose backend functionality through a REST API and use all major HTTP methods while keeping data in in-memory storage (no database).

📌 What This Project Covers
✅ REST API Fundamentals

Backend functionality is exposed using HTTP endpoints

Follows REST principles for resource-based operations

✅ HTTP Methods Implemented

This project uses all required HTTP methods:

GET – Fetch bills

POST – Create a new bill

PUT – Update an entire bill

PATCH – Partially update a bill (mark as settled)

DELETE – Remove a bill

✅ FastAPI Framework

Used FastAPI to build a lightweight and high-performance API

Automatic Swagger documentation available at /docs

✅ Pydantic (Request & Response Validation)

Request bodies are validated using Pydantic models

Ensures clean and structured API input handling

✅ In-Memory Data Storage

Bills are stored in Python data structures

No database is used, keeping the project beginner-friendly

🧩 API Endpoints
Method	Endpoint	Description
GET	/	API status check
POST	/bills	Create a bill
GET	/bills	Get all bills
PUT	/bills/{bill_id}	Update a bill
PATCH	/bills/{bill_id}	Settle a bill
DELETE	/bills/{bill_id}	Delete a bill
🛠 Technologies Used

Python

FastAPI

Pydantic

Uvicorn

✅ Project Outcome

This project demonstrates:

REST API design

Proper use of GET, POST, PUT, PATCH, DELETE

Request validation using Pydantic

Clean FastAPI project structure

✔ Beginner-level task completed successfully
✔ Ready for GitHub and learning showcase
