pagob=5000
op=int
print("cuantos goles anoto?")
print("1.-entre 1 y 3 goles 4%")
print("2.-entre 4 y 6 goles 6%")
print("3.-entre 7 o mas goles 8%")
goles=int(input())
if  goles==1:
    pagob=pagob*1.04
elif goles==2:
    pagob=pagob*1.06
elif goles==3:
    pagob=pagob*1.08  
else:
    print("opcion invalida")
print(pagob)
print("en que posicion quedo su equipo")
print("1.-quedo entre los 3 primeros +3000")
print("2.-quedo entre 4-8 +2000")                
print("3.-quedo  9 o mas +1000") 
p=int(input())

if p==1:
    pagob=pagob+3000
elif p==2:
    pagob=pagob+2000
elif p==3:
    pagob=pagob+1000    
else:
    print("opcion invalida")

print("el sueldo total es",pagob)