# import random
# numadivinar=random.randint(1,50)
# print("ingrese un numero")
# num=int(input())

# while num!=numadivinar:
#     if num>numadivinar:
#      print("ingrese un numero menor")
#     elif num<numadivinar:
#        print("ingrese un numero mayor")
#     num=int(input("ingrese un numero "))   

   
     
# arancel=200000
# descuento=0
# print("ingrese su comuna")
# print("1.-la florida")
# print("2.-la pintana")
# print("3.-puente alto")
# print("4.-san juaquin")
# comuna=int(input())
# if comuna==1:
#     descuento=20
# elif comuna==2:
#     descuento=30    
# elif comuna==3:
#     descuento=25 
# elif comuna==4:
#     descuento=15
# else:
#     print("opcion incorrecta")    

# print("ingrese su grupo familiar")
# print("1= vive una persona")
# print("2= viven de 2 a 4 personas")
# print("3= viven 5 o mas")
# grupo=int(input())
# if grupo==1:
#     descuento+=2
# elif grupo==2:
#     descuento+=3
# elif grupo==3:
#     descuento+=4
# else:
#     print("opcion incorrecta")   
# print("el descuento total es ", descuento)     
# desc=arancel*descuento/100     
# total=arancel-desc
# print("el total a pagar es $", total)  


 
# import random
# puntos=random.randint(1,30)
# print(puntos)
# if puntos>=20:
#     print("logoro abrir la puerta")
# else:
#     print("puntos insuficientes")    


j1=0
j2=0
import time
while j1<30 and j2<30:
    time.sleep(1)
    
    print("turno de j1")
    dado=random.randint(1,6)
    j1=j1+dado
    print("saco",dado)
    print("avanzo a la casilla",j1)

    
    time.sleep(1)
    print("turno de j2")
    dado=random.randint(1,6)
    j2=j2+dado
    print("saco",dado)
    print("avanzo a la casilla",j2)
    
if j1>j2:
    print("Gano j1")
else:
    print("Gano j2")    