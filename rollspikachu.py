# total=0
# while True:
#    op=int(input('''
#             Seleccione una comida
#             1. Pikachu Roll $4500
#             2. Otaku Roll $5000
#             3. Pulpo Venenoso Roll $5200
#             4. Anguila Eléctrica Roll $4800
#             5.-Pagar y salir
#             '''))
#    match op:
#       case 1:
#          total+=4500
#       case 2:
#          total+=5000
#       case 3:
#          total+=5200
#       case 4:
#          total+=4800
#       case 5:
#         print("tiene codigo de descuento? 1.- si, 2.- no")
#         desc=int(input())
#         if desc==1:
#             while True:
#                 cod=input("ingres su codigo de desc")
#                 if cod =="soyotaku":
#                     desc10=total*0.1
#                     total=total-desc10
#                     print("El Descuento es $",desc10)
#                     break
#                 else:
#                    print("Codigo caducado o no valido")
#                    nu=input("Dese intentar nuevamente?1.- si, 2.- no")
#                    if nu!="1":
#                       break
#         print(" EL total es $", total)
#         break
#       case _:
#          print("Opcion invalida")
#    print(f"su total parcial es {total}")

total=0
while True:
   while True:
    try:
        op=int(input('''
                    Seleccione una comida
                    1. Pikachu Roll $4500
                    2. Otaku Roll $5000
                    3. Pulpo Venenoso Roll $5200
                    4. Anguila Eléctrica Roll $4800
                    5.-Pagar y salir
                    '''))
        break
    except Exception:
        print("solo puede ingresar numeros enteros") 
   match op:
            case 1:
                total+=4500
            case 2:
                total+=5000
            case 3:
                total+=5200
            case 4:
                total+=4800
            case 5:
                while True:
                    try:
                        print("tiene codigo de descuento?, 1.-si,2.-no")
                        desc=int(input())
                        break    
                    except Exception:
                     print("solo puede ingresar numeros enteros")
                if desc==1:
                    while True:
                        cod=input("ingrese su codigo de descuento " )
                        if cod=="soyotaku":
                            desc10=total*0.1
                            total=total-desc10
                            print("el descuento es de $",desc10)  
                            break
                        else:
                            print("codigo caducado o incorrecto")
                            try:
                                nu=int(input("desea intentar nuevamente?,1.-si,2.-no " ))
                                if nu!=1:
                                    break
                            except Exception:
                                print("solo puede ingresar numeros enteros")   
                        
                print("su total es",total)
                break
            case _:
                print("opcion invalida")
   print("su total es",total,"pesos") 
            
           
               

         


