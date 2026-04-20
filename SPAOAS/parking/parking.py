from datetime import datetime

class Slot:
    def __init__(self, sid, stype):
        self.id = sid
        self.type = stype   # Bike / Car / EV
        self.status = "Free"
        self.time = str(datetime.now())

    def update(self, status):
        self.status = status
        self.time = str(datetime.now())

    def display(self):
        print(self.id, self.type, self.status, self.time)


class ParkingLot:
    def __init__(self):
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)

    def view_slots(self):
        print("\nID | Type | Status | Time")
        for s in self.slots:
            s.display()

    def find(self, sid):
        for s in self.slots:
            if s.id == sid:
                return s
        return None

    def allocate(self, vtype):
        for s in self.slots:
            if s.status == "Free" and s.type.lower() == vtype.lower():
                s.update("Occupied")
                return s
        return None