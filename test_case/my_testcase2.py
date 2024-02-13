from src.my_reservation import Reservation
from datetime import date
from dateutil.relativedelta import relativedelta


def testCase2():
    dateToday = date.today()

    # Description --------------------------------------------------------------
    # Similar to test 1 with correct inputs

    # Purpose -----------------------------------------------------------------
    # The purpose of this test is to add 2 customers, book the first customer which
    # sells out the hotel, cancel and refund customer 1, and then book customer 2

    R = Reservation()
    R.create_hotel(1, 0, 0, 1)

    dateIn = dateToday
    dateOut = dateToday + relativedelta(days=1)

    customer1 = R.create_customer('Vin', 'Desh', 0, 1234567891)
    customer2 = R.create_customer('John', 'Doe', 0, 1234567891)

    R.add_customer(customer1)
    R.add_customer(customer2)

    R.make_reservation(customer1.returnReservationID(), dateIn, dateOut)
    R.cancel_reservation(customer1.returnReservationID())

    # John should be able to make a reservation
    R.make_reservation(customer2.returnReservationID(), dateIn, dateOut)

    # Expected output: both reservation invoices

    
def test_test():
    assert True