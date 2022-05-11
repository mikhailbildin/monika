import pygame

pygame.init()
pygame.mixer.init()
# Sounds
flip = pygame.mixer.Sound('game/sfx/pageflip.ogg')
over = pygame.mixer.Sound('game/sfx/hover.ogg')
select = pygame.mixer.Sound('game/sfx/select.ogg')

#Colors
colb = (137,64,113)
col = (187,85,136)
colh = (255,170,204)
colhh = (255,200,230)
WHITE = (255,255,255)
BLACK = (0,0,0)
DARK = (50,50,50)
GREY = (200,200,200)
PINK = (236,182,229)

#Data
months = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
days = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]

#x
x11 = 640
x21 = 400
x22 = 880
x31 = 240
x32 = 640
x33 = 1040
x41 = 200
x42 = 493
x43 = 786
x44 = 1080