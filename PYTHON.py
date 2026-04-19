import pygame, random
pygame.init()

speed_x = 3
speed_y = 3
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

pygame.font.init()

font_stat = pygame.font.SysFont('Impact', 60)
lose_label = font_stat.render('YOU LOSE!', True, (255, 40, 40))
win_label = font_stat.render('YOU WIN!', True, (0, 255, 0))


game = True
game_over = False
racket_x = 200
racket_y = 330

class Area(): 
    def __init__(self, x=0, y=0, width=10, height=10, color=None): 
        self.rect = pygame.Rect(x, y, width, height) 
        self.fill_color = back 
        if color: 
            self.fill_color = color 
    def color(self, new_color): 
        self.fill_color = new_color 
    def fill(self): 
        pygame.draw.rect(mw, self.fill_color, self.rect) 
    def collidepoint(self, x, y): 
        return self.rect.collidepoint(x, y) 
    def colliderect(self, rect): 
        return self.rect.colliderect(rect)

class Picture(Area): 
    def __init__(self, filename, x=0, y=0, width=10, height=10): 
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None) 
        self.image = pygame.image.load(filename) 
    def draw(self): 
        mw.blit(self.image, (self.rect.x, self.rect.y))

ball = Picture('ball.webp', 160, 200, 50, 50)
platform = Picture('platform.webp', racket_x, racket_y, 100 , 000)

start_x = 5
start_y = 5
count = 9
monsters = list()
for j in range(3): 
    y = start_y + (55 * j) 
    x = start_x + (27 * j) 
    for i in range(count): 
        d = Picture('enemy.webp', x, y, 50, 50) 
        monsters.append(d) 
        x = x + 55
    count = count - 1

while game: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if not game_over:
        mw.fill(back) 
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y 

        if ball.colliderect(platform.rect):
            speed_y *= -1.010

        if ball.rect.x > 450 or ball.rect.x < 0:
            speed_x *= -1
        if ball.rect.y < 0:
            speed_y *= -1

        
        for m in monsters:
            if ball.colliderect(m.rect):
                monsters.remove(m)
                speed_y *= -1.010
        
        if len(monsters) == 0:
            game_over = True

        if ball.rect.y > 450:
            game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and platform.rect.x < 400:
            platform.rect.x += 5
        if keys[pygame.K_LEFT] and platform.rect.x > 0:
            platform.rect.x -= 5

        for m in monsters: 
            m.draw() 
        
        platform.draw() 
        ball.draw() 
    else:
        if len(monsters) == 0:
            mw.blit(win_label, (180, 160))
        else:
            mw.blit(lose_label, (180, 160))

    pygame.display.update() 
    clock.tick(60)

pygame.quit() 
