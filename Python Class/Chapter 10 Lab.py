import pygame
PI = 3.14

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TRACK = (255, 127, 0)
BENCH = (170, 170, 170)
GRASS = (46, 114, 39)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
pygame.init()
x = 160
xspeed = 0
y = 245
yspeed = 0
keep_x = 150
keep_y = 245
joy_x = 220
joy_y = 280
joy2_x = 220
joy2_y = 210
color2 = BLACK
def players(color, color2):
    # GK
    pygame.draw.ellipse(screen, color, [keep_x, keep_y, 20, 20], 5)
    # CB
    pygame.draw.ellipse(screen, color2, [joy_x, joy_y, 20, 20], 5)
    pygame.draw.ellipse(screen, color2, [joy2_x, joy2_y, 20, 20], 5)
    # RB
    pygame.draw.ellipse(screen, BLACK, [230, 350, 20, 20], 5)
    # LB
    pygame.draw.ellipse(screen, BLACK, [230, 140, 20, 20], 5)
    # MF
    y = 175
    while y < 350:
        pygame.draw.ellipse(screen, BLACK, [300, y, 20, 20], 5)
        y += 75
    # FWD
    y = 175
    x = 375
    while y < 350:
        pygame.draw.ellipse(screen, BLACK, [x, y, 20, 20], 5)
        y += 75    
def feild():
    # Grass
    pygame.draw.rect(screen, GRASS, [150, 100, 400, 300])
    # Track 
    pygame.draw.ellipse(screen, TRACK, [0, 0, 700, 500], 40)
    # Touchlines/Goallines
    pygame.draw.rect(screen, WHITE, [150, 100, 400, 300], 5)
    # Penalty Area
    pygame.draw.rect(screen, WHITE, [150, 175, 75, 150], 5)
    pygame.draw.rect(screen, WHITE, [475, 175, 75, 150], 5)
    # Goal Box
    pygame.draw.rect(screen, WHITE, [150, 215, 30, 75], 5)
    pygame.draw.rect(screen, WHITE, [520, 215, 30, 75], 5)
    # Center Line, Circle and Mark
    pygame.draw.line(screen, WHITE, (350, 100), (350, 400), 5)
    pygame.draw.ellipse(screen, WHITE, [300, 200, 100, 100], 5)
    pygame.draw.ellipse(screen, WHITE, [345, 245, 10, 10])
    # Bench/Table
    pygame.draw.rect(screen, WHITE, [340, 75, 25, 15])
    pygame.draw.rect(screen, BENCH, [200, 75, 100, 10])
    pygame.draw.rect(screen, BENCH, [400, 75, 100, 10])
    # Stands
    pygame.draw.rect(screen, BENCH, [275, 415, 150, 25])
    pygame.draw.line(screen, BLACK, (275, 427), (424, 427), 2)
    # Penalty Arc
    pygame.draw.arc(screen, WHITE, [210, 210, 30, 75], -PI/2, PI/2,  5)
    pygame.draw.arc(screen, WHITE, [460, 215, 30, 75], PI/2, -PI/2, 5)
    # Penalty Mark
    pygame.draw.ellipse(screen, WHITE, [200, 250, 7, 7])
    pygame.draw.ellipse(screen, WHITE, [495, 250, 7, 7])
    # White Lines on Track
    x = 0
    y = 0
    while x < 60 and y < 100:
        pygame.draw.ellipse(screen, WHITE, [0 + x, 0 + x, 700 - y, 500 - y], 3)
        x += 10
        y += 20    
def soccerball(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 10, 10])
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Soccer Pitch")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
#my_joystick = pygame.joystick.Joystick(0)

#my_joystick.init() 
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xspeed = 3
            if event.key == pygame.K_LEFT:
                xspeed = -3
            if event.key == pygame.K_DOWN:
                yspeed = 3
            if event.key == pygame.K_UP:
                yspeed = -3
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xspeed = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                yspeed = 0        
            
 
    # --- Game logic should go here
    x += xspeed
    y += yspeed
    if y < 100:
        y = 100
    if y > 390:
        y = 390
    if x < 150:
        x = 150
    if x > 540:
        x = 540
    pos = pygame.mouse.get_pos()
    keep_x = pos[0]
    keep_y = pos[1]
    if keep_x > 213:
        keep_x = 213
    if keep_x < 153:
        keep_x = 153
    if keep_y < 178:
        keep_y = 178
    if keep_y > 304:
        keep_y = 304
    '''
    if joy_y < 100:
        joy_y = 100
    if joy_y > 380:
        joy_y = 380
    if joy_x < 150:
        joy_x = 150
    if joy_x > 530:
        joy_x = 530    
    if joy2_y < 100:
        joy2_y = 100
    if joy2_y > 380:
        joy2_y = 380
    if joy2_x < 150:
        joy2_x = 150
    if joy2_x > 530:
        joy2_x = 530     
        
    right_stick_x = my_joystick.get_axis(0) * 3
    right_stick_y = my_joystick.get_axis(1) * 3
    left_stick_x = my_joystick.get_axis(2) * 3
    left_stick_y = my_joystick.get_axis(3) * 3
    button0 = my_joystick.get_button(0)
    button1 = my_joystick.get_button(1)
    button2 = my_joystick.get_button(2)
    button3 = my_joystick.get_button(3)
    joy_x += left_stick_x
    joy_y += left_stick_y   
    joy2_x += right_stick_x
    joy2_y += right_stick_y
    '''
    press = pygame.mouse.get_pressed()   
    if press[0]:
        color = GREEN
    else:
        color = BLACK

    
    if button0 > 0:
        color2 = BLUE
    elif button1 > 0:
        color2 = RED
    elif button2 > 0:
        color2 = WHITE
    elif button3 > 0:
        color2 = YELLOW
    else:
        color2 = BLACK
    
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
    
    # --- Drawing code should go here
    feild()
    soccerball(x, y)
    players(color, color2)
    
   
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
