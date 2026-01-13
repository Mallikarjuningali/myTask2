# DevOps Internship Assignment: Django Deployment

Welcome to your practical assessment. You have been provided with a working Django Rest Framework (DRF) application. Your goal is to containerize this application, set up a CI/CD pipeline, and deploy it to a cloud provider.

## Project Overview

The project is a simple API with a single endpoint `/api/hello/` that returns a message from the database.
-   **Core**: Django 5.x
-   **Database**: SQLite (for simplicity, you may switch to PostgreSQL if you wish, but it's not required).
-   **Environment**: Uses `python-dotenv` for configuration.

### Local Setup (for your reference)
1.  `python -m venv venv`
2.  `.\venv\Scripts\Activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3.  `pip install -r requirements.txt`
4.  Create a `.env` file based on your needed configuration (see `settings.py`).
5.  `python manage.py migrate`
6.  `python manage.py runserver`

---

## Your Tasks

### Task 1: Containerization (Docker)
1.  Create a `Dockerfile` for the Django application.
    -   Use a lightweight Python image (e.g., `python:3.11-slim`).
    -   Use **Gunicorn** as the production application server (you may need to add it to `requirements.txt`).
    -   Ensure static files are collected during the build or startup process.
2.  Create a `docker-compose.yml` file to orchestrate the services locally.
    -   Define the Django application service.
    -   Define an **Nginx** service (see Task 2).

### Task 2: Web Server (Nginx)
1.  Configure Nginx as a reverse proxy.
    -   It should forward traffic to the Gunicorn/Django container.
    -   It should serve **static files** directly (Django should not serve static files in production).
2.  Ensure standard security headers are set.

### Task 3: CI/CD Pipeline (GitHub Actions)
1.  Create a GitHub Actions workflow (`.github/workflows/deploy.yml`).
2.  The pipeline should:
    -   Lint the code (e.g., using `flake8`).
    -   Run tests (use `python manage.py test`).
    -   Build the Docker image.

### Task 4: Deployment (Render)
1.  Deploy the application to **Render** (render.com).
    -   You can use Render's "Web Service" with the Docker runtime.
2.  **Configuration**:
    -   Ensure environment variables (`SECRET_KEY`, `DEBUG`) are set in Render's dashboard, NOT hardcoded in the image.
    -   Ensure the database persists (or use Render's managed PostgreSQL if you prefer).
3.  **Submission**:
    -   The live URL (e.g., `https://your-app.onrender.com/api/hello/`) should return a successful response.

## Deliverables
-   A GitHub repository link with your code (Dockerfile, Nginx config, CI/CD workflow).
-   The live URL of the deployed application.
-   A brief text file or markdown document explaining your approach.

Good luck!
