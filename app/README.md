# User Management API

A clean and production-oriented User Management REST API built with FastAPI, focusing on backend fundamentals such as API design, validation, and maintainable architecture.

This project is a personal backend project simulating real-world client requirements, where the primary objective is to design a solid and extensible API contract before introducing a database layer.

This repository has completed Milestone 1, emphasizing correctness, clarity, and backend best practices.

# Simulated Client Context

This API simulates a backend service for a hypothetical SaaS application that requires user management capabilities such as registration, authentication, and role-based access.

The project is intentionally designed to reflect how backend engineers work with:

- product requirements
- API contracts
- validation rules
- incremental backend development

without relying on a frontend application.

# Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

# Key Features (Current Milestone)

- Health check endpoint for service monitoring
- User request & response validation using Pydantic
- Clean API routing structure
- Centralized configuration setup
- Clear separation between API routes and schemas

Note: This milestone focuses on API design and validation.
Database integration and authentication will be introduced in later milestones.

# Project Goals

- Design a RESTful API following backend best practices
- Apply request and response validation with Pydantic
- Build a clean, scalable backend project structure
- Simulate real-world backend development workflows
- Prepare an interview-ready backend portfolio project

# Project Milestones

## Milestone 1 - API Foundation (Completed)

Objective
Build a clean and extensible REST API foundation before introducing persistence or authentication.

Completed Scope

- FastAPI project setup
- Clean backend folder structure
- Request & response validation with Pydantic
- Health check endpoint
- Centralized configuration
- Client-style documentation

Value Demonstrated

- Backend API design fundamentals
- Validation-first development
- Clean architecture mindset

## Milestone 2 - Authentication & Persistence (Planned)

Objective
Introduce secure authentication and data persistence.

Planned Scope

- Database integration
- User CRUD operations
- Password hashing
- JWT-based authentication

## Milestone 3 - Production Readiness (Planned)

Objective
Prepare the API for production-like environments.

Planned Scope

- Role-based access control
- Pagination and filtering
- Logging and environment-based configuration
- Basic automated testing

# Project Structure

app/
-api/ # API route definitions
-schemas/ # Request & response schemas
-core/ # Application configuration
-main.py # Application entry point

# Development Philosophy

- Backend-first approach — API contract before database
- Explicit validation — clear input and output schemas
- Scalable structure — prepared for future feature growth
- Production mindset — readable, maintainable, and testable code

# Running the Project

pip install -r requirements.txt
uvicorn app.main:app --reload

Open the interactive API documentation at:
=> http://127.0.0.1:8000/docs
