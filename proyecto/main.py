import json

def abrirJSON():
    dicFinal={}
    with open("./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./campers.json",'w') as outFile:
        json.dump(dic,outFile)

campers={}
booleanito = True
while(booleanito == True):
    print ("Bienvenido a Campuslands")
    print("1. Para inscribirse")
    print("2. Iniciar como Camper")
    print("3. Iniciar como Trainer")
    print("4. Iniciar como Coordinador")
    opt=input(":")
campers=abrirJSON()
if(opt=="1"):
    print("Ingrese el documento de identidad: "
          )