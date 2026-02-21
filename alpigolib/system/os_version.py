import platform

def osVersion(mode="public"):
    release = platform.release()
    version = platform.version()

    if mode == "public":
        return release

    if mode == "build":
        return version

    if mode == "withBuild":
        return f"{release} ({version})"

    raise ValueError("Geçersiz mod: public | build | withBuild")
