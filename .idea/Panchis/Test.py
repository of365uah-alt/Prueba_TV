from pathlib import Path
import random
# Directorio actual
current_dir = Path(__file__).parent
txtPreguntas = (current_dir / "preguntas.txt")

def cargar_preguntas() -> list:
    lista = []
    for linea in txtPreguntas.read_text(encoding='utf-8').splitlines():
        partes = linea.split('|')
        pregunta = partes[0]
        opciones = partes[1:]
        lista += [{'pregunta': pregunta, 'respuesta': opciones[0], 'opciones': opciones}]
    return lista

def juego(lista: list) -> None:
    salir = False
    puntos = 0

    while not salir:
        pregunta = random.choice(lista)
        print(pregunta['pregunta'])


        dict = {}
        opciones = pregunta['opciones'].copy()
        random.shuffle(opciones)
        valores = ['a', 'b', 'c', 'd']
        for opcion in opciones:
            dict[valores[0]] = opcion
            print(f"{valores[0]}) {opcion}")
            valores = valores[1:]

        respuesta = input("Tu respuesta (a/b/c/d): \n").lower()
        if (pregunta['respuesta'] == dict[respuesta]):
            puntos += 5
            print(f"¡Respuesta correcta! Puntos:\t{puntos}")
        else:
            print("La respuesta correcta es:", pregunta['respuesta'])
            if (input("¿Quieres seguir singando? (s/n):").lower() != 's'):
                print("Puntos finales:" + str(puntos))
            salir = True


juego(cargar_preguntas())




