pokedex=[
    {"nombre":"charizard","tipo":"fuego"},
    {"nombre":"pikachu","tipo":"electrico"}
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
                print(n+1,poke["nombre"],poke["tipo"])
        case 2:
            po=input("nombre del pokemon ")
            ti=input("tipo del pokemon ")
            pokedex.append({"nombre":po,"tipo":ti})
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