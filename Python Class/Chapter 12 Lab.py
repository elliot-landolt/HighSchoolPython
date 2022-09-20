'''
Ch 12 - Classes
Balls and Bubbles
'''

import random
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ch12 Notes")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# CLASSES
class Ball():
    def __init__(self):
        self.width = random.randrange(50, 100)
        self.height = random.randrange(50, 100)
        self.xspeed = random.randrange(-10, 11)
        self.yspeed = random.randrange(-10, 11)
        self.x = random.randrange(0, 700 - self.width)
        self.y = random.randrange(0, 500 - self.height)
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        self.color = (r, g, b)
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height])
        pygame.draw.ellipse(screen, BLACK, [self.x, self.y, self.width, self.height], 2)
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x > 700 - self.width:
            self.xspeed *= -1
        if self.x < 0:
            self.xspeed *= -1
        if self.y > 500 - self.height:
            self.yspeed *= -1
        if self.y < 0:
            self.yspeed *= -1
class Rectangle():
    def __init__(self):
        self.height = random.randrange(10, 101)
        self.width = random.randrange(1, 101)
        self.xspeed = random.randrange(-10, 11)
        self.yspeed = random.randrange(-10, 11)        
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)        
        self.color = (r, g, b)
        self.x = random.randrange(0, 700 - self.width)
        self.y = random.randrange(0, 500 - self.height)
    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
        pygame.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height], 2)
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x > 700 - self.width:
            self.xspeed *= -1
        if self.x < 0:
            self.xspeed *= -1
        if self.y > 500 - self.height:
            self.yspeed *= -1
        if self.y < 0:
            self.yspeed *= -1        
ball_list = []
for i in range(1000):
    new_ball = Ball()
    new_rect = Rectangle()
    ball_list.append(new_ball)
    ball_list.append(new_rect)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    for ball in ball_list:
        ball.move()
        
    
    # --- Screen-clearing code goes here
 
    
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    for ball in ball_list:
        ball.draw()
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()