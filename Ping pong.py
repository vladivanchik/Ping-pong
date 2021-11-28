from pygame import *
from turtle import *
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
end_fill()
window = display.set_mode((700,500))
display.set_caption(Ping pong)
background = transform.scale(image.load("Bacground.png"),(700,500)
player1 = transform.scale(image.load())
ball = transform.scale(image.load("Tennis.png"),(100,100)
game = True
while game:
    window.blit(backgroung,(0,0))
    for e in event.get()
    if e.type == QUIT:
        game = False
