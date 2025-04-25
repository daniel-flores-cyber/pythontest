print("Cuantos productos llevara")
cant=int(input())
total=0
for i in range(cant):
    print('''
    Que producto llevara?
    1.- Diazepan $9000
    2.- Metametazona $18500
    3.- Oblea china $1000''')
    op=int(input())
    if op==1:
      print("usted lleva diazepan")
      total=total+9000
    elif op==2:
      print("usted lleva metametazona")
      total=total+18500
    elif op==2:
      print("usted lleva oblea china")
      total=total+1000
    else:
      print("opcion no valida")

print("el total es",total)
print("el total mas iva es",total*1.19) 


  
                        
    