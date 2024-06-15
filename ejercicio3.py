nota1 = int (input("ingrese la primer nota \n"))
nota2 = int (input("ingrese la seguda nota \n"))
nota3 = int (input("ingrese la tercera nota \n"))
nota4 = int (input("ingrese la cuerta nota \n"))

promedio = ( nota1 + nota2 + nota3 + nota4 )/ 4

if 1 <= promedio <= 10:
        print("su nota final es de ", promedio, "entonces seria F")
elif 11 <= promedio <=20:
        print("su nota final es de ", promedio, "entonces seria E")
elif 21 <= promedio <=30:
        print("su nota final es de ", promedio, "entonces seria D")
elif 31 <= promedio <=40:
        print("su nota final es de ", promedio, "entonces seria C")
elif 41 <= promedio <=50:
        print("su nota final es de ", promedio, "entonces seria B")
elif 51 <= promedio <=100:
        print("su nota final es de ", promedio, "entonces seria A")
else:
        print("su calificacoion esta fuera de rango vuelva a repetirlo")