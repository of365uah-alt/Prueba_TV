import arcade


class Explosion(arcade.Sprite):
    """This class creates an explosion animation"""

    def __init__(self, texture_list):
        super().__init__(texture_list[0])

        # How long the explosion has been around
        self.time_elapsed = 0

        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list

    def update(self, delta_time=1/60):
        # Increase timer
        self.time_elapsed += delta_time

        # Update to the next frame of the animation
        self.current_texture = int(self.time_elapsed * 60)

        # If we still have frames left
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)

        # If animation finished, remove the sprite
        else:
            self.remove_from_sprite_lists()
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Explosion Example")

        # Load explosion textures
        self.explosion_textures = []
        for i in range(1, 9):
            self.explosion_textures.append()

        # Sprite list to hold explosions
        self.explosion_list = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        self.explosion_list.draw()

    def on_update(self, delta_time):
        self.explosion_list.update(delta_time)

    def on_mouse_press(self, x, y, button, modifiers):
        # Create a new explosion at the mouse position
        explosion = Explosion(self.explosion_textures)
        explosion.center_x = x
        explosion.center_y = y
        self.explosion_list.append(explosion)
def main():
    window = MyGame()
    arcade.run()
main()