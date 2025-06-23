pokedex=[
    {"nombre":"charizard","tipo":"fuego","vida":1000},
    {"nombre":"pikachu","tipo":"electrico","vida":400}
]
while True:
    print('''
          1.-ver lista de pokemons
          2.-agregar pokemon y tipo
          3.-borrar pokemon
          4.-actualizar tipo
          5.-salir''')
    op=int(input("ingrese una opcion "))
    match op:
        case 1:
            for n,poke in enumerate(pokedex):
                print(n+1,poke["nombre"],poke["tipo"],poke["vida"])
        case 2:
            po=input("nombre del pokemon ")
            ti=input("tipo del pokemon ")
            vi=input("ingrese la vida ")
            pokedex.append({"nombre":po,"tipo":ti,"vida":vi})
        case 3:
            for n,poke in enumerate(pokedex):
                print(n+1,poke["nombre"],poke["tipo"])
            borrar=input("nombre del pokemon que desea borrar")
            pokedex.pop(borrar)
        case 4:
            for n,poke in enumerate(pokedex):
                print(n+1,poke["nombre"],poke["tipo"])
            act=int(input("que pokemon desea actualizar "))
            tinuevo=input("cual va a ser su nuevo tipo ")
            pokedex[act-1]["tipo"]=tinuevo    
        case 5:
            print("saliendo")
            break
        case _:
            print("opcion invalida")