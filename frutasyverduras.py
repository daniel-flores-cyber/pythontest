total=0
cantart=0
while True:
    try:
        opcion=int(input('''seleccione una opcion
                        1.-comprar frutas
                        2.-comprar verduras
                        3.-pagar
                        4.-salir
                         '''))
        match opcion:
            case 1:
                while True:
                    try:
                        opcion=int(input('''seleccione una opcion
                                        1.-frutilla $1500
                                        2.-pera $2000
                                        3.-manzana $1300
                                        4.-volver al menu principal
                                         '''))
                        match opcion:
                            case 1:
                                print("has selccionado frutilla")
                                total+=1500
                                cantart+=1
                            case 2:
                                print("has selccionado pera")
                                total+=2000
                                cantart+=1    
                            case 3:
                                print("has selccionado manzana")
                                total+=1300
                                cantart+=1    
                            case 4:
                                print("volviendo al menu principal")
                                break    
                            case _:
                                print("opcion invalida")   
                    except Exception:
                        print("solo puede ingresar numeros enteros")
                print("su total hasta ahora es",total)        
            case 2:
                 while True:
                    try:
                        opcion=int(input('''seleccione una opcion
                                        1.-papa $1500
                                        2.-lechuga $2000
                                        3.-cebolla $1300
                                        4.-volver al menu principal
                                         '''))
                        match opcion:
                            case 1:
                                print("has selccionado papa")
                                total+=1500
                                cantart+=1
                            case 2:
                                print("has selccionado lechuga")
                                total+=2000
                                cantart+=1    
                            case 3:
                                print("has selccionado cebolla")
                                total+=1300
                                cantart+=1    
                            case 4:
                                print("volviendo al menu principal")
                                break    
                            case _:
                                print("opcion invalida")   
                    except Exception:
                        print("solo puede ingresar numeros enteros")
                 print("su total hasta ahora es",total)    
            case 3:
                print("Has selccionado pagar")
                print("El total a pagar es",total)
                print("El total a pagar mas iva es",total*1.19)
            case 4:
                print("Saliendo...")
                break    
            case _:
                print("opcion invalida")   
    except Exception:
        print("solo puede ingresar numeros enteros")
