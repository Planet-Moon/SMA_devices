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

class Battery_manager:
    supported_inverters = (SMA_StorageBoy) # add supported_inverters here
    def __init__(self, inverters:list=[]) -> None:
        self._inverters = []
        for i in inverters:
            self.addInverter(i)

        # test if all are working
        self.power
        self.soc
        self.present_discharge
        self.present_charge
        self.charge
        self.total_capacity
        self.charge_missing

    @property
    def inverters(self) -> list:
        return self._inverters

    def addInverter(self, inverter) -> None:
        """Add inverter to BatteryManager

        Args:
            inverter (self.supported_inverters): Any inverter type in supported_inverters

        Raises:
            TypeError: When inverter is not in the tuple of supported inverters
        """
        if isinstance(inverter,self.supported_inverters):
            class InverterModel:
                def __init__(self,inverter,needed_power=0,available_power=0):
                    self.device = inverter
                    self.needed_power = needed_power
                    self.available_power = available_power

            self._inverters.append(InverterModel(inverter))
        else:
            raise TypeError("Inverter not supported")

    @property
    def power(self) -> int:
        """Calculate the power needed or available

        Returns:
            int: power needed (<0) or available (>0) (W)
        """
        needed_power = 0
        available_power = 0
        for i in self._inverters:
            if i.device.AktuellerBatterieladezustand < 65:
                i.needed_power = i.device.maxChargePower
                i.available_power = 0
            if i.device.AktuellerBatterieladezustand > 85:
                i.needed_power = 0
                i.available_power = i.device.maxDischargePower
            needed_power += i.needed_power
            available_power += i.available_power
        if needed_power > 0:
            return needed_power *-1
        else:
            return available_power

    @property
    def soc(self) -> float:
        """Mean state of charge

        Returns:
            float: Mean state of charge (%)
        """
        _soc = 0
        for i in self._inverters:
            _soc += i.device.AktuellerBatterieladezustand
        return _soc/len(self._inverters)

    @property
    def present_discharge(self) -> int:
        """Present amount of power being discharged

        Returns:
            int: discharging power (W)
        """
        _present_discharge = 0
        for i in self._inverters:
            _present_discharge += i.device.Batterieentladung
        return _present_discharge

    @property
    def present_charge(self) -> int:
        """Present amount of power being charged

        Returns:
            int: charging power (W)
        """
        _present_charge = 0
        for i in self._inverters:
            _present_charge += i.device.Batterieladung  # ! BUG
        return _present_charge

    @property
    def charge(self) -> int:
        """Charged energy in the batteries

        Returns:
            int: charged energy (Wh)
        """
        _charge = 0
        for i in self._inverters:
            _charge += i.device.Batterieladung # ! BUG
        return _charge

    @property
    def total_capacity(self) -> int:
        """Total nominal capacity of all batteries

        Returns:
            int: Nominal capacity of all batteries (Wh)
        """
        _cap = 0
        for i in self._inverters:
            _cap += i.device.nomCapacity
        return _cap

    @property
    def charge_missing(self) -> int:
        """Total charge missing until batteries are full

        Returns:
            int: charge missing (Wh)
        """
        _charge_missing = 0
        for i in self._inverters:
            _charge_missing += i.device.nomCapacity - i.device.Batterieladung  # ! BUG
        return _charge_missing
