import json
def abrirJSON():
    dicFinal = {}
    with open('./campers.json', "r") as openFile:
        dicFinal = json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open('./campers.json', "w") as outFile:
        json.dump(dic, outFile, indent=4)

campers_data = abrirJSON()

def agregarCamper():
    print("Agregue el Documento de Identidad:")
    id = (input(": "))
    print("Ingrese el Nombre:")
    nombre = input(": ")
    print("Agregue el Apellido:")
    ap = input(": ")
    print("Ingrese su Dirección:")
    direccion = input(": ")
    print("Ingrese el Nombre de su Acudiente:")
    acu = input(": ")
    print("Ingrese su Número de teléfono:")
    tel = input(": ")
    print("Camper Registrado con éxito")
    
    campers_data["nuevoCamper"].append({
        "Numero de Identificación": id,
        "Nombre": nombre,
        "Apellidos": ap,
        "Dirección": direccion,
        "Acudiente": acu,
        "Teléfono": tel  
    })
    guardarJSON(campers_data)