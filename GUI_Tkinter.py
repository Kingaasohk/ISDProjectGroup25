from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import taxi_system as system

# Global variables for current user
current_username = None
current_role = None
current_linked_id = None

# Admin Passcode
ADMIN_PASSCODE = "ADMIN149"

# Global reference for root window
root = None


# This Function prevents the GUI from making errors when switching from pages by remoing all windgests from the window
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



# Admin MENU
# This Function shows the Admin Menu and Admin options
def show_admin_menu():
    #clear_window()
    root.configure(bg="lightgray")

    # Title with Admin Username entered
    title_label = Label(root, text="Admin Menu - " + current_username,
                        font=("Times New Roman", 22, "bold"), bg="lightgray")
    title_label.pack(pady=30)

    # View All Bookings button
    view_btn = Button(root, text="View All Bookings", width=30, height=2,
                      font=("Times New Roman", 14, "bold"),
                      bg="blue", fg="white", command=show_all_bookings)
    view_btn.pack(pady=10)

    # Assign Driver button
    assign_btn = Button(root, text="Assign Driver to Booking", width=30, height=2,
                        font=("Times New Roman", 14, "bold"),
                        bg="green", fg="white", command=show_assign_driver)
    assign_btn.pack(pady=10)

    # Logout button
    back_btn = Button(root, text="Logout", width=30, height=2,
                      font=("Times New Roman", 14),
                      bg="red", fg="white", command=show_main_menu)
    back_btn.pack(pady=10)


# This Function shows all booking with the system
def show_all_bookings():
    #clear_window()
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
    #clear_window()
    root.configure(bg="white")

    # Title
    title_label = Label(root, text="Assign Driver to Booking",
                        font=("Times New Roman", 20, "bold"), bg="white")
    title_label.pack(pady=20)

    # Creates page frame
    page_frame = Frame(root, bg="white")
    page_frame.pack(pady=20)

    # Booking ID field
    Label(page_frame, text="Booking ID:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=0, column=0, padx=10, pady=15)
    booking_id_entry = Entry(page_frame, width=25, font=("Times New Roman", 12))
    booking_id_entry.grid(row=0, column=1, padx=10, pady=15)

    # Label for Driver dropdown menu
    Label(page_frame, text="Driver:", font=("Times New Roman", 12, "bold"),
          bg="white").grid(row=1, column=0, padx=10, pady=15)

    # Gets all Drivers from system
    drivers = system.get_all_drivers()

    # Creates a list of Driver options
    driver_options = []
    for driver in drivers:
        driver_text = driver['id'] + " - " + driver['name']
        driver_options.append(driver_text)

    # Creates driver dropdown menu
    driver_var = StringVar()
    driver_menu = ttk.Combobox(page_frame, textvariable=driver_var,
                               values=driver_options, state="readonly", width=23)
    driver_menu.grid(row=1, column=1, padx=10, pady=15)

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

        # Pulls Driver ID from selection and uses " - "
        parts = driver_selection.split(" - ")
        driver_id = parts[0]

        # Calls assign function
        success, message = system.assign_driver(booking_id=booking_id, driver_id=driver_id)

        # Displays assignment result to Admin
        if success:
            messagebox.showinfo("Success", message)
            show_admin_menu()
        else:
            messagebox.showerror("Error", message)

    # Creates button frame
    button_frame = Frame(root, bg="white")
    button_frame.pack(pady=20)

    # Assign driver button
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

    # Displays the Main Menu
    show_main_menu()

    # Starts the event loop
    root.mainloop()


# Runs the application
if __name__ == "__main__":
    main()
