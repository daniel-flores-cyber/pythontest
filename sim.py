import random
print("ingrese 2 numeros")
n1=int(input())
n2=int(input())
while n1>n2:
    print("el segundo digito debe ser mayor")
    n2=int(input())

    
n3=random.randint(n1,n2) 
print(n3)
print("▄"*n3)

