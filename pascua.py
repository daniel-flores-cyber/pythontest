# domingo de pascua
# preguntar la cantidad de niños que buscan huevitos de chocolate
# cuando termine la busqueda, preguntar cantos huevos encontro cada uno
# y clasificarlos de la sigiente forma
# menos de una docena : noob
# entre una docena a 24 : master
# 25 huevos o mas : legend
# mostrar resumen, y mostrar la mayor cantidad de huevitos encontrados por un solo niño 
import random
while True:
    try:
      cantniños=int(input("Cuantos niños va a buscar huevitos "))
      while cantniños<=0:
          print("error, solo ingrese numeros positivos")
          cantniños=int(input("Cuantos niños va a buscar huevitos "))
      break
    except Exception:
        print("solo puede ingresar numeros enteros")   
noob=0
master=0
legend=0
top=0
for n in range(cantniños):
    canthuevos=random.randint(5,30)
    if canthuevos>top:
        top=canthuevos
    print("el niñlo",n+1, "encontro",canthuevos,"huevos")
    if canthuevos<12:
        noob+=1
    elif canthuevos>=12 and canthuevos<=24:
        master+=1
    else:
        legend+=1
print("la cantidad de grupo noob es",noob)
print("la cantidad de grupo master es",master)                
print("la cantidad de grupo legend es",legend)
print("la mayor cantidad de huevos encontrada por un niño fue",top)                




   
