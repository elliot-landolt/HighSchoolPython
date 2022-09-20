import pygame
PI = 3.14

r = 46
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
TRACK = (255, 127, 0)
BENCH = (170, 170, 170)
GRASS = (46, 114, 39)
color_list = [BLACK, WHITE, GREEN, RED, TRACK, BENCH, GRASS]
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
my_font = pygame.font.SysFont("Calibri", 100, False, False)
pygame.display.set_caption("Soccer Pitch")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
frame = 0
move = True
goal = False

x_move = 1.4
y_move = 1.4

ball_x = 160
ball_y = 245

fwd_move = 0
x_off = 0
goal_x = 50
red = 0
color_speed = 3
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    ball_x += x_move
    ball_y -= y_move
    frame += 1
   
    
    if frame <= 100:
        if ball_x >= 230 or ball_y <= 140:
            x_move = -0.1
            y_move = -2
    elif frame >= 100 and frame <= 101:
        x_move = 1
        y_move = -1
    elif frame >= 150 and frame < 175:
        x_move = 0.3
        y_move = 1
    elif frame >= 225 and frame < 250:
        x_move = 1
        y_move = 0
    elif frame >= 250 and frame <= 300:
        x_move = 1
        y_move = 1
    elif frame > 325 and frame < 400:
        x_move = 1
        y_move = 0
        fwd_move += 1
    elif frame >= 400 and frame <= 425:
        fwd_move = 0
        x_move = 2
        y_move = -1.75
    elif frame > 435:
        x_move = 0
        y_move = 0
        goal = True
    
    if goal == True:       
        x_off += 3
        if goal_x > 700:
            goal_x = -50 
            
            
    
              
        
    red += color_speed
    if red >= 255:
        color_speed *= -1
    if red <= 0:
        color_speed *= -1
    
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
    
    # --- Drawing code should go here
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
    # Drawing O's (players)
    # GK
    pygame.draw.ellipse(screen, BLACK, [150, 245, 20, 20], 5)
    # CB
    pygame.draw.ellipse(screen, BLACK, [220, 280, 20, 20], 5)
    pygame.draw.ellipse(screen, BLACK, [220, 210, 20, 20], 5)
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
    x = 375 + fwd_move
    while y < 350:
        pygame.draw.ellipse(screen, BLACK, [x, y, 20, 20], 5)
        y += 75   
    # BALL
    pygame.draw.ellipse(screen, WHITE, [ball_x, ball_y, 10, 10])
    
    # GOAL
    if goal == True:
        my_text = my_font.render("GOAL", True, (red, 0, 0))
        screen.blit(my_text, [goal_x + x_off, 30])    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
