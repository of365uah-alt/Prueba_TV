import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tanque"
class player:
    def __init__(self,x,y,dx,dy,dirx,diry):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.dirx = dirx
        self.diry = diry
    def update(self):
        self.x += self.dx
        self.y += self.dy
    def dibujar(self):
        arcade.draw.draw_triangle_outline(self.x-10,self.y-10,self.x+10,self.y-10,self.x+10,self.y,arcade.color.WHITE,5)
        arcade.draw_circle_filled(self.x,self.y,12.5,arcade.color.WHITE)
        arcade.draw_line(self.x,self.y,self.x+self.dirx,self.y+self.diry,arcade.color.WHITE,10)
class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.player1 = player(300,300,0,0,0,0) 
        controllers = arcade.get_controllers()
        if controllers:
            self.controller = controllers[0]
            self.controller.open()
        else:
            print("There are no controllers.")
            self.controller = None
 
    def on_draw(self):
        self.clear()
        self.player1.dibujar()
    def on_update(self, delta_time):
        if self.controller:
            self.player1.dx = self.controller.leftx*10
            self.player1.dy = self.controller.lefty*10
            self.player1.dirx = self.controller.rightx*20
            self.player1.diry = self.controller.righty*20
        self.player1.update()
        limites(self.player1,SCREEN_HEIGHT,SCREEN_WIDTH)

def limites(player,alto,ancho):
    if player.x < 0:
        player.x = 0
    elif player.x > ancho:
        player.x = ancho
    if player.y < 0:
        player.y = 0
    elif player.y > alto:
        player.y = alto

def main():
    window = MiJuego()
    arcade.run()
main()