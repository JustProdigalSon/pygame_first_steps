import pygame as pg
import sys
pg.font.init()

## colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
##spaceships demensions
SPACE_SHIP_WIDTH = 50
SPACE_SHIP_HEIGHT = 50
RED_HEALTH = 100

winner_font = pg.font.SysFont("comicsans", 100)

background_image = pg.image.load("assets/background.png")
background = pg.transform.scale(background_image, (800, 600))

player_yellow_image= pg.image.load("assets/pixel_art/spaceship_yellow.png")
player_yellow = pg.transform.scale(pg.transform.rotate(player_yellow_image,90) 
,(SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT))

player_red_image = pg.image.load("assets/pixel_art/spaceship_red.png")
player_red = pg.transform.scale(pg.transform.rotate(player_red_image,270) 
,(SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT))


Width, Height = 800, 600
pg.display.set_caption("Space Duel") 
WINDOW = pg.display.set_mode((Width, Height))


VEL = 5
BULLETS_VEL = 1
FPS = 60
clock = pg.time.Clock()
yellow_bullets = []
red_bullets = []
YELLOW_HIT = pg.USEREVENT + 1
RED_HIT = pg.USEREVENT + 2
RED_HEALTH = 100
YELLOW_HEALTH = 100


def bullet_heandler(yellow_bullets, red_bullets, yellow, red,):
    for bullet in yellow_bullets:
        bullet.x += BULLETS_VEL
        if red.colliderect(bullet):
            pg.event.post(pg.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        if bullet.x > 800:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLETS_VEL
        if yellow.colliderect(bullet):
            red_bullets.remove(bullet)
            pg.event.post(pg.event.Event(YELLOW_HIT))
        if bullet.x < 0:
                red_bullets.remove(bullet) 


            

def temp_draw_bullets(yellow_bullets,red_bullets):
    for bullet in yellow_bullets:
        bullet.x += BULLETS_VEL
        pg.draw.rect(WINDOW, RED, bullet)
        

    for bullet in red_bullets:
        bullet.x -= BULLETS_VEL
        pg.draw.rect(WINDOW, RED, bullet)
        print(bullet.x)           

def health_handler(player):
    if player == "red":
        global RED_HEALTH
        RED_HEALTH -= 10
        print(RED_HEALTH)
    if player == "yellow":
        global YELLOW_HEALTH
        YELLOW_HEALTH -= 10
def winner():
    if RED_HEALTH <= 0:
        winner_label = winner_font.render("Yellow Wins", 1, YELLOW)
        WINDOW.blit(winner_label, (Width/2 - winner_label.get_width()/2, Height/2 - winner_label.get_height()/2))
    if YELLOW_HEALTH <= 0:
        winner_label = winner_font.render("Red Wins", 1, RED)
        WINDOW.blit(winner_label, (Width/2 - winner_label.get_width()/2, Height/2 - winner_label.get_height()/2))

def health_bar(WINDOW, x, y, health):
    if health < 0:
        health = 0
    pg.draw.rect(WINDOW, BLACK, (x, y, 100, 10))
    pg.draw.rect(WINDOW, RED, (x, y, health, 10))

# def bullet_heandler(red, yellow):
#     bullets = []
#     keys_pressed = pg.key.get_pressed()
#     if keys_pressed[pg.K_v]:
#         bullets.append("X")
#         bullet = pg.rect(red.x, red.y/2, 10, 10)
#         pg.draw.rect(WINDOW, RED, bullet)


def move_red(red):
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[pg.K_a] and red.x - VEL > 0 and (red.x - VEL) > Width/2 - 5: # left
        red.x -= VEL
    if keys_pressed[pg.K_d] and red.x + VEL + red.width < Width: # right
        red.x += VEL
    if keys_pressed[pg.K_w] and red.y - VEL > 0: # up
        red.y -= VEL
    if keys_pressed[pg.K_s] and red.y + VEL + red.height < Height: # down
        red.y += VEL

def move_yellow(yellow):
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[pg.K_LEFT] and yellow.x - VEL > 0:  
        yellow.x -= VEL
    if keys_pressed[pg.K_RIGHT] and yellow.x + VEL + yellow.width < Width and (yellow.x + VEL + yellow.width) < Width/2 - 5: 
        yellow.x += VEL    
    if keys_pressed[pg.K_UP] and yellow.y - VEL > 0: 
        yellow.y -= VEL
    if keys_pressed[pg.K_DOWN] and yellow.y + VEL + yellow.height < Height: 
        yellow.y += VEL

border = pg.Rect(Width/2 - 5, 0, 4, Height)

def draw_window(red, yellow, yellow_bulets):

    WINDOW.fill(WHITE)
    WINDOW.blit(background, (0, 0))
    WINDOW.blit(player_red, (red.x, red.y))
    WINDOW.blit(player_yellow, (yellow.x, yellow.y))

    pg.draw.rect(WINDOW, BLACK, border)
    health_bar(WINDOW, 10, 10, RED_HEALTH)
    health_bar(WINDOW, 690, 10, YELLOW_HEALTH)
    temp_draw_bullets(yellow_bulets, red_bullets)
    winner()
    pg.display.update()
    


def main():
    
    red = pg.Rect(700, 225, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
    yellow = pg.Rect(50, 225, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
    run = True 
    while run: 
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
               run = False  
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LCTRL and len(red_bullets) < 3:
                    bullet = pg.Rect(red.x - SPACE_SHIP_WIDTH, red.y + SPACE_SHIP_HEIGHT//2 - 5, 10, 10)
                    red_bullets.append(bullet)
                    print(bullet)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RCTRL and len(yellow_bullets) < 3:
                            bullet = pg.Rect(yellow.x + SPACE_SHIP_WIDTH, yellow.y + SPACE_SHIP_HEIGHT//2 - 5, 10, 10)
                            yellow_bullets.append(bullet)
            if event.type == RED_HIT:
                health_handler("red")
            if event.type == YELLOW_HIT:
                health_handler("yellow")    
        move_red(red)
        move_yellow(yellow)
        bullet_heandler(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, yellow_bullets)
                





    pg.quit()




if "__main__" == __name__:
    main()