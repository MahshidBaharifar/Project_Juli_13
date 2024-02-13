from src.my_hotel import Hotel
from src.my_customer import Customer
from src.my_room import Room
from src.my_reservation import Reservation
from datetime import date

def main():
    # Step 1: Create a hotel with 3 single rooms, 2 double rooms, and 1 executive room, each available for 5 days
    hotel = Hotel('Hotel1', 3, 2, 1, 5)

    # Step 2: Create a reservation object
    reservation = Reservation()

    # Step 3: Make a reservation
    checkin_date = (2023, 7, 20)
    checkout_date = (2023, 7, 25)

    print("\n===== Making a Reservation =====")
    reservation.make_reservation(checkin_date, checkout_date)

    # Step 4: View available rooms
    print("\n===== Available Rooms =====")
    available_rooms = hotel.available_rooms(checkin_date, checkout_date)
    for room in available_rooms:
        print(f"{room.room_type} Room: {room.return_price_per_night()} USD per night")

    # Step 5: Modify the reservation
    new_checkin_date = (2023, 7, 21)
    new_checkout_date = (2023, 7, 27)

    print("\n===== Modifying Reservation =====")
    customer_id = input("Enter the customer's reservation ID to modify: ")
    reservation.modify_reservation(customer_id, new_checkin_date, new_checkout_date)

    # Step 6: Cancel a reservation
    print("\n===== Canceling Reservation =====")
    customer_id_to_cancel = input("Enter the customer's reservation ID to cancel: ")
    reservation.cancel_reservation(customer_id_to_cancel)

    # Step 7: Check available rooms after cancellation
    print("\n===== Available Rooms After Cancellation =====")
    available_rooms_after_cancellation = hotel.available_rooms(checkin_date, checkout_date)
    for room in available_rooms_after_cancellation:
        print(f"{room.room_type} Room: {room.return_price_per_night()} USD per night")

if __name__ == "__main__":
    main()