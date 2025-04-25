print("ingrese la cantidad de votantes")
v=int(input())
trump=0
biden=0
kast=0
for i in range (v):
    print("1.-trump")
    print("2.-biden")
    print("3.-kast")
    op=int(input())
    if op==1:
     print("Voto por trump")
     trump=trump+1
    elif op==2:
       print("voto por biden")
       biden=biden+1
    elif op==3:
       print("voto por kast") 
       kast=kast+1 
    else:
       print("voto no valido")
if trump>biden:
   print("gano trump",trump)
elif biden>kast:
   print("gano biden",biden)
else:
   print("gano kast",kast)      


   
