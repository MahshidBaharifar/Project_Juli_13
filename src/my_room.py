

from my_calendar import Calendar

class Room:
    def __init__(self, room_type, num_of_days):
        self.room_type = room_type
        self.num_of_days = num_of_days
        self.room_calendar = Calendar(self.num_of_days)

        if self.room_type == 'S':
            self.price = 100
        elif self.room_type == 'D':
            self.price = 200
        elif self.room_type == 'E':
            self.price = 300

    def return_price_per_night(self):
        return self.price

    def return_room_calendar(self):
        return self.room_calendar.return_all_booking_days()

    def is_date_valid(self, check_in_date, check_out_date):
        return check_in_date, check_out_date in self.room_calendar.return_all_booking_days()

    def find_date_index(self, date_to_find):
        for index, item in enumerate(self.room_calendar.return_all_booking_days()):
            if item[0] == date_to_find:
                return index
        return -1

    def is_room_available(self, check_in_date, check_out_date):
        start_index = self.find_date_index(check_in_date)
        end_index = self.find_date_index(check_out_date)
        if start_index == -1 or end_index == -1:
            return False
        return all(item[1] == 'None' for item in self.room_calendar.return_all_booking_days()[start_index:end_index])

    def is_fully_unavailable(self, check_in_date, check_out_date):
        start_index = self.find_date_index(check_in_date)
        end_index = self.find_date_index(check_out_date)
        if start_index == -1 or end_index == -1:
            return False
        return all(item[1] != 'None' for item in self.room_calendar.return_all_booking_days()[start_index:end_index])

    def check_reservation(self, check_in_date, check_out_date):
        if self.is_date_valid(check_in_date, check_out_date) and self.is_room_available(check_in_date, check_out_date):
            self.status = True
        else:
            self.status = False

        return self.status

    def booking_customer(self, check_in_date, check_out_date, ID):
        start_index = self.find_date_index(check_in_date)
        end_index = self.find_date_index(check_out_date)
        if start_index == -1 or end_index == -1:
            return
        for i in range(start_index, end_index):
            self.room_calendar.return_all_booking_days()[i][1] = ID

    def cancel_customer(self, check_in_date, check_out_date, ID):
        start_index = self.find_date_index(check_in_date)
        end_index = self.find_date_index(check_out_date)
        if start_index == -1 or end_index == -1:
            return
        for i in range(start_index, end_index):
            self.room_calendar.return_all_booking_days()[i][1] = 'None'


num_of_days = 10
room_type = "S"
room = Room(room_type, num_of_days)

price_per_night = room.return_price_per_night()
room_calendar = room.return_room_calendar()

print("Price Per Night:", price_per_night)
print("Room Calendar:")
print(room_calendar)
print("-----------------------------")
