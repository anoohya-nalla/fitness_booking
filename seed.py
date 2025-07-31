from datetime import datetime, timedelta
from database import SessionLocal, engine, Base
from models import FitnessClass

# Create tables (if not already)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data (optional)
db.query(FitnessClass).delete()

# Add sample classes
classes = [
    FitnessClass(name="Yoga", instructor="Amit", date_time=datetime.now() + timedelta(days=1), available_slots=5),
    FitnessClass(name="Zumba", instructor="Sara", date_time=datetime.now() + timedelta(days=2), available_slots=10),
    FitnessClass(name="HIIT", instructor="John", date_time=datetime.now() + timedelta(days=3), available_slots=8)
]

db.add_all(classes)
db.commit()
db.close()

print("Sample classes added successfully!")
