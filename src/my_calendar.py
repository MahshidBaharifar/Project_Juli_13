from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class Calendar:
    def __init__(self, num_of_days):
        if num_of_days <= 0:
            raise ValueError("Number of days must be a positive integer")
        
        self.num_of_days = num_of_days
        today = date.today()
        self.booking_date = today.strftime('%Y-%m-%d')
        final_date = today + relativedelta(days=self.num_of_days)
        self.final_date = final_date.strftime('%Y-%m-%d')

        delta = final_date - today
        self.booking_days = []

        for i in range(delta.days + 1):
            day = today + timedelta(days=i)
            item = (day, 'None')
            self.booking_days.append(item)

    def return_all_booking_days(self):
        return self.booking_days

    def return_available_date_range(self):
        return self.booking_date, self.final_date



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




    
            







