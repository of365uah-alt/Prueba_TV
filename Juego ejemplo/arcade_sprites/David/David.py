import arcade
from pyglet.event import EVENT_HANDLE_STATE


# Abrimos la ventana


class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Mi Juego")
        arcade.set_background_color(arcade.color.BLACK)
    #Luna
    def dibujar_luna(self,x: int, y: int):
        arcade.draw.circle.draw_circle_filled(x, y, 70, arcade.color.WHITE_SMOKE)
        arcade.draw.circle.draw_circle_filled(x + 20, y - 30, 15, arcade.color.GRAY)
        arcade.draw.circle.draw_circle_filled(x - 15, y + 20, 30, arcade.color.GRAY)
        arcade.draw.circle.draw_circle_filled(x - 30, y - 35, 10, arcade.color.GRAY)
    def on_draw(self) -> EVENT_HANDLE_STATE:
        self.clear()
        self.dibujar_luna(300, 300)
juego = MiJuego()
arcade.run()