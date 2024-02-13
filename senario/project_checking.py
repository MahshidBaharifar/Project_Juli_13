import os
import sys
from datetime import date
from src.my_calendar import Calendar
from src.my_room import Room
from src.my_hotel import Hotel
from src.my_customer import Customer
from src.my_reservation import Reservation

# Set up the src directory path for importing modules
src_directory = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
sys.path.append(src_directory)

def main():
    print("Welcome to the Hotel Reservation System!")
    num_of_days = 30
    calendar = Calendar(num_of_days)

    all_booking_days = calendar.return_all_booking_days()
    available_date_range = calendar.return_available_date_range()

    print("All Booking Days:")
    print(all_booking_days)
    print("\nAvailable Date Range:")
    print("Check-in:", available_date_range[0])
    print("Check-out:", available_date_range[1])
    print("-----------------------------")

    num_of_days = 10
    room_type = "S"
    room = Room(room_type, num_of_days)

    price_per_night = room.return_price_per_night()
    room_calendar = room.return_room_calendar()

    print("Price Per Night:", price_per_night)
    print("Room Calendar:")
    print(room_calendar)
    print("-----------------------------")



    # Step 1: Create Hotel
    num_s_rooms = 5
    num_d_rooms = 10
    num_e_rooms = 3
    num_days = 90
    hotel = Hotel('Hotel1', num_s_rooms, num_d_rooms, num_e_rooms, num_days)

    # Step 2: Create Customer
    fname = "John"
    lname = "Doe"
    num_guests = 2
    contact_number = "1234567890"
    customer = Customer(fname, lname, num_guests, contact_number)

    # Step 3: Assign Dates to the Customer
    checkin_date = (2023, 8, 1)
    checkout_date = (2023, 8, 3)
    customer.assign_dates(checkin_date, checkout_date)

    # Step 4: Find Available Rooms
    dateIn, dateOut = customer.return_dates()
    available_rooms = hotel.available_rooms(dateIn, dateOut)

    # Step 5: Make Reservation
    if available_rooms:
        room_type = "D"
        available_type_rooms = hotel.available_type_rooms(room_type, dateIn, dateOut)

        if available_type_rooms:
            sel_room = "2D"
            room = hotel.find_specific_room(sel_room)

            if room.is_room_available(dateIn, dateOut):
                room.booking_customer(dateIn, dateOut, customer.return_reservation_id())
                customer.assign_room(sel_room)
                amount = customer.return_duration_days() * room.return_price_per_night()
                customer.charge_customer(amount)
                print("Reservation successfully made.")
            else:
                print("The selected room is not available for the specified dates.")
        else:
            print("No available rooms of the selected type.")
    else:
        print("No available rooms in hotel1 in your date interval")

    # Step 6: Cancel Reservation
    reservation_id = customer.return_reservation_id()
    reservation = Reservation()
    reservation.create_hotel(num_s_rooms, num_d_rooms, num_e_rooms, num_days)
    reservation.add_customer(customer)

    print("\nYour Reservation ID:", reservation_id)
    print("Cancellation Process:")
    reservation.cancel_reservation(reservation_id)

    # Step 7: Modify Reservation
    print("\nYour Reservation ID:", reservation_id)
    print("Modification Process:")
    new_checkin_date = (2023, 8, 5)
    new_checkout_date = (2023, 8, 7)
    reservation.modify_reservation(reservation_id, new_checkin_date, new_checkout_date)

if __name__ == "__main__":
    main()
