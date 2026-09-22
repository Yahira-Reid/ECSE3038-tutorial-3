from fastapi import FastAPI, HTTPException

app = FastAPI()

#task 0: setup
readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]


def average_temp(devices):
    total = 0
    for device in devices:
        total = total + device["temp"]

    return total / len(devices)


def hottest(devices):
    hottest_device = devices[0]

    for device in devices:
        if device["temp"] > hottest_device["temp"]:
            hottest_device = device

    return hottest_device

# task 1: all devices
@app.get("/devices")
def get_devices():
    return readings

# task 2: hottest
@app.get("/devices/hottest")
def get_hottest():
    return hottest(readings)

#task 3: online
@app.get("/devices/online")
def get_online_devices():
    online_devices = []
    for device in readings:
        if device["online"]:
            online_devices.append(device)
    return online_devices

# task 4: one device
@app.get("/devices/{name}")
def get_device(name: str):
    for device in readings:
        if device["name"] == name:
            return device

    raise HTTPException(status_code=404, detail=f"No device called {name}")

#task 5: stats
@app.get("/stats")
def get_stats():
    return {"average_temperature": round(average_temp(readings), 2)}


#task 6: create device
@app.post("/devices", status_code=201)
def create_device(device: dict):
    readings.append(device)
    return device

#task 7: device in room
@app.get("/rooms/{room}/devices")
def get_devices_in_room(room: str):
    devices_in_room = []
    for device in readings:
        if device["room"] == room:
            devices_in_room.append(device)

    if not devices_in_room:
        raise HTTPException(status_code=404, detail=f"No room called {room}")

    return devices_in_room