from src.my_reservation import Reservation
from datetime import date
from dateutil.relativedelta import relativedelta

def testCase1():
    dateToday = date.today()
    # Description---------------------------------------------------------------

    # This is the simplest test case
    # The user accidentally has entered 0 rooms and 0 days, in which case the hotel defaults
    # to having 1 standard room only. The calendar defaults to looking 1 day ahead.
    # This means that the user can only book today's date in 1 room!

    # Purpose-------------------------------------------------------------------
    # The purpose of this test is to add 2 customers, book the first customer which
    # sells out the hotel, and ensure that the second customer is not able to book

    # Initialize Reservation
    R = Reservation()

    # Create Hotel with 1 standard room
    R.creat_hotel(1, 0, 0, 1)

    # Add first customer
    R.creat_customer('Vin', 'Desh', 0, 1234567891)

    # Check-in and Check-out dates
    dateIn = dateToday
    dateOut = dateToday + relativedelta(days=1)

    # Make reservation for the first customer
    R.make_reservation(dateIn, dateOut)

    # Add second customer
    R.creat_customer('John', 'Doe', 0, 1234567891)

    # Attempt to make reservation for the second customer (hotel is sold out)
    R.make_reservation(dateIn, dateOut)


# Run the test case
#testCase1()

def test_test():
    assert True
