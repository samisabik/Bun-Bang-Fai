#!/usr/bin/env python
import socket,time,pycom,machine
import struct
from network import LoRa
from machine import UART

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
    data = s.recv(256)
    if data != b'':
        pycom.rgbled(0x007F00)
        GPS_pos = struct.unpack("ii",  data)
        print(GPS_pos[0]/100000,",", GPS_pos[1]/100000)
        time.sleep(0.3)
        pycom.rgbled(0x000000)
