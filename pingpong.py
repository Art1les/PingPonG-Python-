from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, speed_x, speed_y, player_speed):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (speed_x, speed_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class L_player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

class R_player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed




win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Pingpong")
background = transform.scale(image.load("bg.jpg"), (win_width, win_height))
lplayer = L_player('L_wall.png', 5, 180, 20, 110, 3)
rplayer = R_player('R_wall2.png', 675, 180, 20, 110, 3)
ball = L_player('ball.png', 250, 250,   









game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    ball.rect.x += speed_x
    if ball.rect.y < 0 or ball.rect.y > win_height:
        ball.rect.y *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        lplayer.update()
        rplayer.update()


        lplayer.reset()
        rplayer.reset()
    display.update()
    clock.tick(FPS)
