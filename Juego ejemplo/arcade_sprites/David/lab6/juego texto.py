#Juego por David gutiérrez
import json
import pathlib
jugadorPath = pathlib.Path("jugador.json")
tiendaPath = pathlib.Path("tienda.json")
enemigosPath = pathlib.Path("enemigos.json")

#inicialización


#
def inicializacion():
    print("Bienvenido al juego texto\n")
    print("Tendrás que usar comandos para interactuar con el juego\n")
    print("Si tienes dudas de que comandos puedes hacer usa \"help\"")

    helps()

    return 0

def helps():
    print("Los comandos son: \"personaje\" \"lucha\" \"tienda\" \"comprar [objeto]\" ")
    main()

    return

def personaje():
    stats = json.load(open(jugadorPath, "r"))
    print(f"Vida: {stats['vida']}\nnivel: {stats['nivel']}\nexperiencia: {stats["experiencia"]}\ndinero: {stats['dinero']}")
    print(f"Habilidades:")
    for i,j in stats["habilidades"].items():
        print("\t"+i)
        for k,l in j.items():
            print(f"\t\t{k}: {l}")
    print(f"Objetos:")
    for i,j in stats["objetos"].items():
        print("\t"+i)
        for k,l in j.items():
            print(f"\t\t{k}: {l}")
    main()
    return

def tienda():
    statsTienda = json.load(open(tiendaPath, "r"))
    statsJugador = json.load(open(jugadorPath, "r"))
    if statsJugador["nivel"] <= 1:
        for i,j in statsTienda[0].items():
            print(f"\t{i}:")
            for k,l in j.items():
                print(f"\t\t{k}: {l}")


    main()

def comprar(comando):
    statsTienda = json.load(open(tiendaPath, "r"))
    statsJugador = json.load(open(jugadorPath, "r"))
    objeto = comando.split(" ")[1]
    for i,j in statsTienda[0].items():
        if i==objeto:
            if j["precio"] <= statsJugador["dinero"]:
                print("comprado!")
                statsJugador["dinero"] -= j["precio"]
                if j["tipo"] == "habilidad":
                    statsJugador["habilidades"][i] = j
                else:
                    statsJugador["objetos"][i] = j
                json.dump(statsJugador, open(jugadorPath, "w"), indent=4)
                main()
            else:
                print("Te falta dinero")
    print("Objeto no encontrado")
    main()

def main():
    comando = input().lower()
    if comando == "ayuda":
        helps()
    elif comando == "personaje":
        personaje()
    elif comando == "tienda":
        tienda()
    elif comando.startswith("comprar"):
        comprar(comando)





    else: main()



inicializacion()