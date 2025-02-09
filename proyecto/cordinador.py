import json
def abrirJSON():
    dicFinal = {}
    with open('./campers.json', "r") as openFile:
        dicFinal = json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open('./campers.json', "w") as outFile:
        json.dump(dic, outFile, indent=4)

coordi = abrirJSON()

def cordinador():
    print("//////////////////////////////")
    print("Bienvenido al Módulo de Coordinador")
    print("¿Qué desea hacer?")
    print("1. Crear un Grupo")
    print("2. Ver grupos")
    print("4. Agregar Camper")
    print("5. Subir notas de admisión")
opc=(int(input(": ")))
if (opc =="1"):
    grupo=input("Ingrese el nombre del nuevo grupo")
elif(opc=="5")
    print("Ingrese el documento de estudiante")
