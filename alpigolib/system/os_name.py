import platform

def osName(mode="name"):
    system = platform.system()
    release = platform.release()
    version = platform.version()

    if mode == "name":
        return system

    if mode == "withBuild":
        return f"{system} {release} ({version})"

    raise ValueError("Geçersiz mod: name | withBuild")
