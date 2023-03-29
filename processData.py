import json
from time import sleep
from gpiozero import LED
import time
import serial
ser = serial.Serial(
        port='/dev/ttyUSB0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 115200,
       # parity=serial.PARITY_NONE,
       # stopbits=serial.STOPBITS_ONE,
       # bytesize=serial.EIGHTBITS,
        timeout=1
)


def ProcessData(data):
    #Code pour alummer led ou ske tu veux selon data 
    # pour linstant il n'ya que Led1 et Led2 dans data
    # tu modifies api pour ajouter ou supprimer
    # et tu fais ske tu veux en les utilisant ici
    print(data)
    if int(data["Led"])==1:
        #allumer led
        #led.on()
        msj=1
        ser.write(msj.to_bytes(1, 'little'))
        pass
    else:
        #éteindre led
        #led.off()
        msj=0
        ser.write(msj.to_bytes(1, 'little'))
        pass

#initialize Gpio pins for Led
led= LED(21)

#read initial data from json file
with open("data.json",'r') as f: #si data.json est situé autre part écris le chemin complet
    old_data = json.loads(f.read())

#fs ske tu veux avec old_data
while True:
    try:
        #read new data from json file
        with open("data.json",'r') as f: #si data.json est situé autre part écris le chemin complet
            data = json.loads(f.read())

        #if data changed, process it
        if data != old_data:
            ProcessData(data)
            old_data = data
        #wait a bit before checking new data
        sleep(0.1)
    except:
        pass
Led.close()
