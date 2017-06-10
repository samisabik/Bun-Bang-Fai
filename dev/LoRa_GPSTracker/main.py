#!/usr/bin/env python
import pycom,socket,time,struct
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

def GPS_UART_start():
    com = UART(1,  pins=("P3",  "P4"),  baudrate=9600)
    time.sleep(1)
    return(com)

class NMEA_Parser(object):

    def __init__(self):

        self.valid_sentence = False
        self.latitude = 0.0
        self.longitude = 0.0
        self.fix_stat = 0
        self.nmea_segments = []

    def update(self,  sentence):
        self.valid_sentence = False
        self.nmea_segments = str(sentence).split(',')

        if (self.nmea_segments[0] == "b'$GPGGA"):
            self.valid_sentence = True
            try:
                 fix_stat = int(self.nmea_segments[6])
            except ValueError:
                return False
            if fix_stat:
                try:
                    lat_string = self.nmea_segments[2]
                    lat_degs = float(lat_string[0:2])
                    lat_mins = float(lat_string[2:])
                    lat_hemi = self.nmea_segments[3]
                    lon_string = self.nmea_segments[4]
                    lon_degs = float(lon_string[0:3])
                    lon_mins = float(lon_string[3:])
                    lon_hemi = self.nmea_segments[5]
                except ValueError:
                    return False
                self.latitude = lat_degs + (lat_mins/60)
                if lat_hemi == 'S':
                    self.latitude = -self.latitude
                self.longitude = lon_degs + (lon_mins/60)
                if lon_hemi == 'W':
                    self.longitude = -self.longitude

            self.fix_stat = fix_stat
            return True

com = GPS_UART_start()

while True:
    if (com.any()):
        data = com.readline()
        if (data[0:6] == b'$GPGGA'):
            pycom.rgbled(0x7F0000)
            try:
                GPS = NMEA_Parser()
                GPS.update(data)
                datatosend = struct.pack('ii', int(GPS.latitude*100000),  int(GPS.longitude*100000))
                s.setblocking(True)
                s.send(datatosend)
                s.setblocking(False)
                print('LoRa send: {}\n'.format(datatosend))
            except:
                print ("ERROR!")
        time.sleep(0.1)
        pycom.rgbled(0x000000)
