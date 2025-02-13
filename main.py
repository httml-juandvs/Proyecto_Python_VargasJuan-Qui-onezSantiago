import json
from aggcampers import *
from cordinador import *


def abrirJSON():
    dicFinal={}
    with open("./campuslands.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./campuslands.json",'w') as outFile:
        json.dump(dic,outFile)
def abrirJSONt():
    dicFinal = {}
    with open('./trainers.json', "r") as openFile:
        dicFinal = json.load(openFile)
    return dicFinal

def guardarJSONt(dic):
    with open('./trainers.json', "w") as outFile:
        json.dump(dic, outFile, indent=4)
campers={}
booleanito = True
while(booleanito == True):
    print("//////////////////")
    print ("Bienvenido a Campuslands")
   
    print("2. Iniciar como Camper")
    print("3. Iniciar como Trainer")
    print("4. Iniciar como Coordinador")
    opt=int(input(":"))
    campers=abrirJSON()
    if(opt==1):
        agregarCamper()
    elif(opt==2):
        print("////////////////////")
        print("Bienvenido Camper")
        idCamper = (input("Ingrese su número de identificación: "))
        for i in range (len(campers["nuevoCamper"])):
            verificacion=campers["nuevoCamper"][i]["Numero de Identificaci\u00f3n"]
            if verificacion == idCamper:
                print("//////////////////////////////////////")
                print("Bienvenido",campers["nuevoCamper"][i]["Nombre"])
                print("Su número de identificación es: ",campers["nuevoCamper"][i]["Numero de Identificaci\u00f3n"])
                print("Su estado es: ",campers["nuevoCamper"][i]["estado"])
                print("Su riesgo es: ",campers["nuevoCamper"][i]["riesgo"])
                print("Su horario es: ",campers["nuevoCamper"][i]["horario"])
                print("Su ruta es: ",campers["nuevoCamper"][i]["ruta"])
                print("Sus notas son: ",campers["nuevoCamper"][i]["notas"])
    elif(opt==3):
        train=abrirJSONt()
        print("Bienvenido Trainer")
        idTrainer = int(input("Ingrese su número de identificación: "))
        for i in range (len(train["trainers"])):
            verificacion=train["trainers"][i]["Numero de Identificacion"]
            if verificacion == idTrainer:
                print("//////////////////////////////////////")
                print("Bienvenido",train["trainers"][i]["Nombre"])
                print("")
                print("Su número de identificación es: ",train["trainers"][i]["Numero de Identificacion"])
                print("")
                print("Su horario es: ",train["trainers"][i]["Horario"])
                print("")
    elif(opt==4):
        cordinador()   