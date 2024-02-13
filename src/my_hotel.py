from my_room import Room

class Hotel:
    def __init__(self, name, num_s_rooms, num_d_rooms, num_e_rooms, num_days):
        self.name = name
        self.rooms_data = []

        for i in range(1, num_s_rooms + 1):
            room_ID = f"{i}s"
            new_room = Room('S', num_days)
            self.rooms_data.append((room_ID, new_room))

        for i in range(1, num_d_rooms + 1):
            room_ID = f"{i}D"
            new_room = Room('D', num_days)
            self.rooms_data.append((room_ID, new_room))

        for i in range(1, num_e_rooms + 1):
            room_ID = f"{i}E"
            new_room = Room('E', num_days)
            self.rooms_data.append((room_ID, new_room))

    def get_hotel_name(self):
        return self.name

    def get_rooms_data(self):
        return self.rooms_data

    def find_specific_room(self, specific_ID):
        for item in self.rooms_data:
            if item[0] == specific_ID:
                return item[1]
        return None

    def display_rooms_of_type(self, room_type):
        return [item[1] for item in self.rooms_data if item[0][-1] == room_type]

    def available_type_rooms(self, room_type, checkin_date, checkout_date):
        available_rooms = []
        for item in self.display_rooms_of_type(room_type):
            if item.is_room_available(checkin_date, checkout_date):
                available_rooms.append(item)
        return available_rooms
    
    def available_rooms(self, checkin_date, checkout_date):
        available_rooms = []
        for item in self.rooms_data:
            if item[1].is_room_available(checkin_date, checkout_date):
                available_rooms.append(item[1])
        return available_rooms

    def is_hotel_booked(self, checkin_date, checkout_date):
        return all(item[1].is_fully_unavailable(checkin_date, checkout_date) for item in self.rooms_data)
