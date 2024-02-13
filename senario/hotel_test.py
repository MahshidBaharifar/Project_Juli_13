import sys
sys.path.append("/src")
from my_hotel import Hotel
def main():
    num_s_rooms = 3
    num_d_rooms = 5
    num_e_rooms = 2
    num_days = 90
    
    hotel = src.my_hotel.Hotel("Hotel1", num_s_rooms, num_d_rooms, num_e_rooms, num_days)

    hotel_name = hotel.get_hotel_name()
    rooms_data = hotel.get_rooms_data()

    print("Hotel Name:", hotel_name)
    print("Rooms Data:")
    for room_id, room_obj in rooms_data:
        print(room_id, room_obj.return_price_per_night())
    print("-----------------------------")

  

if __name__ == "__main__":
    main()
    