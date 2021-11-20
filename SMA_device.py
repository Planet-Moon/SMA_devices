from datetime import datetime
from Modbus import Modbus_device
import TypeConversion as TC
import logging

logger = logging.getLogger(__name__)


class SMA_device(Modbus_device):
    def __init__(self, ipAddress: str, port: str = "502"):
        """Generic SMA inverter class

        Args:
            ipAddress (str): ipAddress for TCP Modbus
            port (str, optional): port. Defaults to 502.
        """
        self.serialnumber:int = 0
        self.susyID:int = 0
        self.UnitID:int = 1
        self.Model:int = 0
        self.timeZone:int = 0
        self.error:int = 0
        self.ipAddress:str = ipAddress
        self.port:str = port
        super(SMA_device, self).__init__(ipAddress, port)
        self.modbus_read_all = Modbus_device.read_all
        self._Init_Modbus_Registers()

        try:
            self.get_data("all")
        except Exception as e:
            logger.error("Error - Initialisation of " +
                         self.ipAddress+" failed!, "+str(e))
        pass

    def _Init_Modbus_Registers(self):

        self.newRegister("UnitID", address=42109, length=4)
        UnitID_response = self.read("UnitID")
        self.physicalSerialNumber = TC.list_to_number(
            [UnitID_response[0], UnitID_response[1]], signed=False)
        self.physicalSusyID = UnitID_response[2]
        self.UnitID = UnitID_response[3]
        self.UnitID = UnitID_response[3]

        self.newRegister("SUSyIDModule", address=30003, length=2, signed=False)

        self.newRegister("serialnumber", address=30057, length=2, signed=False)

        self.newRegister("NameplateSerialnumber",
                         address=30057, length=2, signed=False)

        self.newRegister("Model", address=30053, length=2, signed=False)

        self.newRegister("FirmwareVersion", address=40063,
                         length=2, signed=False)

        self.newRegister("timeZone", address=40003, length=2)

        self.newRegister("operationHealth", address=30201, length=2)

        self.newRegister("SpeedwireEnable", address=40157,
                         length=2, signed=False, type_="int", unit="")

        self.read_all()
        pass

    def reboot(self):
        self.newRegister("reboot", address=40077, length=2,
                         signed=False, type_="int", unit="")
        self.write_register("reboot", 1146)
        self.removeRegister("reboot")

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
