import matplotlib.pyplot as plt

def show_status(slots):
    free = 0
    occ = 0

    for s in slots:
        if s.status == "Occupied":
            occ += 1
        else:
            free += 1

    plt.bar(["Free", "Occupied"], [free, occ])
    plt.title("Parking Status")
    plt.show()


def show_types(slots):
    data = {}

    for s in slots:
        if s.type in data:
            data[s.type] += 1
        else:
            data[s.type] = 1

    plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%")
    plt.title("Slot Types")
    plt.show()