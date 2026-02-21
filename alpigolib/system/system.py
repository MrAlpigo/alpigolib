# alpigolib/system/system.py
import platform
import psutil

class System:
    @staticmethod
    def osName(mode="name"):
        if mode == "name":
            return platform.system()
        if mode == "withBuild":
            return f"{platform.system()} {platform.release()}"

    @staticmethod
    def osVersion(mode="public"):
        if mode == "public":
            return platform.version()
        if mode == "build":
            return platform.release()
        if mode == "withBuild":
            return f"{platform.version()} ({platform.release()})"

    @staticmethod
    def osBattery():
        battery = psutil.sensors_battery()
        return battery.percent if battery else None
