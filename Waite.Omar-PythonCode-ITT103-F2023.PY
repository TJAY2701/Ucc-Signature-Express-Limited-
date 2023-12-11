#Omar Waite
#Date Created: December 5, 2023
#course: ITT103
#This program aims to automate seat reservations across first class, business class, and economy class,for the UCC Signature Express Limited.

# 1. Reservation System Menu Display
def DisplayMenu():
    print("UCC Signature Express Limited")
    print("Travel. Live. Experience")
    print("Reservation Options:")
    print(f"First Class (F/f) - {first_class_seats} seats remaining")
    print(f"Business Class (B/b) - {business_class_seats} seats remaining")
    print(f"Economy Class (E/e) - {economy_class_seats} seats remaining")
    print("Quit or Cancel (Q/q)")
    print("Please select an option:")

# 2. Reading User Choice
def GetUserChoice():  
    choice = input().lower()
    return choice

# define the number of seats for each class
first_class_seats = 27
business_class_seats = 38
economy_class_seats = 56

# 3. Two-Dimensional Array to Represent Seats
first_class_bus = [["O" for _ in range(4)] for _ in range(first_class_seats)]
business_class_bus = [["O" for _ in range(4)] for _ in range(business_class_seats)]
economy_class_bus = [["O" for _ in range(4)] for _ in range(economy_class_seats)]

# 4. Making a Reservation
def MakeReservation(bus, class_seats):
    row_number = int(input("Enter a row number: "))  # 1. Prompt for row number
    if row_number <= 0 or row_number > len(bus):  #check if row is valid
        print("Number must be positive or greater than zero!")
        return False

    column_number = int(input("Enter a column number between 1-4 (1 for window, 2 for aisle): "))  # 2. Prompt for window or aisle
    if column_number < 1 or column_number > 4:  # updated check for valid column
        print("Invalid column number!")
        return False
      
    # 4. Reserve seat and display message. Also, 7. Check if the seat is already reserved.
    if bus[row_number - 1][column_number - 1] == "O":
        bus[row_number - 1][column_number - 1] = "X"
        print(f"Reserving seat: row {row_number} column {column_number:02}")
        class_seats -= 1  # Decrease the number of available seats
        return True, class_seats
    else:
        print("Seat is already reserved.")
        return False, class_seats

# 5. Check if all seats are reserved
def CheckFullReservation(bus):
    for row in bus:
        if "O" in row:
            return False
    return True

reservation_type = ""
bus = None
while True:
    DisplayMenu()
    choice = GetUserChoice()

    if choice == "f":
        print("You have selected First class")
        reservation_type = "First Class"
        bus = first_class_bus
        class_seats = first_class_seats
    elif choice == "b":
        print("You have selected Business class")
        reservation_type = "Business Class"
        bus = business_class_bus
        class_seats = business_class_seats
    elif choice == "e":
        print("You have selected Economy class")
        reservation_type = "Economy Class"
        bus = economy_class_bus
        class_seats = economy_class_seats
    elif choice == "q":
        print("You have selected the option to cancel")
        print("Thank you for visiting our site")
        break
    else:
        print("Invalid choice!")  # ii. Invalid choice message
        continue

    if CheckFullReservation(bus):  # 5. Check if no more available seats
        print("No more available seats!")
        continue

    reserved, number_of_seats = MakeReservation(bus, {'f': first_class_seats, 'b': business_class_seats, 'e': economy_class_seats}[choice])  # 6. Display menu again after reservation
    if reserved:
        if choice == "f":
            first_class_seats = number_of_seats
        elif choice == "b":
            business_class_seats = number_of_seats
        elif choice == "e":
            economy_class_seats = number_of_seats
        continue

# i. Final message when 'q' or 'Q' is selected
if bus is not None:  # Check if any reservations were made
    num_seats = sum(len(row) for row in bus)
    num_reserved = sum(row.count("X") for row in bus)
    print(f"Reservation Type: {reservation_type}")
    print(f"Total number of seats: {num_seats}")
    print(f"Total number of seats reserved: {num_reserved}")

