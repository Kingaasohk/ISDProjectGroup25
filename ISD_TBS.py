import os
from datetime import datetime


# Main Menu
def main_menu():
    while True:  # Loop which allow users to choose options
        print("~ A & A's Taxi Booking System ~ \n")
        print("1. Customer \n")
        print("2. Driver \n")
        print("3. Admin \n")
        print("4. Register \n")
        print("5. Exit \n")

        option = input("Select an option (1-4): \n")

        if option == '1':  # Brings users to Customer MENU
            print("\n      ~|Customer MENU|~       \n")
            customer_menu()

        elif option == '2':
            print("\n      ~|Driver MENU|~       \n")
            driver_menu()

        elif option == '3':
            print("\n      ~|Admin MENU|~       \n")
            admin_menu()

        elif option == '4':
            print("\n~|Registration Menu|~\n")
            register_menu()

        elif option == '5':
            print("\n      ~|Exit MENU|~       \n")
            print("You've chosen to exit...")
            print("Hope to see you Soon!")
            break  # Exits the loop

        else:
            print("\n Selection Invalid...Option selected does not exist... \n ")
            print("\n      《°°°Returning to Main Menu°°°》       \n")


def register_func(role_select, user_name, user_password):
    # Ensure username is unique
    users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                if parts:
                    users.append(parts[0])
    except FileNotFoundError:
        pass

    # Basic validation
    if not user_name or not user_name.strip():
        print("Username cannot be empty.")
        return False
    if ',' in user_name or ',' in user_password:
        print("Username and password cannot contain comma character.")
        return False
    if len(user_password) < 6:
        print("Password must be at least 6 characters long.")
        return False
    if user_name in users:
        print("Username already exists. Please try a different username.")
        return False

    # For Users/Drivers/Admins, collect profile details and create a linked record
    linked_id = ""
    if role_select.lower() == "user":
        print("\nRegistering a new Customer profile:")
        name = input("Full name: \n")
        phone = input("Phone number: \n")
        email = input("Email address: \n")
        linked_id = save_customer(name, phone, email)
    elif role_select.lower() == "driver":
        print("\nRegistering a new Driver profile:")
        name = input("Full name: \n")
        phone = input("Phone number: \n")
        email = input("Email address: \n")
        linked_id = save_driver(name, phone, email)
    elif role_select.lower() == "admin":
        print("\nRegistering a new Admin profile:")
        name = input("Full name: \n")
        email = input("Email address: \n")
        linked_id = save_admin(name, email)

    # Persist user login (username,password,role,linked_id)
    with open("users.txt", "a") as f:
        f.write(f"{user_name},{user_password},{role_select},{linked_id}\n")

    print(f"Registration successful for {user_name} as {role_select}.")
    return True


def register_menu():
    register_confirm = input("Do you want to register with us as a User, Driver or Admin? (yes/no): \n")
    if register_confirm.strip().lower() == "yes":
        while True:
            role_select = input("Choose role (Admin/Driver/User) or type 'back' to cancel: \n").strip().lower()
            if role_select == "admin":
                user_name = input("Input your username: \n")
                user_password = input("Input your password: \n")
                if register_func("Admin", user_name, user_password):
                    break
            elif role_select == "driver":
                user_name = input("Input your username: \n")
                user_password = input("Input your password: \n")
                if register_func("Driver", user_name, user_password):
                    break
            elif role_select == "user":
                user_name = input("Input your username: \n")
                user_password = input("Input your password: \n")
                if register_func("User", user_name, user_password):
                    break
            elif role_select == "back":
                print("Registration cancelled. Returning to main menu.")
                return
            else:
                print("Invalid option. Please enter Admin, Driver, User or back.")
        return
    elif register_confirm.strip().lower() == "no":
        print("Registration cancelled.")
        return


def login_user():
    username = input("Username: \n").strip()
    password = input("Password: \n").strip()
    try:
        with open("users.txt", "r") as f:
            for line in f:
                parts = [p.strip() for p in line.strip().split(',')]
                if len(parts) >= 3:
                    u, p, role = parts[0], parts[1], parts[2]
                    linked = parts[3] if len(parts) > 3 else ""
                    if u == username and p == password:
                        return u, role, linked
    except FileNotFoundError:
        pass
    print("Login failed: invalid username or password.")
    return None


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


# This function displays the Customer MENU options
def customer_menu():
    # Loop which allow customers to select options
    while True:

        print("\n1. Book a Taxi \n")
        print("2. View my Booking/s \n")
        print("3. Cancel my Booking/s \n")
        print("4. Return to Main Menu \n")

        option = input("Select an option (1-4): \n")

        # Allows users to enter details and create a taxi booking
        if option == '1':
            print("\nPlease login to book a taxi. If you don't have an account, choose Register from the Main Menu.\n")
            auth = login_user()
            if not auth:
                input("Press Enter to continue")
                continue
            username, role, linked = auth
            if role.strip().lower() != 'user':
                print("Only customers (role 'User') can book taxis. Please register as a User first.")
                input("Press Enter to continue")
                continue

            customer_id = linked
            # If the user account has no linked customer profile, create one now
            if not customer_id:
                print("No customer profile found for this account. Please provide profile details now.")
                name = input("Full name: \n")
                phone = input("Phone number: \n")
                email = input("Email address: \n")
                customer_id = save_customer(name, phone, email)
                # update users.txt to link this account
                update_user_linked_id(username, customer_id)
            else:
                name, phone, email = get_customer_info(customer_id)

            # Get booking-specific details (pickup/dropoff)
            full_pickup_address, full_dropoff_address, pickup_date, pickup_time = booking_details()
            booking_available = booking_time_availability(pickup_date, pickup_time)
            if booking_available == True:
                # Calls on book_taxi() and saves it to bookings.txt
                book_taxi(customer_id, name, full_pickup_address, full_dropoff_address, pickup_date, pickup_time)
            elif booking_available == False:
                print("\n A booking already exists at the selected date and time. Please choose a different slot. \n")
                break
            # Prompts user to press enter to move forward
            input("\n Press Enter to continue \n")

        # Allows customers to view their booking/s
        elif option == '2':
            customer_id = input("\n Enter your Customer ID to view your booking/s: ")
            view_my_bookings(customer_id)
            input("Press Enter to continue")

        # Allows customers to cancel their booking/s
        elif option == '3':
            cancel_booking()
            input("Press Enter to continue")

        # Brings users back to Main Menu
        elif option == '4':  # Returns users to Main Menu
            print("\n Returning to Main Menu... \n")
            break  # Ends the customer menu loop

        else:
            # Outputs statement if users don't enter options '1', '2' or '3'
            print("\n Option selected does not exist...Selection Invalid. \n")


# This function displays the Driver MENU options
def driver_menu():
    print("\n      ~|Driver LOGIN MENU|~       \n")
    auth = login_user()
    if not auth:
        print("\n Returning to Main Menu... \n")
        return

    username, role, linked = auth
    if role.strip().lower() != 'driver':
        print("Access denied: account is not a driver.")
        print("\n Returning to Main Menu... \n")
        return

    driver_id = linked
    # If no linked driver profile exists, prompt to create one
    if not driver_id:
        print("No driver profile found for this account. Please provide driver details now.")
        name = input("Full name: \n")
        phone = input("Phone number: \n")
        email = input("Email address: \n")
        driver_id = save_driver(name, phone, email)
        update_user_linked_id(username, driver_id)

    print(f"\n      ~|Welcome Driver {driver_id}|~       \n")

    # Loop which allow drivers to select options
    while True:
        print("\n 1. View Assigned Trips  \n")
        print("\n 2. Return to Main Menu \n")

        option = input("Select an option (1-2): \n")

        if option == '1':
            view_driver_trips(driver_id)
            input("Press Enter to continue")

        elif option == '2':
            print("Press Enter to continue")
            print("\n Returning to Main Menu... \n")
            break
        else:
            print("\n Option selected does not exist...Selection Invalid. \n")


# This function displays the Admin MENU options
def admin_menu():
    print("\n      ~|Admin LOGIN MENU|~       \n")
    auth = login_user()
    if not auth:
        print("\n Returning to Main Menu... \n")
        return

    username, role, linked = auth
    if role.strip().lower() != 'admin':
        print("Access denied: account is not an admin.")
        print("\n Returning to Main Menu... \n")
        return

    admin_id = linked
    # If no linked admin profile exists, prompt to create one
    if not admin_id:
        print("No admin profile found for this account. Please provide admin details now.")
        name = input("Full name: \n")
        email = input("Email address: \n")
        admin_id = save_admin(name, email)
        update_user_linked_id(username, admin_id)

    print("\n      ~|Admin MENU|~       \n")
    print(f"\n    《Welcome Admin {admin_id}!》       \n")

    # Loop which allow admins to select options
    while True:
        print("\n1. View All Bookings  \n")
        print("2. Assign Driver to Booking  \n")
        print("3. Return to Main Menu \n")

        option = input("Select an option (1-3): \n")

        if option == '1':
            view_all_bookings()
            input("Press Enter to continue")

        elif option == '2':
            assign_driver()
            input("Press Enter to continue")

        elif option == '3':
            print("\n Returning to Main Menu... \n")
            break
        else:
            print("\n Option selected does not exist...Selection Invalid. \n")


# This function generates an ID and saves the customer.
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

    print(
        f"\nYour Customer ID : {customer_id} 《PLEASE NOTE: This unique ID is used to access and cancel your bookings!》 \n")
    print("《It is recommended that you save it.》\n")

    return customer_id  # Returns customer ID


def save_driver(name, phone_num, email):
    # Generates a unique driver ID for each driver
    try:
        with open("drivers.txt", "r") as file:
            driver_id = str(sum(1 for line in file) + 1)
    except FileNotFoundError:
        driver_id = '1'

    with open("drivers.txt", "a") as file:
        file.write(f"{driver_id},{name},{phone_num},{email}\n")

    print(f"\nYour Driver ID : {driver_id}\n")
    return driver_id


def save_admin(name, email):
    # Generates a unique admin ID for each admin
    try:
        with open("admins.txt", "r") as file:
            admin_id = str(sum(1 for line in file) + 1)
    except FileNotFoundError:
        admin_id = '1'

    with open("admins.txt", "a") as file:
        file.write(f"{admin_id},{name},{email}\n")

    print(f"\nYour Admin ID : {admin_id}\n")
    return admin_id


# This function reads the file and finds bookings for the Customer ID entered.
def view_my_bookings(customer_id):
    print(f"\n      ~|Bookings for Customer ID: {customer_id}|~       \n")
    try:
        with open("bookings.txt", "r") as file:
            found = False
            for line in file:
                # Splits the first two commas: booking_id, customer_id, rest
                parts = line.split(',', 2)
                if len(parts) >= 2 and parts[1].strip() == str(customer_id):
                    # Print the entire line except the booking id and customer id
                    rest = parts[2].strip() if len(parts) > 2 else ''
                    print(rest)
                    found = True
            if not found:
                print("No bookings found for this Customer ID.")
    except FileNotFoundError:
        print("No bookings have been made yet.")


# This function allows a customer to cancel booking/s
def cancel_booking():
    print("\n      ~|Cancel Booking MENU|~       \n")

    # Prompts user to enter their Customer ID
    customer_id = input("Enter your Customer ID: ")
    view_my_bookings(customer_id)  # Shows customers their bookings before cancelling

    print("\n      ~|Cancelling Booking Options|~       \n")
    print("1. Cancel a Specific Booking\n")
    print("2. Cancel All my Bookings\n")
    print("3. Return to Customer MENU\n")

    option = input("Select an option (1-3): \n")

    if option == '1':
        # Cancels specific booking
        booking_id = input("\n Enter the Booking ID of the trip you want to cancel: # ")

        original_file = "bookings.txt"
        temp_file = "temp.txt"
        booking_cancelled = False

        try:
            with open(original_file, "r") as infile, open(temp_file, "w") as outfile:
                for line in infile:
                    parts = line.split(',', 2)
                    # Checks if line has Booking ID and Customer ID
                    if len(parts) >= 2 and parts[0].strip() == booking_id and parts[1]:
                        booking_cancelled = True
                        continue
                    outfile.write(line)

            os.replace(temp_file, original_file)

            if booking_cancelled:
                print(f"\nBooking #{booking_id} has been cancelled.")
            else:
                print(f"\nBooking #{booking_id} not found.")

        except FileNotFoundError:
            print("No bookings have been made yet.")

    elif option == '2':
        # Cancel all bookings
        confirm = input("\nAre you sure you want to cancel ALL bookings? (yes/no): ").strip().lower()

        if confirm == 'yes':
            original_file = "bookings.txt"
            temp_file = "temp.txt"
            booking_cancelled = False

            try:
                with open(original_file, "r") as infile, open(temp_file, "w") as outfile:
                    for line in infile:
                        parts = line.split(',', 2)
                        if len(parts) >= 2 and parts[1].strip() == customer_id:
                            booking_cancelled = True
                            continue
                        outfile.write(line)

                os.replace(temp_file, original_file)

                if booking_cancelled:
                    print(f"\nAll bookings for Customer ID #{customer_id} have been cancelled.")
                else:
                    print("\nNo bookings found for this Customer ID.")

            except FileNotFoundError:
                print("No bookings have been made yet.")
        else:
            print("\nCancellation cancelled.")

    elif option == '3':
        print("\nReturning to Customer MENU...")
    else:
        print("\nInvalid option.")


# This function allows Admins to view all bookings made within the system
def view_all_bookings():
    print("\n      ~|All System Bookings|~       \n")
    try:
        with open("bookings.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No bookings to view as yet.")


def view_driver_trips(driver_id):
    print(f"\n      ~|Assigned Trips for Driver ID: {driver_id} |~       \n")

    found = False
    try:
        with open("bookings.txt", "r") as file:
            for line in file:

                # split from the right: ... , status, driver_id
                parts = line.rsplit(',', 2)
                if len(parts) >= 3 and parts[2].strip() == str(driver_id):
                    print(line.strip())
                    found = True

            if not found:
                print("You have no assigned trips.")
    except FileNotFoundError:
        print("No bookings found yet.")


def assign_driver():
    # Displays all the bookings to the admin
    view_all_bookings()

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
            # check booking id as the first CSV field
            first_part = line.split(',', 1)[0].strip()
            if first_part == booking_id:
                if ", Pending, None" in line:
                    updated_status = line.strip().replace(", Pending, None", f",Assigned,{driver_id}\n")
                    lines_to_keep[i] = updated_status
                    updated_booking_status = True
                    print(f"Bookings #{booking_id} Found. Updating Status...")
                else:
                    print(f"Booking #{booking_id} has already been assigned. 《Status Unchanged》")

        if updated_booking_status:
            with open("bookings.txt", "w") as file:
                file.writelines(lines_to_keep)
            print(f"Booking #{booking_id} was successfully assigned to Driver #{driver_id}")
        elif not updated_booking_status and booking_id in [line.split(',')[0] for line in lines_to_keep]:
            print(f"Failed to assign Booking #{booking_id}. 《Status Unchanged》")
        else:
            print(f"Booking with ID #{booking_id} not found.")
    except FileNotFoundError:
        print("No bookings found to assign...")

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



# This function saves the booking.
def book_taxi(customer_id, name, full_pickup_address, full_dropoff_address, pickup_date, pickup_time):
    taxi_booking = input("\n Would you like to confirm and continue with these booking details? (yes/no): ")

    if taxi_booking.lower() == "yes":
        print("\n Checking for available drivers...")

        try:
            num_of_passengers = int(input("\n Enter the number of passengers for this taxi booking: \n "))
            num_of_adults = int(input("\n Enter the number of adults: "))
            num_of_children = int(input("\n Enter the number of children: \n "))
        except ValueError:
            print("\n Invalid Input. PLEASE Enter numbers only. \n")
            print("\n Booking Cancelled... \n")
            return

        print(f"\n This booking contains {num_of_adults} Adult/s and {num_of_children} Child/Children. \n")

        # Checks if number of adults exceeds number of passengers entered
        if num_of_adults > num_of_passengers:
            print("TAXI BOOKING CANCELLED! Adults exceed total passengers. Please Re-try. \n")
            return

        elif num_of_children + num_of_adults != num_of_passengers:
            print(
                "TAXI BOOKING CANCELLED! Adult and Child count does not match the total number of passengers. Please Re-try. \n")
            return

        # Checks if number children exceeds or equals the number of passengers
        elif num_of_children >= num_of_passengers:
            print("TAXI BOOKING CANCELLED! Children exceed or no Adults are present. Please Re-try. \n")
            return

        taxi_type = input("\n Select Taxi type - Regular, Preferred, Premium: ")
        payment = input("\n How will you be paying? - Select either 'Cash' or 'Card': ")

        full_booking = (f"Pickup: {full_pickup_address} | Drop-off: {full_dropoff_address}"
                        f"| Passengers: {num_of_passengers}"
                        f"| {num_of_adults} Adult/s, {num_of_children} Child/Children"
                        f"| Taxi type: {taxi_type}"
                        f"| Payment Method: {payment}")

        print("\n Sending information to Drivers....\n")
        print(full_booking)

        try:
            with open("bookings.txt", "r") as file:

                booking_id = str(sum(1 for line in file) + 1)
        except FileNotFoundError:
            booking_id = '1'

        status = "Pending"
        driver_id = "None"

        with open("bookings.txt", "a") as file:
            file.write(f"{booking_id}, {customer_id}, "
                       f"{full_booking}, {status}, {driver_id}\n")

        print(f"Your Trip Booking #{booking_id} has been made and pending driver assignment.")

    elif taxi_booking.lower() == "no":
        print("You've chosen not to book with us. Hope to see you soon!")


    else:
        print("\n Invalid response. Please enter 'yes' or 'no' ")


# Calling main_menu function to run program when executed directly
if __name__ == "__main__":
    main_menu()
