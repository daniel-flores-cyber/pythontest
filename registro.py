# Hacer un sistema de login con diccionario
# Debe verificar si el usuario existe
# de existir le pregunta la contaseña
# y da solo  3 oportunidades para acertar
# El diccionario debe de estar previamente
# escrito antes de iniciar el sistema

registro={
    "daniel flores": 1234
}
nom=input("ingrese su nombre de usuario ")
if nom in registro:
    cont=int(input("ingrese la contraseña "))
    if cont in registro:
        print("inicio sesion ")
    else:
        print("no")    
else:
    print("no")    