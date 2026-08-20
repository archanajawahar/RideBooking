from RideBooking import RideBooking


print("===== RIDE BOOKING QA =====")


# 1. Normal booking
print("\n1. Normal Booking")

ride = RideBooking()

fare = ride.calculate_fare(
    "C101",
    "Chennai Central",
    "Guindy",
    10,
    2,
    "Sedan",
    14
)

print("Fare:", fare)
print(ride.assign_driver("Sedan"))


# 2. Peak-hour booking
print("\n2. Peak-Hour Booking")

ride = RideBooking()

fare = ride.calculate_fare(
    "C102",
    "T Nagar",
    "Airport",
    10,
    2,
    "SUV",
    8
)

print("Fare:", fare)


# 3. Night booking
print("\n3. Night Booking")

ride = RideBooking()

fare = ride.calculate_fare(
    "C103",
    "Velachery",
    "Adyar",
    10,
    2,
    "Bike",
    23
)

print("Fare:", fare)


# 4. Invalid distance
print("\n4. Invalid Distance")

ride = RideBooking()

print(ride.calculate_fare(
    "C104",
    "Anna Nagar",
    "Guindy",
    0,
    2,
    "Sedan",
    14
))


# 5. Invalid passenger count
print("\n5. Invalid Passenger Count")

print(ride.calculate_fare(
    "C105",
    "Anna Nagar",
    "Guindy",
    10,
    5,
    "Sedan",
    14
))


# 6. Unavailable driver
print("\n6. Unavailable Driver")

ride = RideBooking()

print(ride.assign_driver("Sedan"))
print(ride.assign_driver("Sedan"))


# 7. Maximum discount
print("\n7. Maximum Discount")

ride = RideBooking()

fare = ride.calculate_fare(
    "C106",
    "Chennai",
    "Mahabalipuram",
    100,
    2,
    "Premium",
    14
)

print("Fare after discount:", fare)


# 8. Multiple vehicle types
print("\n8. Multiple Vehicle Types")

for vehicle in ["Bike", "Sedan", "SUV", "Premium"]:

    ride = RideBooking()

    fare = ride.calculate_fare(
        "C107",
        "Chennai",
        "Airport",
        10,
        2,
        vehicle,
        14
    )

    print(vehicle, "Fare:", fare)


# 9. Boundary fare values
print("\n9. Boundary Fare Values")

ride = RideBooking()

print("1 km:",
      ride.calculate_fare(
          "C108", "A", "B", 1, 1, "Bike", 14
      ))

print("2 passengers:",
      ride.calculate_fare(
          "C109", "A", "B", 1, 2, "Bike", 14
      ))

print("4 passengers:",
      ride.calculate_fare(
          "C110", "A", "B", 1, 4, "Bike", 14
      ))


# 10. Driver allocation logic
print("\n10. Driver Allocation Logic")

ride = RideBooking()

print("First assignment:",
      ride.assign_driver("SUV"))

print("Second assignment:",
      ride.assign_driver("SUV"))


print("\n===== QA COMPLETED =====")
