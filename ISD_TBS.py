import os

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
	
    return

def register_menu():
	
	register_confirm = input("Do you want to register with us as a User,Driver or Admin? (yes/no): \n")
	print(register_confirm)
	if register_confirm.lower == "yes":
		while True:
			role_select = input("Admin or Driver: \n")
			if role_select == "Admin" or "admin":
				user_name = input("Input your username: \n")
				user_password = input("Input your password: \n")
				register_func(role_select, user_name,user_password)
			elif role_select == "Driver" or "driver":
				user_name = input("Input your username: \n")
				user_password = input("Input your password: \n")
				register_func(user_name,user_password)
			elif role_select == "User" or "user":
				user_name = input("Input your username: \n")
				user_password = input("Input your password: \n")
				register_func(user_name,user_password)
		else:
			print("Invalid option returning...")
			return
	elif register_confirm.lower == "no":
		print("Debug String \n" + register_confirm)
		return




# This function displays the Customer MENU options
def customer_menu():
    # Loop which allow customers to select options
    while True:

        print("\n1. Register and Book a Taxi \n")
        print("2. View my Booking/s \n")
        print("3. Cancel my Booking/s \n")
        print("4. Return to Main Menu \n")

        option = input("Select an option (1-4): \n")

        # Allows users to enter details and create a taxi booking
        if option == '1':
            # Calls on user_input() and collects user details
            name, full_pickup_address, full_dropoff_address, phone_num, email = user_input()

            # Calls on save_customer() and saves it to customers.txt
            customer_id = save_customer(name, phone_num, email)

            # Calls on book_taxi() and saves it to bookings.txt
            book_taxi(customer_id, name, full_pickup_address,
                      full_dropoff_address)

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

    # Prompts drivers to enter Passcode inorder to LOGIN
    driver_pass = input("Enter your Driver LOGIN Passcode: ")

    # Passcode ALL Drivers have to enter inorder to gain access to the Driver MENU
    if driver_pass == '41895drive':
        print("\n      ~|Driver MENU|~       \n")
        driver_id = int(input("Enter your Driver ID: # "))
        print(f"\n      ~|Welcome Driver {driver_id}|~       \n")

        # Loop which allow drivers to select options
        while True:

            print("1. View Assigned Trips  \n")
            print("2. Return to Main Menu \n")


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
    else:
        print("Invalid Driver ID or Passcode.")
        print("\n Returning to Main Menu... \n")

# This function displays the Admin MENU options
def admin_menu():
    admin_pass = input("Enter your Admin Passcode: ")

    # Passcode ALL Admins have to enter inorder to gain access to the Admin MENU
    if admin_pass == '1413914admin':
        print("\n      ~|Admin MENU|~       \n")
        print(f"\n    《Welcome Admin!》       \n")

        # Loop which allow drivers to select options
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
    else:
        print("Invalid Admin Passcode.")
        print("\n Returning to Main Menu... \n")


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


# This function reads the file and finds bookings for the Customer ID entered.
def view_my_bookings(customer_id):
    print(f"\n      ~|Bookings for Customer ID: {customer_id}|~       \n")
    try:
        with open("bookings.txt", "r") as file:
            found = False
            for line in file:
                # The first part of the line is the customer_id
                if line.startswith(customer_id + ','):
                    # Print the entire line with the booking details
                    print(line[len(customer_id) + 1:].strip())
                    found = True
            if not found:
                print("No bookings found for this Customer ID.")
    except FileNotFoundError:
        print("No bookings have been made yet.")


# This function allows a customer to cancel booking/s
def cancel_booking():
    print("\n      ~|Cancel Booking MENU|~       \n")

    #Prompts user to enter their Customer ID
    customer_id = input("Enter your Customer ID: ")
    view_my_bookings(customer_id)  # Shows them their bookings

    # Starts off by assuming we haven't found the booking
    booking_cancelled = False
    # Collects and stores the lines we want to save
    temp_lines = []

    try:

        # Opens bookings.txt as the original file
        original_file = open("bookings.txt", "r")


        # Opens temp.txt as a temporary file to update bookings.txt if changes are made
        temp_lines = open("temp.txt", "w")

        # Reads each line in original_file
        for line in original_file:

            #Checks each line for the customer_id entered
            if line.strip().startswith(customer_id + ','):
                print("Booking found.")
                # booking_cancelled is now True because the booking was found
                booking_cancelled = True
            else:
                # Continues to write lines from the original file if it does not begin with the ID entered
                temp_lines.append(line)

        # Closes original file before removing or renaming it
        original_file.close()

        if booking_cancelled:
            # Rewrites the bookings.txt file without the cancelled bookings
            with open("bookings.txt", "w") as file:
                file.writelines(temp_lines)
            print(f"All bookings for Customer ID: {customer_id} has been cancelled and removed.")

        else:
            print("No bookings found for this Customer ID")

    except FileNotFoundError:
        print("No bookings found for this Customer ID.")



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

                if line.strip().endswith(',' + driver_id):
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

        original_file =  open("bookings.txt", "r")

        # Reads each line in original_file
        for line in original_file:
            if line.strip().startswith(booking_id + ','):

                #If the booking is found it checks if it currently has "Pending,None"
                if ',Pending,None' in line:
                    # Replaces and updates the Pending status and with Assigned and the Driver ID
                    update_status = line.strip().replace(",Pending,None", f",Assigned,{driver_id}") + "\n"
                    # Adds the updated line to the temporary list
                    lines_to_keep.append(update_status)

                    #
                    updated_booking_status = True
                    print(f"Booking #{booking_id} Found.")
                    print("Updating Status...")
                else:
                    lines_to_keep.append(line)
                    print(f"Booking #{booking_id} Status is NOT Pending and is Assigned.")
            else:
                lines_to_keep.append(line)
        original_file.close()

        if updated_booking_status:
            with open("bookings.txt", "w") as file:
                file.writelines()
            print(f"Booking #{booking_id} was successfully assigned to Driver{driver_id}")
        else:
            print(f"Booking #{booking_id} Status is NOT Pending.")
    except FileNotFoundError:
        print("No bookings found...")




def user_input():
    name = input("\n Please input your name: ")
    print(f" Welcome {name}!")

    pickup_street_num = input("\n Enter your pickup location's street/building number: #")
    pickup_street_name = input("\n Enter your pickup location's street name: \n ")
    pickup_city = input("\n Enter your pickup location's city name: \n ")
    pickup_date = input("Enter the date for your taxi booking (DD/MM/YYYY): ")
    pickup_time = input("Enter the time for your taxi booking (HH:MM): ")

    full_pickup_address = (f"#{pickup_street_num} {pickup_street_name}, {pickup_city} on {pickup_date} at {pickup_time}")
    print(f"\n {name}'s Pickup Location is: {full_pickup_address}")

    dropoff_street_num = input("\n Enter your drop-off location's street/building number: #")
    dropoff_street_name = input("\n Enter your drop-off location's street name: ")
    dropoff_city = input("\n Enter your drop-off location's city name: ")
    full_dropoff_address = (f"#{dropoff_street_num} {dropoff_street_name}, {dropoff_city}")
    print(f"\n {name}'s Drop-off Location is: {full_dropoff_address}")

    phone_num = input("\n Enter your phone number: ")
    email = input("\n Enter your email address: ")

    return name, full_pickup_address, full_dropoff_address, phone_num, email


# This function saves the booking.
def book_taxi(customer_id, name, full_pickup_address, full_dropoff_address):
    taxi_booking = input("\n Would you like to book a taxi with us? (yes/no): ")

    if taxi_booking.lower() == "yes":
        print("\n Checking for available drivers...")

        try:
            num_of_passengers = int(input("\n Enter the number of passengers for this taxi booking: \n "))
            num_of_adults = int(input("Enter the number of adults: \n "))
            num_of_children = int(input("Enter the number of children: \n "))
        except ValueError:
            print("\n Invalid Input. PLEASE Enter numbers only. \n")
            print("\n Booking Cancelled... \n")
            return

        print(f"This booking contains {num_of_adults} Adult/s and {num_of_children} Child/Children. \n")

        # Checks if number of adults exceeds number of passengers entered
        if num_of_adults > num_of_passengers:
            print("TAXI BOOKING CANCELLED! Adults exceed total passengers. Please Re-try. \n")
            return

        elif num_of_children + num_of_adults != num_of_passengers:
            print("TAXI BOOKING CANCELLED! Adult and Child count does not match the total number of passengers. Please Re-try. \n")
            return

        # Checks if number children exceeds or equals the number of passengers
        elif num_of_children >= num_of_passengers:
            print("TAXI BOOKING CANCELLED! Children exceed or no Adults are present. Please Re-try. \n")
            return

        taxi_type = input("\n Select Taxi type - Regular, Preferred, Premium: ")
        payment = input("\n How will you be paying? - Select either 'Cash' or 'Card': ")

        full_booking = (f"Pickup: {full_pickup_address}"
                        f"Drop-off: {full_dropoff_address}"
                        f"Passengers: {num_of_adults} Adult/s, {num_of_children} Child/Children "
                        f"Taxi type: {taxi_type}"
                        f"Payment: {payment}")

        print("\n Sending information to Drivers....")
        print(full_booking)

        try:
            with open("bookings.txt", "r") as file:

                booking_id = str(sum(1 for line in file) + 1)
        except FileNotFoundError:
            booking_id = '1'

        status = "Pending"
        driver_id = "None"

        with open("bookings.txt", "a") as file:
            file.write(f"{booking_id}, {customer_id}, {full_booking}, {status}, {driver_id}")

        print(f"Your Trip Booking #{booking_id} has been assigned to one of our Drivers. ")

    elif taxi_booking.lower() == "no":
        print("You've chosen not to book with us. Hope to see you soon!")


    else:
        print("\n Invalid response. Please enter 'yes' or 'no' ")



# Calling main_menu function to run program when executed directly
if __name__ == "__main__":
    main_menu()


