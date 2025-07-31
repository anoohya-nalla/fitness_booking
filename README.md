
# Fitness Studio Booking API

This is a simple booking API for a fictional fitness studio built using **FastAPI** and **SQLite**.  
It supports:
- Listing available fitness classes
- Booking a class with slot availability check
- Viewing all bookings for a given email
- Timezone conversion for class timings
- Basic input validation, logging, and unit tests


## Setup and Run Instructions

### 1. Install dependencies
Run the following command to install all required libraries:
```bash
pip install fastapi uvicorn sqlalchemy pydantic email-validator pytz pytest httpx
```

### 2. Add sample data

Run the seed script to insert sample fitness classes (Yoga, Zumba, HIIT):

```bash
python seed.py
```

### 3. Run the server

Start the FastAPI development server:

```bash
python -m uvicorn main:app --reload
```

### 4. Open Swagger UI

Open your browser and go to:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
From here, you can directly test the API endpoints.

## Sample API Requests

### Get Classes

Fetch all available fitness classes:

```bash
curl http://127.0.0.1:8000/classes
```

### Book a Class

Book a class by providing class ID, client name, and email:

```bash
curl -X POST http://127.0.0.1:8000/book \
-H "Content-Type: application/json" \
-d '{"class_id":1,"client_name":"John Doe","client_email":"john@example.com"}'
```

### Get Bookings by Email

Fetch all bookings for a specific email:

```bash
curl "http://127.0.0.1:8000/bookings?email=john@example.com"
```

### Timezone Example

Convert class timings to a different timezone (e.g., America/New\_York):

```bash
curl "http://127.0.0.1:8000/classes?timezone=America/New_York"
```

## Running Tests

To run basic unit tests for the API:

```bash
python -m pytest
```

You should see all tests passing.

## Logging

All important actions and errors are logged in `app.log`.

## Author

Nalla Anoohya

