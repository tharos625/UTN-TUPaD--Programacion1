# TP1-EJ5.py
#
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
danoBase_AtPesado = 15
danoBase_enemigo = 12
turno_gladiador = True

primer_turno = True

print("Escape Room: La Arena del Gladiador")
print("--- BIENVENIDO A LA ARENA ---\n")

nombre_gladiador = input("Nombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")



while vida_gladiador > 0 and vida_enemigo > 0:


    if turno_gladiador:
        if primer_turno == True:
            print("=== INICIO DEL COMBATE ===")
            primer_turno = False
        else:
            print("\n=== NUEVO TURNO ===")
        
        print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Posiones: {pociones}")
        print()
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Rafaga Veloz")
        print("3. Curar\n")

        opcion = input("Acción: ")
        while not opcion.isdigit() or (int(opcion) > 3 or int(opcion) < 1):
            print("Error: opción invalida")
            opcion = input("Acción: ")


        match opcion:
            case "1":
                turno_gladiador = False
                if vida_enemigo < 20:
                    ataque = danoBase_AtPesado * 1.5
                    vida_enemigo -= ataque
                    print(f"Atacaste al enemigo por {ataque} puntos de daño!")
                else:
                    ataque = danoBase_AtPesado
                    vida_enemigo -= ataque
                    print(f"Atacaste al enemigo por {ataque} puntos de daño!")
                    

            case "2":
                turno_gladiador = False
                print(">> ¡Inicias una rafaga de golpes!")
                for i in range(3):
                    print("> Golpe conectado por 5 de daño")
                    vida_enemigo -= 5

            case "3":
                turno_gladiador = False
                if pociones <= 3 and pociones > 0:
                    vida_gladiador += 30
                    pociones -= 1
                else:
                    print("¡No quedan pociones!")

            case _:
                turno_gladiador = True
                print()
                print("Opción invalida")
                print()


    else:
        vida_gladiador -= 12
        print(">> ¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador = True
    



if vida_gladiador > 0:
    print()
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla")
    print()
elif vida_gladiador <= 0:
    print()
    print("DERROTA. Has caído en combate.")
    print()
