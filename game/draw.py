import pygame
from pygame import *
from game.resources import *
from game.fonts import *

class Girl(pygame.sprite.Sprite):
    def __init__(self,spr,dfn,name,ras,p,y = 360,z = 0.8*0.95,alpha = 150,lp = 0):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.ras = ras
        self.dfn = dfn
        self.x = xlist["x11"]
        self.y = y
        self.z = z
        self.spr = spr
        self.surf = self.crspr()
        self.alpha = alpha
        self.lp = lp
    def crspr(self):
        surf = Surface((960,960), pygame.SRCALPHA)
        for i in range(len(self.dfn[self.spr])):
            if type(self.dfn[self.spr]) == type("string"):
                iii = image.load('game/images/'+self.ras+self.dfn[self.spr]+'.png').convert_alpha()
            else:
                iii = image.load('game/images/'+self.ras+self.dfn[self.spr][i]+'.png').convert_alpha()
            if self.name == "Нацуки":
                if self.dfn[self.spr][i] == '3' or self.dfn[self.spr][i] == '3b':
                    surf.blit(iii,(-18,-22))
                else:
                    surf.blit(iii,(0,0))
            else:
                surf.blit(iii,(0,0))
        return surf
    def update(self):
        if self.z < 0:
            self.z = 0.8
        self.image = transform.smoothscale(self.surf, (960*self.z, 960*self.z)).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.image.set_alpha(self.alpha)
    def zoom(self,z,dt):
        if z == 0.9:
            if self.z < 0.8*1.05:
                self.z += 0.2*dt
        elif z == 0.8:
            if self.z > 0.8:
                self.z -= 0.2*dt
class Menuspr(pygame.sprite.Sprite):
    def __init__(self,group, ir, number = 1, x = 0, y = 360):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        i = image.load("game/gui/"+ir).convert_alpha()
        self.image = transform.smoothscale(i, (i.get_width()*number,i.get_height()*number))
        self.rect = self.image.get_rect(center=(x,y))
        self.pos = math.Vector2(self.rect.topleft)
    def update(self):
        pass
class Choice(pygame.sprite.Sprite):
    def __init__(self,y,s = 'idle'):
        pygame.sprite.Sprite.__init__(self)
        self.y = y
        self.hov = 0
        self.s = s
        self.image = image.load('game/gui/button/choice_'+self.s+'_background.png').convert_alpha()
        self.rect = self.image.get_rect(center = (640,self.y))
    def update(self):
        self.image = image.load('game/gui/button/choice_'+self.s+'_background.png').convert_alpha()
class OneSprite(pygame.sprite.Sprite):
    def __init__(self,group,ras,x,y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.x = x
        self.y = y
        self.alpha = 255
        self.image = image.load('game/'+ras).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.image.set_alpha(self.alpha)
class Box(pygame.sprite.Sprite):
    def __init__(self,group,x,y,number):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.x = x
        self.y = y
        self.image = Surface((256,144))
        self.image.fill(PINK)
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.text = "пустой слот"
        self.number = number
        self.lx = self.x - 135
        self.ly = self.y
        self.limage = Surface((5,144))
        self.limage.fill(PINK)
        self.lrect = self.limage.get_rect(center = (self.lx,self.ly))
    def line(self,win):
        win.blit(self.limage, self.lrect)
def Confirm(win,words):
    surf = Surface((1280,720),SRCALPHA)
    surf.blit(image.load("game/gui/overlay/confirm.png").convert_alpha(),(0,0))
    boxx = image.load("game/gui/frame.png")
    w = text.render(words,1,BLACK)
    if 100+w.get_width() < 300:
        a = 300
    else:
        a = 100+w.get_width()
    box = transform.scale(boxx,(a,250))
    b = box.get_rect(center=(640,360))
    surf.blit(box,b)
    surf.blit(w,w.get_rect(center=(640,300)))
    win.blit(surf,(0,0))
def Console(win,words1 = "",words2 = "",words3 = ""):
    surf = Surface((480,180),SRCALPHA)
    surf.fill(GREY)
    surf.set_alpha(200)
    w = text.render(str(words1),1,WHITE)
    w2 = text.render(str(words2),1,WHITE)
    w3 = text.render(str(words3),1,WHITE)
    surf.blit(w,(10,10))
    surf.blit(w2,(10,50))
    surf.blit(w3,(10,100))
    win.blit(surf,(0,0))