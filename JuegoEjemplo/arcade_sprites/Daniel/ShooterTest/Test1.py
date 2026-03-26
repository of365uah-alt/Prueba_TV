import math, arcade

from pyglet.event import EVENT_HANDLE_STATE

from JuegoEjemplo.arcade_sprites.Daniel.ShooterTest.geometry import Vector2, Direction


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

WINDOW_TITLE = "Test 1"


class Test1(arcade.Window):

    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.center_window()

        # super().set_update_rate(1/240)
        # super().set_draw_rate(1/240)

        self.fps_txt = arcade.Text("", 10, WINDOW_HEIGHT - 22, arcade.color.WHITE, 12)
        self.fps_display_counter = 0.0
        self.update_rate = 0.5

        self.player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.reticle = Reticle(0, 0)

        self.inputs = set()
        self.mouse_inputs = set()

        self.mouse_pos = Vector2.zero()

        self.bullets: set[Bullet] = set()

        self.reticle.show()
        self.set_mouse_visible(False)

        self.attack_counter = 0
        self.attack_cooldown = 0.35

    def on_draw(self):

        self.clear()

        for bullet in self.bullets:
            bullet.draw()

        self.player.draw()
        self.reticle.draw()

        self.fps_txt.draw()

    def update_fps_display(self, delta_time: float):

        self.fps_display_counter += delta_time

        if self.fps_display_counter >= self.update_rate:
            self.fps_txt.text = f"FPS: {round(1 / delta_time)}"
            self.fps_display_counter = 0.0

    def on_update(self, delta_time: float):

        if self.player.is_moving():
            self.update_player_rotation()

        self.player.update(delta_time)

        for bullet in self.bullets:
            bullet.update(delta_time)
        self.check_bullets_life_time()

        self.check_inputs()

        self.update_fps_display(delta_time)

        if self.attack_counter > 0:
            self.attack_counter -= delta_time
        else:
            if arcade.MOUSE_BUTTON_LEFT in self.mouse_inputs:
                self.check_mouse_inputs()
                self.attack_counter = self.attack_cooldown

    def on_key_press(self, symbol: int, modifiers: int):
        self.inputs.add(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in self.inputs:
            self.inputs.remove(symbol)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):

        self.mouse_pos = Vector2(x, y)

        self.update_player_rotation()
        self.reticle.update_pos(x, y)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button not in self.mouse_inputs:
            self.mouse_inputs.add(button)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button in self.mouse_inputs:
            self.mouse_inputs.remove(button)

    def fire_bullet(self):

        bullet_speed = 600
        bullet_life_time = 2000

        player_facing_dir = self.player.facing_direction
        pos = self.player.get_pos() + player_facing_dir * self.player.player_dimensions["cannon_length"]

        player_motion = self.player.movement_direction * self.player.base_movement_speed
        post_momentum = player_facing_dir * bullet_speed + 0.25 * player_motion

        bullet = Bullet(pos.x, pos.y, post_momentum.length(), bullet_life_time)
        bullet.set_moving(post_momentum.normalized())

        self.bullets.add(bullet)

    def update_player_rotation(self):
        self.player.set_facing_dir(Vector2.distance(self.player.get_pos(), self.mouse_pos))

    def check_bullets_life_time(self):

        expired_bullets = set()

        for bullet in self.bullets:

            if bullet.can_destroy:
                expired_bullets.add(bullet)

        self.bullets -= expired_bullets

    def check_inputs(self):

        if not self.inputs:
            self.player.set_moving(Vector2.zero())
            return

        x, y = 0, 0

        if arcade.key.W in self.inputs:
            y += 1
        if arcade.key.S in self.inputs:
            y -= 1
        if arcade.key.D in self.inputs:
            x += 1
        if arcade.key.A in self.inputs:
            x -= 1

        self.player.set_moving(Vector2(x, y))

    def check_mouse_inputs(self):

        if arcade.MOUSE_BUTTON_LEFT in self.mouse_inputs:
            self.fire_bullet()



class Player:

    def __init__(self, x: float, y: float):

        self.x = x
        self.y = y

        self.player_dimensions = {
            "body_radius": 30,
            "cannon_length": 35,
            "cannon_width": 30
        }

        self.player_colors = {
            "body_filling": (78, 136, 216),
            "body_outline": (30, 73, 132),
            "cannon_filling": (168, 168, 168),
            "cannon_outline": (120, 120, 120)
        }

        self.facing_direction = Vector2.from_dir(Direction.EAST)

        self.movement_direction = Vector2.zero()
        self.base_movement_speed: float = 300.0
        self.movement_speed_multiplier: float = 1

    def get_pos(self) -> Vector2:
        return Vector2(self.x, self.y)

    def is_moving(self) -> bool:
        return self.movement_direction != Vector2.zero()

    def update(self, delta_time: float):
        if self.is_moving():
            self.update_pos(delta_time)

    def set_moving(self, direction: Vector2):
        self.movement_direction = direction.normalized()

    def set_facing_dir(self, direction: Vector2):
        if direction != Vector2.zero():
            self.facing_direction = direction.normalized()

    def update_pos(self, delta_time: float):

        movement = self.base_movement_speed * self.movement_speed_multiplier * delta_time

        self.x += movement * self.movement_direction.x
        self.y += movement * self.movement_direction.y

    def draw(self):
        self.draw_cannon()
        self.draw_body()

    def draw_body(self):

        body_radius = self.player_dimensions["body_radius"]

        circle_segments = 100
        outline_width = 5

        arcade.draw_circle_filled(
            self.x, self.y, body_radius,
            self.player_colors["body_filling"],

            num_segments=circle_segments
        )

        arcade.draw_circle_outline(
            self.x, self.y, body_radius,
            self.player_colors["body_outline"],

            num_segments=circle_segments,
            border_width=outline_width
        )

    def draw_cannon(self):

        body_radius = self.player_dimensions["body_radius"]
        cannon_length = self.player_dimensions["cannon_length"]
        cannon_width = self.player_dimensions["cannon_width"]

        outline_width = 5

        pivot = Vector2(self.x, self.y)
        perp = self.facing_direction.perpendicular()

        angle_buffer = math.atan2((cannon_width / 2), body_radius)
        offset_x = body_radius * math.cos(angle_buffer) * 0.85

        vertex_1 = pivot + self.facing_direction * offset_x - perp * (cannon_width / 2)
        vertex_2 = pivot + self.facing_direction * offset_x + perp * (cannon_width / 2)
        vertex_3 = pivot + self.facing_direction * (offset_x + cannon_length) - perp * (cannon_width / 2)
        vertex_4 = pivot + self.facing_direction * (offset_x + cannon_length) + perp * (cannon_width / 2)

        arcade.draw_polygon_filled(
            [vertex_1, vertex_2, vertex_4, vertex_3],
            self.player_colors["cannon_filling"]
        )

        arcade.draw_polygon_outline(
            [vertex_1, vertex_2, vertex_4, vertex_3],
            self.player_colors["cannon_outline"],

            line_width=outline_width
        )


class Reticle:

    def __init__(self, x: float, y: float):

        self.x = x
        self.y = y

        self.hidden = True

    def update_pos(self, x: float, y: float):
        self.x = x
        self.y = y

    def show(self):
        self.hidden = False

    def hide(self):
        self.hidden = True

    def draw(self):

        if self.hidden:
            return

        line_length = 5
        line_offset = 5

        points = [
            (self.x, self.y + line_offset), (self.x, self.y + (line_offset + line_length)),
            (self.x, self.y - line_offset), (self.x, self.y - (line_offset + line_length)),
            (self.x + line_offset, self.y), (self.x + (line_offset + line_length), self.y),
            (self.x - line_offset, self.y), (self.x - (line_offset + line_length), self.y)
        ]

        arcade.draw_lines(points, arcade.color.WHITE, 2)


class Bullet:

    def __init__(self, x: float, y: float, speed: float, life_time: float):

        self.x = x
        self.y = y

        self.radius = 15

        self.movement_direction = Vector2.zero()
        self.movement_speed = speed

        self.life_time = life_time
        self.counter = 0

        self.can_destroy = False

    def is_moving(self) -> bool:
        return self.movement_direction != Vector2.zero()

    def update(self, delta_time: float):

        if self.can_destroy:
            return

        if self.counter >= self.life_time:
            self.can_destroy = True
            return

        if self.is_moving():
            self.update_pos(delta_time)

        self.counter += delta_time * 1000

    def set_moving(self, direction: Vector2):
        self.movement_direction = direction.normalized()

    def update_pos(self, delta_time: float):

        movement = self.movement_speed * delta_time

        self.x += movement * self.movement_direction.x
        self.y += movement * self.movement_direction.y

    def draw(self):

        arcade.draw_circle_filled(
            self.x, self.y, self.radius,
            (224, 66, 66),

            num_segments=100
        )

        arcade.draw_circle_outline(
            self.x, self.y, self.radius,
            (89, 21, 21),

            num_segments=100,
            border_width=5
        )


if __name__ == "__main__":
    game = Test1()
    arcade.run()