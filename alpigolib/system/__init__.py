from .os_name import osName
from .os_version import osVersion
from .battery import osBattery
from .cpu import osCPU
from .ram import osRAM
from .disk import osDisk
from .uptime import osUptime
from .summary import osJSON

__all__ = [
    "osName",
    "osVersion",
    "osBattery",
    "osCPU",
    "osRAM",
    "osDisk",
    "osUptime",
    "osJSON",
]
