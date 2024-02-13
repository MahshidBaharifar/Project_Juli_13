from src.my_reservation import Reservation
from datetime import date
from dateutil.relativedelta import relativedelta

def testCase5():
    dateToday = date.today()

    # Description --------------------------------------------------------------
    # This is a normal test case, with 10 rooms in each suite, 45 days lookahead, and 2 random bookings

    # Purpose -----------------------------------------------------------------
    # The purpose of these tests is to ensure that these 2 bookings can be made and
    # modified, provided you choose the correct rooms (as per prompt)

    R = Reservation()
    R.create_hotel(10, 10, 10, 45)

    date1 = dateToday
    date2 = dateToday + relativedelta(days=3)
    date3 = dateToday + relativedelta(days=6)
    date4 = dateToday + relativedelta(days=9)

    customer1 = R.create_customer('Vin', 'Desh', 0, 123456789)
    customer2 = R.create_customer('David', 'Venuto', 0, 123456789)

    R.add_customer(customer1)
    R.add_customer(customer2)

    R.make_reservation(customer1.returnReservationID(), date1, date2)
    R.make_reservation(customer2.returnReservationID(), date3, date4)

    # This is your choice, you can choose any random dates here, and modify anyone
    R.modify_reservation(customer1.returnReservationID(), date1, date4)


def test_test():
    assert True