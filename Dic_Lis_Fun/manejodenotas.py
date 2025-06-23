# crear un programa de manejo de notas
# 1.-ingresar notas
# 2.-borrar notas
# 3.-mostrar notas
# 4.-sacar promedio, nota mayor y nota menor
# 5.-limpiar todas las notas
# 6.-salir

notas=[]
while True:
        print('''
    -------.--------
    1.-ingresar nota
    2.-borrar nota
    3.-mostrar notas
    4.-Sacar promedio, nota mayor y nota menor
    5.-limpiar todas las notas
    6.-salir''')
        op=int(input("seleccione una opcion "))
        match op:
            case 1:
                nota=float(input("ingrese una notas "))
                notas.append(nota)
            case 2:
                for num, n in enumerate(notas):
                    print(num+1,".-",n)
                elim=int(input("ingrese cual quiere eliminar "))
                notas.pop(elim-1)    
            case 3:
                print(notas) 
            case 4:
                if len(notas)==0:
                    print("no hay notas para calcular promedio")
                else:
                    promedio=sum(notas)/len(notas)
                    print("el promedio de las notas:",round(promedio, 1))    
                    print("la nota mayor es", max(notas))
                    print("la nota menor es",min(notas))
            case 5:
                notas.clear()
            case 6:
                print("Saliendo")
                break
            case _:
                print("opcion incorrecta")                  

