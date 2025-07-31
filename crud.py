from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import FitnessClass, Booking
from schemas import BookingBase

def get_classes(db: Session):
    """Fetch all available fitness classes."""
    return db.query(FitnessClass).all()

def create_booking(db: Session, booking: BookingBase):
    """Book a spot in a fitness class."""
    # 1. Check if class exists
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == booking.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")

    # 2. Check if slots available
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available for this class")

    # 3. Reduce available slots by 1
    fitness_class.available_slots -= 1

    # 4. Save booking
    db_booking = Booking(
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    return db_booking

def get_bookings_by_email(db: Session, email: str):
    """Fetch all bookings for a specific email."""
    return db.query(Booking).filter(Booking.client_email == email).all()
