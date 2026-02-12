from movement.player_sprite_movement import *
from movement.config import *
pygame.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def createTILEMAP(self):
        for i, row in enumerate(tilemap):
            for j, col in enumerate(row):
                if col == "B":
                    blocks(self, j, i)
                if col == "P":
                    Player_move(self, j, i)

    def new(self):
        #new game starts
        self.playing = True
        # contains all sprites in game
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates() #walls
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates() #attack animations

        self.createTILEMAP()
    def events(self):
        for event in pygame.event.get(): #iterates over every possible pygame event
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #game loop updates
        self.all_sprites.update()
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen) #goes through all sprites and displays image
        self.clock.tick(FPS)
        pygame.display.update() #updates the screen

    def main(self):
        #game loop
        while self.playing:
            self.events() #contains keypress
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass
    def intro(self):
        pass

