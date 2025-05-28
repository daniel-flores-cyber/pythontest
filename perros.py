# perros de caza
# pida al usuario la cantidad de perros
# muestre la cuota minima de conejos 
# luego consulte cuantos conejos trajo
# si el perro trajo la cantidad minima se gana un filete
# si no, no se gana el filete
# muestre un resumen de cuantos perro cumplieros
import random
cumplen=0
while True:
    try:
        cantp=int(input("ingrese la cantidad de perros "))
        while cantp<1:
            print("debe ingresar mas de un perro")
            cantp=int(input("ingrese la cantidad de perros "))
        break    
    except Exception:
        print("solo puede ingresar numeros enteros")        
cuota=random.randint(4,7)
print("la cuota minima es",cuota)
for p in range (cantp):
    conejos=random.randint(0,10)
    print("el perro",p+1,"trajo",conejos,"conejos")
    if conejos>cuota:
       print("el perro",p+1,"cumplio la cuota, se gano un filete")
       cumplen+=1
    else:
       print("el perro",p+1,"se quedo sin filete")
print("la cantidad de perros que cumplieros fueron",cumplen)


        