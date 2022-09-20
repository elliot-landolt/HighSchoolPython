import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
xspeed = 0
yspeed = 0



class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'

good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
 
 
 
for i in range(random.randrange(50)):
    # This represents a block
    block = Block(GREEN, 20, 15)
    block.image = pygame.image.load("bob.png")
    block.rect = block.image.get_rect()    
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width) - block.width
    block.rect.y = random.randrange(screen_height) - block.height
        
    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)
for i in range(random.randrange(50)):
    # This represents a block
    block = Block(RED, 20, 15)
    block.image = pygame.image.load("jack.png")
    block.rect = block.image.get_rect()     
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)  - block.width
    block.rect.y = random.randrange(screen_height) - block.height
 
    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Block(BLUE, 20, 15)
all_sprites_list.add(player)
player.image = pygame.image.load("player.png") 
player.rect = player.image.get_rect()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 25, True, False) 
score = 0
background = pygame.mixer.Sound("background.wav")
jack_hit = pygame.mixer.Sound("jack.wav")
bob_hit = pygame.mixer.Sound("bob.wav")
bump = pygame.mixer.Sound("bump.ogg")
background.play()
# -------- Main Program Loop -----------
while not done:
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
    
    # Clear the screen
    screen.fill(WHITE)
 
    
    
    player.rect.x += xspeed
    player.rect.y += yspeed    
    if player.rect.right > screen_width:
        player.rect.right = screen_width
        bump.play()
    if player.rect.left < 0:
        player.rect.left = 0
        bump.play()
    if player.rect.top < 0:
        player.rect.top = 0
        bump.play()
    if player.rect.bottom > screen_height:
        player.rect.bottom = screen_height
        bump.play()
 
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the list of collisions.
    for block in good_blocks_hit_list:
        score += 1
        bob_hit.play()
        print(score)
    for block in bad_blocks_hit_list:
        score -= 1
        jack_hit.play()
        print(score)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
    text = font.render("Score: "+ str(score), True, BLACK)
    screen.blit(text, [0, 0])
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()