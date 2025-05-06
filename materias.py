suma=0
print("ingrese la cantidad de ramos")
ramos=int(input())
for i in range(ramos):
    
    print("ingrese el promedio")
    prom=int(input())
    suma=suma+prom

promf=suma/ramos
print("su promedio final es",promf)

