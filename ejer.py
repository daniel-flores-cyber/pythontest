# cont=0
# total=0
# opc=0
# while opc !=2:
#     print("1.- ingresar nuevo numero")
#     print("2.-salir")
#     opc=int(input())
#     if opc==1:
#         a=int(input("ingrese el numero: "))
#         cont+=1
#         total+=a
# print(f"la cantidad de numeros ingresados son:{cont}")
# print(f"la suma de los numeros es:{total}")           

num=int(input("ingrese un numero: "))
if num%2==0:
    print("es par")
else:
    print("es impar")
print(f"los numeros pares entre 1 y {num} son: ")
for i in range(1,num+1):
    if i%2==0:
        print(i)   
print(f"los numeros impares entre 1 y {num} son: ")
for i in range(1,num+1):
    if i%2!=0:
        print(i)
    
          
    
