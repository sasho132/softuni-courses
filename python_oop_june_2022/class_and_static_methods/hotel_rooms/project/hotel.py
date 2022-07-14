class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        searched_room = [r for r in self.rooms if room_number == r.number]
        if searched_room:
            room = searched_room[0]
            return room.take_room(people)

    def free_room(self, room_number):
        searched_room = [r for r in self.rooms if room_number == r.number]
        if searched_room:
            room = searched_room[0]
            return room.free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(free_rooms)}\n"
        result += f"Taken rooms: {', '.join(taken_rooms)}"
        return result
