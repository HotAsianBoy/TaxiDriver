"""A program which keeps track of details for a taxi."""

# Initialize variables
driver_name = input("Please enter the driver's name: ")
total_time = 0
total_income = 0
num_trips = 0

# Main loop for recording trips
while True:
    start_trip = input("Would you like to start a new trip? (yes/no): ")
    if start_trip.lower() == "yes":
        try:
            trip_time = int(input("Please enter the time the trip took in minutes: "))
            if trip_time < 0:
                raise ValueError("Sorry, the time cannot be negative.")
            total_time += trip_time
            trip_cost = 10 + 2 * trip_time
            total_income += trip_cost
            num_trips += 1
            print("Trip cost: $", trip_cost)
        except ValueError as e:
            print("Invalid input:", e)
    elif start_trip.lower() == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Calculate average time and cost
average_time = total_time / num_trips if num_trips > 0 else 0
average_cost = total_income / num_trips if num_trips > 0 else 0

# Print summary
print("\nDriver's name:", driver_name)
print("Total time of all trips:", total_time, "minutes")
print("Average time of all trips:", average_time, "minutes")
print("Total income for the day: $", total_income)
print("Average cost of all trips: $", average_cost)