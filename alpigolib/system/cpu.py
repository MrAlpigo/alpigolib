import psutil
import platform

def osCPU():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "usage_percent": psutil.cpu_percent(interval=0.5),
        "architecture": platform.machine(),
        "processor": platform.processor()
    }
