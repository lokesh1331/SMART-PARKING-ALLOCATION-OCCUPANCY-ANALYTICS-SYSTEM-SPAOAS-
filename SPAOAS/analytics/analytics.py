def stats(slots):
    total = len(slots)
    occupied = 0

    for s in slots:
        if s.status == "Occupied":
            occupied += 1

    free = total - occupied
    percent = (occupied / total) * 100 if total > 0 else 0

    print("\n--- Parking Stats ---")
    print("Total:", total)
    print("Occupied:", occupied)
    print("Free:", free)
    print("Occupancy %:", round(percent, 2))


def type_distribution(slots):
    data = {}

    for s in slots:
        if s.type in data:
            data[s.type] += 1
        else:
            data[s.type] = 1

    print("\n--- Slot Type Distribution ---")
    for k, v in data.items():
        print(k, ":", v)

    return data