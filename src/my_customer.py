
 
from datetime import date

class Customer:
    def __init__(self, first_name, last_name, num_guests, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.num_guests = num_guests
        self.contact_number = contact_number
        self.room_assignment = []
        self.total_charge = 0
        self.checkin_date = None
        self.checkout_date = None
        self.duration_days = 0
        self.reservation_id = f"{first_name[0]}{last_name[0]}{str(contact_number)[-4:]}"
        
    def assign_dates(self, checkin_date, checkout_date):
        self.chkInDate = date(checkin_date[0] , checkin_date[1] , checkin_date[2])
        self.chkOutDate = date(checkout_date[0] , checkout_date[1] , checkout_date[2])
        self.durDays= self.chkInDate - self.chkOutDate

    def assign_room(self, room_selection):
        self.room_assignment.append(str(room_selection))

    def reset_data(self):
        self.room_assignment = []
        self.checkin_date = None
        self.checkout_date = None
        self.reservation_id = None

    def charge_customer(self, amount):
        self.total_charge += amount

    def refund_customer(self, amount):
        self.total_charge -= amount
        if self.total_charge <= 0:
            self.total_charge = 0
            print('Fully refunded: $', amount)

    def return_details(self):
        return self.first_name, self.last_name, self.num_guests, self.contact_number

    def return_rooms(self):
        return self.room_assignment

    def return_charge(self):
        return self.total_charge

    def return_reservation_id(self):
        return self.reservation_id

    def return_dates(self):
        return self.checkin_date, self.checkout_date

    def return_duration_days(self):
        return self.duration_days
