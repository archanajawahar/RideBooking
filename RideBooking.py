class RideBooking:

    def __init__(self):
        self.base_fare = {
            "Bike": 30,
            "Sedan": 80,
            "SUV": 120,
            "Premium": 200
        }

        self.rate_per_km = {
            "Bike": 10,
            "Sedan": 15,
            "SUV": 20,
            "Premium": 30
        }

        self.available_drivers = {
            "Bike": True,
            "Sedan": True,
            "SUV": True,
            "Premium": True
        }

    def calculate_fare(self, customer_id, pickup, drop,
                       distance, passengers, vehicle, booking_time):

        # Customer validation
        if not customer_id:
            return "Invalid customer ID"

        # Location validation
        if not pickup or not drop:
            return "Invalid pickup or drop location"

        # Distance validation
        if distance <= 0:
            return "Invalid distance"

        # Passenger validation
        if passengers <= 0 or passengers > 4:
            return "Invalid passenger count"

        # Vehicle validation
        if vehicle not in self.base_fare:
            return "Invalid vehicle type"

        # Booking time validation
        if booking_time < 0 or booking_time > 23:
            return "Invalid booking time"

        # Driver availability
        if not self.available_drivers[vehicle]:
            return "Driver unavailable"

        # Base fare
        fare = self.base_fare[vehicle]

        # Distance-based fare
        fare += distance * self.rate_per_km[vehicle]

        # Peak-hour surcharge
        if 7 <= booking_time <= 10 or 17 <= booking_time <= 20:
            fare += fare * 0.20

        # Night surcharge
        if booking_time >= 22 or booking_time < 6:
            fare += fare * 0.10

        # Extra passenger surcharge
        if passengers > 2:
            fare += (passengers - 2) * 20

        # Promotional discount
        if fare > 1000:
            fare -= fare * 0.10

        return round(fare, 2)

    def assign_driver(self, vehicle):

        if vehicle not in self.available_drivers:
            return "Invalid vehicle type"

        if self.available_drivers[vehicle]:
            self.available_drivers[vehicle] = False
            return "Driver assigned successfully"

        return "Driver unavailable"


# ---------------- MAIN PROGRAM ----------------

ride = RideBooking()

print("===== RIDE BOOKING SYSTEM =====")

fare = ride.calculate_fare(
    customer_id="C101",
    pickup="Chennai Central",
    drop="Guindy",
    distance=20,
    passengers=2,
    vehicle="Sedan",
    booking_time=14
)

print("Customer ID: C101")
print("Pickup: Chennai Central")
print("Drop: Guindy")
print("Vehicle: Sedan")
print("Final Fare:", fare)

print(ride.assign_driver("Sedan"))
