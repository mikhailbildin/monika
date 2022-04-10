import pygame
from pygame import *
from game.resources import *

class Girl(pygame.sprite.Sprite):
    def __init__(self,spr,dfn,name,ras,x,y = 360,z = 0.8):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.ras = ras
        self.dfn = dfn
        self.x = x
        self.y = y
        self.z = z
        self.spr = spr
        self.surf = self.crspr()
        self.alpha = 255
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
        self.image = transform.smoothscale(self.surf, (960*self.z, 960*self.z)).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.image.set_alpha(self.alpha)
    def zoom(self,z,dt):
        if z == 0.9:
            if self.z < 0.9:
                self.z += 0.2*dt
            elif self.z > 0.89:
                self.z = 0.9
        elif z == 0.8:
            if self.z > 0.8:
                self.z -= 0.2*dt
            elif self.z < 0.81:
                self.z = 0.8
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
        self.image = image.load('game/'+ras).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
class Box(pygame.sprite.Sprite):
    def __init__(self,group,x,y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.x = x
        self.y = y
        self.image = Surface((256,144))
        self.image.fill(PINK)
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.text = "пустой слот"