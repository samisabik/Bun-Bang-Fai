#!/usr/bin/env python
import socket,time,pycom
from network import LoRa
a = 0
lora = LoRa(
    mode=LoRa.LORA,
    frequency=915000000,
    power_mode=LoRa.ALWAYS_ON,
    tx_power=20,
    bandwidth=LoRa.BW_125KHZ,
    sf=12,
    preamble=8,
    coding_rate=LoRa.CODING_4_8,
    tx_iq=False,
    rx_iq=False
)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
print (" - Base Station Receiver")
print (" - LoRa network starting at 915MHz")


while True:

    s.send('Marco')
    print ("[OK] Marco : " + str(a) + "s")
    pycom.rgbled(0x7F7F7F)
    time.sleep(0.5)
    pycom.rgbled(0x0)
    time.sleep(10)
    a = a + 10
