credi=0


print("de 500.000 a 1.000.000")
print("de 1.000.000 a 1.500.000")
print("mas de 1.500.001")

ingresos=int(input("de cuanto son sus ingresos "))
if ingresos>=500000 and ingresos<=1000000:
    credi=300000
elif ingresos>=1000000 and ingresos<=1500000:
    credi=650000
elif ingresos>1500001:
    credi=1000000    
else:
    print("opcion invalida")       
print(credi)
print("su nivel educacional")
print("1.-Basico")
print("2.-medio")
print("3.-superior")
nivel=int(input())
if nivel==1:
    credi=credi*1
elif nivel==2:
    credi=credi*1.3
else:
    credi=credi*1.5    

print("su nacionalidad")
print("1-chilena")
print("2-extranjera")
nacio=int(input())
if nacio==1:
    credi=credi+300000
else:
    credi=credi+0    

print("el total de sus creditos son",credi)    
