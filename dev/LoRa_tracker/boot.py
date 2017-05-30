#!/usr/bin/env python
import pycom,machine,time
from network import WLAN

pycom.heartbeat(False)
wlan = WLAN()

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)
    wlan.ifconfig(config=('192.168.1.40', '255.255.255.0', '192.168.1.1', '8.8.8.8'))

if not wlan.isconnected():
    wlan.connect('The Republic', auth=(WLAN.WPA2, 'nosciencejustrockets'), timeout=5000)
    for cycles in range(5):
        pycom.rgbled(0x00007F)
        time.sleep(0.3)
        pycom.rgbled(0x000000)
        time.sleep(0.3)
    time.sleep(2)
    while not wlan.isconnected():
        pycom.rgbled(0x7F0000)
        machine.idle()
