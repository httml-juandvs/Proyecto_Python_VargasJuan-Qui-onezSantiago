''' 
booleanito = True
while(booleanito==True):
    print("##########################")
    print("######-Casa Inmobiliaria CajaCampus-#######")
    print("##########################")
    print("##########################")
    print("¿Qué te gustaría hacer?")
    print("1. Cambiar precio (Tener cuidado )")
    opt = int(input(":"))
    if(opt==1):
        inmuebles=abrirJSON()
'''
from datetime import datetime
import json
def abrirJSON():
    dicFinal={}
    with open("./bbdd.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./bbdd.json",'w') as outFile:
        json.dump(dic,outFile)


#Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
#Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5

def funcionPrecios():
    inmuebles={}
    inmuebles=abrirJSON()
    print("#########################")
    print("###Inmuebles Antes ##")
    print("#########################")
    for i in range(len(inmuebles["inmuebles"])):
        print("\nVivienda #",i+1)
        print("Zona:",inmuebles["inmuebles"][i]["zona"])
        print("Año de construcción:",inmuebles["inmuebles"][i]["año"])
        print("Tamaño:",inmuebles["inmuebles"][i]["metros"],"m2")
        print("Habitaciones:",inmuebles["inmuebles"][i]["habitaciones"])
        if(inmuebles["inmuebles"][i]["garaje"]==True):
            garaje=1
            print("Garaje: Disponible")
        else:
            garaje=0
            print("Garaje: No disponible")
        if(inmuebles["inmuebles"][i]["zona"]=="A"):
            current_year = datetime.now().year
            precioFinalA=((inmuebles["inmuebles"][i]["metros"]) * 1000 + (inmuebles["inmuebles"][i]["habitaciones"]) * 5000 + garaje * 15000) * (1-(current_year-inmuebles["inmuebles"][i]["año"])/100)
            inmuebles["inmuebles"][i]["precio"]=precioFinalA
        else:
            current_year = datetime.now().year
            precioFinalB=((inmuebles["inmuebles"][i]["metros"]) * 1000 + (inmuebles["inmuebles"][i]["habitaciones"]) * 5000 + garaje * 15000) * (1-(current_year-inmuebles["inmuebles"][i]["año"])/100)*1.5
            inmuebles["inmuebles"][i]["precio"]=precioFinalB
    print("\n#########################")
    print("###Inmuebles Ahora ##")
    print("#########################")
    for i in range(len(inmuebles["inmuebles"])):
        print("\nVivienda #",i+1)
        print("Zona:",inmuebles["inmuebles"][i]["zona"])
        print("Año de construcción:",inmuebles["inmuebles"][i]["año"])
        print("Tamaño:",inmuebles["inmuebles"][i]["metros"],"m2")
        print("Habitaciones:",inmuebles["inmuebles"][i]["habitaciones"])
        if(inmuebles["inmuebles"][i]["garaje"]==True):
            garaje=1
            print("Garaje: Disponible")
        else:
            garaje=0
            print("Garaje: No disponible")
        print("Precio:",inmuebles["inmuebles"][i]["precio"])
        guardarJSON(inmuebles)
    return inmuebles

inmueblesGeneral={}
inmueblesGeneral=abrirJSON()

booleanito = True
while(booleanito==True):
    print("1.Agregar inmueble")
    print("2.Arreglar Precios")
    opt=int(input(":"))
    if(opt==1):
        inmuebleNuevo={}
        zonaNuevo=input("Zona A/B:")
        inmuebleNuevo["zona"]=zonaNuevo
        anoNuevo=int(input("Año Construcción:"))
        inmuebleNuevo["año"]=anoNuevo
        metrosNuevo=int(input("Metros Construidos:"))
        inmuebleNuevo["metros"]=metrosNuevo
        habitacionesNuevo=int(input("Habitaciones:"))
        inmuebleNuevo["habitaciones"]=habitacionesNuevo
        garajeNuevo=int(input("¿Tiene garaje?(Si=1,No=0):"))
        if(garajeNuevo==1):
            garaje=1
            inmuebleNuevo["garaje"]=True
        else:
            garaje=0
            inmuebleNuevo["garaje"]=False
        if(inmuebleNuevo["zona"]=="A"):
            current_year = datetime.now().year
            precioFinalA=((inmuebleNuevo["metros"]) * 1000 + (inmuebleNuevo["habitaciones"]) * 5000 + garaje * 15000) * (1-(current_year-inmuebleNuevo["año"])/100)
            inmuebleNuevo["precio"]=precioFinalA
        else:
            current_year = datetime.now().year
            precioFinalB=((inmuebleNuevo["metros"]) * 1000 + (inmuebleNuevo["habitaciones"]) * 5000 + garaje * 15000) * (1-(current_year-inmuebleNuevo["año"])/100)*1.5
            inmuebleNuevo["precio"]=precioFinalB
        print("\n#########################")
        print("###Inmueble Nuevo ##")
        print("#########################")
        print("Zona:",inmuebleNuevo["zona"])
        print("Año de construcción:",inmuebleNuevo["año"])
        print("Tamaño:",inmuebleNuevo["metros"],"m2")
        print("Habitaciones:",inmuebleNuevo["habitaciones"])
        if(inmuebleNuevo["garaje"]==True):
            garaje=1
            print("Garaje: Disponible")
        else:
            garaje=0
            print("Garaje: No disponible")
        print("Precio:",inmuebleNuevo["precio"])
        inmueblesGeneral["inmuebles"].append(inmuebleNuevo)
        guardarJSON(inmueblesGeneral)
    if(opt==2):
        funcionPrecios()