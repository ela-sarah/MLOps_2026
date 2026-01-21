# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from score import estimate_price

app = FastAPI()

class ApartmentInput(BaseModel):
    location: str
    area_sqm: float
    num_rooms: int


@app.get("/")
def root():
    return {"status": "Apartment price estimation service running"}


@app.post("/estimate")
def estimate_apartment(data: ApartmentInput):

    if data.area_sqm <= 0 or data.num_rooms <= 0:
        raise HTTPException(
            status_code=400,
            detail="Surface and number of rooms must be positive values"
        )

    price = estimate_price(
        surface=data.area_sqm,
        rooms=data.num_rooms
    )

    return {
        "location": data.location,
        "price_estimate": price,
        "inputs": {
            "area_sqm": data.area_sqm,
            "rooms": data.num_rooms
        }
    }