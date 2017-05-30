# boot.py -- run on boot-up
import os,pycom,time
from machine import UART

uart = UART(0, 115200)
os.dupterm(uart)

pycom.heartbeat(False)

for cycles in range(5):
    pycom.rgbled(0x00007F)
    time.sleep(0.3)
    pycom.rgbled(0x000000)
    time.sleep(0.3)
