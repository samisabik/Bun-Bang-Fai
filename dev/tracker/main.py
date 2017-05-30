from network import LoRa
import socket
import time
import pycom

lora = LoRa(mode=LoRa.LORA, frequency=915000000, power_mode=LoRa.ALWAYS_ON, tx_power=20, bandwidth=LoRa.BW_125KHZ, sf=12, preamble=8, coding_rate=LoRa.CODING_4_8, tx_iq=False, rx_iq=False)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:

    if s.recv(64) == b'Marco':
        pycom.rgbled(0x7F007F)
        time.sleep(1)
    time.sleep(1)
    pycom.rgbled(0x0)
