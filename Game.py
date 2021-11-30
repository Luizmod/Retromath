#!/usr/bin/python3

import pygame, sys
import random
import operator

mainClock = pygame.time.Clock()
from pygame.locals import *

SCREEN_WIDTH = 540
SCREEN_HEIGHT = 360

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (219, 42, 11)

pygame.init()
pygame.display.set_caption('RetroMath')
screen = pygame.display.set_mode((540, 360), 0, 32)
background_image = pygame.image.load('background.jpg').convert()
font = pygame.font.Font('retrofont.TTF', 27)
font1 = pygame.font.Font('retrofont.TTF', 30)
font2 = pygame.font.Font('retrofont.TTF', 15)
problema = {"num1": 0, "num2": 0, "resultado": 0}
score = 0
puntajes = {}
sound1= pygame.mixer.Sound('item1.ogg')
sound2 = pygame.mixer.Sound('item2.ogg')
sound3 = pygame.mixer.Sound('music.mp3')
dificultad = 10


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def botones(screen, boton, palabra):
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen,(RED),boton,2)
        texto = font.render(palabra, True, (0, 0, 0))
        screen.blit(texto, (boton.x + (boton.width - texto.get_width()) / 2,
                            boton.y + (boton.height - texto.get_height()) / 2))
    else:
        pygame.draw.rect(screen, (0, 0, 0), boton,2)
        texto = font.render(palabra,True,(BLACK))
        screen.blit(texto,(boton.x+(boton.width-texto.get_width())/2,
                           boton.y+(boton.height-texto.get_height())/2))


def main_menu():
    with open("Puntaje alto.txt", "r") as f:
        for line in f:
            (key, val) = line.split()
            puntajes[key] = val
    while True:
        screen.blit(background_image, (0, 0))
        draw_text('Menu principal', font, (BLACK), screen, 150, 20)
        mx, my = pygame.mouse.get_pos()
        items = ['Jugar', 'Puntajes altos', 'Salir']
        rect_list = []

        for i in range(0,3):
            size = font.size(items[i])
            width = size[0]
            height = size[1]
            posX = (SCREEN_WIDTH / 2) - (width / 2)
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (i * height)
            rect = pygame.Rect(posX, posY, width, height)
            rect_list.append(rect)

        botones(screen,rect_list[0],'Jugar')
        botones(screen,rect_list[1],'Puntajes altos')
        botones(screen,rect_list[2],'Salir')

        for event in pygame.event.get():
            if rect_list[0].collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    game()
            if rect_list[1].collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    highscore()
            if rect_list[2].collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    quit()
            if event.type == QUIT:
                    quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()

        pygame.display.update()
        mainClock.tick(60)


def suma():
    a = random.randint(1, dificultad)
    b = random.randint(1, dificultad)
    problema["num1"] = a
    problema["num2"] = b
    problema["resultado"] = a + b


def resta():
    a = random.randint(0, dificultad)
    b = random.randint(0, dificultad)
    if a > b:
        problema["num1"] = a
        problema["num2"] = b
        problema["resultado"] = a - b
    else:
        problema["num1"] = b
        problema["num2"] = a
        problema["resultado"] = b - a


def multiplicacion():
    a = random.randint(1, dificultad)
    b = random.randint(1, dificultad)
    problema["num1"] = a
    problema["num2"] = b
    problema["resultado"] = a * b


def division():
    divisor = random.randint(1, dificultad)
    dividendo = divisor * random.randint(1, 12)
    cosiente = dividendo / divisor
    problema["num1"] = dividendo
    problema["num2"] = divisor
    problema["resultado"] = int(cosiente)


def game():
    global score
    global dificultad

    if score == 0:
        sound3.play()

    operacion = ''
    ejercicio = random.randint(1,4)

    if ejercicio == 1:
        suma()
        operacion = '+'

    if ejercicio == 2:
        resta()
        operacion = '-'

    if ejercicio == 3:
        multiplicacion()
        operacion = 'x'

    if ejercicio == 4:
        division()
        operacion = '/'

    if score == 20:
        dificultad += 5

    if score == 40:
        dificultad += 10

    if score == 60:
        dificultad += 20

    button_list = []
    numero = random.randint(1, 4)
    num1 = (problema["resultado"]+10)
    num2 = problema["resultado"]-10
    num3 = int((problema["resultado"]+(10/1.5)))
    num4 = int((problema["resultado"]+(10*0.5)))
    width = 85
    height = 50
    t_w = width * 2 + 50 #Total_Width
    posX = (SCREEN_WIDTH / 2) - 150
    posY = 100
    running = True

    while running:
        screen.blit(background_image,(0,0))
        draw_text(str(problema["num1"]), font1, BLACK,screen,125,40)
        draw_text(str(operacion), font1, BLACK, screen, 210, 40)
        draw_text(str(problema["num2"]) + " = ?", font1, BLACK,screen,275,40)
        draw_text('Puntaje: ' + str(score), font2, BLACK,screen,20,10)

        if numero == 1:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[0], str(problema["resultado"]))
            res = 0
        else:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[0], str(num1))

        posX = (SCREEN_WIDTH / 2) - (t_w / 2) + 150

        if numero == 2:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[1], str(problema["resultado"]))
            res = 1
        else:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[1], str(num2))

        posX = (SCREEN_WIDTH / 2) - 150
        posY = 160

        if numero == 3:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[2], str(problema["resultado"]))
            res = 2
        else:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[2], str(num3))

        posX = (SCREEN_WIDTH / 2) - (t_w / 2) + 150

        if numero == 4:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[3], str(problema["resultado"]))
            res = 3
        else:
            btn = pygame.Rect(posX, posY, width, height)
            button_list.append(btn)
            botones(screen, button_list[3], str(num4))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sound3.stop()
                    frames()
            if event.type == MOUSEBUTTONDOWN:
                if button_list[0].collidepoint(pygame.mouse.get_pos()):
                    if res != 0:
                        sound2.play()
                        sound3.stop()
                        frames()
                        return True
                    if res == 0:
                        sound1.play()
                        score += 5
                        game()
                        pygame.display.update()
                        mainClock.tick(60)

                if button_list[1].collidepoint(pygame.mouse.get_pos()):
                    if res != 1:
                        sound2.play()
                        sound3.stop()
                        frames()
                        return True
                    if res == 1:
                        sound1.play()
                        score += 5
                        game()
                        pygame.display.update()
                        mainClock.tick(60)

                if button_list[2].collidepoint(pygame.mouse.get_pos()):
                    if res != 2:
                        sound2.play()
                        sound3.stop()
                        frames()
                        return True
                    if res == 2:
                        sound1.play()
                        score += 5
                        game()
                        pygame.display.update()
                        mainClock.tick(60)

                if button_list[3].collidepoint(pygame.mouse.get_pos()):
                    if res != 3:
                        sound2.play()
                        sound3.stop()
                        frames()
                        return True
                    if res == 3:
                        sound1.play()
                        score += 5
                        game()
                        pygame.display.update()
                        mainClock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)


def frames():
    global score
    running = True
    items = ('Menu principal', 'Puntajes altos')
    rect_list = []
    for i in range(0, 2):
        size = font.size(items[i])
        width = size[0]
        height = size[1]
        posX = (SCREEN_WIDTH / 2) - (width / 2)
        t_h = len(items) * height
        posY = (100+(SCREEN_HEIGHT / 2)) - (t_h / 2) + (i * height)
        rect = pygame.Rect(posX, posY, width, height)
        rect_list.append(rect)

    while running:
        screen.blit(background_image,(0,0))
        if score >= 20:
            draw_text('Puntaje alto!',font,BLACK,screen,130,140)
            draw_text('Escriba su nombre:', font2, BLACK, screen, 160, 180)
            puntaje()
        else:
            draw_text("perdiste",font,BLACK,screen,200,20)
            draw_text('su puntaje fue de: ',font,BLACK,screen,100,50)
            draw_text(f'{str(score)}',font,BLACK,screen,SCREEN_WIDTH/2,100)
            botones(screen, rect_list[0], 'Menu principal')
            botones(screen,rect_list[1],'Puntajes altos')

        for event in pygame.event.get():
            if rect_list[0].collidepoint((pygame.mouse.get_pos())):
                if event.type == MOUSEBUTTONDOWN:
                    score = 0
                    main_menu()
            if rect_list[1].collidepoint((pygame.mouse.get_pos())):
                if event.type == MOUSEBUTTONDOWN:
                    highscore()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    score = 0
                    running = False
                    main_menu()
        pygame.display.update()
        mainClock.tick(60)


def puntaje():
    clock = pygame.time.Clock()
    input_box = pygame.Rect(165, 200, 100, 32)
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    frames()
                if event.key == pygame.K_ESCAPE:
                    return True
                if active:
                    if event.key == pygame.K_ESCAPE:
                        return True
                    if event.key == pygame.K_RETURN:
                        with open("Puntaje alto.txt", "a") as f:
                            f.write(f'\n{text} {int(score)}')
                        text = f''
                        main_menu()
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.update()
        clock.tick(60)


def highscore():
    global puntajes
    running = True
    while running:
        puntajes_sort = sorted(puntajes.items(), key=operator.itemgetter(1), reverse=True)
        screen.blit(background_image,(0,0))
        texto = font.render('Puntajes altos',True,(255,255,255))
        draw_text('Puntajes altos', font, BLACK, screen, (screen.get_width()-texto.get_width())/2,20)
        i=0
        for name in enumerate(puntajes_sort):
            i+=1
            draw_text((name[1][0]) ,font,BLACK,screen,150,160*i/2)
            draw_text((puntajes[name[1][0]]),font,BLACK,screen,300,160*i/2)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)
main_menu()