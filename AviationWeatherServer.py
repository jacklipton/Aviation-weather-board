







import network
import urequests as requests
import machine, neopixel
import json
import time
import sys
import esp

np = neopixel.NeoPixel(machine.Pin(14),50)

def turnOff():
  for i in range(50):
    np[i] = (0,0,0)
    np.write()

def turnOn(clr):

  ltOrder = [1,4,7,8,14,17,19,21,26,31,32,35,36,38,41,44,48]
  for i in range(len(ltOrder)):
    if clr == "green":
      np[ltOrder[i]] = (25,0,0)
      np.write()
    elif clr == "red":
      np[ltOrder[i]] = (0,25,0)
      np.write()


def conNet():
  esp.osdebug(None)

  ssid = '23Bev'
  password = "bunchajews"

  station = network.WLAN(network.STA_IF)

  station.active(True)
  station.connect(ssid, password)


  start_time = time.time()

  while station.isconnected() == False:
    if (time.time() - start_time) >30:
      turnOn("red")
      time.sleep(1)
      turnOff()
      sys.exit()


    pass

  print('Connection successful')
  print(station.ifconfig())
  turnOn("green")
  time.sleep(1)
  turnOff()


def removeLet(CC):
    alphabet ="QWERTYUIOPASDFGHJKLZXCVBNM"
    for letter in alphabet:
        if letter in CC:
            CC = CC.replace(letter,'')
    return(CC)

def colours(fr,ltNum):
  if fr == 'VFR':
    np[ltNum] = (20,0,0)
  elif fr == 'MVFR':
    np[ltNum] = (0,0,35)
  elif fr == 'IFR':
    np[ltNum] = (0,25,0)
  elif fr == 'LIFR':
    np[ltNum] = (0,25,25)
  np.write()



def AvWeather():

  airports = "KOGS,KMSS,CYOW,CYND,CYGK,CYTR,CYPQ,CYOO,CYQA,CYTZ,CYYZ,CYSN,KIAG,KBUF,CYHM,CYKF,CYXU"

  ltOrder = [14,41,44,8,21,7,19,26,35,17,31,48,32,38,36,4,1]
  #colAdd = np.empty(len(airports))
  #status = np.column_stack([airports, colAdd])
  #skyCond = ["SKC", "CLR","FEW", "SCT", "BKN", "OVC","VV"]
  i = 0

  print("test")
  hdr = {"X-API-Key": "e99ef131b8f04bc9853ddaed7f"}
  r = requests.request("GET","https://api.checkwx.com/metar/"+ airports, headers=hdr)

  cyData = json.loads(r.text)['data']


  for cy in cyData:
    metarParts = cy.split(" ")
    for part in metarParts:

      if 'SM' in part:
        if '/' in part:
          vis = 1
        elif int(part[:-2])>= 5:
          vis = 4
        elif int(part[:-2])>= 3 and int(part[:-2])< 5:
          vis = 3
        elif int(part[:-2])>= 1 and int(part[:-2])< 3:
          vis = 2
        else:
          vis = 1
      if "SKC" in part or "FEW" in part or "SCT" in part or "BKN" in part or "OVC" in part or "VV0" in part or "CLR" in part:
        if "BKN" in part or "OVC" in part or "VV" in part:
          if int(removeLet(part)) > 30:
            cloud = 4
          elif int(removeLet(part)) > 10 and int(removeLet(part))<=30:
            cloud = 3
          elif int(removeLet(part)) > 5 and int(removeLet(part))<=10:
            cloud = 2
          elif int(removeLet(part)) < 5:
            cloud = 1
          break
        else:
          cloud = 4

    if cloud == 4 and vis == 4:
      print("VFR")
      colours("VFR",ltOrder[i])
    else:
      if min(cloud,vis) == 3:
        print("MVFR")
        colours("MVFR",ltOrder[i])
      elif min(cloud,vis) == 2:
        print("IFR")
        colours("IFR",ltOrder[i])
      elif min(cloud,vis) == 1:
        print("LIFR")
        colours("LIFR",ltOrder[i])

    print(cy)
    i=i+1


def main():

  conNet()
  while True:
    AvWeather()
    time.sleep(900)


main()






