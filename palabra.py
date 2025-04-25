
palabra=input("ingrese una frase")
cont=0
vocales=0
cons=1
for i in palabra.lower():
    cont=cont+1
    print(cont,i)
    if i in "aeiou":
        # vocales=vocales+1
        vocales+=1
    else:
        cons+=1    
print("la cantidad de caractereses es",cont)
print("la cantidad de vocales es",vocales)        
print("la cantidad de consonantes son",cons)
   