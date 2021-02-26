from datetime import datetime
from Modbus import modbus_device
import TypeConversion as TC
import logging

class SMA_device(modbus_device):
    def __init__(self, ipAddress:str):
        self.serialnumber = 0
        self.susyID = 0
        self.UnitID = 1
        self.Model = 0
        self.timeZone = 0
        self.error = 0
        self.ipAddress = ipAddress
        super().__init__(ipAddress)
        self.modbus_read_all = modbus_device.read_all
        self._Init_Modbus_Registers()

        try:
            self.get_data("all")
        except Exception as e:
            logging.error("Error - Initialisation of "+self.ipAddress+" failed!, "+str(e))
        pass

    def _Init_Modbus_Registers(self):

        self.newRegister("UnitID", address=42109, length=4)
        UnitID_response = self.read("UnitID")
        self.physicalSerialNumber = TC.list_to_number([UnitID_response[0], UnitID_response[1]], signed=False)
        self.physicalSusyID = UnitID_response[2]
        self.UnitID = UnitID_response[3]
        self.UnitID = UnitID_response[3]

        self.newRegister("SUSyIDModule", address=30003, length=2, signed=False)

        self.newRegister("serialnumber", address=30057, length=2, signed=False)

        self.newRegister("NameplateSerialnumber", address=30057, length=2, signed=False)

        self.newRegister("Model", address=30053, length=2, signed=False)

        self.newRegister("FirmwareVersion", address=40063, length=2, signed=False)

        self.newRegister("timeZone", address=40003, length=2)

        self.newRegister("operationHealth", address=30201, length=2)

        self.newRegister("SpeedwireEnable", address=40157, length=2, signed=False, type_="int", unit="")

        self.read_all()
        pass

    def get_data(self, dataName):
        if dataName == "all":
            return self.read_all()
        else:
            return self.read_value(dataName)

    def read_all(self):
        data = self.modbus_read_all(self)
        interString = []
        for i in data:
            interString.append("{}: {}{}".format(*i))
        string = "\n".join(interString)
        return string

    @property
    def operationHealth(self):
        return self.get_data("operationHealth")
