#  TP1-EJ1.py
#

total = 0
totalConDesc = 0

cliente = input("Nombre cliente: ")
while not cliente.isalpha():
    cliente = input("Nombre cliente: ")


cantProduc = input("Cantidad de productos: ")
while not cantProduc.isdigit() and int(cantProduc) > 0:
    cantProduc = input("Cantidad de productos: ")
    
for i in range(int(cantProduc)):
    print(f"Producto{i+1} -", end=" ")
    precio = int(input("Precio: "))


    descuento = input("Descuento S/N: ")
    while descuento != "s" and descuento != "n" and descuento != "S" and descuento != "N":
        descuento = input("Descuento S/N: ")

    if descuento == "s" or descuento == "S":
        total = total + precio
        valorDescuento = precio * 0.10
        totalConDesc =  totalConDesc + (precio - valorDescuento)
    else:
        total = total + precio
        totalConDesc =  totalConDesc + precio
        

print("Cliente: ", cliente)
print("Cantidad de productos: ", cantProduc)
print("Total sin descuento: ", total)
print("Total con descuento: ", totalConDesc)
print("Ahorro: ", total - totalConDesc)
print(f"Promedio por producto: {totalConDesc/int(cantProduc):.2f}")
