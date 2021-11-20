from SMA_SunnyBoy import SMA_SunnyBoy

sma_SunnyBoy = SMA_SunnyBoy(ipAddress="192.168.178.128",name="testSunnyBoy")
sma_SunnyBoy.get_deltaPower()
print(sma_SunnyBoy.read_all())
