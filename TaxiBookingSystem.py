# Prompting user to enter their Name
name = input("Please input your name: ")
# Outputting the user's Name input
print(f"Welcome {name}!")

# Prompting user to enter their Location details
street_num = int(input("Enter your location's street/building number: "))
street_name = input("Enter your location's street name: ")
city = input("Enter your location's city name: ")

# Variable storing the location details entered by the user
full_address = (f"#{street_num} {street_name}, {city}")
# Outputting the user's location.
print(f"{name}'s Location is: {full_address}")

phone_num = input("Enter your phone number: ")

taxi_booking = input("Would you like to book a taxi with us? (yes/no): ")

if taxi_booking == "yes" or "Yes":
    print("Checking for available drivers...")
    num_of_passengers = int(input("Enter the number of passengers for this taxi booking: "))
    num_of_adults = int(input("Enter the number of adults: "))
    # print("Cost per Adult: $5 x distance")
    num_of_children = int(input("Enter the number of children: "))
    # print("Cost per Child: $2 x distance")
    print(f"This booking contains {num_of_adults} Adult/s and {num_of_children} Child/Children.")


elif taxi_booking == "no" or "No":
    print("You've chosen not to book with us o~o.")
    print("Hope to see you soon!")
else:
    print("Invalid respond. Please try again.")
    print("Please enter 'yes' or 'no'")

if num_of_adults > num_of_passengers:
    print("TAXI BOOKING CANCELLED! This exceeds the number of passengers booked. Please re-try.")

elif num_of_children >= num_of_passengers:
    print("TAXI BOOKING CANCELLED! This input either exceeds the number of passengers or doesn't contain an adult. Please re-try.")
else:
    taxi_type = input("Select Taxi type - Regular, Preferred, Premium: ")
    payment = input("How will you be paying? - Select either 'Cash' or 'Card': ")
    print("Sending information to Drivers...")
    print(f"{name}'s Taxi Booking: Location - {full_address}, Passengers: {num_of_adults} Adults, {num_of_children} Child/Children, Payment method - {payment}.")









