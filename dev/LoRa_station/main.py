#!/usr/bin/env python
import socket,time,pycom,os
from machine import UART
from network import LoRa

print (" - Base Station Receiver")

uart = UART(0, 115200)
os.dupterm(uart)
print (" - Serial starting at 115200bps")

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
print (" - LoRa network starting at 915MHz")

while True:
    data = s.recv(64)
    if data:
        print (" - LoRa RX : " + str(data))
        pycom.rgbled(0x7F0000)
        time.sleep(0.5)
        pycom.rgbled(0x000000)
