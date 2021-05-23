from SMA_device import SMA_device

class SMA_SunnyBoy(SMA_device):
    def __init__(self, ipAddress:str):
        super().__init__(ipAddress)
        self._add_Modbus_registers()

    def _add_Modbus_registers(self):
        self.newRegister("power", address=30775, length=2, signed=True, type_="float", unit=" W")
        self.newRegister("dcwatt", address=30773, length=2, signed=True, type_="float", unit=" W")
        self.newRegister("todayEnergy", address=30535, length=2, type_="float", unit=" Wh")
        self.newRegister("LeistungEinspeisung", address=30867, length=2, signed=True, type_="float", unit=" W")
        self.newRegister("LeistungBezug", address=30865, length=2, signed=True, type_="float", unit=" W")
        self.newRegister("GesamtErtrag", address=30513, length=4, signed=False, type_="float", unit=" Wh")
        self.newRegister("ZählerstandBezugszähler", address=30581, length=2, signed=False, type_="float", unit=" Wh")
        self.newRegister("ZählerstandEinspeisezähler", address=30583, length=2, signed=False, type_="float", unit=" Wh")
        # self.modbus.read_all()
        pass

    def get_deltaPower(self):
        value = self.modbus.read_value("LeistungEinspeisung") - self.modbus.read_value("LeistungBezug")
        string = "Delta: {}{}".format(value, self.modbus.register["LeistungEinspeisung"].unit)
        return string

    def read_all(self):
        data = self.modbus_read_all(self)
        interString = []
        for i in data:
            # TODO: add to modbus register
            if i[0] == "power" and i[1] < 0:
                i[1] = 0
            if i[0] == "dcwatt" and i[1] < 0:
                i[1] = 0
            # end TODO --------------------
            interString.append("{}: {}{}".format(*i))
        string = "\n".join(interString)
        return string

    @property
    def power(self):
        value = self.get_data("power")
        if value >= 0:
            return value
        else:
            return 0

    @property
    def dcwatt(self):
        value = self.get_data("dcwatt")
        if value >= 0:
            return value
        else:
            return 0

    @property
    def todayEnergy(self):
        return self.get_data("todayEnergy")

    @property
    def LeistungEinspeisung(self):
        return self.get_data("LeistungEinspeisung")

    @property
    def LeistungBezug(self):
        return self.get_data("LeistungBezug")

    @property
    def GesamtErtrag(self):
        return self.get_data("GesamtErtrag")

    @property
    def ZaehlerstandBezugszaehler(self):
        return self.get_data("ZählerstandBezugszähler")

    @property
    def ZaehlerstandEinspeiseZaehler(self):
        return self.get_data("ZählerstandEinspeisezähler")
