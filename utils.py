import pytz
from datetime import datetime
import logging

# ---------- Logging Setup ----------
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message: str):
    logging.info(message)

def log_error(message: str):
    logging.error(message)

# ---------- Timezone Conversion ----------
def convert_ist_to_timezone(ist_datetime: datetime, target_timezone: str = "Asia/Kolkata") -> datetime:
    """
    Converts an IST datetime to given timezone.
    If no timezone given, returns IST itself.
    """
    try:
        # Define IST timezone
        ist = pytz.timezone("Asia/Kolkata")
        # Localize datetime to IST
        ist_time = ist.localize(ist_datetime) if ist_datetime.tzinfo is None else ist_datetime
        # Convert to target timezone
        target_tz = pytz.timezone(target_timezone)
        converted_time = ist_time.astimezone(target_tz)
        return converted_time
    except Exception as e:
        log_error(f"Timezone conversion error: {e}")
        # If conversion fails, just return original IST time
        return ist_datetime
