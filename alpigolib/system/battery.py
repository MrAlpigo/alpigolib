import psutil

def osBattery():
    battery = psutil.sensors_battery()

    if battery is None:
        return None

    return {
        "percent": battery.percent,
        "plugged": battery.power_plugged
    }
