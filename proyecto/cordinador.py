import json
def abrirJSON():
    dicFinal = {}
    with open('./campuslands.json', "r") as openFile:
        dicFinal = json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open('./campuslands.json', "w") as outFile:
        json.dump(dic, outFile, indent=4)

def abrirJSONt():
    dicFinal = {}
    with open('./trainers.json', "r") as openFile:
        dicFinal = json.load(openFile)
    return dicFinal

def guardarJSONt(dic):
    with open('./trainers.json', "w") as outFile:
        json.dump(dic, outFile, indent=4)

train=abrirJSONt()
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
    if (opc ==1):
        coordi=abrirJSON
        train=abrirJSONt
        grupo=input("Ingrese el nombre del nuevo grupo: ")
        trainer=int(input(("Ingrese el id del trainer: ")))
        print(("Ingrese el # del salòn "))
        print("1. Apolo")
        print("2. Artemis")
        print("3. Sputnik")
        salon=int(input(" :"))
        print("Ingrese el horario deseado")
        print("1. 6:00 am - 10:00 am")
        print("2. 10:00 am - 2:00 pm")
        print("3. 2:00 pm - 6:00 pm")
        print("4. 6:00 pm - 10:00 pm")
        horario=int(input(" :"))
        print(("Ingrese la ruta deseada"))
        print("1. Ruta JAVA ")
        print("2.Ruta NodeJS ")
        print("3. Ruta .Netcore")
        ruta=int(input(" :"))
        for i in range (len(train["trainers"])):
            verificacion=train["trainers"][i]["Numero de Identificacion"]
            if verificacion == trainer:
                nombretrainer=train["trainers"][i]["Nombre"]
                # apellidotrainer=train["trainers"][i]["Apelllidos"]
                # rol=train["trainers"][i]["Rol"]
        coordi["Campuslands"].append({grupo:[]})
        longitud=((len(coordi["Campuslands"])))-1
        coordi["Campuslands"][longitud][grupo].append({"trainer":[{"Numero de Identificacion":verificacion,"Nombre":nombretrainer}],"Horario":{"horario":horario},"ruta":[{"ruta":ruta}],"campers":[]})
        # coordi["Campuslands"][longitud][grupo]["trainer"].append()
        # coordi["Campuslands"][longitud][grupo]["ruta"].append()
        guardarJSON(coordi)
    elif(opc==2):
        coordi= {}
        coordi=abrirJSON

        for grupo in coordi["Campuslands"]:
            print("Grupo: ",grupo[0])
            #
    elif(opc=="5"):
        print("Ingrese el documento de estudiante")
        