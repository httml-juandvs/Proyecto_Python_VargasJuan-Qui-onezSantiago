import json
import json

def abrirJSON():
    dicFinal={}
    with open("./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./campers.json",'w') as outFile:
        json.dump(dic,outFile)

open=abrirJSON()
def aggcamper():
    print("Agregue el Documento de Identidad:")
    id=int(input(": "))
    print("Ingrese el Nombre :")
    nombre=int(int(": "))
    print("Agregue el Apellido:")
    ap=int(input(": "))
    print("Ingrese su Direcciòn :")
    direccion=int(int(": "))
    print("Ingrese el Nombre de su Acudiente :")
    id=int(input(": "))
    print("Ingrese su Numero de telefono:")
    nombre=int(int(": "))
    open["campers"].append({
        "id":id,
        "nombre":nombre,
        "apellido"

    })