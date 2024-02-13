from my_hotel import Hotel
from my_customer import Customer


class Reservation:
    def __init__(self, nSRooms, nDRooms, nERooms, n):
        self.hotel = Hotel('Hotel 1', nSRooms, nDRooms, nERooms, n)
        self.customers = {}

    def addCustomer(self, fname, lname, nguests, number):
        customer = Customer(fname, lname, nguests, number)
        cRID = customer.returnReservationID()
        if cRID not in self.customers:
            self.customers[cRID] = customer
        else:
            print('Customer already exists!')

    def makeReservation(self, ID, chkInDate, chkOutDate):
        if ID in self.customers:
            customer = self.customers[ID]
            customer.assign_date(chkInDate, chkOutDate)
            dateIn, dateOut = customer.returnCustomerDates()
            if not self.hotel.checkIfHotelBooked(dateIn, dateOut):
                if not customer.returnCustomerRooms():
                    try:
                        print('\nBooking for ID', ID)
                        roomSel = input('Choose a room from the available list: ').upper()
                        room = self.hotel.find_specific_room(roomSel)
                        flag = room.check_reservation(dateIn, dateOut)
                        if flag:
                            room.booking_customer(dateIn, dateOut, ID)
                            customer.assignCustomerRoom(roomSel)
                            amount = customer.returnCustomerDays() * room.price_per_night()
                            customer.chargeCustomer(amount)
                            self.returnReservationDetails(ID)
                        else:
                            print('Booking unsuccessful for customer ID:', ID)
                            print('Failed to assign customer booking dates')
                    except (ValueError, AttributeError):
                        print('Incorrect Room Selection Choice')
                else:
                    print('\n')
                    print(ID, 'is already booked in Room:', customer.returnCustomerRooms())
                    print('\n')
            else:
                print(ID, ': Hotel is sold out for the selected dates!')
        else:
            print('Invalid ID')

    def cancelReservation(self, ID):
        if ID in self.customers:
            customer = self.customers[ID]
            roomsAssigned = customer.returnCustomerRooms()
            if roomsAssigned:
                room = self.hotel.find_specific_room(roomsAssigned[0])
                room.cancel_customer(*customer.returnCustomerDates(), ID)
                amount = customer.returnCustomerCharge()
                customer.refundCustomer(amount)
                customer.resetCustomerData()
                del self.customers[ID]
                print('Reservation', ID, 'Cancelled')
            else:
                print('No rooms assigned for customer', ID)
        else:
            print('Invalid ID')

    def returnReservationDetails(self, ID):
        if ID in self.customers:
            customer = self.customers[ID]
            hname = self.hotel.hotel_name()
            fname, lname, guests, number = customer.returnCustomerDetails()
            totCharge = customer.returnCustomerCharge()
            rooms = customer.returnCustomerRooms()
            dates = customer.returnCustomerDates()
            if rooms:
                rSel = rooms[0]
            else:
                rSel = rooms
            customer.cInvoice.printBill(hname, fname, lname, guests, number, rSel, totCharge, dates[0], dates[1], ID)
        else:
            print('Invalid ID')

    def modifyReservation(self, ID, newInDate, newOutDate):
        if ID in self.customers:
            customer = self.customers[ID]
            rooms = customer.returnCustomerRooms()
            if rooms:
                fname, lname, nguests, number = customer.returnCustomerDetails()
                oldDates = customer.returnCustomerDates()
                print(ID, 'has room', rooms, 'booked between', oldDates[0], 'and', oldDates[1])
                self.cancelReservation(ID)
                self.addCustomer(fname, lname, nguests, number)
                bFlag = self.makeReservation(ID, newInDate, newOutDate)
                if not bFlag:
                    print('Modification unsuccessful since another customer is booked, resetting dates...\n')
                    self.makeReservation(ID, oldDates[0], oldDates[1])
            else:
                print('No rooms booked!')
        else:
            print('Invalid ID')
