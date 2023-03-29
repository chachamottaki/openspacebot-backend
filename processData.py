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
    print(int(data["Desk"]))    
    desk=int(data["Desk"])
    ser.write(desk.to_bytes(1, 'little'))
    pass
    
    
    

#initialize Gpio pins for Led
#led= LED(21)

#read initial data from json file
with open("data.json",'r') as f: #si data.json est situé autre part écris le chemin complet
    old_data = json.loads(f.read())

#fs ske tu veux avec old_data
while True:
    try:
        #read new data from json file
        with open("data.json",'r') as f: #si data.json est situé autre part écris le chemin complet
            data = json.loads(f.read())
        
        
        state = ser.readline().decode().strip()
        statex = json.loads(state)
            
        with open("databack.json",'r+') as f: #si data.json est situé autre part écris le chemin complet
            databack = json.load(f)
            databack["botstate"] = statex["botstate"]
            f.seek(0)
            databack["batterystate"] = statex["batterystate"]
            f.seek(1)
            json.dump(databack, f,indent=4)
            f.close()

            #print(state)
            print(statex["botstate"])
            
        
        #if data changed, process it
        if data != old_data:
            ProcessData(data)
            old_data = data
        
        
        #wait a bit before checking new data
        sleep(0.1)
    except:
        pass
#Led.close()
