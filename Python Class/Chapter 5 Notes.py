"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame # FIRST THING IN PROGRAM
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GRAY = (130, 130, 130)
PURPLE = (152, 0, 255)
ORANGE = (200, 100, 0)
MAROON = (100, 0, 0)


pygame.init() # starts pygame before any pygame calls
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chapter 5 Notes")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# make a font
# ("font", font_size, bold, italics)
my_font = pygame.font.SysFont("Calibri", 40, False, False)

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Chapter 5 code should go here
    
    # draw a line
    # (screen, color, (x1, y1), (x2, y2), line_width)
    pygame.draw.line(screen, GRAY, (100, 100), (200, 200), 3)
    pygame.draw.line(screen, BLUE, (50, 0), (50, 500), 5) # vertical
    pygame.draw.line(screen, MAGENTA, (0, 50), (700, 50), 5) # horizontal
    
    for x in range(25, 700, 25):
        pygame.draw.line(screen, ORANGE, (x, 0), (x, 500), 5) # lines across screen
    
    for y in range(25, 500, 25):
        pygame.draw.line(screen, MAGENTA, (0, y), (700, y), 5)
    # Ignore me    
    '''
    for x in range(25, 700, 25):
        for y in range(25, 500, 25):
            pygame.draw.line(screen, WHITE, (x, 0), (0, y), 3)
    '''
    # Draw a rectangle
    #(screen, COLOR, [x, y, width, height], optional_borderwidth)
    pygame.draw.rect(screen, RED, [0, 0, 100, 50])
    pygame.draw.rect(screen, GREEN, [350, 250, 350, 250])
    
    for x in range(0, 700, 100):
        for y in range(0, 500, 100):
            pygame.draw.rect(screen, PURPLE, [x, y, 50, 50])
    
    # Draw an ellipse
    #(screen, COLOR, [x, y, width, height], optional_borderwidth)    
    # ellipse is circumscribed in the defined rectangle
    pygame.draw.ellipse(screen,BLUE, [0, 0, 100, 50])
    pygame.draw.ellipse(screen,RED, [400, 400, 20, 100])
    # offset my yeild sign
    x_off = 200
    y_off = 0

    
    # Draw a polygon
    # (screen, COLOR, [[x1, y1], [x2, y2],[x3, y3]...], optional border
    pygame.draw.polygon(screen, RED, [[0 + x_off, 0 + y_off],[200 + x_off, 0 + y_off], [100 + x_off, 200 + y_off]])
    
    
    
    
    # Add text
    # ("Text to display", anti-alias, COLOR)
    my_text = my_font.render("YEILD", True, YELLOW)
    screen.blit(my_text, [50 + x_off, 30])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()