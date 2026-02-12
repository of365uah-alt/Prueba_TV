# Juego: ¿De qué país de Latinoamérica serías?

print("🌎 Bienvenido al juego: ¿De qué país de Latinoamérica serías?")
print("Responde las siguientes preguntas escribiendo la letra de tu opción.\n")

paises = {
    "Mexico": 0,
    "Argentina": 0,
    "Colombia": 0,
    "Brasil": 0,
    "Chile": 0
}

def preguntar(pregunta, opciones):
    print(pregunta)
    for letra, texto, pais in opciones:
        print(f"{letra}) {texto}")
    respuesta = input("Tu respuesta: ").lower()
    for letra, texto, pais in opciones:
        if respuesta == letra:
            paises[pais] += 1
    print()

# Preguntas
preguntar("1. ¿Qué comida prefieres?",
          [("a", "Tacos", "Mexico"),
           ("b", "Asado", "Argentina"),
           ("c", "Arepas", "Colombia"),
           ("d", "Feijoada", "Brasil"),
           ("e", "Empanadas", "Chile")])

preguntar("2. ¿Qué clima te gusta más?",
          [("a", "Calor desértico", "Mexico"),
           ("b", "Templado", "Argentina"),
           ("c", "Tropical", "Colombia"),
           ("d", "Playero", "Brasil"),
           ("e", "Frío montañoso", "Chile")])

preguntar("3. ¿Qué música prefieres?",
          [("a", "Mariachi", "Mexico"),
           ("b", "Rock nacional", "Argentina"),
           ("c", "Reggaetón", "Colombia"),
           ("d", "Samba", "Brasil"),
           ("e", "Indie alternativo", "Chile")])

preguntar("4. ¿Qué bebida eliges?",
          [("a", "Tequila", "Mexico"),
           ("b", "Mate", "Argentina"),
           ("c", "Café", "Colombia"),
           ("d", "Caipirinha", "Brasil"),
           ("e", "Vino", "Chile")])

preguntar("5. ¿Qué paisaje prefieres?",
          [("a", "Desierto", "Mexico"),
           ("b", "Pampa", "Argentina"),
           ("c", "Selva", "Colombia"),
           ("d", "Playa", "Brasil"),
           ("e", "Cordillera", "Chile")])

preguntar("6. ¿Qué deporte te gusta más?",
          [("a", "Boxeo", "Mexico"),
           ("b", "Fútbol", "Argentina"),
           ("c", "Ciclismo", "Colombia"),
           ("d", "Vóley playa", "Brasil"),
           ("e", "Esquí", "Chile")])

preguntar("7. ¿De que color eres?",
          [("a", "Negro", "Mexico"),
           ("b", "Italiano", "Argentina"),
           ("c", "cocainomano", "Colombia"),
           ("d", "Futbol", "Brasil"),
           ("e", "Gay", "Chile")])

preguntar("8. ¿Qué dulce prefieres?",
          [("a", "Churros", "Mexico"),
           ("b", "Alfajores", "Argentina"),
           ("c", "Obleas", "Colombia"),
           ("d", "Brigadeiro", "Brasil"),
           ("e", "Kuchen", "Chile")])

preguntar("9. ¿Qué fiesta te gustaría vivir?",
          [("a", "Día de Muertos", "Mexico"),
           ("b", "Carnaval porteño", "Argentina"),
           ("c", "Feria de Cali", "Colombia"),
           ("d", "Carnaval de Río", "Brasil"),
           ("e", "Fiestas Patrias", "Chile")])

preguntar("10. ¿Qué color te representa más?",
          [("a", "Verde", "Mexico"),
           ("b", "Celeste", "Argentina"),
           ("c", "Amarillo", "Colombia"),
           ("d", "Verde y amarillo", "Brasil"),
           ("e", "Rojo", "Chile")])

# Resultado final
resultado = max(paises, key=paises.get)

print("🌟 Resultado final 🌟")
print(f"Según tus respuestas, serías de: {resultado} 🇱🇦")
