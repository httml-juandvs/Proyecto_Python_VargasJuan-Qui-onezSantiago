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
if "nuevoCamper" not in campers_data:
    campers_data["nuevoCamper"] = []

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
    print("Ingrese su Número de teléfono fijo , SI NO TIENE PRESIONE ENTER:")
    telefonoFijo = input(": ")
    print("Camper Registrado con éxito")
    
    campers_data["nuevoCamper"].append({
        "Numero de Identificación": id,
        "Nombre": nombre,
        "Apellidos": ap,
        "Dirección": direccion,
        "Acudiente": acu,
        "Teléfono de Celular": tel,
        "Telefono fijo(Si no tien precione enter)": telefonoFijo,
        "Nota de Admisión": "",
        'nombre': nombre,
        'apellidos': ap,
        'numeroDocumento': id,
        'direccion': direccion,
        'acudiente': acu,
        'telefonos': {
            'celular': tel,
            'fijo': telefonoFijo,
            },
        'estado':"Inscrito",
        'riesgo': False,
        'horario': '6:00 am - 10:00 pm',
        'ruta': '1. Java',
        "Nota Admision": "",
         'notas': {
            "modulo1": 0,
            "modulo2": 0,
            "modulo3": 0,
            "modulo4": 0,
            "modulo5": 0
            }
    })
    guardarJSON(campers_data)