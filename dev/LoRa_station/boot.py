# boot.py -- run on boot-up
import os,pycom,machine,time
from network import WLAN

pycom.heartbeat(False)
wlan = WLAN()

for cycles in range(5):
    pycom.rgbled(0x00007F)
    time.sleep(0.3)
    pycom.rgbled(0x000000)
    time.sleep(0.3)

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    wlan.ifconfig(config=('192.168.1.30', '255.255.255.0', '192.168.1.1', '8.8.8.8'))

if not wlan.isconnected():
    wlan.connect('The Republic', auth=(WLAN.WPA2, 'nosciencejustrockets'), timeout=5000)
    pycom.rgbled(0x007F00)
    time.sleep(2)
    while not wlan.isconnected():
        machine.idle()
