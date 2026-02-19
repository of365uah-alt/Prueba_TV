import pygame
import sys
import random
from enum import Enum
from collections import deque

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class SnakeGame:
    def __init__(self, width=800, height=600, grid_size=20):
        pygame.init()
        
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.cols = width // grid_size
        self.rows = height // grid_size
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        self.reset_game()
        
    def reset_game(self):
        start_x = self.cols // 2
        start_y = self.rows // 2
        self.snake = deque([(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)])
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.food = self.spawn_food()
        self.score = 0
        self.game_over = False
        
    def spawn_food(self):
        while True:
            x = random.randint(0, self.cols - 1)
            y = random.randint(0, self.rows - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.direction != Direction.DOWN:
                    self.next_direction = Direction.UP
                elif event.key == pygame.K_s and self.direction != Direction.UP:
                    self.next_direction = Direction.DOWN
                elif event.key == pygame.K_a and self.direction != Direction.RIGHT:
                    self.next_direction = Direction.LEFT
                elif event.key == pygame.K_d and self.direction != Direction.LEFT:
                    self.next_direction = Direction.RIGHT
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.reset_game()
        
        return True
    
    def update(self):
        if self.game_over:
            return
        
        self.direction = self.next_direction
        
        head_x, head_y = self.snake[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        # Colisiones con paredes
        if (new_head[0] < 0 or new_head[0] >= self.cols or
            new_head[1] < 0 or new_head[1] >= self.rows):
            self.game_over = True
            return
        
        # Colisión con el mismo cuerpo
        if new_head in self.snake:
            self.game_over = True
            return
        
        self.snake.appendleft(new_head)
        
        # Comer comida
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            self.snake.pop()
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        # Dibujar serpiente
        for i, (x, y) in enumerate(self.snake):
            color = (0, 255, 0) if i == 0 else (0, 200, 0)
            pygame.draw.rect(self.screen, color, 
                           (x * self.grid_size, y * self.grid_size, 
                            self.grid_size - 1, self.grid_size - 1))
        
        # Dibujar comida
        fx, fy = self.food
        pygame.draw.rect(self.screen, (255, 0, 0), 
                        (fx * self.grid_size, fy * self.grid_size, 
                         self.grid_size - 1, self.grid_size - 1))
        
        # Dibujar puntuación
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        
        # Dibujar mensaje de game over
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, (255, 0, 0))
            restart_text = self.font.render("Presiona SPACE para reiniciar", True, (255, 255, 255))
            
            text_rect1 = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 40))
            text_rect2 = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 20))
            
            self.screen.blit(game_over_text, text_rect1)
            self.screen.blit(restart_text, text_rect2)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        
        while running:
            running = self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(10)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
