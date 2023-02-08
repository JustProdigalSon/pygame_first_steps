import pygame as pg
import sys

print("hello world")
Width, Height = 800, 600
WINDOW = pg.display.set_mode((Width, Height));
pg.display.set_caption("Hello World")
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
           run = False
            
    pg.draw.rect(WINDOW, (255, 0, 0), (350, 250, 100, 100))
    pg.display.update()
pg.quit()