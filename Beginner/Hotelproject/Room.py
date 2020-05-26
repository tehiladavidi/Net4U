
class Room:
    def __init__(self, base_cost, people_count, breakfast, occupied_dates=None):
        self.base_cost = base_cost
        self.people_count = people_count
        self.breakfast = breakfast
        self.occupied_dates = []

    def is_free(self):
        pass

    def reserve(self, date):
        pass


read_files():
    for file in files:
        json = [{}, {}, {}, {}]
        rooms = []
        for json_room in json:
            rooms.append(Room(json_room.cost, json_room.people_count))


people_count_choices = []
for room in rooms:
    pc = room.people_count
    if pc not in people_count_choices:
        people_count_choices.append(pc)

