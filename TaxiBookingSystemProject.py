
#Function to create main menu
def main_menu():
    while True: #Loop which allows user to choose options
        print("~ A & A's Taxi Booking System ~ \n")
        print("1. Customer")
        print("2. Driver")
        print("3. Admin")
        print("4. Exit \n")

        option = input("Select an option (1-4): ")

        if option == '1': #Brings users to Customer MENU
            print("~ Customer MENU ~")
            customer_menu()

        elif option == '2':
            print("~ Driver MENU ~")

        elif option == '3':
            print("~ Admin MENU ~")

        elif option == '4':
            print("You've chosen to exit...")
            print("Hope to see you Soon!")
            break #Exits the loop

        else:
            print("Option selected does not exist...Selection Invalid.")

#Function to display customer menu and options within it
def customer_menu():
    # Loop which allow customers to select options and runs until customer returns to Main Menu
    while True:
        print("~ Customer MENU ~ \n")
        print(" 1. Register and Book a Taxi \n ")
        print(" 2. Return to Main Menu \n ")


        option = input("Select an option (1-2): ")

        # Allows users to enter details and create a taxi booking
        if option == '1':
            #Calls on user_input() and collects user details
            name, full_address, phone_num = user_input()

            #Calls on save_customer() and saves it to customer.txt
            save_customer(name, full_address, phone_num)

            #Calls on book_taxi() and saves it to bookings.txt
            book_taxi(name, full_address)

            #Prompts user to press enter to move forward
            input("Press Enter to continue")

        # Brings users back to Main Menu
        elif option == '2': #Returns users to Main Menu
            print("Returning to Main Menu...")
            break #Ends the customer menu loop

        else:
            #Outputs statement if users don't enter options '1' or '2'
            print("Option selected does not exist...Selection Invalid.")


#Function saves customer details to customers.txt and appends it when info is added
def save_customer(name, address, phone):
    with open("customers.txt", "a") as file:
        file.write(f"{name}, {address}, {phone} \n")

#Function saves customer booking to bookings.txt and appends it when info is added
def save_booking(full_booking):
    with open("bookings.txt", "a") as file:
        file.write(f"{full_booking} \n")


# Function that receives user input and their personal details
def user_input():
   name = input("Please input your name: ")
   print(f"Welcome {name}!")

   street_num = int(input("Enter your location's street/building number: # "))
   street_name = input("Enter your location's street name: ")
   city = input("Enter your location's city name: ")
   full_address = (f"#{street_num} {street_name}, {city}")
   print(f"{name}'s Location is: {full_address}")


   phone_num = (input("Enter your phone number: "))


   return name, full_address, phone_num

#Function that receives booking details
def book_taxi(name, full_address):
   taxi_booking = input("Would you like to book a taxi with us? (yes/no): ")

   if taxi_booking.lower() == "yes":
       print("Checking for available drivers...")
       num_of_passengers = int(input("Enter the number of passengers for this taxi booking: "))
       num_of_adults = int(input("Enter the number of adults: "))

       num_of_children = int(input("Enter the number of children: "))

       print(f"This booking contains {num_of_adults} Adult/s and {num_of_children} Child/Children.")

       #Checks if number of adults exceeds number of passengers entered
       if num_of_adults > num_of_passengers:
           print("TAXI BOOKING CANCELLED! Adults exceeds total passengers. Please re-try.")
           return

       #Checks if number children exceeds or equals the number of passengers
       elif num_of_children >= num_of_passengers:
           print("TAXI BOOKING CANCELLED! Children exceed or no Adults are present. Please re-try.")
           return


       taxi_type = input("Select Taxi type - Regular, Preferred, Premium: ")
       payment = input("How will you be paying? - Select either 'Cash' or 'Card': ")

       full_booking = (f"{name}'s Taxi Booking: Location - {full_address}, "
                            f"Passengers: {num_of_adults} Adults, "
                            f"{num_of_children} Child/Children, Taxi type: {taxi_type}, "
                            f"Payment method - {payment}.")


       print("Sending information to Drivers....")
       print(full_booking)

       save_booking(full_booking)


   elif taxi_booking.lower() == "no":
       print("You've chosen not to book with us. Hope to see you soon!")


   else:
       print("Invalid response. Please enter 'yes' or 'no' ")


#Calling main_menu function to run program
main_menu()