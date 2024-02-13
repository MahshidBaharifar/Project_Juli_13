from src.my_hotel import Hotel
from src.my_customer import Customer
from src.my_room import Room
from datetime import date
from dateutil.relativedelta import relativedelta




from src.my_hotel import Hotel
from datetime import date

class Reservation:
    def __init__(self):
        self.hotel = None
        self.current_customer = None
        self.customer_data = []

    def create_hotel(self, num_s_rooms, num_d_rooms, num_e_rooms, num_days):
        self.hotel = Hotel('Hotel1', num_s_rooms, num_d_rooms, num_e_rooms, num_days)

    def create_customer(self, first_name, last_name, num_guests, contact_number):
        customer = Customer(first_name, last_name, num_guests, contact_number)
        return customer

    def add_customer(self, new_customer):
        new_reservation_id = new_customer.return_reservation_id()
        self.customer_data.append((new_reservation_id, new_customer))

    def get_current_customer(self, ID):
        for item in self.customer_data:
            if item[0] == ID:
                self.current_customer = item[1]

    def return_current_customer(self, ID):
        for item in self.customer_data:
            if item[0] == ID:
                return item[1]

    def if_customer_valid(self, ID):
        return ID in [item[0] for item in self.customer_data]

    def make_reservation(self, checkin_date, checkout_date):
        fname = input('First Name: ')
        lname = input('Last Name: ')
        num_guests = int(input('Number of Guests: '))
        contact_number = int(input('Contact Number: '))

        self.current_customer = self.create_customer(fname, lname, num_guests, contact_number)
        ID = self.current_customer.return_reservation_id()

        if ID in [item[0] for item in self.customer_data]:
            print("It's not a new reservation.")
        else:
            self.customer_data.append((ID, self.current_customer))
            self.current_customer.assign_dates(checkin_date, checkout_date)
            dateIn, dateOut = self.current_customer.return_dates()

            if self.hotel.is_hotel_booked(dateIn, dateOut):
                print("Hotel is fully booked for the selected dates.")
            else:
                all_available_rooms = self.hotel.available_rooms(dateIn, dateOut)
                if all_available_rooms:
                    room_type = input('Select the room type, please: ')
                    available_rooms = self.hotel.available_type_rooms(room_type, dateIn, dateOut)

                    if available_rooms:
                        sel_room = input('Choose a room from the available rooms: ')
                        room = self.hotel.find_specific_room(sel_room)

                        if room.is_room_available(dateIn, dateOut):
                            room.booking_customer(dateIn, dateOut, ID)
                            self.current_customer.assign_room(sel_room)
                            amount = self.current_customer.return_duration_days() * room.return_price_per_night()
                            self.current_customer.charge_customer(amount)
                            print("Reservation successfully made.")
                        else:
                            print("The selected room is not available for the specified dates.")
                    else:
                        print("No available rooms of the selected type.")
                else:
                    print("No available rooms in hotel1 in your date interval")

    def cancel_reservation(self, ID):
        if self.if_customer_valid(ID):
            self.current_customer = self.return_current_customer(ID)
            rooms = self.current_customer.return_rooms()
            if rooms:
                for room in rooms:
                    current_room = self.hotel.find_specific_room(room)
                    check_in_date = self.current_customer.return_dates()[0]
                    check_out_date = self.current_customer.return_dates()[1]
                    current_room.cancel_customer(check_in_date, check_out_date, ID)

                amount = self.current_customer.return_charge()
                self.current_customer.refund_customer(amount)
                self.current_customer.reset_data()
                print('Reservation', ID, 'Cancelled')

                # Delete customer data from the reservation database
                self.customer_data.remove((ID, self.current_customer))
            else:
                print("There is no room assigned to this customer.")
        else:
            print("ID is not valid!")

    def modify_reservation(self, ID, new_in_date, new_out_date):
        if self.if_customer_valid(ID):
            self.current_customer = self.return_current_customer(ID)
            rooms = self.current_customer.return_rooms()
            if rooms:
                # Store old data in case modification is not successful
                (fname, lname, num_guests, contact_number) = self.current_customer.return_details()
                old_dates = self.current_customer.return_dates()
                print(ID, 'has room(s)', rooms, 'booked between', old_dates[0], 'and', old_dates[1])

                for room in rooms:
                    current_room = self.hotel.find_specific_room(room)
                    check_in_date = self.current_customer.return_dates()[0]
                    check_out_date = self.current_customer.return_dates()[1]
                    current_room.cancel_customer(check_in_date, check_out_date, ID)

                # Cancel and re-initialize customer
                self.current_customer.reset_data()
                self.add_customer(self.current_customer)

                # Reserve with new dates
                self.make_reservation(new_in_date, new_out_date)

                if not self.if_customer_valid(ID):
                    # Reservation was unsuccessful, reset to old dates
                    print('Modification unsuccessful since another customer is booked, resetting dates...\n')
                    self.make_reservation(old_dates[0], old_dates[1])
            else:
                print('No rooms booked!')
        else:
            print('Invalid ID')






