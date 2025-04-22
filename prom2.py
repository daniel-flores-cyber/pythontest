print("ingrese el numero de notas")
cant=int(input())
suma=0
for i in range(cant):
    print("ingrese la nota",i+1)
    nota=float(input())
    suma=suma/cant
    prom=suma/cant
print("su promedio es ",prom)