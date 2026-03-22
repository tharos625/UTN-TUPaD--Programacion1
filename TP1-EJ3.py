#  TP1-EJ3.py
#

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

print("Agenda de Turnos con Nombres")
operador = input("Nombre del Operador: ")
while not operador.isalpha():
    operador = input("Nombre del Operador: ")

while True:

    print("\n1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema\n")

    opcion = input("Opción: ")
    while not opcion.isdigit() or (int(opcion) > 5 or int(opcion) < 1):
        opcion = input("Opción: ")

    match opcion:
        case "1":
            print("\n1 = Lunes, 2 = Martes")
            dia = input("Elija día: ")

            match dia:
                case "1":
                    nombre = input("Ingrese nombre: ")

                    if (nombre != lunes1 and lunes1 == "") or nombre == lunes1:
                        lunes1 = nombre
                        continue
                    elif (nombre != lunes2 and lunes2 == "") or nombre == lunes2:
                        lunes2 = nombre
                        continue
                    elif (nombre != lunes3 and lunes3 == "") or nombre == lunes3:
                        lunes3 = nombre
                        continue
                    elif (nombre != lunes4 and lunes4 == "") or nombre == lunes4:
                        lunes4 = nombre
                        continue

                case "2":
                    nombre = input("Ingrese nombre: ")

                    if (nombre != martes1 and martes1 == "") or nombre == martes1:
                        martes1 = nombre
                        continue
                    elif (nombre != martes2 and martes2 == "") or nombre == martes2:
                        martes2 = nombre
                        continue
                    elif (nombre != martes3 and martes3 == "") or nombre == martes3:
                        martes3 = nombre
                        continue

        case "2":
            print("\n1 = Lunes, 2 = Martes")
            dia = input("Elija día: ")

            match dia:
                case "1":
                    nombre = input("Ingrese nombre: ")

                    if nombre == lunes1:
                        lunes1 = ""
                        continue
                    elif nombre == lunes2:
                        lunes2 = ""
                        continue
                    elif nombre == lunes3:
                        lunes3 = ""
                        continue
                    elif nombre == lunes4:
                        lunes4 = ""
                        continue

                case "2":
                    nombre = input("Ingrese nombre: ")

                    if nombre == martes1:
                        martes1 = ""
                        continue
                    elif nombre == martes2:
                        martes2 = ""
                        continue
                    elif nombre == martes3:
                        martes3 = ""
                        continue
            

        case "3":
            if lunes1 == "":
                print("Lunes: Turno 1: libre")
            else:
                print("Lunes: Turno 1:", lunes1)
            if lunes2 == "":
                print("Lunes: Turno 2: libre")
            else:
                print("Lunes: Turno 2:", lunes2)
            if lunes3 == "":
                print("Lunes: Turno 3: libre")
            else:
                print("Lunes: Turno 3:", lunes3)
            if lunes4 == "":
                print("Lunes: Turno 4: libre")
            else:
                print("Lunes: Turno 4:", lunes4)

            if martes1 == "":
                print("Martes: Turno 1: libre")
            else:
                print("Martes: Turno 1:", martes1)
            if martes2 == "":
                print("Martes: Turno 2: libre")
            else:
                print("Martes: Turno 2:", martes2)
            if martes3 == "":
                print("Martes: Turno 3: libre")
            else:
                print("Martes: Turno 3:", martes3)


        case "4":
            luneslibre = 0
            marteslibre = 0

            if lunes1 == "":
                luneslibre += 1
            if lunes2 == "":
                luneslibre += 1
            if lunes3 == "":
                luneslibre += 1
            if lunes4 == "":
                luneslibre += 1

            if martes1 == "":
                marteslibre += 1
            if martes2 == "":
                marteslibre += 1
            if martes3 == "":
                marteslibre += 1

            
            print("Lunes")
            print("Turnos ocupados: ", 4 - luneslibre)
            print("Turnos disponibles: ", luneslibre)
            print("")
            print("Martes")
            print("Turnos ocupados: ", 3 - marteslibre)
            print("Turnos disponibles: ", marteslibre)
            print("")

            if luneslibre > marteslibre:
                print("Dia con mas turnos: Lunes")
            elif luneslibre == marteslibre:
                print("Dia con mas turnos: empate")
            else:
                print("Dia con mas turnos: Martes")


        case "5":
            break
