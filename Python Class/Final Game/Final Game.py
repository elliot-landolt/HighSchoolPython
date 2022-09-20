import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 225, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (155, 155, 155)
ready = False
xspeed = 0
yspeed = 0
screen_width = 900
screen_height = 700
score = 0
difficulty = 50
missiles = 75
out_of_missiles = False
# CLASSES
class Plane(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("plane.png")
        self.rect = self.image.get_rect()        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = random.randrange(1,3)
        for i in range(difficulty):
            if self.health == 1:
                self.image = pygame.image.load("enemy_plane2.png")
                self.rect = self.image.get_rect()
                self.rect.x = random.randrange(screen_width - self.rect.width)
                self.rect.y = random.randrange(-15 * screen_height, -self.rect.height)        
            elif self.health == 2:
                self.image = pygame.image.load("enemy_plane1.png")
                self.rect = self.image.get_rect()
                self.rect.x = random.randrange(screen_width - self.rect.width)
                self.rect.y = random.randrange(-15 * screen_height, -self.rect.height)            
    def update(self):
        self.rect.y += 5
        if random.randrange(100) == 0 and self.rect.y > 0 and self.rect.y < 200:
            enemy_rocket = Enemy_Bullet()
            enemy_rocket.image = pygame.image.load("rocket2.png")
            enemy_rocket.image.get_rect()
            enemy_rocket.rect.x = self.rect.x
            enemy_rocket.rect.y = self.rect.y
            all_sprites_list.add(enemy_rocket)
            enemy_rocket_list.add(enemy_rocket)
            
            
            
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 12])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 10
        
class Enemy_Bullet(Bullet):
    def __init__(self):
        super().__init__()
    def update(self):
        self.rect.y += 10

# Create sprite groups
all_sprites_list = pygame.sprite.Group()
rocket_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
enemy_rocket_list = pygame.sprite.Group()

# Player info
player = Plane(15, 10)
player.rect.x = 400
player.rect.y = 550

# Create enemies

for i in range(difficulty):
    new_enemy = Enemy()
    all_sprites_list.add(new_enemy)
    enemy_list.add(new_enemy)    

# Add objects button to all sprite list
all_sprites_list.add(player)

pygame.init()
 
# Set the width and height of the screen [width, height]

size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Air Attack!")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Text Fonts
font = pygame.font.SysFont('PT Mono', 75, True, False)
font2 = pygame.font.SysFont("Calibri", 30, False, False)
font3 = pygame.font.SysFont("Calibri", 50, True, False)
font4 = pygame.font.SysFont("PT Mono", 25, False, False)


# Background images and music
background_image = pygame.image.load("background.png")
game_background = pygame.image.load("game_background.jpeg")
game_over = pygame.image.load("game_over.jpeg")
intro_music = pygame.mixer.Sound("intro_music.wav")
missile_launch = pygame.mixer.Sound("missile_launch.wav")
missile_launch.set_volume(0.25)
missile_hit = pygame.mixer.Sound("missile_hit.wav")
enemy_kill = pygame.mixer.Sound("enemy_kill.wav")
enemy_kill.set_volume(1.5)

# Cutscreens

def cut_screen():
    
    done = False # loop condition to end the function
    intro_font = pygame.font.SysFont('Courier', 75, True, False)
    intro_music.play()
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        clicked = pygame.mouse.get_pressed()
        if clicked[0] == True:
                done = True
                ready = True
        # background image      
        screen.blit(background_image, [0,0])
        
        # text display
        text = font.render("Air Attack!", True, RED)
        text2 = font2.render("Shoot down the enemy planes in your jet and avoid their missiles!", True, RED)
        text3 = font2.render("Move with the arrow keys and hit the space bar to fire your missiles!", True, RED)
        text4 = font3.render("Click the mouse button to start!", True, BLACK)
        screen.blit(text, [225, 250])
        screen.blit(text2, [125, 350])
        screen.blit(text3, [125, 375])
        screen.blit(text4, [275, 450])        
        pygame.display.flip()
        clock.tick(60)
def cut_screen2():
    intro_music.stop()
    done = False # loop condition to end the function
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        clicked = pygame.mouse.get_pressed()
        if clicked[0] == True:
                done = True
                ready = True
        # background image      
        screen.blit(game_over, [0,0])
        
        # text display
        text = font2.render("Game Over", True, RED)
        text2 = font2.render("You killed " + str(score) + " planes", True, RED)
        screen.blit(text, [225, 250])
        screen.blit(text2, [125, 350])      
        pygame.display.flip()
        clock.tick(60)

cut_screen()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xspeed = 10
            if event.key == pygame.K_LEFT:
                xspeed = -10
            if event.key == pygame.K_DOWN:
                yspeed = 10
            if event.key == pygame.K_UP:
                yspeed = -10
            if event.key == pygame.K_SPACE: # Missile shoot button
                if missiles > 0:
                    new_rocket = Bullet()
                    all_sprites_list.add(new_rocket)
                    new_rocket.image = pygame.image.load("rocket.png")
                    new_rocket.image.get_rect()
                    new_rocket.rect.centerx = player.rect.centerx
                    new_rocket.rect.centery = player.rect.centery
                    rocket_list.add(new_rocket)  
                    missile_launch.play()
                    missiles -= 1
                elif missiles <= 0:
                    out_of_missiles = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xspeed = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                yspeed = 0        
 
    # --- Game logic should go here
    player.rect.x += xspeed
    player.rect.y += yspeed    
    if player.rect.right > screen_width:
        player.rect.right = screen_width
    if player.rect.left < 0:
        player.rect.left = 0        
    if player.rect.top < 500:
        player.rect.top = 500    
    if player.rect.bottom > screen_height:
        player.rect.bottom = screen_height
      
     # Collisions 
            
    if new_enemy.rect.y > 700:
        new_enemy.kill()
    enemy_list.update()
    rocket_list.update()
    enemy_rocket_list.update()
    for rocket in rocket_list:
        hit_list = pygame.sprite.spritecollide(rocket, enemy_list, False)
        for enemy in hit_list:
            rocket.kill()
            enemy.health -= 1
            if enemy.health <= 0:
                enemy.kill()
                score += 1
                enemy_kill.play()
    
    hit_list = pygame.sprite.spritecollide(player, enemy_rocket_list, False)
    for enemy_rocket in hit_list:
        done = True
        missile_hit.play()
        
        
    hit_list2 = pygame.sprite.spritecollide(player, enemy_list, False)
    for enemy in hit_list2:
        done = True
        missile_hit.play()
    # --- Screen-clearing code goes here
    
   

    screen.blit(game_background, [0,0])
 
    
    # --- Drawing code should go here
    
    # Draw all objects
    all_sprites_list.draw(screen)
    text = font4.render("Score: " + str(score), True, BLACK)
    
    if out_of_missiles == False:
        missile_text = font4.render("Missiles: " + str(missiles), True, BLACK)
        screen.blit(missile_text, [0, 50])
    elif out_of_missiles == True:
        out_of_missile_text = font4.render("Missiles: OUT OF MISSILES", True, RED)
        screen.blit(out_of_missile_text, [0, 50])
    
    screen.blit(text, [0,0])
    
    if done == True:
        cut_screen2()
    
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
