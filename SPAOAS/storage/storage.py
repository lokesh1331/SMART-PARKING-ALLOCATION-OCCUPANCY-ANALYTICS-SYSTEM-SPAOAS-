import csv
from parking import Slot
from datetime import datetime

SLOT_FILE = "../data/slots.csv"
LOG_FILE = "../data/logs.csv"


def save_slots(slots):
    with open(SLOT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "type", "status", "time"])
        for s in slots:
            writer.writerow([s.id, s.type, s.status, s.time])


def load_slots():
    slots = []
    try:
        with open(SLOT_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                s = Slot(int(row["id"]), row["type"])
                s.status = row["status"]
                s.time = row["time"]
                slots.append(s)
    except:
        pass
    return slots


def log_action(sid, action):
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sid, action, str(datetime.now())])