import math

import arcade
from pyglet.event import EVENT_HANDLE_STATE
import pathlib

# Abrimos la ventana
class Avion:
    def __init__(self,x,y,v,dirr):
        self.x = x
        self.y = y
        self.dir = dirr
        self.v = v
        self.lockeado = False

    def draw(self):
        if self.dir == 0:
            self.x = self.x + self.v
        else:
            self.x = self.x - self.v
        arcade.draw_point(self.x,self.y,arcade.color.BLACK,size=10)

class MisilDA:
    def __init__(self,x:int,y:int,target:Avion):

        self.x = x
        self.y = y

        self.vx = 0
        self.vy = 0

        self.vcooldown = 0

        self._maxv = 5

        self.size = 5
        self.color = arcade.color.BLACK
        self.target = target

        self.targetx = target.x
        self.targety = target.y

        self.tvx = 0
        self.tvy = 0

        self.velocidadSam = 0

        self.distaciaInicial = ((self.target.x-self.x)**2+(self.target.y-self.y)**2) **0.5

        self.velocidadDiffX = self.tvx - self.vx
        self.velocidadDiffY = self.tvy - self.tvy

        self.tiempoX = 0
        self.tiempoY = 0

        self.predictX = 0
        self.predictY = 0

    def draw(self):

        if self.tvx == 0:
            self.tvx = self.target.x-self.targetx
            self.tvy = self.target.y-self.targety


        self.velocidadSam = ((self.target.x-self.x)**2+(self.target.y-self.y)**2) **0.5 - self.distaciaInicial
        self.distaciaInicial = ((self.target.x-self.x)**2+(self.target.y-self.y)**2) **0.5

        self.x = self.x + self.vx
        self.y = self.y + self.vy

        arcade.draw_point(self.x,self.y,self.color,self.size)
        self.velocidadDiffX = abs(self.tvx - self.vx)
        self.velocidadDiffY = abs(self.tvy - self.vy)
        self.tiempoX = abs((self.x - self.predictX)/(self.velocidadDiffX + 0.5))
        self.tiempoY = abs((self.y - self.target.y)/(self.velocidadDiffY + 0.5))
        self.predictX = self.target.x + (self.velocidadDiffY * self.tiempoY)
        self.move(self.predictX,self.target.y)


    def move(self,nx,ny):
        if self.vcooldown == 0:
            print(self.target.x,self.velocidadDiffX *self.tiempoX,self.velocidadDiffY * self.tiempoY)
            if nx > self.x:
                if self.vx < self._maxv:
                    self.vx += 1
            else:
                if self.vx > -self._maxv:
                    self.vx -= 1
            if ny > self.y:
                if (ny - self.y) >= 3*(self.vy * (self.vy + 1)) / 2:
                    if self.vy < self._maxv:
                        self.vy += 1
                else:
                    self.vy -= 1
            else:
                if self.vy > -self._maxv:
                    self.vy -= 1
            self.vcooldown = 2
        else:
            self.vcooldown -= 1




class Sams:
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        self.size = 15
        self.delay = 0
    def draw(self):
        arcade.draw_point(self.X,self.Y,arcade.color.WHITE_SMOKE,self.size)
        if self.delay > 0:
            self.delay = self.delay - 1
    def lanzar(self, target:Avion):
        misil = MisilDA(self.X,self.Y,target)
        self.delay = 120
        return misil

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Mi Juego",draw_rate=0.1 ,update_rate=0.1)
        arcade.set_background_color(arcade.color.CYAN)

        #sprites
        self.baseSprites = arcade.SpriteList()
        self.baseSprites.append(arcade.text.create_text_sprite("Epstein", arcade.color.BLACK, 32, align="right"))

        self.sams = [Sams(200,200), Sams(400,200),Sams(600,200)]
        self.misilesDA = []

        self.aviones = []
        self.aviones.append(Avion(0,500,3,0))




#    def on_update(self, delta_time: float) -> bool | None:
#        if self.luna_movingUp:
#        if self.luna_movingDown:
#        if self.luna_movingLeft:
#        if self.luna_movingRight:

#    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
#        if symbol == arcade.key.W:
#        if symbol == arcade.key.S:
#        if symbol == arcade.key.D:
#        if symbol == arcade.key.A:
#    def on_key_release(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
#        if symbol == arcade.key.W:
#        if symbol == arcade.key.S:
#        if symbol == arcade.key.D:
#        if symbol == arcade.key.A:

    def on_draw(self) -> EVENT_HANDLE_STATE:
        self.clear()
        arcade.draw.draw_lbwh_rectangle_filled(0,0,800,200,arcade.color.GREEN_YELLOW)
        self.baseSprites.draw()
        for i in self.sams:
            i.draw()
            if i.delay <= 0:
                for j in self.aviones:
                    if not j.lockeado:
                        self.misilesDA.append(i.lanzar(j))
                        j.lockeado = True
        for i in self.misilesDA:
            i.draw()

        for i in self.aviones:
            i.draw()
            if i.x < 0:
                self.aviones.remove(i)
            elif i.x > 800:
                self.aviones.remove(i)

        #tierra
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> EVENT_HANDLE_STATE:
        self.aviones.append(Avion(0,500,3,0))
        #print(len(self.aviones))



juego = MiJuego()
arcade.run()