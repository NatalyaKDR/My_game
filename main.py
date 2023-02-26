import pygame
import sys

pygame.init()

W = 500
H = 500
popal=False
move_right=True
move_left=False
bullets_left=3
bullet=True

window = pygame.display.set_mode((W, H))
fps = 60
clock = pygame.time.Clock()

#шрифт
font=pygame.font.Font(None,50)
font1_render=font.render("Попал",True,(250,250,250))
font1_rect=font1_render.get_rect()

font2=pygame.font.Font(None,30)


#мишень
class Target(pygame.sprite.Sprite):
    def __init__(self,x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(filename).convert_alpha()
        self.image=pygame.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect(center=(x,y))

target= Target(W//2,H//2,"target.png")

#звук
sound_shoot=pygame.mixer.Sound('vyistrel.wav')
sound_reloading=pygame.mixer.Sound('perezaryadka.wav')


pygame.display.update()

while True:
    clock.tick(fps)
    window.fill((0, 0, 0))
    window.blit(target.image, target.rect)

    font2_render = font2.render(f"Осталось выстрелов {bullets_left}", True, (250, 250, 250))
    font2_rect = font2_render.get_rect()
    window.blit(font2_render, (20, 400))

    font3_render = font2.render("Для перезарядки нажмите SPACE", True, (250, 250, 250))
    font3_rect = font3_render.get_rect()
    window.blit(font3_render, (20, 450))

# движение мишени туда-сюда
    if target.rect.centerx < 400 and move_right:
        target.rect.centerx += 3
    elif target.rect.centerx == 400:
        move_right = False
        move_left = True
        target.rect.centerx -= 3
    elif target.rect.centerx > 100 and move_left:
        target.rect.centerx -= 3
    elif target.rect.centerx == 100:
        move_right = True
        move_left = False
        target.rect.centerx += 3


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and bullet:
            bullets_left-=1
            point = pygame.mouse.get_pos()
            collide = target.rect.collidepoint(point)
            sound_shoot.play()

            if collide:
                popal=True
            if bullets_left==0:
                bullet=False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and popal==False:
            sound_reloading.play()
            bullets_left = 3
            bullet = True


    if popal:
        window.blit(font1_render, ((W - font1_rect.width) // 2, 100)) #пишем попал
        target = Target(W // 2, H // 2, "target2.png")
        bullet = False


    pygame.display.update()
