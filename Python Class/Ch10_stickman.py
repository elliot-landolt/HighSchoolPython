"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x = 0
y = 0

# keyboard variables
key_x = 0
key_y = 0
key_xspeed = 0
key_yspeed = 0

# joystick variables
joy_x = 0
joy_y = 0

# Functions
def stickman(x, y, color):
# Head
    pygame.draw.ellipse(screen, BLACK, [96 - 95 + x,83 - 83 + y,10,10], 0)
# Legs
    pygame.draw.line(screen, BLACK, [100 - 95 + x,100 - 83 + y], [105 - 95 + x,110 - 83 + y], 2)
    pygame.draw.line(screen, BLACK, [100 - 95 + x,100 - 83 + y], [95 - 95 + x,110 - 83 + y], 2)
# Body
    pygame.draw.line(screen, color, [100 - 95+ x,100 - 83 + y], [100 - 95 + x,90 - 83 + y], 2)
# Arms
    pygame.draw.line(screen, color, [100 - 95 + x,90 - 83 + y], [104 - 95 + x,100 - 83 + y], 2)
    pygame.draw.line(screen, color, [100 - 95 + x,90 - 83 + y], [96 - 95 + x,100 - 83 + y], 2)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # a button was pressed
            if event.key == pygame.K_RIGHT:
                key_xspeed = 10
            if event.key == pygame.K_LEFT:
                key_xspeed = -10
            if event.key == pygame.K_DOWN:
                key_yspeed = 10
            if event.key == pygame.K_UP:
                key_yspeed = -10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                key_xspeed = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                key_yspeed = 0
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    
    
    left_stick_x = my_joystick.get_axis(0) * 10
    left_stick_y = my_joystick.get_axis(1) * 10
    joy_x += left_stick_x
    joy_y += left_stick_y


    key_x += key_xspeed
    key_y += key_yspeed
    press = pygame.mouse.get_pressed()

    if  key_x < 0:
        key_x = 0
    if key_x >= 690:
        key_x = 690
    if key_y < 0:
        key_y = 0
    if key_y > 471:
        key_y = 471
    if  joy_x < 0:
        joy_x = 0
    if joy_x >= 690:
        joy_x = 690
    if joy_y < 0:
        joy_y = 0
    if joy_y > 471:
        joy_y = 471    
    
    if press[0]:
        color = RED
    else:
        color = GREEN
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    # Draw a stick man
    stickman(x, y, color)
    stickman(key_x, key_y, BLACK)
    stickman(joy_x, joy_y, color)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
