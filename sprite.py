import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
screen = pygame.display.set_mode((640,480),pygame.SCALED)
clock = pygame.time.Clock()
score = 0


#create the background

background= pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))

#Text in the background
font=pygame.font.Font(None,64)
text=font.render("Score: " + str(score) ,True, (0,0,0))
textpos=text.get_rect(centerx=background.get_width() / 2, y=10)
background.blit(text, textpos)


# Cargamos la imagen del sprite
sprite_imagen = pygame.image.load("figura.png")
sprite_rect = sprite_imagen.get_rect()


screen.blit(sprite_imagen, sprite_rect)

x = 400
y = 400
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    sprite_rect.center = (mouse_x, mouse_y)


    screen.blit(background, (0, 0))
    screen.blit(sprite_imagen, sprite_rect)
    rectangulo=pygame.draw.rect(screen,(0,0,255),(50,50,50,50))
    if rectangulo.colliderect(sprite_rect):
        score+=1

    font=pygame.font.Font(None,64)
    text=font.render("Score: " + str(score) ,True, (0,0,0))
    textpos=text.get_rect(centerx=background.get_width() / 2, y=10)
    background.blit(text, textpos)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
