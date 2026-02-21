from alpigolib.logger import Logger
from alpigolib.network import Network
from alpigolib.crypto import sha256
from alpigolib.utils import Utils
from alpigolib.system import (
    osName,
    osVersion,
    osBattery,
    osCPU,
    osRAM,
    osDisk,
    osUptime,
    osJSON,
)

print(osName("name"))
print(osVersion("public"))
print(osBattery())
print(osCPU())
print(osRAM())
print(osDisk())
print(osUptime())
print(osJSON())

os_log = Logger("OS INFO")
os_number = osVersion("public")

if osName("name") == "Darwin":
    os_log.info("MacOS " + os_number)
    print('Your OS is MacOS and your MacOS version is ' + os_number)


print(Utils.random_int(16))

net = Network()
print(net.publicIP())

log = Logger("app")
log.info("Hello alpigolib")
log.warn("🍺 alpigolib v 0.6.0 is coming soon!")
log.error("An error not occured 🐍")
print(sha256("pera"))