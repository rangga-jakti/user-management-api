# User Management API

A simple and clean **User Management REST API** built with **FastAPI**, focusing on backend fundamentals such as API design, validation, and clean architecture.

This project represents **Phase 1**, where the goal is to define a solid API contract before introducing a database.

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Project Goals

- Build a RESTful API using FastAPI
- Practice request and response validation with Pydantic
- Apply clean backend project structure
- Prepare an interview-ready backend portfolio project

---

## Project Structure

app/
api/ # API route definitions
schemas/ # Request & response schemas
core/ # Application configuration
main.py # Application entry point

---

## Running the Project

pip install -r requirements.txt
uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs
