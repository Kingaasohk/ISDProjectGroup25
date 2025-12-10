
import os
from datetime import datetime



# This Functions registers new users as Customers or Drivers
def register_func(role_select, user_name, user_password, name, phone, email):

    # Ensures username is unique
    users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if parts:
                    users.append(parts[0])
    except FileNotFoundError:
        pass

    # Checks Username to ensure they meet certain conditions
    if not user_name or not user_name.strip():
        return False, "Username cannot be empty."

    if ',' in user_name or ',' in user_password:
        return False, "Username and password cannot contain comma character."

    if len(user_password) < 6:
        return False, "Password must be at least 6 characters long."

    if user_name in users:
        return False, "Username already exists. Please try a different username."

    # Saves and creates personal details along with a linked_id

    linked_id = ""
    if role_select.lower() == "customer":
        linked_id = save_customer(name, phone, email)
    elif role_select.lower() == "driver":
        linked_id = save_driver(name, phone, email)

    # Saves User login details to users.txt file

    with open("users.txt", "a") as f:
        f.write(f"{user_name},{user_password},{role_select},{linked_id}\n")

    return True, f"Registration successful for {user_name} as {role_select}. Your ID is: {linked_id}"

# This Function check User Details to verify login
def login_user(username, password):

    try:
        with open("users.txt", "r") as f:
            for line in f:
                parts = [p.strip() for p in line.strip().split(',')]
                if len(parts) >= 3:
                    u, p, role = parts[0], parts[1], parts[2]
                    linked = parts[3] if len(parts) > 3 else ""
                    if u == username and p == password:
                        return True, u, role, linked
    except FileNotFoundError:
        pass

    return False, None, None, None

# This Function updates linked_id for a User account
def update_user_linked_id(username, new_linked_id):

    try:
        lines = []
        with open("users.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return False

    updated = False
    for i, line in enumerate(lines):
        parts = [p.strip() for p in line.strip().split(',')]
        if parts and parts[0] == username:
            while len(parts) < 4:
                parts.append("")
            parts[3] = str(new_linked_id)
            lines[i] = ','.join(parts) + '\n'
            updated = True
            break

    if updated:
        with open("users.txt", "w") as f:
            f.writelines(lines)
    return updated


# This Function generates a new Customer ID for each Customer and saves their details
def save_customer(name, phone_num, email):

    # Generates a unique customer ID for each customer
    try:
        with open("customers.txt", "r") as file:
            # Counts each line to get to the next customer ID
            customer_id = str(sum(1 for line in file) + 1)
    except FileNotFoundError:
        # If the file is not found it will create this as the first ID
        customer_id = '1'

    # Saves customer details with ID in a simple format
    with open("customers.txt", "a") as file:
        file.write(f"{customer_id},{name},{phone_num},{email}\n")

    return customer_id  # Returns customer ID

# This Function accesses Customer information using Customer ID
def get_customer_info(customer_id):

    try:
        with open("customers.txt", "r") as f:
            for line in f:
                parts = [p.strip() for p in line.strip().split(',')]
                if parts and parts[0] == str(customer_id):
                    # customer_id,name,phone,email
                    return parts[1], parts[2], parts[3]
    except FileNotFoundError:
        pass
    return None, None, None

# This Function receives booking details from Customer
def booking_details():

    enter_prompt = print("\n |~Enter Pickup Details~|  \n")
    pickup_street_num = input("\n Enter your pickup location's street/building number: #")
    pickup_street_name = input("\n Enter your pickup location's street name: \n ")
    pickup_city = input("\n Enter your pickup location's city name: \n ")
    pickup_date = input("\n Enter the date for your taxi booking (DD/MM/YYYY): ")
    pickup_time = input("\n Enter the time for your taxi booking (HH:MM): ")

    full_pickup_address = (
        f"#{pickup_street_num} {pickup_street_name}, {pickup_city} on {pickup_date} at {pickup_time}")
    print(f"\n Pickup Location is: {full_pickup_address}")

    enter_prompt = print("\n |~Enter Drop-off Details~|  \n")
    dropoff_street_num = input("\n Enter your drop-off location's street/building number: #")
    dropoff_street_name = input("\n Enter your drop-off location's street name: ")
    dropoff_city = input("\n Enter your drop-off location's city name: ")
    full_dropoff_address = (f"#{dropoff_street_num} {dropoff_street_name}, {dropoff_city}")
    print(f"\n Drop-off Location is: {full_dropoff_address}")

    return full_pickup_address, full_dropoff_address, pickup_date, pickup_time


# This Function creates a new taxi booking
def book_taxi(customer_id, name, full_pickup_address, full_dropoff_address,
              num_of_passengers, num_of_adults, num_of_children, taxi_type, payment):


    try:
        num_of_passengers = int(num_of_passengers)
        num_of_adults = int(num_of_adults)
        num_of_children = int(num_of_children)
    except ValueError:
        return False, "Invalid Input. PLEASE Enter numbers only."

    # Checks if number of adults exceeds number of passengers entered
    if num_of_adults > num_of_passengers:
        return False, "TAXI BOOKING CANCELLED! Adults exceed total passengers. Please Re-try."

    elif num_of_children + num_of_adults != num_of_passengers:
        return False, "TAXI BOOKING CANCELLED! Adult and Child count does not match the total number of passengers. Please Re-try."

    # Checks if number children exceeds or equals the number of passengers
    elif num_of_children >= num_of_passengers:
        return False, "TAXI BOOKING CANCELLED! Children exceed or no Adults are present. Please Re-try."

    # Creates full booking string
    full_booking = (f"Pickup: {full_pickup_address} | Drop-off: {full_dropoff_address}"
                    f"| Passengers: {num_of_passengers}"
                    f"| {num_of_adults} Adult/s, {num_of_children} Child/Children"
                    f"| Taxi type: {taxi_type}"
                    f"| Payment Method: {payment}")

    # Generate booking ID
    try:
        with open("bookings.txt", "r") as file:
            booking_id = str(sum(1 for line in file) + 1)
    except FileNotFoundError:
        booking_id = '1'


    status = "Pending"
    driver_id = "None"

    # Save booking
    with open("bookings.txt", "a") as file:
        file.write(f"{booking_id}, {customer_id}, "
                   f"{full_booking}, {status}, {driver_id}\n")

    return True, f"Your Trip Booking #{booking_id} has been made and pending driver assignment."

# This Function allows Customers to view their bookings using their Customer ID
def view_my_bookings(customer_id):

    bookings = []

    try:
        with open("bookings.txt", "r") as file:
            for line in file:
                # Splits the first two commas: booking_id, customer_id, rest
                parts = line.split(',', 2)
                if len(parts) >= 2 and parts[1].strip() == str(customer_id):
                    booking_id = parts[0].strip()
                    # Get the entire line except the Booking ID and Customer ID
                    rest = parts[2].strip() if len(parts) > 2 else ''
                    bookings.append({'id': booking_id, 'details': rest})
    except FileNotFoundError:
        pass

    return bookings

# This Function allows Customers to select specific cancellation option using Booking ID and Customer ID
def cancel_booking(booking_id=None, customer_id=None, cancel_all=False):

    original_file = "bookings.txt"
    temp_file = "temp.txt"
    booking_cancelled = False

    try:
        with open(original_file, "r") as infile, open(temp_file, "w") as outfile:
            for line in infile:
                parts = line.split(',', 2)

                if cancel_all:
                    # Cancel all bookings for this customer
                    if len(parts) >= 2 and parts[1].strip() == str(customer_id):
                        booking_cancelled = True
                        continue
                else:
                    # Cancel specific booking by ID
                    if len(parts) >= 2 and parts[0].strip() == str(booking_id):
                        booking_cancelled = True
                        continue

                outfile.write(line)

        os.replace(temp_file, original_file)

        if booking_cancelled:
            if cancel_all:
                return True, f"All bookings for Customer ID #{customer_id} have been cancelled."
            else:
                return True, f"Booking #{booking_id} has been cancelled."
        else:
            if cancel_all:
                return False, "No bookings found for this Customer ID."
            else:
                return False, f"Booking #{booking_id} not found."

    except FileNotFoundError:
        return False, "No bookings have been made yet."

# This Function checks if a booking already exists in the system with the same date and time entered when a new booking is being submitted
def booking_time_availability(pickup_date, pickup_time):

    try:
        with open("bookings.txt", "r") as file:
            for raw_line in file:
                line = raw_line.strip()

                # Skip empty or corrupted lines
                if not line or "Pickup:" not in line:
                    continue

                # Find the pickup section safely
                try:
                    pickup_section = line.split("Pickup:", 1)[1]
                except:
                    continue

                # Extract the date
                if " on " not in pickup_section or " at " not in pickup_section:
                    continue

                try:
                    after_on = pickup_section.split(" on ", 1)[1]
                    date_part = after_on.split(" at ", 1)[0].strip()

                    # Extract time (before next pipe '|')
                    after_at = after_on.split(" at ", 1)[1]
                    time_part = after_at.split("|", 1)[0].strip()

                except:
                    continue

                # Compare
                if date_part == pickup_date and time_part == pickup_time:
                    return False  # Found overlapping booking

    except FileNotFoundError:
        return True

    return True



# This Function Generates a new Driver ID for each Driver and saves their Details
def save_driver(name, phone_num, email):

    # Generates a unique driver ID for each driver
    try:
        with open("drivers.txt", "r") as file:
            driver_id = str(sum(1 for line in file) + 1)
    except FileNotFoundError:
        driver_id = '1'

    with open("drivers.txt", "a") as file:
        file.write(f"{driver_id},{name},{phone_num},{email}\n")

    return driver_id

# This Function allows Drivers to view trips/bookings assigned to them by Admins through their Driver ID
def view_driver_trips(driver_id):

    trips = []

    try:
        with open("bookings.txt", "r") as file:
            for line in file:
                # split from the right: ... , status, driver_id
                parts = line.rsplit(',', 2)
                if len(parts) >= 3 and parts[2].strip() == str(driver_id):
                    trips.append(line.strip())
    except FileNotFoundError:
        pass

    return trips

# This Function gets a list of all Drivers for Admins to assign Customer Bookings
def get_all_drivers():

    drivers = []

    try:
        with open("drivers.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    drivers.append({'id': parts[0], 'name': parts[1]})
    except FileNotFoundError:
        pass

    return drivers


# This Function generates  an Admin ID for admins and saves their details
# No need for this again I believe
def save_admin(name, email):

    # Generates a unique admin ID for each admin
    try:
        with open("admins.txt", "r") as file:
            admin_id = str(sum(1 for line in file) + 1)
    except FileNotFoundError:
        admin_id = '1'

    with open("admins.txt", "a") as file:
        file.write(f"{admin_id},{name},{email}\n")

    return admin_id

# This Function displays all booking within the system to Admins
def view_all_bookings():

    bookings = []

    try:
        with open("bookings.txt", "r") as file:
            for line in file:
                bookings.append(line.strip())
    except FileNotFoundError:
        pass

    return bookings

# This Function allows Admins to assign a Driver to a booking using the Booking ID and Driver ID
def assign_driver(booking_id=None, driver_id=None):


    if booking_id is None or driver_id is None:
        # Displays all the bookings to the Admin
        all_bookings = view_all_bookings()
        for booking in all_bookings:
            print(booking)

        # Prompts Admin to enter the Booking ID they want to assign
        booking_id = input("\n Enter the Booking ID of the trip you would like to assign: \n")
        # Prompts Admin to enter the Driver ID they want to assign the booking to
        driver_id = input("\n Enter the Driver ID of the driver you would like to assign the trip to: \n")

    # Starts of by assuming the status of the booking is not updated
    updated_booking_status = False
    # A list which temporarily stores all the lines in the file
    lines_to_keep = []

    try:
        with open("bookings.txt", "r") as file:
            lines_to_keep = file.readlines()

        for i, line in enumerate(lines_to_keep):
            # Checks Booking ID as the first CSV field
            first_part = line.split(',', 1)[0].strip()
            if first_part == booking_id:
                if ", Pending, None" in line:
                    updated_status = line.strip().replace(", Pending, None", f", Assigned, {driver_id}\n")
                    lines_to_keep[i] = updated_status
                    updated_booking_status = True
                else:
                    return False, f"Booking #{booking_id} has already been assigned. 《Status Unchanged》"

        if updated_booking_status:
            with open("bookings.txt", "w") as file:
                file.writelines(lines_to_keep)
            return True, f"Booking #{booking_id} was successfully assigned to Driver #{driver_id}."
        else:
            return False, f"Booking with ID #{booking_id} not found."

    except FileNotFoundError:

        return False, "No bookings found to assign..."
