import arcade, random

from JuegoEjemplo.arcade_sprites.Daniel.ShooterTest.geometry import Vector2

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

WINDOW_TITLE = "Sprites"


PLAYER_SPRITE_SCALING = 2
CHEESE_SPRITE_SCALING = 0.15

CHEESE_COUNT = 50


class SpritesTest(arcade.Window):

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        self.score = 0
        self.score_txt = None

        self.player_sprite = None

        self.player_list = None
        self.cheese_list = None

        self.inputs = set()

        self.set_mouse_visible(False)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.cheese_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("player.png", PLAYER_SPRITE_SCALING)
        self.player_sprite.center_x = WINDOW_WIDTH / 2
        self.player_sprite.center_y = WINDOW_HEIGHT / 2

        self.player_list.append(self.player_sprite)

        for i in range(0, CHEESE_COUNT):

            cheese = arcade.Sprite("cheese.png", CHEESE_SPRITE_SCALING)

            cheese.center_x = random.randrange(WINDOW_WIDTH)
            cheese.center_y = random.randrange(WINDOW_HEIGHT)

            self.cheese_list.append(cheese)

        self.score_txt = arcade.Text("", 10, WINDOW_HEIGHT - 24, arcade.color.WHITE, 14)

    def on_update(self, dt: float):

        self.check_inputs(dt)

        self.cheese_list.update()
        cheese_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.cheese_list)

        for cheese in cheese_hit_list:
            cheese.remove_from_sprite_lists()
            self.score += 1

    def on_draw(self):

        self.clear()

        self.cheese_list.draw()
        self.player_list.draw()

        self.score_txt.text = f"Score: {self.score}"
        self.score_txt.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol not in self.inputs:
            self.inputs.add(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in self.inputs:
            self.inputs.remove(symbol)

    def check_inputs(self, dt: float):

        if not self.inputs: return

        direction = Vector2(0, 0)

        if arcade.key.W in self.inputs:
            direction.y += 1
        if arcade.key.S in self.inputs:
            direction.y -= 1

        if arcade.key.A in self.inputs:
            direction.x -= 1
        if arcade.key.D in self.inputs:
            direction.x += 1

        direction.normalize()

        self.player_sprite.center_x += direction.x * 250 * dt
        self.player_sprite.center_y += direction.y * 250 * dt


class Player:

    def __init__(self, pos: Vector2):
        self.pos = pos

    def update(self, dt: float):
        pass

    def draw(self):
        pass


def main():

    window = SpritesTest()
    window.setup()

    arcade.run()

if __name__ == "__main__":
    main()