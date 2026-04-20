from parking.parking import ParkingLot, Slot
from storage.storage import save_slots, load_slots, log_action
from analytics.analytics import stats, type_distribution
from charts.charts import show_status, show_types

lot = ParkingLot()
lot.slots = load_slots()

while True:
    print("\n--- SMART PARKING SYSTEM ---")
    print("1 Add Slot")
    print("2 View Slots")
    print("3 Update Status")
    print("4 Allocate Slot")
    print("5 Analytics")
    print("6 Charts")
    print("7 Exit")

    ch = input("Enter choice: ")

    try:
        if ch == "1":
            sid = int(input("Enter ID: "))
            stype = input("Enter Slot Type (Bike/Car/EV): ")
            lot.add_slot(Slot(sid, stype))
            print("Slot added")

        elif ch == "2":
            lot.view_slots()

        elif ch == "3":
            sid = int(input("Enter ID: "))
            s = lot.find(sid)
            if s:
                status = input("Enter Status (Free/Occupied/Reserved): ")
                s.update(status)
                log_action(sid, status)
                print("Updated")
            else:
                print("Slot not found")

        elif ch == "4":
            vtype = input("Enter Vehicle Type (Bike/Car/EV): ")
            s = lot.allocate(vtype)
            if s:
                print("Allocated Slot:", s.id)
                log_action(s.id, "Allocated")
            else:
                print("No slot available")

        elif ch == "5":
            stats(lot.slots)
            type_distribution(lot.slots)

        elif ch == "6":
            show_status(lot.slots)
            show_types(lot.slots)

        elif ch == "7":
            save_slots(lot.slots)
            print("Saved & Exit")
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)
