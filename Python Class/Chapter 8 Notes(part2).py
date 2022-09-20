import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKYBLUE = (142, 185, 255)
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# list for snowflakes and their values
snow_list = []



for i in range(1000):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    speed = random.randrange(1, 5)
    snow_list.append([x, y, speed])
    

depth = 1
red = 0
blue = 255
green = 0
color_speed = 1
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    for i in range(len(snow_list)):
        snow_list[i][1] += snow_list[i][2]
        if snow_list[i][1] > 500:
            snow_list[i][1] = -20  
            snow_list[i][0] = random.randrange(0, 700)
            depth += 0.01
    red += color_speed
    green += color_speed
    if red >= 255:
        color_speed *= -1
    if red <= 0:
        color_speed *= -1
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill((red, green, blue))
 
    # --- Drawing code should go here
    # snowflake
    for i in range(len(snow_list)):
        pygame.draw.ellipse(screen, WHITE, [snow_list[i][0],snow_list[i][1], snow_list[i][2] * 2, snow_list[i][2] * 2])
    pygame.draw.rect(screen, WHITE, [0, 500 - depth, 700, depth + 1])
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()