import time
import webrepl
import network
import sys

def conNet():


    ssid = 'SSID'
    password = "PASSWORD"

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)


    start_time = time.time()

    while station.isconnected() == False:
        if (time.time() - start_time) >30:

            time.sleep(1)
            return False

        pass

    print('Connection successful')
    print(station.ifconfig())
    webrepl.start()
    time.sleep(1)
    return True