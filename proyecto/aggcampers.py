import json
def abrirJSON():
    dicFinal = {}
    with open('./campuslands.json', "r") as openFile:
        dicFinal = json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open('./campuslands.json', "w") as outFile:
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
    
    fijo = input("Telefono fijo(Si no tien precione enter):")  # Define the variable "fijo"
    
    campers_data["nuevoCamper"].append({
        "Numero de Identificación": id,
        "Nombre": nombre,
        "Apellidos": ap,
        "Dirección": direccion,
        "Acudiente": acu,
        "Teléfono de Celular": tel,
        "Telefono fijo(Si no tien precione enter)": fijo,
        "Notas de Admisión": "",
        "Estado": ""
    })
    guardarJSON(campers_data)