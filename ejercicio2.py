numero = int(input("ingrese su factura \n"))
div = numero / 0.5
if numero < 10000:
    print("la factura es un total de ", numero, " no se cobra comision")
else:
    print("la factura es un total de ", numero, " con la comision es un total de ", div)
