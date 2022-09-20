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
 
pygame.display.set_caption("Animation")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# variables
x = 0
x_speed = 10
y = 0 
y_speed = 10

x2 = 0 
x2_speed = 3
y2 = 0
y2_speed = 0
accel = 0.08


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    x += x_speed
    y += y_speed
    
    y2_speed += accel
    x2 += x2_speed
    y2 += y2_speed    
    
    
    if x > 600:
        x_speed *= -1
    elif x < 0:
        x_speed *= -1
        
    if y > 420:
        y_speed *= -1
    elif y < 0:
        y_speed *= -1

    if x2 > 600:
        x2_speed *= -1
    elif x2 < 0:
        x2_speed *= -1
    if y2 > 420:
        y2_speed *= -1
    elif y2 < 0:
        y2_speed *= -0.7
        x2_speed *= 0.7
    
    
    '''
    #wrap around screen
    if x > 700:
        x = -100
    '''
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, RED, [x, y, 100, 80])
    pygame.draw.rect(screen, GREEN, [x2, y2, 100, 80])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()