import json
from time import sleep
from gpiozero import LED


def ProcessData(data):
    #Code pour alummer led ou ske tu veux selon data 
    # pour linstant il n'ya que Led1 et Led2 dans data
    # tu modifies api pour ajouter ou supprimer
    # et tu fais ske tu veux en les utilisant ici
    print(data)
    if int(data["Led"])==1:
        #allumer led
        led.on()
        pass
    else:
        #éteindre led
        led.off()
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
