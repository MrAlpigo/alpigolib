from alpigolib.system import osName, osVersion

os_name = osName("name") # It should be "name"
os_version = osVersion("public") # "public" means numbers for version like 25.2.0
os_build = osVersion("withBuild") # "withBuild" means shows the build of the os

if os_name == "Darwin": # macOS appears with "Darwin" we need to show it like macOS
    print("OS Name: " + os_name + " (known as macOS)") # We give user "Darwin" and "macOS" name
    print("Build: " + os_build) # Shows the user kernel version
    if os_version == "25.2.0": # If our app detects the code version of macOS, we give user the known name
        print("Version: 26.2 or " + os_version) # We give user the known name and code version

else: # Other OS
    print("OS Name: " + os_name)
    print("Build: " + os_version)
    print("Version: " + os_build)

#🍺 Works fine with alpigolib v0.5.0