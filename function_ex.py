# 🪐 Mars Mission Planner — Challenge Steps
#
# function to calculate how long it takes to reach Mars at a given speed.


def travel_time(distance=225000000, speed):
    time = distance / speed
    return round(time)

def total_fuel_cost(distance, fuel_usage=0.3, price_per_liter=1.8):
    total_cost = (distance * fuel_usage * price_per_liter)
    return round(total_cost, 2)

print("Mission 1: [Pathfinder: 40,000 km/h]")


mission 2: [Perseverance: 75,000 km/h]
mission 3: [Starship: 120,000 km/h]



#
# 4. For each mission, print a report showing:
#    - Mission name
#    - Travel time (hours)
#    - Total fuel cost


print("===== Mars Mission Planner =====\n")
