# perros de caza
# pida al usuario la cantidad de perros
# muestre la cuota minima de conejos 
# luego consulte cuantos conejos trajo
# si el perro trajo la cantidad minima se gana un filete
# si no, no se gana el filete
# muestre un resumen de cuantos perro cumplieros

# import random 
# while True:
#     try:          
#         perros=int(input("ingrese la cantidad de perros "))
#         while perros<1:
#             print("debe ingresar 1 o mas perros")
#             perros=int(input("ingrese la cantidad de perros "))

#         cuota=random.randint(3,5)
#         cumplen=0
#         print("la cuota es de",cuota)
#         for p in range(perros):
#             conejos=random.randint(0,7)
#             if conejos>=cuota:
#                 print("el perro",p+1,"trajo",conejos,"conejos, cumplio la cuota")
#                 cumplen+=1
#             else:
#                 print("el perro",p+1,"trajo",conejos,"conejos, se quedo sin filete")  
#         print("el total de perros que cumplio la cuota fue",cumplen)
#         print("el total de perros que no cumplio la cuota fue",perros-cumplen)
#         break        
#     except Exception:
#         print("solo debes poner numeros enteros")   
#  
# -----------------------------------------------------------------------------------------------------------

# quiere pasar el ramo?
# pregunte la cantidad de rojos en el curso
# los talleres que hay en el semestre son 4
# por cada taller asistido obtiene 0.3 decimas
# si el alumno tiene mas de un punto
# tiene la bendicion del profesor
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acomuladas
# muestre si aprueba o reprueba
suma=0
ramos=int(input("ingrese la cantidad de rojos en el curso "))
talleres=int(input("ingrese la cantidad de talleres a los que asistio "))
while talleres>4:
    print("opcion invalida")
    talleres=int(input("ingrese la cantidad de talleres a los que asistio "))
if talleres==1:
    suma=suma+0.3
elif talleres==2:
    suma=suma+0.6
elif talleres==3:
    suma=suma+0.9
elif talleres==4:
    suma=suma+1.2    
nota=float(input("ingrese su nota "))
print("su nota final es",nota+suma)


