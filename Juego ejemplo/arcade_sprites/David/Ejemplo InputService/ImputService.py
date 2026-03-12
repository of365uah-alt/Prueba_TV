import math

import arcade
from pyglet.event import EVENT_HANDLE_STATE
import pathlib
import pyglet




print("Dispositivos totales detectados:", pyglet.input.get_devices())
class Personaje:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.vel = 5
        self.bCooldown = 0
        self.bTime = 0

    def draw(self) -> None:
        arcade.draw_circle_filled(self.x,self.y,12,arcade.color.BLACK,0)
        arcade.draw_circle_filled(self.x + 800,self.y,12,arcade.color.BLACK,0)
        arcade.draw_circle_filled(self.x - 800,self.y,12,arcade.color.BLACK,0)
        arcade.draw_circle_filled(self.x,self.y + 600,12,arcade.color.BLACK,0)
        arcade.draw_circle_filled(self.x,self.y - 600,12,arcade.color.BLACK,0)

    def logic(self, dt) -> None:
        if self.x > 900:
            self.x -= 800
        if self.x < -100:
            self.x += 800
        if self.y > 700:
            self.y -= 600
        if self.y < -100:
            self.y += 600
        if self.bTime <= 0:
            self.vel = 5
        self.bTime -= dt
        self.bCooldown -= dt


    def boost(self):
        if self.bCooldown < 0:
            self.bCooldown = 3
            self.bTime = 1
            self.vel = 12
    def up(self): self.y += self.vel
    def down(self): self.y -= self.vel
    def left(self): self.x -= self.vel
    def right(self): self.x += self.vel

    def move(self,x: float, y:float):
        self.x += (x * self.vel)
        self.y += (y * self.vel)


class Eye_chutulu:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.scale = 1
        self.tilt = 0

        self.diffX = 0
        self.diffY = 0

    def logic(self, dt, player):
        self.diffX = player.x - self.x
        self.diffY = player.y - self.y
        if self.diffX > 0 and self.diffY > 0:
            self.tilt = 180 - math.degrees(math.atan(self.diffY / self.diffX))
        elif self.diffX < 0 and self.diffY > 0:
             self.tilt = 180 - (90 + abs(math.degrees(math.atan(self.diffY / abs(self.diffX))) - 90))
        elif self.diffX < 0 and self.diffY < 0:
             self.tilt = 180 - (180 + abs(math.degrees(math.atan(abs(self.diffY) / self.diffX))))
        elif self.diffX > 0 and self.diffY < 0:
             self.tilt = 180 - (180 + abs(math.degrees(math.atan(abs(self.diffY) / abs(self.diffX)))))


    def draw(self) -> None:
        radius = 50 * self.scale

        tentacle_angle_1 = math.radians(45 - self.tilt)
        tentacle_angle_2 = math.radians(-45 - self.tilt)
        tentacle_angle_3 = math.radians(0 - self.tilt)

        eye_angle = math.radians(-self.tilt)

        # tentacle
        arcade.draw_triangle_filled(
            self.x + radius * math.cos(tentacle_angle_1), self.y + radius * math.sin(tentacle_angle_1),
            self.x + radius * math.cos(tentacle_angle_2), self.y + radius * math.sin(tentacle_angle_2),
            self.x + 2.5 * radius * math.cos(tentacle_angle_3), self.y + 2.5 * radius * math.sin(tentacle_angle_3),
            (120, 24, 24)
        )

        # eye body
        arcade.draw_circle_filled(self.x, self.y, radius, (227, 227, 227), 0, 100)
        arcade.draw_circle_outline(self.x, self.y, radius, (120, 24, 24), 5 * self.scale, 0, 100)

        # eye
        arcade.draw_ellipse_filled(self.x - 20 * self.scale * math.cos(eye_angle), self.y - 20 * self.scale * math.sin(eye_angle),
                                30 * self.scale, 45 * self.scale, (25, 53, 99), self.tilt, 100)
        arcade.draw_ellipse_filled(self.x - 20 * self.scale * math.cos(eye_angle), self.y - 20 * self.scale * math.sin(eye_angle),
                                22.5 * self.scale, 35 * self.scale, (28, 82, 36), self.tilt, 100)
        arcade.draw_ellipse_filled(self.x - 20 * self.scale * math.cos(eye_angle), self.y - 20 * self.scale * math.sin(eye_angle),
                                15 * self.scale, 25 * self.scale, (24, 24, 24), self.tilt, 100)



class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Mi Juego")
        arcade.set_background_color(arcade.color.CYAN)

        self.eye = Eye_chutulu()
        self.personaje = Personaje()

        #movement logic
        self.mUP = False
        self.mDOWN = False
        self.mLEFT = False
        self.mRIGHT = False

        # Primero intentamos usar la función de mandos de pyglet
        controladores = pyglet.input.get_controllers()

        if controladores:
            self.joystick = controladores[0]
            self.joystick.open()
            self.joystick.push_handlers(self)
            print("¡Mando detectado (Controller)!:", self.joystick)
        else:
            # Si falla, buscamos exactamente ese "XInput0" que vimos en tu consola
            dispositivos = pyglet.input.get_devices()
            mandos_xinput = [d for d in dispositivos if d.name == "XInput0"]

            if mandos_xinput:
                self.joystick = mandos_xinput[0]
                self.joystick.open()
                # self.joystick.push_handlers(self) # A veces no es necesario en este nivel
                print("¡Mando detectado (Directo)!:", self.joystick.name)
            else:
                print("No joystick")
                self.joystick = None



    def on_update(self, delta_time: float) -> bool | None:
        self.eye.logic(delta_time, self.personaje)

        if self.mUP:
            self.personaje.up()
        if self.mDOWN:
            self.personaje.down()
        if self.mLEFT:
            self.personaje.left()
        if self.mRIGHT:
            self.personaje.right()

        if self.joystick:
            self.personaje.move(self.joystick.leftx, self.joystick.lefty)
            if self.joystick.a:  # Si la 'A' está pulsada
                self.personaje.boost()


        self.personaje.logic(delta_time)

    def on_key_press(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if symbol == arcade.key.W: self.mUP = True
        if symbol == arcade.key.S: self.mDOWN = True
        if symbol == arcade.key.D: self.mRIGHT = True
        if symbol == arcade.key.A: self.mLEFT = True
        if symbol == arcade.key.SPACE: self.personaje.boost()
    def on_key_release(self, symbol: int, modifiers: int) -> EVENT_HANDLE_STATE:
        if symbol == arcade.key.W: self.mUP = False
        if symbol == arcade.key.S: self.mDOWN = False
        if symbol == arcade.key.D: self.mRIGHT = False
        if symbol == arcade.key.A: self.mLEFT = False


    def on_draw(self) -> EVENT_HANDLE_STATE:
        self.clear()
        self.eye.draw()
        self.personaje.draw()

juego = MiJuego()
arcade.run()