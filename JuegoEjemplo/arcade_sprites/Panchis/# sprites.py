# sprites
import arcade
import random as rd
from pathlib import Path
cdir = Path(__file__).parent
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Cheese Collector"
class player:
    def __init__(self,x,y,dx,dy,dirx,diry,player_list , player_sprite):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.dirx = dirx
        self.diry = diry
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.SpriteList()
    def update(self):
        self.x += self.dx
        self.y += self.dy

    def dibujar(self):
        self.player_sprite.draw()
    def setup(self):
        self.player_sprite = arcade.Sprite(Path(cdir / "jane.png"), 0.02)
        self.player_sprite.center_x = self.x
        self.player_sprite.center_y = self.y
        self.player_list.append(self.player_sprite)

class MiJuego(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        

        self.coin_list = None


        self.player = player(300,300,0,0,0,0,None,None) 
        self.score = 0

        self.score_tx = None

        self.set_mouse_cursor(None)
        
        arcade.set_background_color(arcade.color.BLACK)
        controllers = arcade.get_controllers()
        if controllers:
            self.controller = controllers[0]
            self.controller.open()
        else:
            print("There are no controllers.")
            self.controller = None

        

    def setup(self):
        self.player.setup()



        self.score_tx = arcade.Text("", 10, 590, arcade.color.WHITE, 14)

        for i in range(50):
            coin = arcade.Sprite(Path(cdir / "cheese.png"), 0.02)
            coin.center_x = rd.randrange(SCREEN_WIDTH)
            coin.center_y = rd.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player.dy = 10
        elif key == arcade.key.S:
            self.player.dy = -10
        elif key == arcade.key.A:
            self.player.dx = -10
        elif key == arcade.key.D:
            self.player.dx = 10
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player.dy = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player.dx = 0
 
    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.coin_list.draw()
        self.score_tx.draw()
        

    def on_update(self, delta_time):
        if self.controller:
            self.player.dx = self.controller.leftx*10
            self.player.dy = self.controller.lefty*10
            self.player.dirx = self.controller.rightx*20
            self.player.diry = self.controller.righty*20
        self.player.update()
        self.score_tx.text = f"Score: {self.score}"
        limites(self.player,SCREEN_HEIGHT,SCREEN_WIDTH)

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
    window.setup()
    arcade.run()
main()