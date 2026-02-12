from movement.game_loop import *
import sys
pygame.init()

g = Game()
g.intro()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()