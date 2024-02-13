HotelReservation
A simple hotel reservation system
A hotel can be defined with any number of rooms of 3 different suites: Standard, Deluxe, Executive (varying prices). The features are:
Any number of customers can be added and stored in a database. Each customer has a unique ID which is used to create/modify/cancel a booking.
Each room has a calendar that keeps track of bookings. The calendar length is customizable - i.e. the booking date range can be up to the user (90-120 days ahead is a good value). This is meant for realism, you can't book something 10 years in advance!
Reservations can be cancelled or modified. Refunds are also provided.
Each customer has an Invoice which prints the bill at the end and is updated if the reservation is cancelled or modified.
The program shows the user which rooms are available on the selected dates, along with the range of booking dates possible (how late the checkout date can be). If a room is sold out for the dates requested, it will not show up on the list.
The following describes the current limitations of the program, as the degree of complexity is endless:
There is only one Hotel
If the user inputs incorrect values or data types, there is an error message provided, however the function has to be re-initialized again. However to avoid this happening, the program provides prompts throughout - as in point 5 above.
There is no housekeeping or receptionist assigned to each room.
The price of each suite type is uniform and holidays are not considered.
If 2 customers have the same first name and last name letter, along with the same last 4 digits of phone number, this will conflict the ID, however what are the chances of that in real life!
The following edge cases are considered:
Sold out Hotel
Incorrect customer ID selected
Overlapping of booking dates between two customers of the same room (when modifying or creating a new reservation)
Dates falling outside the booking database limits
Double booking of the same customer
The time complexity for some of the methods is as follows: Let the variables represent:
nRooms = number of total Rooms
nDays = number of Calendar days (per room)
nBookedDays = number of days booked by the customer (<nDays) - (checkOutDate - checkInDate)
