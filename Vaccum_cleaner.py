class VacuumCleaner:
    def __init__(self, rooms):
        self.rooms = rooms
        self.position = 0

    def move_right(self):
        if self.position < len(self.rooms) - 1:
            self.position += 1
            print(f"Moved to room {self.position + 1}")

    def move_left(self):
        if self.position > 0:
            self.position -= 1
            print(f"Moved to room {self.position + 1}")

    def clean(self):
        if self.rooms[self.position] == "Dirty":
            self.rooms[self.position] = "Clean"
            print(f"Room {self.position + 1} cleaned!")
        else:
            print(f"Room {self.position + 1} is already clean.")

    def show_rooms(self):
        print("Rooms:", self.rooms)


# Create rooms
rooms = ["Dirty", "Clean", "Dirty", "Dirty", "Clean"]

vacuum = VacuumCleaner(rooms)

vacuum.show_rooms()

# Clean all rooms
for i in range(len(rooms)):
    vacuum.clean()