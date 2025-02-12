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
    print("5. Cambiar estado de camper")
    print("6. Asignar Camper a Grupo")
    print("7. Subir notas de admisión")
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
        if ruta==1:
            rutaa="Java"
        elif ruta==2:
            rutaa="NodeJS"
        elif rutaa==3:
            rutaa=".Netcore"
        for i in range (len(train["trainers"])):
            verificacion=train["trainers"][i]["Numero de Identificacion"]
            if verificacion == trainer:
                nombretrainer=train["trainers"][i]["Nombre"]
        coordi["Campuslands"].append({grupo:[]})
        longitud=((len(coordi["Campuslands"])))-1
        coordi["Campuslands"][longitud][grupo].append({"trainer":[{"Numero de Identificacion":verificacion,"Nombre":nombretrainer}],"Horario":{"horario":horario},"ruta":[{"ruta":rutaa}],"campers":[]})
        if ruta==1:
            coordi["Campuslands"][longitud][grupo]["ruta"].append({{"Intro": 0, "Python": 0, "HTML/CSS": 0, "Scrum": 0, "Git": 0, "JavaScript": 0, "Intro Back": 0, "Intro BBDD": 0, "MySQL": 0, "Java": 0, "PostgreSQL": 0, "SpringBoot": 0}
:0})
        if ruta==2:
            coordi["Campuslands"][longitud][grupo]["ruta"].append({{"Intro": 0, "Python": 0, "HTML/CSS": 0, "Scrum": 0, "Git": 0, "JavaScript": 0, "Intro Back": 0, "Intro BBDD": 0, "MongoDB": 0, "JavaScript": 0, "MySQL": 0, "Express": 0}
})
        if ruta==3 :
            coordi["Campuslands"][longitud][grupo]["ruta"].append({{"Intro": 0, "Python": 0, "HTML/CSS": 0, "Scrum": 0, "Git": 0, "JavaScript": 0, "Intro Back": 0, "Intro BBDD": 0, "MySQL": 0, "C#": 0, "PostgreSQL": 0, ".Net Core": 0}
})
        guardarJSON(coordi)
    elif(opc==2):
        coordi= {}
        coordi=abrirJSON
        for i in range(len(coordi["Campuslands"]["p1"])):
            print("Grupo: ",coordi["Campuslands"][i])
    elif(opc==5):  
        coordi= {}
        coordi=abrirJSON
        print("Ingrese el id del camper")
        idcamper=int(input(": "))   
        print("Ingrese el estado del camper")
        print("1. Inscrito")
        print("2. Asignado")
        print("3. Aprobado")
        print("4. Cursando")    
        print("5. Graduado")
        print("6. Expulsado")
        print("7. Retirado")    
        print("8. Rehazado por prueba de ingreso")
        estado=int(input(": "))
        print(len(coordi["Campuslands"]))
        for i in range (len(coordi["Campuslands"])):
            for j in range (len(coordi["Campuslands"][i])):
                for k in range (len(coordi["Campuslands"][i][j]["campers"])):
                    if coordi["Campuslands"][i][j]["campers"][k]["Numero de Identificación"]==idcamper:
                        if estado==1:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]["Inscrito"]=True
                        elif estado==2:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]["Asignado"]=True
                        elif estado==3:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]["Aprobado"]=True
                        elif estado==4:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]["Cursando"]=True
                        elif estado==5:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]["Graduado"]=True
                        elif estado==6:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]["Expulsado"]=True
                        elif estado==7:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]["Retirado"]=True
                        elif estado==8:
                            coordi["Campuslands"][i][j]["campers"][k]["Estado"]="Rehazado por prueba de ingreso"
                        guardarJSON(coordi)
    elif(opc==6):
        coordi={}
        coordi=abrirJSON()
        print("Ingrese el id del camper")
        idcamper=int(input(": "))
        print("Ingrese el grupo al que desea asignar al camper")
        grupo=input(": ")
        for i in range (len(coordi["nuevoCamper"])):
            verificacion=coordi["nuevoCamper"][i]["Numero de Identificación"]
            verificacionnombre=coordi["nuevoCamper"][i]["Nombre"]
            verificacionapellido=coordi["nuevoCamper"][i]["Apellidos"]
            verificaciondirecion=coordi["nuevoCamper"][i]["Dirección"]
            verificacionacudiente=coordi["nuevoCamper"][i]["Acudiente"]
            verificaciontelefono=coordi["nuevoCamper"][i]["Tel\u00e9fono"]
            if idcamper==verificacion:
                for k in range (len(coordi["Campuslands"][i])):
                    if coordi["Campuslands"][k]==idcamper:
                        coordi["Campuslands"][k]["campers"].append({"Numero de Identificación":verificacion,"Nombre":verificacionnombre,"Apellidos":verificacionapellido,"Dirección":verificaciondirecion,"Acudiente":verificacionacudiente,"Tel\u00e9fono":verificaciontelefono})
                    guardarJSON(coordi)

            
    elif(opc==7):
        print("Ingrese el id del camper")
        idcamper=int(input(": "))
        print("Ingrese la nota de admisión")
        nota=int(input(": "))
        for i in range (len(coordi["Campuslands"])):
            for j in range (len(coordi["Campuslands"][i])):
                for k in range (len(coordi["Campuslands"][i][j]["campers"])):
                    if coordi["Campuslands"][i][j]["campers"][k]["Numero de Identificación"]==idcamper:
                        coordi["Campuslands"][i][j]["campers"][k]["Nota de Admisión"]=nota
                        guardarJSON(coordi)


