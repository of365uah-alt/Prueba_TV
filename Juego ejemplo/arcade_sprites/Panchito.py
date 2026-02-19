import arcade
import time



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color((3, 194, 252))

        # Posición inicial del tanque
        self.x = 50
        self.y = 200
        self.sprite_scale = 0.5

        # Velocidad del tanque
        self.speed = 100  # píxeles por segundo


    def draw_tank(self,x,y, scale):
            # dibuja el tanque
            ## cuerpo del tanque
            arcade.draw_lbwh_rectangle_filled(x,y, 200*scale, 75*scale, (44, 71, 48)) 
            arcade.draw_lbwh_rectangle_filled(x+50*scale, y+75*scale, 100*scale, 25*scale, (44, 71, 48))

            # ruedas del tanque
            arcade.draw_circle_filled(x+25*scale, y, 25*scale, (73, 105, 89))
            arcade.draw_circle_filled(x+75*scale, y, 25*scale, (73, 105, 89))
            arcade.draw_circle_filled(x+125*scale, y, 25*scale, (73, 105, 89))
            arcade.draw_circle_filled(x+175*scale, y, 25*scale, (73, 105, 89))
            arcade.draw_arc_outline(x+25*scale, y, 50*scale, 50*scale, (13, 15, 14), 90, 270, 10*scale)
            arcade.draw_arc_outline(x+175*scale, y, 50*scale, 50*scale, (13, 15, 14), 90, 270, 10*scale, 180)
            arcade.draw_line(x+25*scale, y+25*scale, x+175*scale, y+25*scale, (13, 15, 14), 5*scale)
            arcade.draw_line(x+25*scale, y-25*scale, x+175*scale, y-25*scale, (13, 15, 14), 5*scale)

            # Cañon del tanque
            arcade.draw_line(x +150*scale, y+82*scale, x+250*scale, y+82*scale, (44, 71, 48), 10*scale)

    def on_draw(self):
        self.clear()
        arcade.draw_lbwh_rectangle_filled(0, 0, 1200, 250, (255, 221, 0)) # dibuja el suelo
        self.draw_tank( self.x, self.y, self.scale)

    def on_update(self, delta_time):
        self.x += self.speed * delta_time


if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()