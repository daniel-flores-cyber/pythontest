# uso y explicacion de MATCH

# def suma():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("ingrese otro numero "))
#     print("el resultado de la suma es",n1+n2)


# def resta():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("ingrese otro numero "))
#     print("el resultado de la resta es",n1-n2)


# def multiplicacion():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("ingrese otro numero "))
#     print ("el resultado de la multiplicacion es",n1+n2)


# def division():
#     try:
#         n1=int(input("ingrese un numero "))
#         n2=int(input("ingrese otro numero "))
#         print("el resultado de la division es",n1/n2)
#     except ZeroDivisionError as nombre_de_exepcion:
#         print(f"se produjo una excepcion: ",nombre_de_exepcion)    



# def calcu():
#     while True:
#         try:
#             op=int(input("""ingrese una opcion
#                         1.-suma
#                         2.-resta
#                         3.-multiplicacion
#                         4.-division 
#                         5.-opcion 4 salir 
#                         """))
#             match op:
#                 case 1:
#                     print("suma")
#                     suma()
#                 case 2:
#                     print("resta")
#                     resta()
#                 case 3:
#                     print("multiplicacion")
#                     multiplicacion()
#                 case 4:
#                     print("division")
#                     division()      
#                 case 5:
#                     break 
#         except ValueError as mati:
#             print("solo puedes ingresar numeros, no caracteres")
#             print("error",mati)
             
# calcu()       

           

# -----------------------------------------------------------------
# def prom():
#     print("ingrese el numero de notas")
#     cant=int(input())
#     suma=0
#     for i in range(cant):
#         print("ingrese la nota",i+1)
#         nota=float(input())
#         suma=suma+nota
#     prom=suma/cant
#     print("su promedio es ", round (prom,1))
#     if prom>=4:
#         print("Aprobo",prom) 
#     else:
#         print("Reprobo",prom)


# def votos():
#     print("ingrese la cantidad de votantes")
#     v=int(input())
#     trump=0
#     biden=0
#     kast=0
#     for i in range (v):
#         print("1.-trump")
#         print("2.-biden")
#         print("3.-kast")
#         op=int(input())
#         if op==1:
#          print("Voto por trump")
#          trump=trump+1
#         elif op==2:
#          print("voto por biden")
#          biden=biden+1
#         elif op==3:
#          print("voto por kast") 
#          kast=kast+1 
#         else:
#          print("voto no valido")
#     if trump>biden:
#      print("gano trump",trump)
#     elif biden>kast:
#      print("gano biden",biden)
#     else:
#      print("gano kast",kast)      
# print("1.-promedio")
# print("2.-votos")     

# op=int(input())
# if op==1:
#     prom()
# elif op==2:
#    votos()    