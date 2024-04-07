# This file is executed on every boot (including wake-boot from deepsleep)
import gc



import connect_to_wifi
import AviationWeatherServer

wifiStat = connect_to_wifi.conNet()
AviationWeatherServer.main(wifiStat)


gc.collect()