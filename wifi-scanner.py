import subprocess
import re
from time import sleep


def quantizer(signal):
    maxValue = -20
    minValue = -90
    quantizedScale=40
    return(int((signal-minValue)*quantizedScale/(maxValue - minValue)))

cmd = 'iwconfig'
interface = 'wlan0'
while(True):
    data = subprocess.check_output([cmd,interface])
    match  = re.search(r'-\d+',data.decode("utf-8"))
   # print(int(match.group(0)))
    print(quantizer(int(match.group(0))))
    sleep(0.2)
