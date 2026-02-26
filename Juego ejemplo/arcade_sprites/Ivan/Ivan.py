import arcade
import random

ANCHO = 800
ALTO = 800
VELOCIDAD = 4
ANCHO_EDIFICIO = 90


class Juego(arcade.Window):

    def __init__(self):
        super().__init__(ANCHO, ALTO, "Hyperphoria - Retrofuture")
        arcade.set_background_color((10, 0, 30))

        self.edificios = []
        self.estrellas = []
        self.lineas_carretera = []

        # Crear estrellas
        for _ in range(80):
            self.estrellas.append((random.randint(0, ANCHO),
                                   random.randint(400, ALTO)))

        # Crear edificios iniciales
        x = 0
        while x < ANCHO:
            self.edificios.append({
                "x": x,
                "altura": random.randint(200, 400),
                "color": random.choice([(0,255,255),(255,0,255),(0,150,255)])
            })
            x += random.randint(120, 200)

        # Líneas de carretera
        for i in range(10):
            self.lineas_carretera.append(i * 120)

    # -------------------------
    # DIBUJADO
    # -------------------------
    def on_draw(self):
        self.clear()
        self.fondo()
        self.dibujar_edificios()
        self.carretera()
        self.coche()

    # -------------------------
    # UPDATE
    # -------------------------
    def on_update(self, delta_time):

        # Mover edificios a la izquierda
        for edificio in self.edificios:
            edificio["x"] -= VELOCIDAD

        # Eliminar edificios fuera
        if self.edificios and self.edificios[0]["x"] < -ANCHO_EDIFICIO:
            self.edificios.pop(0)

        # Crear nuevos edificios por la derecha
        if self.edificios:
            ultimo = self.edificios[-1]
            if ultimo["x"] < ANCHO - 150:
                self.edificios.append({
                    "x": ANCHO + random.randint(50,150),
                    "altura": random.randint(200, 400),
                    "color": random.choice([(0,255,255),(255,0,255),(0,150,255)])
                })

        # Animar líneas de carretera
        for i in range(len(self.lineas_carretera)):
            self.lineas_carretera[i] -= VELOCIDAD * 2
            if self.lineas_carretera[i] < -100:
                self.lineas_carretera[i] = ANCHO

    # -------------------------
    # FONDO
    # -------------------------
    def fondo(self):

        # Sol retro con líneas
        arcade.draw_circle_filled(400, 550, 130, (255, 60, 120))
        for i in range(0, 130, 15):
            arcade.draw_line(270, 550 - i,
                             530, 550 - i,
                             (255, 120, 180), 3)

        # Estrellas
        for estrella in self.estrellas:
            arcade.draw_circle_filled(estrella[0], estrella[1], 2, arcade.color.WHITE)

    # -------------------------
    # EDIFICIOS
    # -------------------------
    def dibujar_edificios(self):
        for edificio in self.edificios:
            x = edificio["x"]
            altura = edificio["altura"]
            color = edificio["color"]

            arcade.draw_lbwh_rectangle_filled(x, 250, ANCHO_EDIFICIO, altura, color)

            # Ventanas iluminadas aleatorias
            for y in range(0, altura, 25):
                if random.random() > 0.3:
                    arcade.draw_lbwh_rectangle_filled(
                        x + 10, 260 + y,
                        ANCHO_EDIFICIO - 20, 5,
                        (255, 255, 120)
                    )

    # -------------------------
    # CARRETERA
    # -------------------------
    def carretera(self):
        arcade.draw_lbwh_rectangle_filled(0, 0, ANCHO, 250, (20, 0, 40))

        for x in self.lineas_carretera:
            arcade.draw_lbwh_rectangle_filled(x, 120, 80, 8, (255, 0, 200))

    # -------------------------
    # COCHE RETRO
    # -------------------------
    def coche(self):

        # Sombra
        arcade.draw_ellipse_filled(400, 180, 250, 40, (0,0,0,120))

        # Carrocería
        arcade.draw_lbwh_rectangle_filled(300, 200, 200, 40, (0, 255, 255))
        arcade.draw_triangle_filled(450, 240, 500, 240, 470, 280, (255, 0, 255))

        # Ventanas
        arcade.draw_lbwh_rectangle_filled(340, 230, 70, 25, (100, 0, 150))
        arcade.draw_lbwh_rectangle_filled(415, 230, 40, 25, (100, 0, 150))

        # Ruedas
        arcade.draw_circle_filled(340, 200, 22, arcade.color.BLACK)
        arcade.draw_circle_filled(460, 200, 22, arcade.color.BLACK)
        arcade.draw_circle_outline(340, 200, 22, (0,255,255), 3)
        arcade.draw_circle_outline(460, 200, 22, (0,255,255), 3)


# -------------------------
# EJECUCIÓN
# -------------------------
if __name__ == "__main__":
    ventana = Juego()
    arcade.run()
