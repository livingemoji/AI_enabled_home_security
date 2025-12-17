import requests
from datetime import datetime
from config import GEO_API_URL

def get_location():
    try:
        response = requests.get(GEO_API_URL, timeout=5)
        data = response.json()
        if data.get("status") == "success":
            return f"{data.get('city')}, {data.get('country')}"
    except:
        pass
    return "Unknown Location"

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_location_and_time():
    return f"📍 Location: {get_location()}\n🕒 Time: {get_timestamp()}"
