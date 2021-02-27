from SMA_SunnyBoy import SMA_SunnyBoy
from SMA_StorageBoy import SMA_StorageBoy
from Modbus import modbus_device

if __name__ == "__main__":
    storageBoy = SMA_StorageBoy("192.168.178.113")
    sunnyBoy = SMA_SunnyBoy("192.168.178.128")
    sunnyBoy.newRegister("LänderNorm", address=41121, length=2, signed=False, type_="int", unit="")
    a = sunnyBoy.read_value("LänderNorm")
    print("LänderNorm: {}".format(a))

    testDevice = modbus_device("192.168.178.107")
    if not testDevice.newRegister("TestRegister",125,2):
        raise Exception("ahhhh")
    testDevice.write_register("TestRegister",2**20-1)
    pass
