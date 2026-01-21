# score.py

def estimate_price(surface: float, rooms: int) -> int:
    return int(surface * 3000 + rooms * 10000)
    
