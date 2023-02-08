import pygame as pg
import os
import time

#constants
WIDTH = 600
HEIGHT = 800
FPS = 60
clock = pg.time.Clock()
#images_properties
SPACE_SHIP_WIDTH = 40
SPACE_SHIP_HEIGHT = 40
ALIEN_WIDTH = 30
ALIEN_HEIGHT = 30
#other
vel = 6
alien_vel = 1

#images
background_image = pg.image.load(os.path.join("assets", "background_space.png"))
background = pg.transform.scale(background_image, (WIDTH, HEIGHT))


#player
player_image = pg.image.load(os.path.join("assets", "spaceship_red.png"))
player_character = pg.transform.scale(pg.transform.rotate(player_image,180) ,(SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT))

#aliens
alien_red_image = pg.image.load(os.path.join("assets","aliens","alien_red.png"))
alien_red = pg.transform.scale(alien_red_image,(ALIEN_WIDTH, ALIEN_HEIGHT))

alien_yellow_image = pg.image.load(os.path.join("assets","aliens","alien_yellow.png"))
alien_yellow = pg.transform.scale(alien_yellow_image,(ALIEN_WIDTH, ALIEN_HEIGHT))

alien_green_image = pg.image.load(os.path.join("assets","aliens","alien_green.png"))
alien_green = pg.transform.scale(alien_green_image,(ALIEN_WIDTH, ALIEN_HEIGHT))

alien_pink_image = pg.image.load(os.path.join("assets","aliens","alien_pink.png"))
alien_pink = pg.transform.scale(alien_pink_image,(ALIEN_WIDTH, ALIEN_HEIGHT))


WIN = pg.display.set_mode((WIDTH, HEIGHT))

class Alien:
    def __init__(self, x=-50 , y=60, color=alien_pink, health=10 ):
        self.x = x
        self.y = y
        self.health = health
        self.color = color
    def drift(self,):
            if self.x <= WIDTH:
                self.x += alien_vel
            else:
                self.x = -15       
    def draw(self):
        WIN.blit(self.color, (self.x, self.y))

  
         



class Player:
    def __init__(self, x=WIDTH/2, y=HEIGHT/2, health=100, ammo = 10):
        self.x = x
        self.y = y
        self.health = health
        self.ammo = ammo
        self.player_image = player_character
        self.mask = pg.mask.from_surface(self.player_image)

    def draw(self,):
        WIN.blit(self.player_image, (self.x, self.y))
    
    def get_width(self):
        return self.player_image.get_width()

    def get_height(self):
        return self.player_image.get_height()
    def move(self, vel):
        if pg.key.get_pressed()[pg.K_LEFT] and self.x - vel > 0: #left
            self.x -= vel
        if pg.key.get_pressed()[pg.K_RIGHT] and self.x + vel + self.get_width() < WIDTH:
            self.x += vel
        if pg.key.get_pressed()[pg.K_UP] and self.y - vel > 0: #up
            self.y -= vel
        if pg.key.get_pressed()[pg.K_DOWN] and self.y + vel + self.get_height() + 15 < HEIGHT: #down
            self.y += vel
    def shoot(self):
        pass
        # if pg.key.get_pressed()[pg.K_SPACE]:
        #     bullet = pg.Rect(self.x + self.get_width()//2 - 2, self.y, 5, 10)
        # pg.draw.rect(WIN, (255,0,0), bullet)        

player = Player()
pink_alien = Alien(-100, 50)
red_alien = Alien(-200,100, alien_red)
green_alien = Alien(-300, 150, alien_green)
yellow_alien = Alien(-400, 200, alien_yellow)


def draw_window():
    WIN.blit(background, (0, 0))
    player.move(4)
    player.draw()
    player.shoot()
    pink_alien.draw()
    green_alien.draw()
    red_alien.draw()
    yellow_alien.draw()

    pg.display.update()


def main():
    pg.init()
    pg.display.set_caption("Space Invaders")
    clock.tick(FPS)
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False       
        draw_window()
        pink_alien.drift()        
        red_alien.drift()        
        yellow_alien.drift()        
        green_alien.drift()     



    pg.quit()

if __name__ == '__main__':
    main()