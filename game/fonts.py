import pygame
from pygame import *
from game.resources import *
import game.border as border

font.init()

text = font.Font('game/gui/font/GillSansC.otf', 30)
fn = font.Font('game/gui/font/GillSansC-Bold.otf', 25)
ft = font.Font('game/gui/font/GillSansT.otf', 26)
monikafont = font.Font('game/gui/font/m1.ttf', 25)
fl = font.Font('game/gui/font/GillSansC.otf', 14)
fs = font.Font('game/gui/font/GillSansT.otf', 30)
fbig = font.Font('game/gui/font/GillSansC-Bold.otf', 38)

class MButton(pygame.sprite.Sprite):
    def __init__(self,group,ny,name,nx = 80):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.nx = nx
        self.ny = ny
        self.name = name
        self.col = col
    def update(self, f = fn):
        r = f.render(self.name,1,self.col)
        w = f.render(self.name,1,WHITE)
        surf = Surface((w.get_width()+10,40),SRCALPHA)
        x = (w.get_width()+8)//2
        y = 18
        pw = w.get_rect(center=(x, y))
        surf.blit(border.render(self.name,f,3,WHITE,self.col),(pw))
        self.image = surf
        self.rect = self.image.get_rect(topleft=(self.nx,self.ny))
class SButton(pygame.sprite.Sprite):
    def __init__(self,group,ny,name,nx = 450):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.nx = nx
        self.ny = ny
        self.name = name
        self.col = GREY
    def update(self, f = ft):
        w = f.render(self.name,1,self.col)
        self.image = w
        self.rect = self.image.get_rect(topleft=(self.nx,self.ny))
class LButton(pygame.sprite.Sprite):
    def __init__(self,group,nx,name,ny = 695):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(group)
        self.nx = nx
        self.ny = ny
        self.name = name
        self.col = DARK
    def update(self, f = fl):
        w = f.render(self.name,1,self.col)
        self.image = w
        self.rect = self.image.get_rect(center=(self.nx,self.ny))
def obvtext(win, nx, ny, name, f = fn, x = 3,ocol = BLACK,col = WHITE):
    w = f.render(name,1,BLACK)
    pw = w.get_rect(topleft=(nx-x, ny-x))
    win.blit(border.render(name,f,x,col,ocol),pw)
def justtext(win,x,y,name,f = ft,col = BLACK):
    r = f.render(name,1,col)
    p = r.get_rect(center=(x,y))
    win.blit(r,p)
def poemdef(win,zag, tex, f):
    z = f.render(zag,1,BLACK)
    win.blit(z,(250,40))
    for i in range(len(tex)):
        a = f.render(tex[i],1,BLACK)
        win.blit(a,(260, 100+40*i))
def say(win, m, name, normal = 1,f = ft,fn = fn):
    if name != 'i':
        nb = image.load('game/gui/namebox.png').convert_alpha()
        nbx = 265
        nby = 530
        nx = 350
        ny = 545
        win.blit(nb,(nbx,nby))
        nw = fn.render(name,1,WHITE)
        pn = nw.get_rect(center=(nx,ny))
        win.blit(border.render(name,fn,3),pn)
    ram = image.load('game/gui/textbox.png').convert_alpha()
    pr = ram.get_rect(center=(640,640))
    surf = Surface((816,146), pygame.SRCALPHA)
    win.blit(ram,pr)
    fx = 30
    fy = 30
    if normal and len(m) > 59:
        l = ''
        l2 = ''
        l3 = ''
        for o in range(len(m)):
            if len(l) < 59:
                l += m[o]
            elif len(l2) < 59:
                l2 += m[o]
            else:
                l3 += m[o]
        if l[-1] == ' ':
            pass
        else:
            if l2[0] == ' ':
                l2 = l2[1:]
            else:
                for oo in range(len(l)):
                    if l[-1] == " ":
                        break
                    else:
                        l2 = l[-1]+l2
                        l = l[:len(l)-1:]
        if len(l3) > 0:
            if l2[-1] == ' ':
                pass
            else:
                if l3[0] == ' ':
                    l3 = l3[1:]
                else:
                    for oo in range(len(l2)):
                        if l2[-1] == " ":
                            break
                        else:
                            l3 = l2[-1]+l3
                            l2 = l2[:len(l2)-1:]
        surf.blit(border.render(l,ft,1,WHITE,BLACK),(fx,fy))
        surf.blit(border.render(l2,ft,1,WHITE,BLACK),(fx,fy+25))
        surf.blit(border.render(l3,ft,1,WHITE,BLACK),(fx,fy+50))
    elif not normal or len(m) <= 59:
        surf.blit(border.render(m,ft,1,WHITE,BLACK),(fx,fy))
    win.blit(surf,(pr))