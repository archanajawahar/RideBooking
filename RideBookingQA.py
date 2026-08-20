from RideBooking import RideBooking


print("===== RIDE BOOKING QA =====")

ride = RideBooking()


# 1. Normal booking
print("\n1. Normal Booking")
fare = ride.calculate_fare(10, 2, "Sedan", 14)
print("Fare:", fare)
print(ride.assign_driver("Sedan"))


# 2. Peak-hour booking
print("\n2. Peak-Hour Booking")
fare = ride.calculate_fare(10, 2, "SUV", 8)
print("Fare:", fare)


# 3. Night booking
print("\n3. Night Booking")
ride2 = RideBooking()
fare = ride2.calculate_fare(10, 2, "Bike", 23)
print("Fare:", fare)


# 4. Invalid distance
print("\n4. Invalid Distance")
ride3 = RideBooking()
print(ride3.calculate_fare(0, 2, "Sedan", 14))


# 5. Invalid passenger count
print("\n5. Invalid Passenger Count")
print(ride3.calculate_fare(10, 5, "Sedan", 14))


# 6. Unavailable driver
print("\n6. Unavailable Driver")
ride4 = RideBooking()
print(ride4.assign_driver("Sedan"))
print(ride4.assign_driver("Sedan"))


# 7. Maximum discount
print("\n7. Maximum Discount")
ride5 = RideBooking()
fare = ride5.calculate_fare(100, 2, "Premium", 14)
print("Fare after discount:", fare)


# 8. Multiple vehicle types
print("\n8. Multiple Vehicle Types")

for vehicle in ["Bike", "Sedan", "SUV", "Premium"]:
    test_ride = RideBooking()
    fare = test_ride.calculate_fare(10, 2, vehicle, 14)
    print(vehicle, "Fare:", fare)


# 9. Boundary fare values
print("\n9. Boundary Fare Values")

ride6 = RideBooking()

print("1 km:", ride6.calculate_fare(1, 1, "Bike", 14))
print("2 passengers:", ride6.calculate_fare(1, 2, "Bike", 14))
print("4 passengers:", ride6.calculate_fare(1, 4, "Bike", 14))


# 10. Driver allocation logic
print("\n10. Driver Allocation Logic")

ride7 = RideBooking()

print("First assignment:",
      ride7.assign_driver("SUV"))

print("Second assignment:",
      ride7.assign_driver("SUV"))


print("\n===== QA COMPLETED =====")
