import pygame
import time

back = (47, 79, 79) #фон
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

 
class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > -90:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height-210:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > -90:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - 210:
            self.rect.y += self.speed

player1 = Player('L_wall.png', 10, 100, 30, 300, 15)
player2 = Player('R_wall2.png', win_width-40, 100, 30, 300, 15)
ball = GameSprite('ball.png', 280, 200, 40, 40, 4) 

dx = 3
dy = 3

pygame.font.init()
font = pygame.font.Font(None, 40)
win2 = font.render('PLAYER 2 WIN!', True, (0, 255, 0))
win1 = font.render('PLAYER 1 WIN!', True, (0, 255, 0))

score_left = 0 
score_right = 0

while game:
    time_start = time.time()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if finish != True:
        window.fill(back)
        player1.update_l()
        player2.update_r()
        
        
        ball.rect.x += dx 
        ball.rect.y += dy 

        time_end = time.time()
        res = time_end-time_start
        if pygame.sprite.collide_rect(player1, ball)  or pygame.sprite.collide_rect(player2, ball): 
            dx *= -1  



        if ball.rect.y < 0 or ball.rect.y > win_height-40: 
            dy *= -1    

        if ball.rect.x < 0: 
            score_right += 1
            ball.rect.x = 280
            ball.rect.y = 200
            time.sleep(0.1)
            if dx > 0:
                dx *= -1           

        
        if ball.rect.x > win_width:
            score_left += 1
            ball.rect.x = 280
            ball.rect.y = 200
            time.sleep(0.1)
            if dx < 0:
                dx *= -1  

        player1.reset()
        player2.reset()

        ball.reset() 

        score_l = font.render(str(score_left), True, (0,0,0))
        score_r = font.render(str(score_right), True, (0,0,0))
        window.blit(score_l, (10,10))
        window.blit(score_r, (win_width-25,10))

        if score_right >= 5:
            finish = True
            window.blit(win2, (200, 200))


        if score_left >= 5:
            finish = True
            window.blit(win1, (200, 200))


    pygame.display.update()
    clock.tick(FPS)
