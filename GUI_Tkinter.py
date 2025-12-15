from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import taxi_system as system

# Global variables for current user
current_username = None
current_role = None
current_linked_id = None

# Admin Passcode
ADMIN_PASSCODE = "ADMIN149"

# Global reference for root window
root = None


def show_main_menu():
    clear_window()
    root.configure(bg="#34495E")

    #Title
    title_label = Label(root, text="Welcome To",
                        font=("Times New Roman", 24, "bold"), bg="#34495E", fg="gold")
    title_label.pack(pady=20)

    # Subtitle
    subtitle_label = Label(root, text="A & A's TAXI Booking System",
                           font=("Times New Roman", 20),
                           bg="#34495E", fg="gold")
    subtitle_label.pack(pady=10)

    # Customer Login button
    customer_btn = Button(root, text="Customer Login", width=30, height=2,
                          font=("Times New Roman", 14, "bold"),
                          bg="lightblue", command=show_customer_login)
    customer_btn.pack(pady=10)
    # Driver Login button
    driver_btn = Button(root, text="Driver Login", width=30, height=2,
                        font=("Times New Roman", 14, "bold"),
                        bg="lightgreen", command=show_driver_login)
    driver_btn.pack(pady=10)
    # Admin Login button
    admin_btn = Button(root, text="Admin Login", width=30, height=2,
                       font=("Times New Roman", 14, "bold"),
                       bg="lightgrey", command=show_admin_login)
    admin_btn.pack(pady=10)
    # Registration button
    register_btn = Button(root, text="Register New Account", width=30, height=2,
                          font=("Times New Roman", 14, "bold"),
                          bg="orange", command=show_registration)
    register_btn.pack(pady=10)
    exit_btn = Button(root, text="Exit Application", width=30, height=2,
                      font=("Times New Roman", 14, "bold"),
                      bg="red", command=root.quit)
    exit_btn.pack(pady=10)


# This Function prevents the GUI from making errors when switching from pages by removing all widgets from the window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


# Registration MENU
# This Function displays the registration page for Customer and Driver
def show_registration():
    clear_window()
    root.configure(bg="white")

    # Title
    title_label = Label(root, text="Create New Account",
                        font=("Times New Roman", 22, "bold"), bg="white")
    title_label.pack(pady=20)

    # Creates page frame
    page_frame = Frame(root, bg="white")
    page_frame.pack(pady=20)

    # Role selection options using radio buttons
    Label(page_frame, text="I am a:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=0, column=0, sticky=W, padx=10, pady=10)

    role_var = StringVar()
    role_var.set("Customer")

    Radiobutton(page_frame, text="Customer", variable=role_var,
                value="Customer", font=("Times New Roman", 11),
                bg="white").grid(row=0, column=1, sticky=W)
    Radiobutton(page_frame, text="Driver", variable=role_var,
                value="Driver", font=("Times New Roman", 11),
                bg="white").grid(row=0, column=2, sticky=W)

    # Username field
    Label(page_frame, text="Username:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=1, column=0, sticky=W, padx=10, pady=10)
    username_entry = Entry(page_frame, width=30, font=("Times New Roman", 12))
    username_entry.grid(row=1, column=1, columnspan=2, pady=10)

    # Password field
    Label(page_frame, text="Password:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=2, column=0, sticky=W, padx=10, pady=10)
    password_entry = Entry(page_frame, show="*", width=30, font=("Times New Roman", 12))
    password_entry.grid(row=2, column=1, columnspan=2, pady=10)

    # Full Name field
    Label(page_frame, text="Full Name:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=3, column=0, sticky=W, padx=10, pady=10)
    name_entry = Entry(page_frame, width=30, font=("Times New Roman", 12))
    name_entry.grid(row=3, column=1, columnspan=2, pady=10)

    # Phone field
    Label(page_frame, text="Phone:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=4, column=0, sticky=W, padx=10, pady=10)
    phone_entry = Entry(page_frame, width=30, font=("Times New Roman", 12))
    phone_entry.grid(row=4, column=1, columnspan=2, pady=10)

    # Email field
    Label(page_frame, text="Email:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=5, column=0, sticky=W, padx=10, pady=10)
    email_entry = Entry(page_frame, width=30, font=("Times New Roman", 12))
    email_entry.grid(row=5, column=1, columnspan=2, pady=10)

    def register_button():

        # Stores all the values from the User
        role = role_var.get()
        username = username_entry.get()
        password = password_entry.get()
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        # Checks if fields are empty
        if username == "" or password == "" or name == "" or phone == "" or email == "":
            messagebox.showerror("Error", "All fields are required!")
            return

        success, message = system.register_func(role, username, password, name, phone, email)

        # Shows result to User
        if success:
            messagebox.showinfo("Success", message)
            show_main_menu()
        else:
            messagebox.showerror("Error", message)

    # Creates button frame
    button_frame = Frame(root, bg="white")
    button_frame.pack(pady=20)

    # Register button
    register_btn = Button(button_frame, text="Register", width=15, height=2,
                          font=("Times New Roman", 12, "bold"),
                          bg="green", fg="white", command=register_button)
    register_btn.pack(side=LEFT, padx=10)

    # Back button
    back_btn = Button(button_frame, text="Back", width=15, height=2,
                      font=("Times New Roman", 12),
                      bg="gray", fg="white", command=show_main_menu)
    back_btn.pack(side=LEFT, padx=10)


# LOGIN Screens

# This Function displays the Customer LOGIN Screen
def show_customer_login():
    show_login_screen("Customer")


# This Function displays the Driver LOGIN Screen
def show_driver_login():
    show_login_screen("Driver")


# This Function displays the Admin LOGIN Screen
def show_admin_login():
    clear_window()
    root.configure(bg="white")

    # Title
    title_label = Label(root, text="Admin Login",
                        font=("Times New Roman", 22, "bold"), bg="white")
    title_label.pack(pady=30)

    # Info label
    info_label = Label(root, text="Enter Admin passcode to access Admin MENU",
                       font=("Times New Roman", 10, "italic"), bg="white", fg="gray")
    info_label.pack()

    # Creates form frame
    page_frame = Frame(root, bg="white")
    page_frame.pack(pady=30)

    # Username field
    Label(page_frame, text="Username:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=0, column=0, sticky=W, padx=10, pady=15)
    username_entry = Entry(page_frame, width=30, font=("Times New Roman", 12))
    username_entry.grid(row=0, column=1, pady=15)

    # Passcode field
    Label(page_frame, text="Passcode:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=1, column=0, sticky=W, padx=10, pady=15)
    passcode_entry = Entry(page_frame, show="*", width=30, font=("Times New Roman", 12))
    passcode_entry.grid(row=1, column=1, pady=15)

    # This Function creates the Admin Login button
    def admin_login_button():

        global current_username, current_role, current_linked_id

        # Stores username and passcode entered
        username = username_entry.get()
        passcode = passcode_entry.get()

        # Checks if both fields are filled
        if username == "" or passcode == "":
            messagebox.showerror("Error", "Please enter both username and passcode!")
            return

        # Checks if passcode is correct
        if passcode != ADMIN_PASSCODE:
            messagebox.showerror("Access Denied", "Invalid passcode!")
            return

        # Sets current user details
        current_username = username
        current_role = "Admin"
        current_linked_id = username

        # Shows success message and displays Admin MENU
        messagebox.showinfo("Success", "Welcome, Admin!")
        show_admin_menu()

    # Creates button frame
    button_frame = Frame(root, bg="white")
    button_frame.pack(pady=20)

    # Login button
    login_btn = Button(button_frame, text="Login", width=15, height=2,
                       font=("Times New Roman", 12, "bold"),
                       bg="gray", fg="white", command=admin_login_button)
    login_btn.pack(side=LEFT, padx=10)

    # Back button
    back_btn = Button(button_frame, text="Back", width=15, height=2,
                      font=("Times New Roman", 12),
                      bg="red", fg="white", command=show_main_menu)
    back_btn.pack(side=LEFT, padx=10)


# This Function displays a Login Screen for Customer and Driver roles
def show_login_screen(role_name):
    clear_window()
    root.configure(bg="white")

    # Title
    title_label = Label(root, text=role_name + " Login",
                        font=("Times New Roman", 22, "bold"), bg="white")
    title_label.pack(pady=30)

    # Creates page frame
    page_frame = Frame(root, bg="white")
    page_frame.pack(pady=30)

    # Username field
    Label(page_frame, text="Username:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=0, column=0, sticky=W, padx=10, pady=15)
    username_entry = Entry(page_frame, width=30, font=("Times New Roman", 12))
    username_entry.grid(row=0, column=1, pady=15)

    # Password field
    Label(page_frame, text="Password:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=1, column=0, sticky=W, padx=10, pady=15)
    password_entry = Entry(page_frame, show="*", width=30, font=("Times New Roman", 12))
    password_entry.grid(row=1, column=1, pady=15)

    # This Function creates the Login button
    def login_button():

        global current_username, current_role, current_linked_id

        # Stores Username and Password from fields
        username = username_entry.get()
        password = password_entry.get()

        # Check if both fields are filled
        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter both username and password!")
            return

        success, username_result, role, linked_id = system.login_user(username, password)

        # Checks if login failed
        if success == False:
            messagebox.showerror("Error", "Invalid username or password!")
            return

        # Checks if the role entered matches
        role_lower = role.lower()
        role_name_lower = role_name.lower()

        if role_lower != role_name_lower:
            messagebox.showerror("Error", "This account is not registered as a " + role_name + "!")
            return

        # Sets current User Details
        current_username = username_result
        current_role = role
        current_linked_id = linked_id

        # Displays successful login message
        messagebox.showinfo("Success", "Welcome, " + username + "!")

        # Goes to menu based on User role
        if role_name == "Customer":
            show_customer_menu()
        elif role_name == "Driver":
            show_driver_menu()

    # Creates button frame
    button_frame = Frame(root, bg="white")
    button_frame.pack(pady=20)

    # Login button
    login_btn = Button(button_frame, text="Login", width=15, height=2,
                       font=("Times New Roman", 12, "bold"),
                       bg="blue", fg="white", command=login_button)
    login_btn.pack(side=LEFT, padx=10)

    # Back button
    back_btn = Button(button_frame, text="Back", width=15, height=2,
                      font=("Times New Roman", 12),
                      bg="gray", fg="white", command=show_main_menu)
    back_btn.pack(side=LEFT, padx=10)


def show_customer_menu():
    clear_window()
    root.configure(bg="#34495E")

    # Title with Customer Username entered
    title_label = Label(root, text="Customer Menu - Welcome! " + current_username,
                        font=("Times New Roman", 22, "bold"), bg="#34495E", fg="gold")
    title_label.pack(pady=30)

    # Book a Taxi button
    book_btn = Button(root, text="Book a Taxi", width=30, height=2,
                      font=("Times New Roman", 14, "bold"),
                      bg="lightgreen", command=show_book_taxi)
    book_btn.pack(pady=10)

    # View My Bookings button
    view_btn = Button(root, text="View My Bookings", width=30, height=2,
                      font=("Times New Roman", 14, "bold"),
                      bg="orange", command=show_view_my_bookings)
    view_btn.pack(pady=10)

    # Logout button
    back_btn = Button(root, text="Logout", width=30, height=2,
                      font=("Times New Roman", 14),
                      bg="red", fg="white", command=show_main_menu)
    back_btn.pack(pady=10)


# Driver MENU
def show_driver_menu():
    clear_window()
    root.configure(bg="#34495E")

    # Title with Driver Username entered
    title_label = Label(root, text="Driver Menu - Welcome! " + current_username,
                        font=("Times New Roman", 22, "bold"), bg="#34495E", fg="gold")
    title_label.pack(pady=30)

    # View Assigned Bookings button
    view_btn = Button(root, text="View Assigned Bookings", width=30, height=2,
                      font=("Times New Roman", 14, "bold"),
                      bg="lightgreen", command=show_view_assigned_bookings)
    view_btn.pack(pady=10)

    # Logout button
    back_btn = Button(root, text="Logout", width=30, height=2,
                      font=("Times New Roman", 14),
                      bg="red", fg="white", command=show_main_menu)
    back_btn.pack(pady=10)


# Admin MENU
# This Function shows the Admin Menu and Admin options
def show_admin_menu():
    clear_window()
    root.configure(bg="#34495E")

    # Title with Admin Username entered
    title_label = Label(root, text="Admin Menu - Welcome! " + current_username,
                        font=("Times New Roman", 22, "bold"), bg="#34495E", fg="gold")
    title_label.pack(pady=30)

    # View All Bookings button
    view_btn = Button(root, text="View All Bookings", width=30, height=2,
                      font=("Times New Roman", 14, "bold"),
                      bg="lightblue", command=show_all_bookings)
    view_btn.pack(pady=10)

    # Assign Driver button
    assign_btn = Button(root, text="Assign Driver to Booking", width=30, height=2,
                        font=("Times New Roman", 14, "bold"),
                        bg="lightgreen", command=show_assign_driver)
    assign_btn.pack(pady=10)

    # Logout button
    back_btn = Button(root, text="Logout", width=30, height=2,
                      font=("Times New Roman", 14),
                      bg="red", fg="white", command=show_main_menu)
    back_btn.pack(pady=10)


def show_book_taxi():
    clear_window()
    root.configure(bg="white")

    # Title
    title_label = Label(root, text="Book a Taxi",
                        font=("Times New Roman", 20, "bold"), bg="white")
    title_label.pack(pady=5)

    # Creates page frame
    page_frame = Frame(root, bg="white")
    page_frame.pack(pady=5)

    # PICKUP Details SECTION
    pickup_label = Label(page_frame, text="Pickup Details",
                         font=("Times New Roman", 14, "bold"), bg="white", fg="blue")
    pickup_label.grid(row=0, column=0, columnspan=4, pady=5, sticky=W, padx=10)

    # Pickup Street Number
    Label(page_frame, text="Street Number:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=1, column=0, sticky=W, pady=3, padx=10)
    pickup_num = Entry(page_frame, width=5, font=("Times New Roman", 12))
    pickup_num.grid(row=1, column=1, columnspan=3, sticky=W, pady=3)

    # Pickup Street Name
    Label(page_frame, text="Street Name:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=2, column=0, sticky=W, pady=3, padx=10)
    pickup_street = Entry(page_frame, width=40, font=("Times New Roman", 12))
    pickup_street.grid(row=2, column=1, columnspan=3, sticky=W, pady=3)

    # Pickup City
    Label(page_frame, text="City:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=3, column=0, sticky=W, pady=3, padx=10)
    pickup_city = Entry(page_frame, width=40, font=("Times New Roman", 12))
    pickup_city.grid(row=3, column=1, columnspan=3, sticky=W, pady=3)

    # Date and Time on same row
    Label(page_frame, text="Date (DD/MM/YYYY):", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=4, column=0, sticky=W, pady=3, padx=10)
    date_entry = Entry(page_frame, width=15, font=("Times New Roman", 12))
    date_entry.grid(row=4, column=1, sticky=W, pady=3, padx=(0, 20))

    Label(page_frame, text="Time (HH:MM):", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=4, column=2, sticky=W, pady=3, padx=10)
    time_entry = Entry(page_frame, width=10, font=("Times New Roman", 12))
    time_entry.grid(row=4, column=3, sticky=W, pady=3)

    # DROP-OFF Details SECTION
    dropoff_label = Label(page_frame, text="Drop-off Details",
                          font=("Times New Roman", 14, "bold"), bg="white", fg="red")
    dropoff_label.grid(row=5, column=0, columnspan=4, pady=5, sticky=W, padx=10)

    # Drop-off Street Number
    Label(page_frame, text="Street Number:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=6, column=0, sticky=W, pady=3, padx=10)
    dropoff_num = Entry(page_frame, width=5, font=("Times New Roman", 12))
    dropoff_num.grid(row=6, column=1, columnspan=3, sticky=W, pady=3)

    # Drop-off Street Name
    Label(page_frame, text="Street Name:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=7, column=0, sticky=W, pady=3, padx=10)
    dropoff_street = Entry(page_frame, width=40, font=("Times New Roman", 12))
    dropoff_street.grid(row=7, column=1, columnspan=3, sticky=W, pady=3)

    # Drop-off City
    Label(page_frame, text="City:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=8, column=0, sticky=W, pady=3, padx=10)
    dropoff_city = Entry(page_frame, width=40, font=("Times New Roman", 12))
    dropoff_city.grid(row=8, column=1, columnspan=3, sticky=W, pady=3)

    # PASSENGER Details SECTION
    passenger_label = Label(page_frame, text="Passenger Details",
                            font=("Times New Roman", 14, "bold"), bg="white", fg="green")
    passenger_label.grid(row=9, column=0, columnspan=4, pady=5, sticky=W, padx=10)

    # Total Passengers
    Label(page_frame, text="Total Passengers:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=10, column=0, sticky=W, pady=3, padx=10)
    passengers_entry = Entry(page_frame, width=40, font=("Times New Roman", 12))
    passengers_entry.grid(row=10, column=1, columnspan=3, sticky=W, pady=3)

    # Adults and Children on same row
    Label(page_frame, text="Number of Passengers:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=11, column=0, sticky=W, pady=3, padx=10)

    # Passenger
    passenger_frame = Frame(page_frame, bg="white")
    passenger_frame.grid(row=11, column=1, columnspan=3, sticky=W, pady=3)

    Label(passenger_frame, text="Adults:", font=("Times New Roman", 11),
          bg="white").pack(side=LEFT, padx=(0, 5))
    adults_entry = Entry(passenger_frame, width=5, font=("Times New Roman", 12))
    adults_entry.pack(side=LEFT, padx=(0, 20))

    Label(passenger_frame, text="Children:", font=("Times New Roman", 11),
          bg="white").pack(side=LEFT, padx=(0, 5))
    children_entry = Entry(passenger_frame, width=5, font=("Times New Roman", 12))
    children_entry.pack(side=LEFT)

    # Taxi Type
    taxi_type = StringVar()
    taxi_type.set("Standard")

    Label(page_frame, text="Select taxi type:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=12, column=0, sticky=W, pady=5, padx=10)
    Radiobutton(page_frame, text="Standard", variable=taxi_type,
                value="Standard", font=("Times New Roman", 11),
                bg="white").grid(row=12, column=1, sticky=W, pady=5)
    Radiobutton(page_frame, text="Premium", variable=taxi_type,
                value="Premium", font=("Times New Roman", 11),
                bg="white").grid(row=12, column=2, sticky=W, pady=5)

    # Payment Method
    payment_method = StringVar()
    payment_method.set("Cash")

    Label(page_frame, text="Select payment option:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=13, column=0, sticky=W, pady=5, padx=10)
    Radiobutton(page_frame, text="Cash", variable=payment_method,
                value="Cash", font=("Times New Roman", 11),
                bg="white").grid(row=13, column=1, sticky=W, pady=5)
    Radiobutton(page_frame, text="Card", variable=payment_method,
                value="Card", font=("Times New Roman", 11),
                bg="white").grid(row=13, column=2, sticky=W, pady=5)

    def book_button():
        # Stores all the values from the User
        pickup_street_num = pickup_num.get()
        pickup_street_name = pickup_street.get()
        pickup_city_name = pickup_city.get()

        dropoff_street_num = dropoff_num.get()
        dropoff_street_name = dropoff_street.get()
        dropoff_city_name = dropoff_city.get()

        pickup_date = date_entry.get()
        pickup_time = time_entry.get()
        num_of_passengers = passengers_entry.get()
        num_of_adults = adults_entry.get()
        num_of_children = children_entry.get()
        taxi_selection = taxi_type.get()
        payment_selection = payment_method.get()

        # Checks if fields are empty
        if (pickup_street_num == "" or pickup_street_name == "" or pickup_city_name == "" or
                dropoff_street_num == "" or dropoff_street_name == "" or dropoff_city_name == "" or
                pickup_date == "" or pickup_time == "" or num_of_passengers == "" or
                taxi_selection == "" or payment_selection == ""):
            messagebox.showerror("Error", "All fields are required!")
            return

        # Validate date & time format (DD/MM/YYYY and HH:MM)
        try:
            datetime.strptime(pickup_date, "%d/%m/%Y")
            datetime.strptime(pickup_time, "%H:%M")
        except Exception:
            messagebox.showerror("Error", "Please enter booking date in DD/MM/YYYY and time in HH:MM format")
            return

        # Check for overlapping bookings using system function
        if not system.booking_time_availability(pickup_date, pickup_time):
            messagebox.showerror("Error", "Sorry, a booking already exists at that date and time.")
            return

        # Constructs full addresses from individual fields
        pickup_location = f"{pickup_street_num} {pickup_street_name}, {pickup_city_name}"
        dropoff_location = f"{dropoff_street_num} {dropoff_street_name}, {dropoff_city_name}"

        # Construct pickup address including date/time so booking has it recorded
        full_pickup_address = pickup_location + f" on {pickup_date} at {pickup_time}"

        success, message = system.book_taxi(
            customer_id=current_linked_id,
            full_pickup_address=full_pickup_address,
            full_dropoff_address=dropoff_location,
            num_of_passengers=num_of_passengers,
            num_of_adults=num_of_adults,
            num_of_children=num_of_children,
            taxi_type=taxi_selection,
            payment=payment_selection
        )

        # Shows result to User
        if success:
            messagebox.showinfo("Success", message)
            show_customer_menu()
        else:
            messagebox.showerror("Error", message)

    # Creates button frame
    button_frame = Frame(root, bg="white")
    button_frame.pack(pady=10)

    # Book button
    book_btn = Button(button_frame, text="Book Taxi", width=15, height=2,
                      font=("Times New Roman", 12, "bold"),
                      bg="green", fg="white", command=book_button)
    book_btn.pack(pady=5)

    # Back button
    back_btn = Button(button_frame, text="Back", width=15, height=2,
                      font=("Times New Roman", 12),
                      bg="gray", fg="white", command=show_customer_menu)
    back_btn.pack(pady=5)


def show_view_my_bookings():
    clear_window()
    root.configure(bg="white")
    # Title
    title_label = Label(root, text="My Bookings",
                        font=("Times New Roman", 20, "bold"), bg="white")
    title_label.pack(pady=20)

    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    # Creates scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Creates listbox to display all booking with the system
    listbox = Listbox(frame, yscrollcommand=scrollbar.set, font=("Courier", 9))
    listbox.pack(fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    # Displays all bookings from user
    bookings = system.view_my_bookings(current_linked_id)
    # Adds bookings to listbox
    if len(bookings) > 0:
        for booking in bookings:
            display_text = f"{booking['id']}: {booking['details']}"
            listbox.insert(END, display_text)
    else:
        listbox.insert(END, "You have no bookings.")

    # Back button
    back_btn = Button(root, text="Back", width=20, height=2,
                      font=("Times New Roman", 12),
                      bg="gray", fg="white", command=show_customer_menu)
    back_btn.pack(pady=10)

    # Cancel Selected Booking button
    def cancel_selected():
        selection = listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a booking to cancel!")
            return

        selected_text = listbox.get(selection[0])
        # ID: Details
        if ":" in selected_text:
            booking_id = selected_text.split(":", 1)[0].strip()
        else:
            messagebox.showerror("Error", "Unable to parse selected booking ID.")
            return

        success, msg = system.cancel_booking(booking_id=booking_id, customer_id=current_linked_id)
        if success:
            messagebox.showinfo("Success", msg)
            show_view_my_bookings()
        else:
            messagebox.showerror("Error", msg)

    cancel_btn = Button(root, text="Cancel Selected Booking", width=25, height=2,
                        font=("Times New Roman", 12), bg="red", fg="white", command=cancel_selected)
    cancel_btn.pack(pady=10)


def show_view_assigned_bookings():
    clear_window()
    root.configure(bg="white")
    # Title
    title_label = Label(root, text="Assigned Bookings",
                        font=("Times New Roman", 20, "bold"), bg="white")
    title_label.pack(pady=20)
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    # Creates scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Creates listbox to display all booking assigned to driver
    listbox = Listbox(frame, yscrollcommand=scrollbar.set, font=("Courier", 9))
    listbox.pack(fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    # Display assigned bookings for the current driver
    trips = system.view_driver_trips(current_linked_id)
    if len(trips) > 0:
        for trip in trips:
            listbox.insert(END, trip)
    else:
        listbox.insert(END, "You have no assigned trips.")

    # Back button
    back_btn = Button(root, text="Back", width=20, height=2,
                      font=("Times New Roman", 12),
                      bg="gray", fg="white", command=show_driver_menu)
    back_btn.pack(pady=10)


# This Function shows all booking with the system
def show_all_bookings():
    clear_window()
    root.configure(bg="white")

    # Title
    title_label = Label(root, text="All System Bookings",
                        font=("Times New Roman", 20, "bold"), bg="white")
    title_label.pack(pady=20)

    # Creates frame for listbox
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    # Creates scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Creates listbox to display all booking with the system
    listbox = Listbox(frame, yscrollcommand=scrollbar.set, font=("Courier", 9))
    listbox.pack(fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    # Displays all bookings from system
    bookings = system.view_all_bookings()

    # Adds bookings to listbox
    if len(bookings) > 0:
        for booking in bookings:
            listbox.insert(END, booking)
    else:
        listbox.insert(END, "No bookings in the system.")

    # Back button
    back_btn = Button(root, text="Back", width=20, height=2,
                      font=("Times New Roman", 12),
                      bg="gray", fg="white", command=show_admin_menu)
    back_btn.pack(pady=10)


# This Function shows the Assign Driver Screen
def show_assign_driver():
    clear_window()
    root.configure(bg="white")

    # Title
    title_label = Label(root, text="Assign Driver to Booking",
                        font=("Times New Roman", 20, "bold"), bg="white")
    title_label.pack(pady=10)

    # Creates frame for showing all bookings
    bookings_frame = Frame(root, bg="white")
    bookings_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

    # Label for bookings list
    Label(bookings_frame, text="Available Bookings:",
          font=("Times New Roman", 12, "bold"), bg="white").pack(anchor=W, pady=5)

    # Creates scrollbar for bookings
    scrollbar = Scrollbar(bookings_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Creates listbox to display all bookings
    listbox = Listbox(bookings_frame, yscrollcommand=scrollbar.set,
                      font=("Courier", 9), height=10)
    listbox.pack(fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    # Displays all bookings from system
    bookings = system.view_all_bookings()

    # Adds bookings to listbox
    if len(bookings) > 0:
        for booking in bookings:
            listbox.insert(END, booking)
    else:
        listbox.insert(END, "No bookings in the system.")

    # Creates page frame for assignment fields
    page_frame = Frame(root, bg="white")
    page_frame.pack(pady=10)

    # Booking ID field
    Label(page_frame, text="Booking ID:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=0, column=0, padx=10, pady=10)
    booking_id_entry = Entry(page_frame, width=25, font=("Times New Roman", 12))
    booking_id_entry.grid(row=0, column=1, padx=10, pady=10)

    # Label for Driver dropdown menu
    Label(page_frame, text="Driver:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=1, column=0, padx=10, pady=10)

    # Gets all Drivers within system
    drivers = system.get_all_drivers()

    # Creates a list of Driver with their Driver ID and Full Name
    driver_options = []
    for driver in drivers:
        driver_text = driver['id'] + " - " + driver['name']
        driver_options.append(driver_text)

    # Creates Driver dropdown menu
    driver_var = StringVar()
    driver_menu = ttk.Combobox(page_frame, textvariable=driver_var,
                               values=driver_options, state="readonly", width=23)
    driver_menu.grid(row=1, column=1, padx=10, pady=10)

    # Displays selection if Drivers exist
    if len(driver_options) > 0:
        driver_menu.current(0)

    def assign_button():

        # Stores Booking ID entered
        booking_id = booking_id_entry.get()

        # Stores selected Driver
        driver_selection = driver_var.get()

        # Checks if Booking ID is entered
        if booking_id == "":
            messagebox.showerror("Error", "Please enter a Booking ID!")
            return

        # Checks if Driver is selected
        if driver_selection == "":
            messagebox.showerror("Error", "Please select a Driver!")
            return

        # Pulls Driver ID from list using " - "
        parts = driver_selection.split(" - ")
        driver_id = parts[0]

        # Calls assign function
        success, message = system.assign_driver(booking_id=booking_id, driver_id=driver_id)

        # Displays Assignment result to Admin
        if success:
            messagebox.showinfo("Success", message)
            show_assign_driver()
        else:
            messagebox.showerror("Error", message)

    # Creates button frame
    button_frame = Frame(root, bg="white")
    button_frame.pack(pady=10)

    # Assign Driver button
    assign_btn = Button(button_frame, text="Assign Driver", width=15, height=2,
                        font=("Times New Roman", 12, "bold"),
                        bg="green", fg="white", command=assign_button)
    assign_btn.pack(side=LEFT, padx=10)

    # Back button
    back_btn = Button(button_frame, text="Back", width=15, height=2,
                      font=("Times New Roman", 12),
                      bg="gray", fg="white", command=show_admin_menu)
    back_btn.pack(side=LEFT, padx=10)


# Main Function which allows the application to start
def main():
    global root

    # Creates the Main Window
    root = Tk()
    root.title("A & A's Taxi Booking System")
    root.geometry("800x700")
    root.resizable(True, True)
    root.iconbitmap(False, 'taxi.ico')
    # Displays the Main Menu
    show_main_menu()
    # Starts the event loop
    root.mainloop()


# Runs the application
if __name__ == "__main__":
    main()
