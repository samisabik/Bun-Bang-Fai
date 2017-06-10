#!/usr/bin/env python
import pycom,os,time
from machine import UART

pycom.heartbeat(False)

uart = UART(0, 115200)
time.sleep(1)
os.dupterm(uart)
