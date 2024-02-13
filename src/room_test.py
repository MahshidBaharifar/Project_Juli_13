
from my_room import Room
def main():
    num_of_days = 10
    room_type = "S"
    room = Room(room_type, num_of_days)

    price_per_night = room.return_price_per_night()
    room_calendar = room.return_room_calendar()

    print("Price Per Night:", price_per_night)
    print("Room Calendar:")
    print(room_calendar)
    print("-----------------------------")

if __name__ == "__main__":
    main()