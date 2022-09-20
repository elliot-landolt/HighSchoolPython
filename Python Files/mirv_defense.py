"""
MISSILE DEFENSE GAME
my attempt at Missile Command Clone
by Aaron Lee
"""
import pygame
import random


# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
BLUE     = (   100,   100, 255)
YELLOW   = ( 255, 255,   0)
GREEN    = (   0, 140,   0)       #Dark green for plane

class Base(pygame.sprite.Sprite):
    """ This class represents the Player's bases and player too. """
    def __init__(self):
        """ They are Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([50, 20])
        self.width = 50
        self.height = 20
        self.image.set_colorkey(BLACK)
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.y = 360
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, [self.rect.x - 2, self.rect.y-2, self.width+4, self.height+4])
        pygame.draw.rect(screen, BLUE, [self.rect.x, self.rect.y, self.width, self.height])
        

class Button (pygame.sprite.Sprite):
    '''Menu buttons for the start screen'''
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([150, 40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width//2 - 75
        self.rect.y = screen_height//2 -20
        

class Controller():
    '''holds the global type variables and controls the levels, lives, etc.'''
    def __init__(self):
        self.frame = 0 # frame to track time and other 
        self.high_score = 0 # experimental, not used yet in code
        self.restarter = False # boolean to track restart trigger
        self.level = 1 
        self.score = 0
        self.missile_count = 50 # DIFFICULTY SETTING
        self.missile_dead = 0
        self.framerate = 30 
        self.num_base = 5
        self.font = pygame.font.SysFont('Calibri', 20, True, False)
        self.font_med = pygame.font.SysFont('Calibri', 30, True, False)
        self.font_game_over = pygame.font.SysFont('Calibri', 50, True, False)         
    def start(self):        
        ready = False
        
        intro_text1 = self.font.render("Left click to fire at incoming missiles and score!" ,True,BLACK)
        intro_text2 = self.font.render("Protect your bases from MIRV hits to win the day!!!" ,True,BLACK)
        intro_text3 = self.font.render("Get bonuses for remaining bases and ammo after each wave!" ,True,BLACK)
        intro_text4 = self.font.render("     Click to start......." ,True,BLACK)
        intro_text5 = self.font.render("Original game: by Aaron Lee", True, GREEN)
        intro_text6 = self.font.render("Made with Python and Pygame, 2015", True, GREEN)
        for i in range(20):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break            
            screen.fill(WHITE)
            pygame.display.flip()
            clock.tick(self.framerate)
        title = "M.I.R.V. DEFENSE" 
        for letters in range(len(title)+1):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break            
            screen.fill(WHITE)   
            intro_text0 = self.font_game_over.render(title[:letters] ,True,RED)
            screen.blit(intro_text0, [160, 50])
            pygame.display.flip() 
            clock.tick(8)        
        while not ready:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        ready = True
            screen.fill(WHITE)
            screen.blit(intro_text0, [160, 50])               
            screen.blit(intro_text1, [140, 120])
            screen.blit(intro_text2, [140, 150])
            screen.blit(intro_text3, [140, 180]) 
            screen.blit(intro_text4, [220, 240]) 
            screen.blit(intro_text5, [300, 300])
            screen.blit(intro_text6, [300, 325])
            pygame.event.get()
            clicked = pygame.mouse.get_pressed()
            print(clicked)
            if clicked[0] == True:
                ready = True            
            pygame.display.flip() 
            #clock.tick(-1)
        for i in range(self.num_base):
            base = Base()
            base.rect.y = 360
            base.rect.x = (i+1) * screen_width//(self.num_base+1)-20
            base_list.add(base)
            all_sprites_list.add(base)      
    def game_over(self):
        for frame in range(self.framerate*3):
            screen.fill(WHITE)
            game_over_text = self.font_game_over.render("GAME OVER",True,BLACK)
            score_text = self.font_med.render("You scored: " + str(self.score) + " pts!",True, RED)
            screen.blit(score_text, [50, 10])            
            screen.blit(game_over_text, [200, 175])
            
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip() 
            # --- Limit to 20 frames per second
            clock.tick(self.framerate)
        self.restarter = True
        self.frame = 0
        pygame.quit()
                   
    def next_level(self):
        self.level+=1
        self.missile_dead = 0
        all_sprites_list.empty()
        missile_list.empty()
        explosion_list.empty()
        planes_list.empty()
        self.score += (self.level-1)*10 * len(base_list)
        self.score += self.missile_count
        for frame in range(self.framerate*5):
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break            
            screen.fill(WHITE)
            next_level_text = font.render("Wave " + str(self.level-1) + " Complete" ,True,BLACK)
            next_level_text2 = font.render("City bonus: " + str((self.level-1) * 10) + " x " + str(len(base_list)) + " cities = " + str((self.level-1)*10*len(base_list)) + "pts",True, BLACK)
            next_level_text3 = font.render("Remaining Missile bonus: " + str(self.missile_count) + " pts", True, BLACK)
        
            screen.blit(next_level_text, [screen_width//2 - 75, screen_height//2 - 20])
            screen.blit(next_level_text2, [screen_width//2 - 150, screen_height//2 + 20])
            screen.blit(next_level_text3, [screen_width//2 - 150, screen_height//2 + 60])
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip() 
            # --- Limit to 20 frames per second
            clock.tick(self.framerate)
        self.missile_count = 50
        plane = Plane()
        planes_list.add(plane)
        all_sprites_list.add(plane)        
        
    def restart(self):
        ready = False
        start_button = Button(200,300)
        buttons_list.add(start_button)
        #screen.fill(WHITE)
        #pygame.display.flip()
        restart_text = controller.font.render("Click to Restart" ,True,WHITE)
        while not ready:
            print("STILL NOT")
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        ready = True            
            screen.fill(WHITE)
            buttons_list.draw(screen)
            screen.blit(restart_text, [start_button.rect.x + 10,start_button.rect.y + 5])
            pygame.event.get()
            pos = pygame.mouse.get_pos()
            clicked = pygame.mouse.get_pressed()
            print(clicked)
            if clicked[0]==1 and start_button.rect.collidepoint(pos):
                ready = True
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip() 
            # --- Limit to 20 frames per second
            clock.tick(self.framerate)            
        print("READY")
        self.level=1
        self.missile_dead = 0
        all_sprites_list.empty()
        missile_list.empty()
        explosion_list.empty()
        planes_list.empty()
        base_list.empty()
        self.missile_count = 50
        self.framerate = 20
        self.score = 0
        controller.start()
        
 
class Missile(pygame.sprite.Sprite):
    """ This class represents the incoming missiles. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.duplicate_yes = random.randrange(2)
        self.duplicate = random.randrange(1,controller.level+1)
        self.duplicate_spacing = random.randrange(10,100)
        self.image = pygame.Surface([5, 5])
        
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.startx = random.randrange(screen_width)
        self.starty = -10
        self.rect.x = self.startx
        self.rect.y = self.starty
        self.xspeed = random.randrange(-3,3)
        self.yspeed = random.randrange(1,controller.level//2+2) 
    def draw_line(self):
        pygame.draw.line(screen, BLACK, [self.startx, self.starty], [self.rect.x,self.rect.y],4)
        pygame.draw.line(screen, RED, [self.startx, self.starty], [self.rect.x,self.rect.y],2)
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        self.draw_line()
        if self.rect.x < 0 or self.rect.x> screen_width or self.rect.y > screen_height:
            self.kill()
            controller.missile_dead
        if random.randrange(1000//controller.level +100) == 0:
            self.split()
    def split(self):
        for i in range(random.randrange(1,controller.level//2+2)):
            split_missile = Missile()
            split_missile.startx = self.rect.x
            split_missile.starty = self.rect.y
            split_missile.rect.x = self.rect.x
            split_missile.rect.y = self.rect.y
            split_missile.xspeed = self.xspeed + random.randrange(-2,3)
            split_missile.yspeed = self.yspeed
            split_missile.yspeed = self.yspeed
            missile_list.add(split_missile)
            all_sprites_list.add(split_missile)
    def draw(self):
        pygame.draw.circle(screen, BLACK, [self.rect.x, self.rect.y], 5)
        pygame.draw.circle(screen, BLUE, [self.rect.x, self.rect.y], 3)
        
        
class Plane(pygame.sprite.Sprite):
    """ This class represents the Player. """
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
        print("a plane is born")
        self.height = 10
        self.width = 30
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(20, (screen_height*2)//3)
        
        if random.randrange(2) == 0:
            self.rect.x = -30
            self.startx = -30
            self.speedx = random.randrange(1,6)
        else:
            self.rect.x = screen_width +30
            self.startx = screen_width +30
            self.speedx = random.randrange(-5,0)
    def update(self):
        self.rect.x += self.speedx
        if (random.randrange(20) == 0) and controller.missile_dead < controller.level*10:
            missile = Missile()
            missile.startx = self.rect.x + 6
            missile.starty = self.rect.y + 2
            missile.rect.x = self.rect.x + 6
            missile.rect.y = self.rect.y + 2
            missile_list.add(missile)
            all_sprites_list.add(missile)
        if (self.startx<0 and self.rect.x> screen_width + self.width):
            self.kill()
        if (self.startx>screen_width and self.rect.x<0):
            self.kill()
        
    def draw_plane(self):
        if self.startx < 0:
            pygame.draw.polygon(screen, BLACK, [[self.rect.x + self.width, self.rect.y], [self.rect.x + self.width,self.rect.y + self.height], [self.rect.x+self.width+10,self.rect.y+self.height//2]], 4) #cone moving right
            pygame.draw.polygon(screen, BLACK, [[self.rect.x,self.rect.y], [self.rect.x,self.rect.y-8], [self.rect.x+4,self.rect.y]], 4) #tail moving right
            pygame.draw.rect(screen, BLACK, [self.rect.x,self.rect.y, self.width, self.height], 4)            
            
            pygame.draw.polygon(screen, GREEN, [[self.rect.x + self.width, self.rect.y], [self.rect.x + self.width,self.rect.y + self.height], [self.rect.x+self.width+10,self.rect.y+self.height//2]]) #cone moving right
            pygame.draw.polygon(screen, GREEN, [[self.rect.x,self.rect.y], [self.rect.x,self.rect.y-8], [self.rect.x+4,self.rect.y]]) #tail moving right
            pygame.draw.rect(screen, GREEN, [self.rect.x,self.rect.y, self.width, self.height])
        else:
            pygame.draw.polygon(screen, BLACK, [[self.rect.x,self.rect.y], [self.rect.x-10,self.rect.y+self.height//2], [self.rect.x,self.rect.y+self.height]], 4) #cone moving left
            pygame.draw.polygon(screen, BLACK, [[self.rect.x + self.width,self.rect.y], [self.rect.x+self.width,self.rect.y-8], [self.rect.x+self.width-4,self.rect.y]], 4)   #tail  moving left  
            pygame.draw.rect(screen, BLACK, [self.rect.x,self.rect.y, self.width, self.height], 4) 
            
            pygame.draw.polygon(screen, GREEN, [[self.rect.x,self.rect.y], [self.rect.x-10,self.rect.y+self.height//2], [self.rect.x,self.rect.y+self.height]]) #cone moving left
            pygame.draw.polygon(screen, GREEN, [[self.rect.x + self.width,self.rect.y], [self.rect.x+self.width,self.rect.y-8], [self.rect.x+self.width-4,self.rect.y]])   #tail  moving left  
            pygame.draw.rect(screen, GREEN, [self.rect.x,self.rect.y, self.width, self.height])



class Patriot(Missile):
    '''Missiles fired at incoming'''
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([4, 4])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.startx = screen_width//2
        self.starty = screen_height-40
        self.rect.x = self.startx
        self.rect.y = self.starty
        self.pos = pygame.mouse.get_pos()
        self.xspeed = (-self.rect.x+self.pos[0])//10
        self.yspeed = (-self.rect.y+self.pos[1])//10
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.y <= self.pos[1]:
            explosion = Explosion(self.pos[0],self.pos[1])
            all_sprites_list.add(explosion)
            explosion_list.add(explosion) 
            all_sprites_list.remove(self)
            patriot_list.remove(self)        
    def pat_draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.rect.x, self.rect.y,5, 5])


class Explosion(pygame.sprite.Sprite):

    """ This class represents the bullet . """
    xbig = 0
    ybig = 0
    
    def __init__(self,x,y):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([1, 1])
        #self.image.fill(BLACK)
        #self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.expanding = True
        self.second_expand = False        
    def update(self):
        if self.expanding:
            self.xbig+=2
            self.ybig+=2
        else:
            self.xbig-=1
            self.ybig-=1            
        if self.ybig > 60 and self.expanding == True:
            self.expanding = False
        if self.ybig <30 and  self.expanding == False :
            explosion_list.remove(self)
            all_sprites_list.remove(self) 
        self.image = pygame.Surface([self.xbig, self.xbig])
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.xbig//2
        self.rect.y = self.y -self.ybig//2
        """ Move the bullet. """
        
    def draw(self):
        """ draw ellipse"""
        pygame.draw.ellipse(screen,BLACK,[self.rect.x - 2, self.rect.y -2 , self.xbig + 4,self.ybig +4])   
        pygame.draw.ellipse(screen,RED,[self.rect.x, self.rect.y, self.xbig,self.ybig])         
        
pygame.init()
 

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# Sprite groups
all_sprites_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
missile_list = pygame.sprite.Group()
base_list = pygame.sprite.Group()
patriot_list = pygame.sprite.Group()
buttons_list = pygame.sprite.Group()
planes_list = pygame.sprite.Group()
# Create sprites 
controller = Controller()

#Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates

clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 20, True, False)    
font_game_over = pygame.font.SysFont('Calibri', 50, True, False) 

#high_score()
controller.start()



# -------- Main Program Loop -----------

while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if controller.missile_count > 0:
                newpatriot = Patriot()
                patriot_list.add(newpatriot)
                all_sprites_list.add(newpatriot)
                controller.missile_count-=1
            
                
 
    # --- Game logic
    if (random.randrange((12-controller.level)*3) == 0) and controller.missile_dead < controller.level*10:
        missile = Missile()
        if missile.duplicate_yes == 1:
            for i in range(1,missile.duplicate+1):
                duplicate = Missile()
                duplicate.startx = missile.rect.x +missile.duplicate_spacing*i
                duplicate.starty = missile.rect.y
                duplicate.rect.x = missile.rect.x +missile.duplicate_spacing*i
                duplicate.rect.y = missile.rect.y
                duplicate.xspeed = missile.xspeed
                duplicate.yspeed = missile.yspeed
                missile_list.add(duplicate)
                all_sprites_list.add(duplicate)
        if random.randrange(20)== 0:
            plane = Plane()
            planes_list.add(plane)
            all_sprites_list.add(plane)
            
        missile_list.add(missile)
        all_sprites_list.add(missile)
    
    
    
        
    if controller.missile_dead >= controller.level*10 and (len(missile_list) == 0):
        controller.next_level()        

    # Call the update() method on all the sprites
    missile_list.update()
    
    
    screen.fill(WHITE)
    
    # Calculate mechanics for each bullet
    explosion_list.draw(screen)
    for explosion in explosion_list:
        explosion.update()
        explosion.draw()
    
    patriot_list.draw(screen)    
    for patriot in patriot_list:
        patriot.update()
        patriot.pat_draw()
        
    
    #explosion_list.draw(screen)
    #all_sprites_list.draw(screen)
    for planes in planes_list:
        planes.update()
        planes.draw_plane()
    for missiles in missile_list:
        missiles.draw_line()
               
    for bases in base_list:
        bases.draw(screen)
        
    missile_hit_list = pygame.sprite.groupcollide(missile_list, explosion_list, True, False)
    base_hit_list = pygame.sprite.groupcollide(base_list, missile_list, True, True)
    plane_hit_list = pygame.sprite.groupcollide(planes_list, explosion_list, True, False)
    base2_hit_list = pygame.sprite.groupcollide(base_list, explosion_list, False, True)
    for bases in base_hit_list:
        explosion = Explosion(bases.rect.x+20, bases.rect.y+10)
        all_sprites_list.add(explosion)
        explosion_list.add(explosion)        
           
    for missiles in missile_hit_list:
        controller.score += controller.level
        explosion = Explosion(missiles.rect.x, missiles.rect.y)
        all_sprites_list.add(explosion)
        explosion_list.add(explosion)
        controller.missile_dead+=1
    for planes in plane_hit_list:
        controller.score += 10 * controller.level
        explosion = Explosion(planes.rect.x + planes.width//2, planes.rect.y + planes.height//2)
        all_sprites_list.add(explosion)
        explosion_list.add(explosion)
        planes.kill()        
    if len(base_list) == 0:
        controller.game_over()
        #high_score()
        
        
    if controller.restarter == True:
        controller.restarter = False
        controller.restart()
    
    base_list.draw(screen)
    for missiles in missile_list:
        missiles.draw()
    missile_text = font.render("Missiles: " + str(controller.missile_count),True,BLACK)
    score_text = font.render("Score: " + str(controller.score), True, BLACK)
    level_text = font.render("Level: " + str(controller.level), True, BLACK)
    screen.blit(score_text, [20,50])
    screen.blit(missile_text, [300, 375])
    screen.blit(level_text, [20, 20])
    if controller.missile_count == 0 and (controller.frame//10)%2 == 0:
        empty_text = controller.font_med.render("OUT OF MISSILES!!!" ,True,RED)
        screen.blit(empty_text, [250, 200])
    controller.frame += 1
    #explosion_list.draw(screen)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(controller.framerate)
 
pygame.quit()