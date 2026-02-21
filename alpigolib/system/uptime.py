import psutil
import time

def osUptime():
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)

    hours = uptime_seconds // 3600
    minutes = (uptime_seconds % 3600) // 60

    return {
        "seconds": uptime_seconds,
        "hours": hours,
        "minutes": minutes
    }
