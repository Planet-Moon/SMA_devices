from SMA_device import SMA_device

class SMA_StorageBoy(SMA_device):
    def __init__(self, ipAddress:str,port:str=""):
        """SMA Battery inverter class

        Args:
            ipAddress (str): ipAddress of battery inverter
            port (str, optional): port. Defaults to 502.
        """
        super().__init__(ipAddress,port)
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
        self.newRegister("Batteriestrom", address=30843, length=2, signed=True, type_="float", unit=" A")
        self.newRegister("AktuellerBatterieladezustand", address=30845, length=2, signed=False, type_="float", unit=" %")
        self.newRegister("AktuelleBatteriekapazitaet", address=30847, length=2, signed=False, type_="float", unit=" %")
        self.newRegister("Batterietemperatur", address=30849, length=2, signed=True, factor=0.1, type_="float", unit=" °C")
        self.newRegister("Batteriespannung", address=30851, length=2, signed=False, factor=0.01, type_="float", unit=" V")
        self.newRegister("MomentaneBatterieladung", address=31393, length=2, signed=False, type_="float", unit=" W")
        self.newRegister("MomentaneBatterieentladung", address=31395, length=2, signed=False, type_="float", unit=" W")
        self.newRegister("Batterieladung", address=31397, length=4, signed=False, type_="float", unit=" Wh")
        self.newRegister("Batterieentladung", address=31401, length=4, signed=False, type_="float", unit=" Wh")
        self.newRegister("UntereEntladegrenzeBeiEigenverbrauch", address=40073, length=2, signed=False, type_="int", unit="")
        self.newRegister("BatterieStatus", address=34659, length=2, signed=False, type_="int", unit="")
        self.newRegister("BatterieZustand", address=31391, length=2, signed=False, type_="int", unit="")
        self.newRegister("BatterieBetriebsstatus", address=30955, length=2, signed=False, type_="int", unit="")
        self.newRegister("BatterieNutzungsBereichStatus", address=31057, length=2, signed=False, type_="int", unit="")
        self.newRegister("UntereGrenzeTiefenendladungVorAbschaltung", address=40719, length=2, signed=False, type_="int", unit="")
        self.newRegister("MinimaleBreiteTiefenEntladeschutz", address=40721, length=2, signed=False, type_="int", unit="")
        self.newRegister("BreiteErhaltungBatterieladezustand", address=40725, length=2, signed=False, type_="int", unit=" %")
        self.newRegister("nomCapacity", address=40187, length=2, signed=False, type_="int", unit=" Wh")
        self.newRegister("maxChargePower", address=40189, length=2, signed=False, type_="int", unit=" W")
        self.newRegister("maxDischargePower", address=40191, length=2, signed=False, type_="int", unit=" W")
        pass

    def reboot(self):
        self.newRegister("reboot", address=40077, length=2, signed=False, type_="int", unit="")
        self.write_register("reboot", 1146)
        self.removeRegister("reboot")

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

    @property
    def Batteriestrom(self):
        return self.get_data("Batteriestrom")

    @property
    def AktuellerBatterieladezustand(self):
        return self.get_data("AktuellerBatterieladezustand")

    @property
    def AktuelleBatteriekapazitaet(self):
        return self.get_data("AktuelleBatteriekapazitaet")

    @property
    def Batterietemperatur(self):
        return self.get_data("Batterietemperatur")

    @property
    def Batteriespannung(self):
        return self.get_data("Batteriespannung")

    @property
    def MomentaneBatterieladung(self):
        return self.get_data("MomentaneBatterieladung")

    @property
    def MomentaneBatterieentladung(self):
        return self.get_data("MomentaneBatterieentladung")

    @property
    def Batterieladung(self):
        return self.get_data("Batterieladung")

    @property
    def Batterieentladung(self):
        return self.get_data("Batterieentladung")

    @property
    def BreiteErhaltungBatterieladezustand(self):
        return self.get_data("BreiteErhaltungBatterieladezustand")

    @property
    def nomCapacity(self):
        return self.get_data("nomCapacity")

    @property
    def maxChargePower(self):
        return self.get_data("maxChargePower")

    @property
    def maxDischargePower(self):
        return self.get_data("maxDischargePower")
