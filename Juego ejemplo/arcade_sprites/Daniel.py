import arcade as arc
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arc.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Prueba Dibujo")
        arc.set_background_color((13, 26, 38, 255))

        # Posición inicial
        self.x = 100
        self.y = 450
        self.sprite_scale = 1.25
        self.tilt = 180

        # Velocidad (pixeles por segundo)
        self.change_x = 150
        self.change_y = 0

    def on_draw(self):
        self.clear()

        # Suelo
        arc.draw_lrbt_rectangle_filled(0, 800, 0, 200, (44, 87, 53))

        # Dibujar el ojo usando la posición actual
        self.draw_eye_of_cthulhu(self.x, self.y, self.sprite_scale, self.tilt)

    def on_update(self, delta_time):

        self.x += self.change_x * delta_time
        self.y += self.change_y * delta_time

    def draw_eye_of_cthulhu(self, x: float, y: float, scale: float, tilt: float) -> None:
        radius = 50 * scale

        tentacle_angle_1 = math.radians(45 - tilt)
        tentacle_angle_2 = math.radians(-45 - tilt)
        tentacle_angle_3 = math.radians(0 - tilt)

        eye_angle = math.radians(-tilt)

        # tentacle
        arc.draw_triangle_filled(
            x + radius * math.cos(tentacle_angle_1), y + radius * math.sin(tentacle_angle_1),
            x + radius * math.cos(tentacle_angle_2), y + radius * math.sin(tentacle_angle_2),
            x + 2.5 * radius * math.cos(tentacle_angle_3), y + 2.5 * radius * math.sin(tentacle_angle_3),
            (120, 24, 24)
        )

        # eye body
        arc.draw_circle_filled(x, y, radius, (227, 227, 227), 0, 100)
        arc.draw_circle_outline(x, y, radius, (120, 24, 24), 5 * scale, 0, 100)

        # eye
        arc.draw_ellipse_filled(x - 20 * scale * math.cos(eye_angle), y - 20 * scale * math.sin(eye_angle),
                                30 * scale, 45 * scale, (25, 53, 99), tilt, 100)
        arc.draw_ellipse_filled(x - 20 * scale * math.cos(eye_angle), y - 20 * scale * math.sin(eye_angle),
                                22.5 * scale, 35 * scale, (28, 82, 36), tilt, 100)
        arc.draw_ellipse_filled(x - 20 * scale * math.cos(eye_angle), y - 20 * scale * math.sin(eye_angle),
                                15 * scale, 25 * scale, (24, 24, 24), tilt, 100)


if __name__ == "__main__":
    juego = MiJuego()
    arc.run()