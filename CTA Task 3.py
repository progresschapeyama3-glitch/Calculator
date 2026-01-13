from datetime import datetime
"""allow the system to generate and 
display the exact date and time
 when a travel voucher is issued."""

# Data Structures

ZONES = {
    1: {"name": "Central", "stations": ["Centrala", "Jaund", "Soth"]},
    2: {"name": "Midtown", "stations": ["Decia", "Jorsh"]},
    3: {"name": "Downtown", "stations": ["Marend", "Pyrd", "Zord"]}
}

FARE_RATES = {
    "Adult": 2105,
    "Child": 1410,
    "Senior": 1025,
    "Student": 1750
}


# Display Functions

def display_station_board():
    print("\nCentrala Underground – Station Board")
    print("-----------------------------------")
    for zone_id, zone_data in ZONES.items():
        stations = ", ".join(sorted(zone_data["stations"]))
        print(f"Zone {zone_id} ({zone_data['name']}): {stations}")
    input("\nTo continue Press Enter : ")


def select_zone(prompt):
    while True:
        try:
            choice = int(input((prompt)))
            if choice in ZONES:
                return choice
            print("Invalid zone. Please select 1, 2 or 3.")
        except ValueError:
            print("Please enter a number.")


def get_traveller_count(category):
    while True:
        try:
            count = int(input(f"Number of {category}: "))
            if count >= 0:
                return count
            print("Value cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


# -----------------------------
# Processing Functions
# -----------------------------

def calculate_zones_travelled(start, end):
    return abs(start - end) + 1


def calculate_fares(travellers, zones_travelled):
    totals = {}
    for category, count in travellers.items():
        totals[category] = count * FARE_RATES[category] * zones_travelled
    return totals


def display_voucher(start, end, travellers, totals, zones_travelled):
    print("\n--------- CTA TRAVEL VOUCHER ---------")
    print(f"Issue Date/Time: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"From: Zone {start} ({ZONES[start]['name']})")
    print(f"To:   Zone {end} ({ZONES[end]['name']})")
    print(f"Zones Travelled: {zones_travelled}\n")

    total_travellers = 0
    grand_total = 0

    for category in travellers:
        count = travellers[category]
        cost = totals[category]
        total_travellers += count
        grand_total += cost
        print(f"{category}s: {count} | Cost: {cost} cents")

    print("\nTotal Travellers:", total_travellers)
    print("Total Fare:", grand_total, "cents")
    print("----------------------------------")



# Main Program
# -----------------------------

def main():
    while True:
        display_station_board()
        start_zone = select_zone("Select your starting zone from (1-3) ")
        end_zone = select_zone ("Select your end zone from (1-3) ")
        travellers = {
            "Adult": get_traveller_count("Adult"),
            "Child": get_traveller_count("Child"),
            "Senior": get_traveller_count("Senior"),
            "Student": get_traveller_count("Student")
        }
        zones_travelled = calculate_zones_travelled(start_zone, end_zone)
        totals = calculate_fares(travellers, zones_travelled)

        display_voucher(start_zone, end_zone, travellers, totals, zones_travelled)
        again = input("\nIssue another voucher? (yes/no): ")
        if again != "yes":
            print("Thank you for using the CTA Ticketing System.")
            break
if __name__ == "__main__":
    main()
