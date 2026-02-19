import arcade
from pyglet.event import EVENT_HANDLE_STATE


# Abrimos la ventana


class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Mi Juego")
        self.luna_movingDown = None
        self.luna_movingRight = None
        self.luna_movingLeft = None

        self.velocidad = 2
        arcade.set_background_color(arcade.color.BLACK)
        self.lunax = 300
        self.lunay = 300
        self.luna_movingUp =  False


    #Luna
    def dibujar_luna(self,x: int, y: int):
        arcade.draw.circle.draw_circle_filled(x, y, 70, arcade.color.WHITE_SMOKE)
        arcade.draw.circle.draw_circle_filled(x + 20, y - 30, 15, arcade.color.GRAY)
        arcade.draw.circle.draw_circle_filled(x - 15, y + 20, 30, arcade.color.GRAY)
        arcade.draw.circle.draw_circle_filled(x - 30, y - 35, 10, arcade.color.GRAY)

    def on_update(self, delta_time: float) -> bool | None:
        if self.luna_movingUp:
            self.lunay += self.velocidad
        if self.luna_movingDown:
            self.lunay -= self.velocidad
        if self.luna_movingLeft:
            self.lunax -= self.velocidad
        if self.luna_movingRight:
            self.lunax += self.velocidad


    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if symbol == arcade.key.W:
            self.luna_movingUp = True
        if symbol == arcade.key.S:
            self.luna_movingDown = True
        if symbol == arcade.key.D:
            self.luna_movingRight = True
        if symbol == arcade.key.A:
            self.luna_movingLeft = True
    def on_key_release(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if symbol == arcade.key.W:
            self.luna_movingUp = False
        if symbol == arcade.key.S:
            self.luna_movingDown = False
        if symbol == arcade.key.D:
            self.luna_movingRight = False
        if symbol == arcade.key.A:
            self.luna_movingLeft = False
  #  def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> EVENT_HANDLE_STATE:
   #     self.lunax = x
    #    self.lunay = y

    def on_draw(self) -> EVENT_HANDLE_STATE:
        self.clear()
        self.dibujar_luna(self.lunax, self.lunay)
juego = MiJuego()
arcade.run()