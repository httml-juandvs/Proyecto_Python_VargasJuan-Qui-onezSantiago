import json
def abrirJSON():
    with open('./campuslands.json', "r") as openFile:
        return json.load(openFile)

def guardarJSON(dic):
    with open('./campuslands.json', "w") as outFile:
        json.dump(dic, outFile, indent=4)

def abrirJSONt():
    with open('./trainers.json', "r") as openFile:
        return json.load(openFile)

def guardarJSONt(dic):
    with open('./trainers.json', "w") as outFile:
        json.dump(dic, outFile, indent=4)

def cordinador():
    while True:
        print("//////////////////////////////")
        print("Bienvenido al Módulo de Coordinador")
        print("¿Qué desea hacer?")
        print("1. Crear un Grupo")
        print("2. Editar grupos")
        print("3. Cambiar estado del camper")
        print("4. Agregar Camper")
        print("5. Asignar camper a grupo")
        print("6. Subir notas de admisión")
        print("7. Cambiar el estado del Camper")
        print("7. Ver todos los trainers")
        print("8. Salir")

        opc = int(input(": "))
        coordi = abrirJSON()
        train = abrirJSONt()

        if opc == 1:  # Crear un nuevo grupo
            grupo = input("Ingrese el nombre del nuevo grupo: ")
            trainer = int(input("Ingrese el ID del trainer: "))
            
            print("Ingrese el # del salón:")
            print("1. Apolo")
            print("2. Artemis")
            print("3. Sputnik")
            salon = int(input(": "))

            print("Ingrese el horario deseado:")
            print("1. 6:00 am - 10:00 am")
            print("2. 10:00 am - 2:00 pm")
            print("3. 2:00 pm - 6:00 pm")
            print("4. 6:00 pm - 10:00 pm")
            horario = int(input(": "))

            print("Ingrese la ruta deseada:")
            print("1. Ruta JAVA")
            print("2. Ruta NodeJS")
            print("3. Ruta .Netcore")
            ruta = int(input(": "))

            nombretrainer = None
            for i in range(len(train["trainers"])):
                if train["trainers"][i]["Numero de Identificacion"] == trainer:
                    nombretrainer = train["trainers"][i]["Nombre"]
                    break

            if nombretrainer:
                if "Campuslands" not in coordi:
                    coordi["Campuslands"] = {}
                if grupo not in coordi["Campuslands"]:
                    coordi["Campuslands"][grupo] = {
                        "trainer": [{"Numero de Identificacion": trainer, "Nombre": nombretrainer}],
                        "Horario": {"horario": horario},
                        "ruta": [{"ruta": ruta}],
                        "campers": []  # Lista de IDs de campers en este grupo
                    }
                guardarJSON(coordi)
                print(f"Grupo {grupo} creado con éxito.")
            else:
                print("Trainer no encontrado.")

        elif opc == 2:  # Editar un grupo existente
            grupo = input("Ingrese el nombre del grupo: ")
            if grupo in coordi.get("Campuslands", {}):
                print("/////////////////////")
                print("Grupo: ", grupo)
                print("Trainer: ", coordi["Campuslands"][grupo]["trainer"][0]["Nombre"])
                print("Horario: ", coordi["Campuslands"][grupo]["Horario"]["horario"])
                print("Ruta: ", coordi["Campuslands"][grupo]["ruta"][0]["ruta"])
                print("Campers: ", coordi["Campuslands"][grupo]["campers"])
                print("/////////////////////")
                print("¿Qué desea hacer?")
                print("1. Editar Trainer")
                print("2. Editar Horario")
                print("3. Editar Ruta")
                print("4. Agregar Camper al grupo")
                print("5. Eliminar Camper del grupo")
                print("6. Eliminar Grupo")

                opc2 = int(input(": "))
                if opc2 == 1:  # Editar Trainer
                    trainer = int(input("Ingrese el nuevo ID del trainer: "))
                    nombretrainer = None
                    for i in range(len(train["trainers"])):
                        if train["trainers"][i]["Numero de Identificacion"] == trainer:
                            nombretrainer = train["trainers"][i]["Nombre"]
                            break
                    if nombretrainer:
                        coordi["Campuslands"][grupo]["trainer"][0]["Numero de Identificacion"] = trainer
                        coordi["Campuslands"][grupo]["trainer"][0]["Nombre"] = nombretrainer
                        guardarJSON(coordi)
                        print(f"Trainer del grupo {grupo} actualizado con éxito.")
                    else:
                        print("Trainer no encontrado.")

                elif opc2 == 2:  # Editar Horario
                    print("Ingrese el nuevo horario:")
                    print("1. 6:00 am - 10:00 am")
                    print("2. 10:00 am - 2:00 pm")
                    print("3. 2:00 pm - 6:00 pm")
                    print("4. 6:00 pm - 10:00 pm")
                    horario = int(input(": "))
                    coordi["Campuslands"][grupo]["Horario"]["horario"] = horario
                    guardarJSON(coordi)
                    print(f"Horario del grupo {grupo} actualizado con éxito.")

                elif opc2 == 3:  # Editar Ruta
                    print("Ingrese la nueva ruta:")
                    print("1. Ruta JAVA")
                    print("2. Ruta NodeJS")
                    print("3. Ruta .Netcore")
                    ruta = int(input(": "))
                    coordi["Campuslands"][grupo]["ruta"][0]["ruta"] = ruta
                    guardarJSON(coordi)
                    print(f"Ruta del grupo {grupo} actualizada con éxito.")

                elif opc2 == 4:  # Agregar Camper
                    documento = input("Ingrese el documento del camper: ")
                    if documento in coordi.get("Campuslands", {}).get("campers", {}):
                        if documento not in coordi["Campuslands"][grupo]["campers"]:
                            coordi["Campuslands"][grupo]["campers"].append(documento)
                            guardarJSON(coordi)
                            print(f"Camper {documento} agregado al grupo {grupo}.")
                        else:
                            print("El camper ya está en este grupo.")
                    else:
                        print("Camper no encontrado.")

                elif opc2 == 5:  # Eliminar Camper del grupo
                    documento = input("Ingrese el documento del camper: ")
                    if documento in coordi["Campuslands"][grupo]["campers"]:
                        coordi["Campuslands"][grupo]["campers"].remove(documento)
                        guardarJSON(coordi)
                        print(f"Camper {documento} eliminado del grupo {grupo}.")
                    else:
                        print("Camper no encontrado en este grupo.")

                elif opc2 == 6:  # Eliminar Grupo
                    del coordi["Campuslands"][grupo]
                    guardarJSON(coordi)
                    print(f"Grupo {grupo} eliminado con éxito.")
            else:
                print("Grupo no encontrado.")

        elif opc == 3:  # Cambiar el estado de un camper
            documento = input("Ingrese el documento del estudiante: ")
            nuevo_estado = input("Ingrese el nuevo estado del camper: ")

            if documento in coordi.get("Campuslands", {}).get("campers", {}):
                coordi["Campuslands"]["campers"][documento]["estado"] = nuevo_estado
                guardarJSON(coordi)
                print(f"Estado del camper {documento} actualizado a {nuevo_estado}.")
            else:
                print("Camper no encontrado.")

        elif opc == 4:  # Agregar Camper
            from aggcampers import agregarCamper
            agregarCamper()

        elif opc == 5:  # Asignar camper a un grupo
            documento = input("Ingrese el documento del estudiante: ")
            grupo = input("Ingrese el grupo al que desea asignar al camper: ")
            camper_data = 0
            for camper in coordi["nuevoCamper"]:
                if camper["Numero de Identificaci\u00f3n"] == documento:
                    camper_data = camper
                    break
            if camper_data:
                if documento in coordi["Campuslands"][grupo]["campers"]:
                    print("El camper ya está en este grupo.")
                else:
                    coordi["Campuslands"][grupo]["campers"].append({
                        "Numero de Identificacion": documento,
                        "Nombre": camper_data["Nombre"],
                        "Apellidos": camper_data["Apellidos"],
                        "Estado": camper_data["estado"],
                        "Riesgo": camper_data["riesgo"],
                        "Horario": camper_data["horario"],
                        "Ruta": camper_data["ruta"],
                        "Notas": camper_data["notas"]
                    })
                    guardarJSON(coordi)
                    print(f"Camper {documento} asignado al grupo {grupo}.")
            else:
                print("Camper no encontrado.")
                        
        elif opc == 6:  # Subir notas de admisión
            documento = input("Ingrese el documento del estudiante: ")
            notasAdmin = input("Ingrese las notas de admisión: ")
            camper_encontrado = False
            for camper in coordi["nuevoCamper"]:
                if camper["Numero de Identificaci\u00f3n"] == documento:
                    camper["Nota de Admisi\u00f3n"] = notasAdmin
                    camper_encontrado = True
                    break
            if camper_encontrado:
                guardarJSON(coordi)
                print(f"Notas del camper {documento} actualizadas con éxito.")
            else:
                print("Camper no encontrado.")

        elif opc == 7: #Cambiar el estado del Camper
            documento = input("Ingrese el documento del estudiante: ")
            nuevo_estado = input("Ingrese el nuevo estado del camper: ")
            for camper in coordi["nuevoCamper"]:
                if camper["Numero de Identificaci\u00f3n"] == documento:
                    camper["estado"] = nuevo_estado
                    guardarJSON(coordi)
                    print(f"Estado del camper {documento} actualizado a {nuevo_estado}.")
                    break
            else:
                print("Camper no encontrado")

        elif opc == 8:  # Ver todos los trainers
            for trainer in train["trainers"]:
                print("/////////////////////")
                print("Nombre: ", trainer["Nombre"])
                print("Apellidos: ", trainer["Apellidos"])
                print("Documento: ", trainer["Numero de Identificacion"])
                print("Horario: ", trainer["Horario"])
                print("Rol: ", trainer["Rol"])

        elif opc == 8:  # Salir
            print("Saliendo del módulo de coordinador...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")