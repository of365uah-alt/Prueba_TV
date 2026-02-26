import arcade, math
from enum import Enum
from typing import Self


# --- APP CONSTANTS --- #

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 360

WINDOW_TITLE = "pong-prototype-0.3"


# --- WINDOW CLASS --- #

class PongGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.input_buffer = set()

        self.player_1 = Player(50, 142.5)
        self.player_2 = Player(580, 142.5)

        self.ball = Ball(320, 180, Vector2(2, 1))

    def on_update(self, delta_time: float):

        self.capture_input()

        self.player_1.update(delta_time)
        self.player_2.update(delta_time)

        self.ball.update(delta_time)

        self.check_player_ball_collision(self.player_1, delta_time)
        self.check_player_ball_collision(self.player_2, delta_time)

    def on_draw(self):

        self.clear()

        self.player_1.draw()
        self.player_2.draw()

        self.ball.draw()

    def check_player_ball_collision(self, player: "Player", delta_time: float):

        ball_x = self.ball.x
        ball_y = self.ball.y

        player_x = player.x
        player_y = player.y

        closest_x = max(player_x, min(ball_x, player_x + Player.WIDTH))
        closest_y = max(player_y, min(ball_y, player_y + Player.HEIGHT))

        dist_x = ball_x - closest_x
        dist_y = ball_y - closest_y

        if math.pow(dist_x, 2) + math.pow(dist_y, 2) <= math.pow(Ball.RADIUS, 2):
            self.ball.on_player_collision(player, Vector2(dist_x, dist_y), delta_time)


    def on_key_press(self, symbol: int, modifiers: int):
        self.input_buffer.add(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        self.input_buffer.discard(symbol)

    def capture_input(self):

        if arcade.key.W in self.input_buffer:
            self.player_1.set_y_dir(1)
        elif arcade.key.S in self.input_buffer:
            self.player_1.set_y_dir(-1)
        else:
            self.player_1.set_y_dir(0)

        if arcade.key.UP in self.input_buffer:
            self.player_2.set_y_dir(1)
        elif arcade.key.DOWN in self.input_buffer:
            self.player_2.set_y_dir(-1)
        else:
            self.player_2.set_y_dir(0)


# --- 2D VECTOR CLASS --- #

class Vector2:

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def module(self):
        return math.hypot(self.x, self.y)

    def normalized(self) -> Self:

        length = self.module()

        if length == 0:
            return type(self)(0.0, 0.0)

        x = self.x / length
        y = self.y / length

        return type(self)(x, y)

    def normalize(self):

        length = self.module()

        if length != 0:
            self.x /= length
            self.y /= length

    @staticmethod
    def dot(v1: "Vector2", v2: "Vector2") -> float:
        return v1.x * v2.x + v1.y * v2.y


# --- SURFACE TYPE ENUM --- #

class SurfaceType(Enum):

    HORIZONTAL_UP = Vector2(0, 1)
    HORIZONTAL_DOWN = Vector2(0, -1)
    VERTICAL_RIGHT = Vector2(1, 0)
    VERTICAL_LEFT = Vector2(-1, 0)

    def __init__(self, normal: Vector2):
        self.normal = normal


# --- PLAYER CLASS --- #

class Player:

    WIDTH = 10
    HEIGHT = 75

    SPEED = 300

    def __init__(self, x: float, y: float):

        self.x = x
        self.y = y

        self.y_dir = 0

    @property
    def collider(self) -> tuple:
        return self.x, self.y, self.x + Player.WIDTH, self.y + Player.HEIGHT

    def update(self, delta_time: float):

        self.update_pos(delta_time)

        if self.y < 0:
            self.y = 0

        if self.y + Player.HEIGHT > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - Player.HEIGHT

    def draw(self):

        arcade.draw_lbwh_rectangle_filled(
            self.x,
            self.y,
            Player.WIDTH,
            Player.HEIGHT,
            arcade.color.WHITE
        )

    def update_pos(self, delta_time: float):
        self.y += self.y_dir * Player.SPEED * delta_time

    def set_y_dir(self, y_dir: float):
        self.y_dir = y_dir


# --- BALL CLASS --- #

class Ball:

    RADIUS = 10
    SPEED = 400

    def __init__(self, x: float, y: float, facing_dir: Vector2):

        self.x = x
        self.y = y

        self.facing_dir = facing_dir.normalized()

    @property
    def collider(self) -> tuple:
        return self.x, self.y, Ball.RADIUS

    def update(self, delta_time: float):
        self.update_pos(delta_time)
        self.check_collision()

    def draw(self):

        arcade.draw_circle_filled(
            self.x,
            self.y,
            Ball.RADIUS,
            arcade.color.WHITE,
            0,
            100
        )

    def update_pos(self, delta_time: float):
        self.x += self.facing_dir.x * Ball.SPEED * delta_time
        self.y += self.facing_dir.y * Ball.SPEED * delta_time

    def check_collision(self):

        if self.y + Ball.RADIUS >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - Ball.RADIUS
            self.bounce(SurfaceType.HORIZONTAL_DOWN.normal)

        elif self.y - Ball.RADIUS <= 0:
            self.y = Ball.RADIUS
            self.bounce(SurfaceType.HORIZONTAL_UP.normal)

        if self.x + Ball.RADIUS >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - Ball.RADIUS
            self.bounce(SurfaceType.VERTICAL_LEFT.normal)

        elif self.x - Ball.RADIUS <= 0:
            self.x = Ball.RADIUS
            self.bounce(SurfaceType.VERTICAL_RIGHT.normal)

    def on_player_collision(self, player: Player, dist: Vector2, delta_time: float):

        abs_x = abs(dist.x)
        abs_y = abs(dist.y)

        self.fix_pos(player, dist, delta_time)

        if abs_x == abs_y:
            self.bounce(dist.normalized())
        elif abs_x > abs_y:
            self.bounce(Vector2(dist.x / abs_x, 0))
        else:
            self.bounce(Vector2(0, dist.y / abs_y))

    def fix_pos(self, player: Player, dist: Vector2, delta_time: float):

        penetration = Ball.RADIUS - dist.module()
        normal = dist.normalized()

        self.x += normal.x * penetration
        self.y += normal.y * penetration + player.y_dsir * Player.SPEED * delta_time


    def bounce(self, normal: Vector2):

        dot = Vector2.dot(self.facing_dir, normal)

        self.facing_dir.x = self.facing_dir.x - 2 * dot * normal.x
        self.facing_dir.y = self.facing_dir.y - 2 * dot * normal.y

        self.facing_dir.normalize()


# --- GAME START --- #

if __name__ == "__main__":
    game = PongGame()
    arcade.run()