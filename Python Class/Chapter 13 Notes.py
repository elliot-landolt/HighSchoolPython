# Chapter 13 Notes - Sprites
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
 
# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Chapter 13 Notes")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.rect = self.image.get_rect()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 5

# Create my pygame group
all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()



player = Player()
all_sprites_list.add(player) 

for i in range(200):
    new_enemy = Enemy()
    new_enemy.rect.x = random.randrange(screen_width - new_enemy.rect.width)
    new_enemy.rect.y = random.randrange(-10 * screen_height, 0)
    all_sprites_list.add(new_enemy)
    enemy_list.add(new_enemy)

score = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    player.rect.centerx, player.rect.centery = pygame.mouse.get_pos()
    
    enemy_list.update()
    
    
    
    hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
    for enemy in hit_list:
        done = True
    
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()