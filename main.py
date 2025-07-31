from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from database import Base, engine, get_db
from models import FitnessClass
import crud, schemas
from utils import convert_ist_to_timezone, log_info, log_error

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Studio Booking API")

@app.get("/classes", response_model=List[schemas.FitnessClassOut])
def get_classes(timezone: str = Query("Asia/Kolkata"), db: Session = Depends(get_db)):
    """
    Get all classes. Default timezone = IST.
    If timezone provided (e.g., America/New_York), class times are converted.
    """
    try:
        classes = crud.get_classes(db)
        # Convert times
        for cls in classes:
            cls.date_time = convert_ist_to_timezone(cls.date_time, timezone)
        log_info(f"Classes retrieved for timezone: {timezone}")
        return classes
    except Exception as e:
        log_error(f"Error retrieving classes: {e}")
        raise e

@app.post("/book", response_model=schemas.BookingOut)
def book_class(booking: schemas.BookingBase, db: Session = Depends(get_db)):
    """
    Book a spot in a fitness class.
    """
    try:
        booking_result = crud.create_booking(db, booking)
        log_info(f"Booking successful for {booking.client_email} in class {booking.class_id}")
        return booking_result
    except Exception as e:
        log_error(f"Booking error: {e}")
        raise e

@app.get("/bookings", response_model=List[schemas.BookingOut])
def get_bookings(email: str, db: Session = Depends(get_db)):
    """
    Get all bookings for a given email.
    """
    try:
        bookings = crud.get_bookings_by_email(db, email)
        log_info(f"Bookings retrieved for email: {email}")
        return bookings
    except Exception as e:
        log_error(f"Error fetching bookings: {e}")
        raise e
