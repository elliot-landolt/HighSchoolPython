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
        self.image = pygame.image.load("ship.png")
        #self.image = pygame.Surface([30, 30])
        self.rect = self.image.get_rect()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.health = random.randrange(1,3)
    def update(self):
        self.rect.y += 5
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 12])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 10
        


# Create my pygame group
all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()



player = Player()
all_sprites_list.add(player) 

for i in range(200):
    new_enemy = Enemy()
    new_enemy.rect.x = random.randrange(screen_width - new_enemy.rect.width)
    new_enemy.rect.y = random.randrange(-10 * screen_height, 0)
    all_sprites_list.add(new_enemy)
    enemy_list.add(new_enemy)
    if new_enemy.health == 1:
        new_enemy.image.fill(RED)
    elif new_enemy.health == 2:
        new_enemy.image.fill(BLACK)
score = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            new_bullet = Bullet()
            all_sprites_list.add(new_bullet)
            new_bullet.rect.centerx = player.rect.centerx
            new_bullet.rect.centery = player.rect.centery
            bullet_list.add(new_bullet)
            
 
    # --- Game logic should go here
    pos = pygame.mouse.get_pos()
    player.rect.centerx = pos[0]
    player.rect.bottom = screen_height

    
    
    enemy_list.update()
    bullet_list.update()
    
    for bullet in bullet_list:
        hit_list = pygame.sprite.spritecollide(bullet, enemy_list, False)
        for enemy in hit_list:
            bullet.kill()
            enemy.health -= 1
            if enemy.health <= 0:
                enemy.kill()
            
    
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