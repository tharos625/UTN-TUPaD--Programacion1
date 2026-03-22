#  TP1-EJ2.py
#

for i in range(3):
    usuario = input(f"Intento {i+1}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == "alumno" and clave == "python123":
        print("Acceso concedido.")
        print("1 Estado 2) Cambiar clave 3) Mensaje 4) Salir")

        while True:
            menu = input("Opción: ")

            if not menu.isdigit():
                print("Error: ingrese un número valido.")
                continue

            if int(menu) > 4:
                print("Error: opción fuera de rango.")
                continue
        
            match menu:
                case "1":
                    print("Inscripto")

                case "2":
                    print("Cambiar clave")
                    nuevaClave = input("Nueva clave: ")
                    if len(nuevaClave) >= 6:
                        confirmacion = input("Confirmación: ")
                        if nuevaClave == confirmacion:
                            print("Cambio de clave realizado.")
                        else:
                            print("Las claves no coinciden.")
                    else:
                        print("Error: mínimo 6 carecteres.")

                case "3":
                    print("A programar en Python!!!")

                case "4":
                    break
        break

    elif i == 2:
        print("Cuenta bloqueada.")
    else:
        print("Credenciales invalidas")
