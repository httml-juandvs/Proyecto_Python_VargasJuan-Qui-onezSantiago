import json
from aggcampers import *


def abrirJSON():
    dicFinal={}
    with open("./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./campers.json",'w') as outFile:
        json.dump(dic,outFile)

p1={}
trainers= abrirJSON()
def trainers():
    print("//////////////////////////")
    print("Bienvenido a Trainers")
    print("Ingrese su curso para acceder")
    opt=(int(input(": ")))
    if (opt=="p1"):
        print("Bienvenido Pedro")
        print("Agregue el Documento de Identidad:")
        sk1 = int(input(": "))
        trainers["p1"]["trainers"]["campers"].append({
        "Notas Skill1": sk1      
    })
    else:
        (opt=="m2")
        print("Bienvenido Miguel")


guardarJSON(trainers)