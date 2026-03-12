# kybor
import arcade

# Dimensiones de la ventana
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "mover teclado"



class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.player1 = player(300,300,0,0,10) 
        controllers = arcade.get_controllers()
        if controllers:
            self.controller = controllers[0]
            self.controller.open()
        else:
            print("There are no controllers.")
            self.controller = None
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player1.dy = 10
        elif key == arcade.key.DOWN:
            self.player1.dy = -10
        elif key == arcade.key.LEFT:
            self.player1.dx = -10
        elif key == arcade.key.RIGHT:
            self.player1.dx = 10
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player1.dy = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player1.dx = 0
    

    def on_draw(self):
        self.clear()
        self.player1.dibujar()


    def on_update(self, delta_time):
        if self.controller:
            self.player1.dx = self.controller.leftx*10
            self.player1.dy = self.controller.lefty*10
        self.player1.update()
        limites(self.player1,SCREEN_HEIGHT,SCREEN_WIDTH)

class player:
    def __init__(self,x,y,dx,dy,radius):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
    
    def dibujar(self):
        arcade.draw_circle_filled(self.x,self.y,self.radius,arcade.color.WHITE)

    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        

def main():
    window = MiJuego()
    arcade.run()
def limites(player,alto,ancho):
    if player.x < 0 + player.radius:
        player.x = 0 + player.radius
    elif player.x > ancho - player.radius:
        player.x = ancho - player.radius
    if player.y < 0 + player.radius:
        player.y = 0 + player.radius
    elif player.y > alto - player.radius:
        player.y = alto - player.radius

main()