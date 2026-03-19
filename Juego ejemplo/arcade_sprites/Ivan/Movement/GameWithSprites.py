import arcade
import random
import os
import pathlib

# Path Handling
DIRECTORIO_BASE = pathlib.Path(__file__).parent.resolve()

def get_path(nombre_archivo):
    ruta = os.path.join(DIRECTORIO_BASE, nombre_archivo)
    # DEBUG: This will print in your terminal so you can see if the path is correct
    if not os.path.exists(ruta):
        print(f"--- ALERTA: No se encuentra el archivo: {ruta} ---")
    return ruta

# Constants
ANCHO = 800
ALTO = 800
TITULO = "Sprite Collector Game"

class Player(arcade.Sprite):
    def __init__(self):
        # We pass the path directly into the parent constructor
        super().__init__(get_path("chess_queen.png"), scale=0.5)  
        print("Imagen cargada:", self.texture)      
        
        self.center_x = ANCHO // 2
        self.center_y = 100
        self.speed = 7
        self.vida = 5

class FallingObject(arcade.Sprite):
    def __init__(self, filename, scale):
        # Explicitly calling the Sprite constructor
        super().__init__(filename, scale)
        self.reset_pos()

    def reset_pos(self):
        self.center_x = random.randint(50, ANCHO - 50)
        self.center_y = random.randint(ALTO, ALTO + 300)
        self.change_y = -random.randint(4, 8)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(ANCHO, ALTO, TITULO)
        arcade.set_background_color((20, 0, 30))
        
        # Initialize Sprites
        self.player = Player()
        self.moneda = FallingObject(get_path("dice_detailed.png"), 0.5)
        self.bolita = FallingObject(get_path("cards_skull.png"), 0.5)
        
        self.puntuacion = 0
        self.game_over = False
        
        self.keys = {arcade.key.W: False, arcade.key.S: False, 
                     arcade.key.A: False, arcade.key.D: False}

    def on_draw(self):
        self.clear()
        
        if self.game_over:
            arcade.draw_text("GAME OVER", ANCHO/2, ALTO/2 + 50, arcade.color.RED, 50, anchor_x="center")
            arcade.draw_text(f"Puntos: {self.puntuacion}", ANCHO/2, ALTO/2, arcade.color.WHITE, 20, anchor_x="center")
        else:
            # If the error persists here, it means 'self.player' was not created as a Sprite
            self.player.draw()
            self.moneda.draw()
            self.bolita.draw()
            
            arcade.draw_text(f"Vidas: {self.player.vida}", 10, ALTO - 30, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        if self.game_over:
            return

        # Player logic
        if self.keys[arcade.key.W] and self.player.top < ALTO: self.player.center_y += self.player.speed
        if self.keys[arcade.key.S] and self.player.bottom > 0: self.player.center_y -= self.player.speed
        if self.keys[arcade.key.A] and self.player.left > 0: self.player.center_x -= self.player.speed
        if self.keys[arcade.key.D] and self.player.right < ANCHO: self.player.center_x += self.player.speed

        self.moneda.update()
        self.bolita.update()

        if arcade.check_for_collision(self.player, self.moneda):
            self.puntuacion += 1
            self.moneda.reset_pos()
        
        if arcade.check_for_collision(self.player, self.bolita):
            self.player.vida -= 1
            self.bolita.reset_pos()
            if self.player.vida <= 0:
                self.game_over = True

        if self.moneda.top < 0: self.moneda.reset_pos()
        if self.bolita.top < 0: self.bolita.reset_pos()

    def on_key_press(self, key, modifiers):
        if key in self.keys: self.keys[key] = True

    def on_key_release(self, key, modifiers):
        if key in self.keys: self.keys[key] = False

if __name__ == "__main__":
    game = MyGame()
    arcade.run()