trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

for trip in trips:
    distance = trip["distance"]
    hour = trip["hour"]
    fare = 0.0
    
    # 1. Calculate base distance fare
    if distance <= 2:
        fare = 150
    elif distance <= 10:
        # 150 for first 2 km + 35 per km for the rest
        fare = 150 + (distance - 2) * 35
    else:
        # 150 for first 2 km + 8 km at 35 + rest at 28
        fare = 150 + (8 * 35) + (distance - 10) * 28
        
    # 2. Apply Night Surcharge (10 PM to 5 AM)
    # 10 PM is 22:00, 5 AM is 5:00
    if hour >= 22 or hour <= 5:
        fare = fare + (fare * 0.10)
        time_type = "Night (Surcharge Applied)"
    else:
        time_type = "Day"
        
    print(f"Trip: {distance} km at hour {hour} ({time_type}) -> Total Fare: NPR {fare:.2f}")