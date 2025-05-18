suma=0
nota=0
prom=0
canta=int(input("ingrese la cantidad de alumnos: "))
cantn=int(input("ingrese la cantidad de notas por alumno: "))
for i2 in range (canta):
    for i in range (cantn):
        print("nota",i+1,"de alumno",i2+1)
        nota=int(input())
        suma=nota+suma
    prom=suma/cantn
    print("Su promedio es", round (prom,1))
    if prom>=4:
        print("El alumno",i2+1,"aprobo")
    else:
        print("el alumno",i2+1,"reprobo") 

       

    
