# ==================================================
#        MOVIE TICKET MANAGEMENT SYSTEM
# ==================================================

users = {
    "student": ["student123", "user"],
    "admin": ["admin123", "admin"]
}

Movies = [

    ['12001', 'HANUMAN ANSH'],
    ['12101', 'THE PARADISE'],
    ['12622', 'THE Vvaan-FORCE OF THE FORREST'],
    ['12951', 'RESIDENT EVIL'],
    ['12985', 'FORGOTTEN ISLAND']

]

tickets = []
cust = 1


# ---------- LOGIN ----------

def login(role):                           #Username - student (for users) , Username - admin(for admin)
    print("\n--- LOGIN ---")               #Password - student123        , Password - admin123
    u = input("Username: ")
    p = input("Password: ")

    if u in users and users[u][0] == p and users[u][1] == role:
        print("Login successful!")
        return u

    print("Invalid login.")
    return None

# ---------- SHOW TICKET ----------

def show_ticket(t):
    print("\n-----------------------------")
    print("CUST :", t[0])
    print("User :", t[1])
    print("MOVIE :", t[2], "-", t[3])
    print("Date :", t[4])
    print("Time :", t[5])
    print("Customers :", ", ".join(t[6]))
    print("Status :", t[7])
    print("-----------------------------")

# ---------- BOOK TICKET ----------

def book(user):
    global cust

    print("\n--- AVAILABLE MOVIES ---")
    for i in range(len(Movies)):
        print(f"{i+1}. {Movies[i][0]} - {Movies[i][1]}")

    try:
        choice = int(input("Select movie (1-5): "))
        movie = Movies[choice - 1]
    except (ValueError, IndexError):
        print("Invalid movie.")
        return

    booking_date = input("Enter Booking Date (DDMM2026): ")
    booking_time = input("Enter Booking Time (HHMMSS): ")

    try:
        count = int(input("Number of customers: "))
    except ValueError:
        print("Invalid number.")
        return

    if count < 1:
        print("Customer count must be positive.")
        return

    names = [input(f"Customer {i + 1} Name: ").lower() for i in range(count)]

    tickets.append([
        cust, user, movie[0], movie[1],
        booking_date, booking_time,
        names, "Confirmed"
    ])

    print(f"\nTicket booked! CUST Number: {cust}")
    cust += 1

# ---------- SEARCH ----------

def search():
    try:
        number = int(input("Enter CUST Number: "))
    except ValueError:
        print("Invalid CUST Number.")
        return

    ticket = next((t for t in tickets if t[0] == number), None)

    if ticket:
        show_ticket(ticket)
    else:
        print("Ticket not found.")

# ---------- CANCEL ----------

def cancel(user, admin=False):
    try:
        number = int(input("Enter CUST Number: "))
    except ValueError:
        print("Invalid CUST Number.")
        return

    ticket = next((t for t in tickets if t[0] == number), None)

    if not ticket:
        print("Ticket not found.")
        return

    if not admin and ticket[1]!= user:
        print("You can cancel only your own ticket.")
        return

    if ticket[7] == "Cancelled":
        print("Ticket already cancelled.")
        return

    ticket[7] = "Cancelled"
    print("Ticket cancelled successfully.")

# ---------- USER MENU ----------

def user_menu(user):
    while True:
        print("\n--- USER MENU ---")
        print("1. Book Ticket")
        print("2. My Bookings")
        print("3. Search Ticket")
        print("4. Cancel Ticket")
        print("5. Logout")
        ch = input("Choice: ")

        if ch == "1":
            book(user)
        elif ch == "2":
            mine = [t for t in tickets if t[1] == user]
            if not mine:
                print("No bookings.")
            else:
                for t in mine:
                    show_ticket(t)
        elif ch == "3":
            search()
        elif ch == "4":
            cancel(user)
        elif ch == "5":
            break
        else:
            print("Invalid choice.")

# ---------- ADD MOVIE ----------

def add_movie():
    number = input("Movie number: ")
    name = input("Movie name: ")
    Movies.append([number, name])
    print("Movie added successfully.")

# ---------- STATISTICS ----------

def statistics():
    confirmed = sum(t[7] == "Confirmed" for t in tickets)
    cancelled = sum(t[7] == "Cancelled" for t in tickets)
    total_customers = sum(len(t[6]) for t in tickets)

    print("\n--- MOVIE STATISTICS ---")
    print("Total bookings :", len(tickets))
    print("Confirmed :", confirmed)
    print("Cancelled :", cancelled)
    print("Total Customers:", total_customers)

# ---------- ADMIN MENU ----------

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. All Bookings")
        print("2. Search Ticket")
        print("3. Cancel Booking")
        print("4. Statistics")
        print("5. Add Movie")
        print("6. Logout")
        ch = input("Choice: ")

        if ch == "1":
            if tickets:
                for t in tickets:
                    show_ticket(t)
            else:
                print("No bookings.")
        elif ch == "2":
            search()
        elif ch == "3":
            cancel("admin", True)
        elif ch == "4":
            statistics()
        elif ch == "5":
            add_movie()
        elif ch == "6":
            break
        else:
            print("Invalid choice.")

# ---------- MAIN PROGRAM ----------

while True:
    print("\n==============================")
    print(" MOVIE TICKETING SYSTEM")
    print("==============================")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        user = login("user")
        if user:
            user_menu(user)
    elif choice == "2":
        admin = login("admin")
        if admin:
            admin_menu()
    elif choice == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice.")
