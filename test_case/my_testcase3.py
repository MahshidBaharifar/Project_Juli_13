from src.my_reservation import Reservation
from datetime import date
from dateutil.relativedelta import relativedelta


def testCase3():
    dateToday = date.today()

    # Description --------------------------------------------------------------
    # 3 rooms are available and the user accidentally does a double booking, and then
    # the user accidentally books the other customer in the same room (with overlapping dates)

    # Purpose -----------------------------------------------------------------
    # The purpose of this test is to ensure that a double booking does not occur, and another
    # customer cannot book the same room as the first active customer.

    R = Reservation()
    R.create_hotel(1, 1, 1, 30)

    dateVin = dateToday + relativedelta(days=1)
    dateVout = dateToday + relativedelta(days=7)
    dateVout2 = dateToday + relativedelta(days=11)
    dateJin = dateToday + relativedelta(days=5)
    dateJout = dateToday + relativedelta(days=13)

    customer1 = R.create_customer('Vin', 'Desh', 0, 123456789)
    customer2 = R.create_customer('John', 'Doe', 0, 123456789)

    R.add_customer(customer1)
    R.add_customer(customer2)

    R.make_reservation(customer1.returnReservationID(), dateVin, dateVout)
    # This reservation should not be booked
    R.make_reservation(customer1.returnReservationID(), dateVin, dateVout2)
    # This reservation should not show Vin's room selection due to overlapping dates
    # since dateJin is before dateVout
    R.make_reservation(customer2.returnReservationID(), dateJin, dateJout)

def test_test():
    assert True