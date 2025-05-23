suma=0
op=int
print("eliga su Roll")
while op!=5:
    print('''
      1.-pikachu roll $4500
      2.-otaku roll $5000
      3.-pulpo venenoso roll $5200
      4.-anguila electrica roll $4800
      5.-Finalizar compra''')
    try:
        op=int(input())
        if op==1:
            suma=suma+4500
        elif op==2:
            suma=suma+5000
        elif op==3:
            suma=suma+5200   
        elif op==4:
            suma=suma+4800
        elif op==5:
            print("compra finalizada")
        else:
            print("opcion incorrecta")
    except Exception:
        print("solo puedes ingresar numeros enteros")        
                
des=str
cont=str
des="soyotaku"        
print("El total es",suma)    
print("Tiene un codigo de descuento")
print("1.-si")
print("2.-no")
op=int(input())

if op==1:
    print("ingrese el codigo")
    cont=str(input())
    while cont!=des:
        print("codigo incorrecto")
        cont=str(input())
    print("el total con descuento es",suma*0.9)     
else:
    print("su total es",suma)           
             
 

        
