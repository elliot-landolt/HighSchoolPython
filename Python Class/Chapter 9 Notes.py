import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (150, 75, 75)


# DEFS GO HERE
def draw_tree(x_off, y_off):
    pygame.draw.rect(screen, BROWN, [60 + x_off, 400 - 230 + y_off, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150 + x_off, 400 - 230 + y_off], [75 + x_off, 250 - 230 + y_off], [0 + x_off, 400 - 230 + y_off]])
    pygame.draw.polygon(screen, GREEN, [[140 + x_off, 350 - 230 + y_off], [75 + x_off, 230 -230 + y_off], [10 + x_off, 350 - 230 + y_off]])




 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x_off = 0
y_off = 0
x = 0

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    x += 1
    screen.fill(WHITE)
    
    # --- Drawing code should go here
    
    draw_tree(x, 200)

    
    # --- Go ahead and update the screen with what we've drawn.
    
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()