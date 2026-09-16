readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

# Print each device's name and temperature

print("\n Task 1: List Devices ")

def list_devices(devices):
    for device in devices:
        print(f"Device: {device['name']}, Temperature: {device['temp']}°C")

list_devices(readings)

# Returning average temperatures

print("\n Task 2: Average Temperature ")

def average_temp(devices):
    total = 0
    for device in devices:
        total = total + device["temp"]

    return total / len(devices)

print(f"Average Temperature: {average_temp(readings)}°C")

# Returning the whole dictionary of the hottest device

print("\n Task 3: Hottest Device ")


def hottest(devices):
    hottest_device = devices[0]

    for device in devices:
        if device["temp"] > hottest_device["temp"]:
            hottest_device = device

    return hottest_device

print(hottest(readings))


# Take one device and return a new dictionary

print("\n Task 4: Status Object ")

def to_status(device):
    if device["online"] == True:
        status = "ok"
    else:
        status = "offline"

    return {
        "device": device["name"],
        "status": status,
        "celsius": device["temp"]
    }

print(to_status(readings[3]))

# Return a dictionary of room names to lists of device names

print("\n Task 5: Group by room ")

def by_room(devices):
    rooms = {}

    for device in devices:
        room = device["room"]

        if room not in rooms:
            rooms[room] = []

        rooms[room].append(device["name"])

    return rooms

print(by_room(readings))