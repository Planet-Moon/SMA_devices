from SMA_StorageBoy import SMA_StorageBoy, Battery_manager

def main():
    sma_StorageBoy = SMA_StorageBoy("192.168.178.113")
    print("power: {}".format(sma_StorageBoy.power))
    print("dcwatt: {}".format(sma_StorageBoy.dcwatt))
    print("todayEnergy: {}".format(sma_StorageBoy.todayEnergy))
    print("LeistungEinspeisung: {}".format(sma_StorageBoy.LeistungEinspeisung))
    print("LeistungBezug: {}".format(sma_StorageBoy.LeistungBezug))
    print("GesamtErtrag: {}".format(sma_StorageBoy.GesamtErtrag))
    print("ZaehlerstandBezugszaehler: {}".format(sma_StorageBoy.ZaehlerstandBezugszaehler))
    print("ZaehlerstandEinspeiseZaehler: {}".format(sma_StorageBoy.ZaehlerstandEinspeiseZaehler))
    print("Batteriestrom: {}".format(sma_StorageBoy.Batteriestrom))
    print("soc: {}".format(sma_StorageBoy.soc))
    print("AktuelleBatteriekapazitaet: {}".format(sma_StorageBoy.AktuelleBatteriekapazitaet))
    print("Batterietemperatur: {}".format(sma_StorageBoy.Batterietemperatur))
    print("Batteriespannung: {}".format(sma_StorageBoy.Batteriespannung))
    print("MomentaneBatterieladung: {}".format(sma_StorageBoy.MomentaneBatterieladung))
    print("MomentaneBatterieentladung: {}".format(sma_StorageBoy.MomentaneBatterieentladung))
    print("present_charge: {}".format(sma_StorageBoy.present_charge))
    print("present_discharge: {}".format(sma_StorageBoy.present_discharge))
    print("BreiteErhaltungBatterieladezustand: {}".format(sma_StorageBoy.BreiteErhaltungBatterieladezustand))

    print("nomCapacity: {}".format(sma_StorageBoy.nomCapacity))
    print("maxChargePower: {}".format(sma_StorageBoy.maxChargePower))
    print("maxDischargePower: {}".format(sma_StorageBoy.maxDischargePower))

    battery_manager = Battery_manager(inverters=[sma_StorageBoy])
    print("soc: "+str(battery_manager.soc))

if __name__ == "__main__":
    main()
