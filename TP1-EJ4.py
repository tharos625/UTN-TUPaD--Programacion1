#  TP1-EJ4.py
#

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_cerradura = 0

print("Escape Room: La Bóveda\n")
nombre = input("Nombre: ")
while not nombre.isalpha():
    nombre = input("Nombre: ")

while True:
    print("")
    print(f"Energia: {energia}, Tiempo: {tiempo}, Cerraduras abiertas: {cerraduras_abiertas}", end=", ")
    if alarma == False:
        print("Alarma: Desactivada")
    else:
        print("Alarma: Activada")

    print("")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar\n")

    opcion = input("Opción: ")
    while not opcion.isdigit():
        opcion = input("Opción: ")

    match opcion:
        case "1":

            if energia < 40:
                print("Riesgo de alarma")
                
                numero_alarma = input("Número 1-3")
                while not numero_alarma.isdigit() or (int(numero_alarma) > 3 or int(numero_alarma) < 1):
                    numero_alarma = input("Número 1-3") # falta cheque de 1 a 3
                    if numero_alarma == 3:
                        alarma = True

            forzar_cerradura = forzar_cerradura + 1

            if forzar_cerradura == 3:
                energia = energia - 20
                tiempo = tiempo - 2
                alarma = True
                print("\nAlarma activada - la cerradura se trabó\n")


            elif alarma == False:
                energia = energia - 20
                tiempo = tiempo - 2
                cerraduras_abiertas = cerraduras_abiertas + 1


        case "2":
            forzar_cerradura = 0
            
            energia = energia - 10
            tiempo = tiempo - 3

            for i in range(4):
                codigo_parcial = codigo_parcial + "X"
                print(f"Codigo parcial: {codigo_parcial}")

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas = cerraduras_abiertas + 1
                codigo_parcial = ""

        case "3":
            forzar_cerradura = 0
            energia = energia + 15
            if energia > 100:
                energia = 100

            if alarma == True:
                energia = energia - 10
            
            tiempo = tiempo - 1

    if cerraduras_abiertas == 3:
        print("\nVICTORIA")
        break
    elif energia <= 0 or tiempo <= 0:
        print("\nDERROTA")
        break
    elif alarma == True and tiempo <= 3:
        print("\nDERROTA (bloqueo)")
        break
