#!/usr/bin/env python
import socket,time,pycom,machine
from network import LoRa

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

while True:
    data = [machine.rng() for i in range(100)]
    s.send(str(data))
    pycom.rgbled(0x7F7F7F)
    time.sleep(0.5)
    pycom.rgbled(0x0)
    time.sleep(10)
    data = ''
