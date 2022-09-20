import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
tree_x = 0
tree_y = 0
tree_speed = 10

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    tree_x += tree_speed
    if tree_x >= 700 - 150:
        tree_speed *= -1
    elif tree_x <= 0:
        tree_speed *= -1
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    # tree is 150 wide
    pygame.draw.rect(screen, BLACK, [60 + tree_x, 400 - 230, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150 + tree_x, 400 - 230], [75 + tree_x, 250 - 230], [0 + tree_x, 400 - 230]])
    pygame.draw.polygon(screen, GREEN, [[140 + tree_x, 350 - 230], [75 + tree_x, 230 - 230], [10 + tree_x, 350 - 230]])    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()