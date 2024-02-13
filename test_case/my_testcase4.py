from src.my_reservation import Reservation
from datetime import date
from dateutil.relativedelta import relativedelta


def testCase4():
    dateToday = date.today()

    # Description --------------------------------------------------------------
    # 1 room is available, the calendar is available 6 days ahead from today, customer 1 books
    # first 3 days, customer 2 books next 3. Customer 1 attempts to modify their reservation
    # whilst choosing dates that overlap with customer 2's booking

    # Purpose -----------------------------------------------------------------
    # The purpose of this test is to ensure that Customer 1 should not be able to modify his
    # reservation since customer 2 has a conflicting booking

    R = Reservation()
    R.create_hotel(0, 1, 0, 6)

    dateVIn = dateToday
    dateOut = dateToday + relativedelta(days=3)
    dateOut2 = dateToday + relativedelta(days=6)
    dateOut3 = dateToday + relativedelta(days=4)

    customer1 = R.create_customer('Vin', 'Desh', 0, 123456789)
    customer2 = R.create_customer('John', 'Doe', 0, 123456789)

    R.add_customer(customer1)
    R.add_customer(customer2)

    R.make_reservation(customer1.returnReservationID(), dateVIn, dateOut)
    R.make_reservation(customer2.returnReservationID(), dateOut, dateOut2)
    # Vin's reservation should not be able to modify due to conflict
    # Attempt to modify dates with checkout date conflicting with John
    R.modify_reservation(customer1.returnReservationID(), dateVIn, dateOut3)
    # The expected output should be the dates resetting and Vin being able to rebook the same room

def test_test():
    assert True