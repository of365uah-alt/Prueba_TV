
#Por favor, mantener limpio este proyecto, no añadir cosas desagradables, no añadir cosas que no tengan nada que ver con el proyecto
import pygame
import random
from enum import Enum
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mus - Spanish Deck Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Card suits
class Suit(Enum):
    OROS = "Oros"
    COPAS = "Copas"
    ESPADAS = "Espadas"
    BASTOS = "Bastos"

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} de {self.suit.value}"

class MusGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.players = 2
        self.player_hand = []
        self.dealer_hand = []
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 36)
        
    def create_deck(self):
        """Create a Spanish deck (40 cards)"""
        deck = []
        values = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]  # Spanish deck values
        suits = [Suit.OROS, Suit.COPAS, Suit.ESPADAS, Suit.BASTOS]
        
        for suit in suits:
            for value in values:
                deck.append(Card(value, suit))
        
        random.shuffle(deck)
        return deck
    
    def deal_cards(self):
        """Deal 4 cards to each player"""
        self.player_hand = [self.deck.pop() for _ in range(4)]
        self.dealer_hand = [self.deck.pop() for _ in range(4)]
    
    def draw(self):
        """Draw game screen"""
        screen.fill(GREEN)
        
        # Draw player hand
        title = self.font.render("Tu mano:", True, WHITE)
        screen.blit(title, (50, 650))
        
        for i, card in enumerate(self.player_hand):
            card_text = self.font.render(str(card), True, WHITE)
            screen.blit(card_text, (50 + i * 250, 700))
        
        # Draw dealer info
        dealer_text = self.font.render(f"Repartidor tiene: {len(self.dealer_hand)} cartas", True, WHITE)
        screen.blit(dealer_text, (50, 50))
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        self.deal_cards()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()

# Start game
game = MusGame()
game.run()
