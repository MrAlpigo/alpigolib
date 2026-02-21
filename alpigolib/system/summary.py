from .os_name import osName
from .os_version import osVersion
from .battery import osBattery
from .cpu import osCPU
from .ram import osRAM
from .disk import osDisk
from .uptime import osUptime

def osJSON():
    return {
        "os": {
            "name": osName("name"),
            "full": osName("withBuild"),
            "version": osVersion("public"),
            "build": osVersion("build")
        },
        "battery": osBattery(),
        "cpu": osCPU(),
        "ram": osRAM(),
        "disk": osDisk(),
        "uptime": osUptime()
    }
