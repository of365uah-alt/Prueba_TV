print("Hola mundo")

import random
def metodo(s: str) -> int:
    tabla = []
    for i in range(10):
        tabla.append(random.randint(1,10))
        print(tabla)
    return 0

metodo("Hola")