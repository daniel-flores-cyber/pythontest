# explicacion de while
# clave=3344
# intento=1
# pasword=int(input("ingrese su pass: "))
# while clave!=pasword and intento<=3:
#     print("error")
#     intentos=intentos+1
#     print(intentos)
#     pasword=int(input("ingrese su pass "))
# if intento>=3:
#     print("ya no tiene intentos")
# else:
#     print("bienvenido")        
# NUMERO AL AZAR
# import random
# numAzar=random
# print(numAzar)
# dado=random.randint(1,6)
# print(dado)

import random
meta=30
turno=1
j2=0
j1=0
while j1 or j2 !=30:
    if turno%2==0:
     print("turno de j1")
     dado=random.randint(1,6)
     j1=j1+dado
     print("j1 saco", dado)
     print("avanzo a la casilla ", j1)
    else: 
     print("turno de j2 ")   
     dado=random.randint(1,6)
     j2=j2+dado
     print("j1 saco", dado)
     print("avanzo a la casilla ", j2)

if j1>=30:
  print("gano el j1")
else:
  print("gano el j2")