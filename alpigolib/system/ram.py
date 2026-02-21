import psutil

def osRAM():
    ram = psutil.virtual_memory()
    return {
        "total_gb": round(ram.total / (1024 ** 3), 2),
        "used_gb": round(ram.used / (1024 ** 3), 2),
        "free_gb": round(ram.available / (1024 ** 3), 2),
        "percent": ram.percent
    }
