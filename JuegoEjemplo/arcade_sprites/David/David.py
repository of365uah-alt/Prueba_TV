import arcade
from pyglet.event import EVENT_HANDLE_STATE
import pathlib

# Abrimos la ventana
Nave = pathlib.Path('Assets/Nave.png')


class Luna:
    def __init__(self,x,y):
        self.x =x
        self.y = y

    def draw(self):
        arcade.draw.circle.draw_circle_filled(self.x, self.y, 70, arcade.color.WHITE_SMOKE)
        arcade.draw.circle.draw_circle_filled(self.x + 20, self.y - 30, 15, arcade.color.GRAY)
        arcade.draw.circle.draw_circle_filled(self.x - 15, self.y + 20, 30, arcade.color.GRAY)
        arcade.draw.circle.draw_circle_filled(self.x - 30, self.y - 35, 10, arcade.color.GRAY)


class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Mi Juego")
        self.luna_movingDown = None
        self.luna_movingRight = None
        self.luna_movingLeft = None

        self.luna = Luna(200,200)

        self.luna_velocidad = 2
        arcade.set_background_color(arcade.color.BLACK)
        self.luna_movingUp =  False

        #sprites
        self.sprites = arcade.SpriteList()

        self.playerModel = arcade.Sprite(Nave)
        self.playerModel.scale = 0.05
        self.playerModel.position = self.center
        self.sprites.append(self.playerModel)


    def on_update(self, delta_time: float) -> bool | None:
        if self.luna_movingUp:
            self.luna.y += self.luna_velocidad
        if self.luna_movingDown:
            self.luna.y -= self.luna_velocidad
        if self.luna_movingLeft:
            self.luna.x -= self.luna_velocidad
        if self.luna_movingRight:
            self.luna.x += self.luna_velocidad


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

    def on_draw(self) -> EVENT_HANDLE_STATE:
        self.clear()
        self.luna.draw()
        self.sprites.draw()
juego = MiJuego()
arcade.run()