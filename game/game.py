import pygame, sys, time as TIM
from pygame import *
from game.fonts import *
from game.descript import Descripter
from game.draw import *
from game.definitions import *
from game.easings import *
from game.poems import *
import game.default as default
from game.resources import *
import game.settings as settings
import game.border as border

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.menu = 1
        self.flags = settings.flags
        self.ifprop = settings.ifprop
        self.ifnewtext = settings.ifnewtext
        self.skort = settings.skort
        self.skora = settings.skora
        self.gromm = settings.gromm
        self.gromz = settings.gromz
        self.win_size = (1280,720)
        self.win = display.set_mode(self.win_size,self.flags)
        display.set_icon(image.load('game/gui/app.png'))
        display.set_caption("DLC of DDLC")
        self.clock = time.Clock()
        self.t = TIM.localtime()
        self.g = 0
        self.oksurf = pygame.Surface(self.win_size,SRCALPHA)
        self.oksurf.blit(image.load('game/gui/overlay/confirm.png').convert_alpha(),(0,0))
    def notjustmonika(self,go):
        self.g = 1
        run = 1
        mus = "game/bgm/morning.ogg"
        pbg = "game/images/bg/bedroom_evening.png"
        pcg = ""
        pcge = ""
        dspr = '1forma'
        script = 0
        bg = transform.smoothscale(image.load(pbg).convert(),self.win_size)
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
        kd = 0
        name = ''
        r = ''
        okm = 1
        a = 0
        doki = []
        girls = pygame.sprite.Group()
        Monika = Girl(dspr,m,"Моника",'monika/',x11)
        Sayori = Girl(dspr,s,"Сайори",'sayori/',x11)
        Yuri = Girl(dspr,y,"Юри",'yuri/',x11)
        Natsuki = Girl(dspr,n,"Нацуки",'natsuki/',x11)
        doki.append(Monika)
        doki.append(Sayori)
        doki.append(Yuri)
        doki.append(Natsuki)
        csurf = Surface(self.win_size, pygame.SRCALPHA)
        tim = 0
        choice = 0
        buttons = pygame.sprite.Group()
        button_list = [Choice(360),Choice(300),Choice(240),Choice(180)]
        butg = pygame.sprite.Group()
        auto = LButton(butg,590,"Авто")
        prop = LButton(butg,485,"Пропуск")
        hist = LButton(butg,360,"История")
        sohr = LButton(butg,690,"Сохранить")
        zagr = LButton(butg,805,"Загрузить")
        nast = LButton(butg,920,"Настройки")
        butg.update()
        ctcg = pygame.sprite.GroupSingle()
        ctc = OneSprite(ctcg,'/gui/ctc.png',1017,687)
        poem = 0
        pok = 1
        plist = image.load('game/images/bg/poem.jpg').convert()
        placepoem = plist.get_rect(center=(640,360))
        ok = 0
        cgt = 0
        sok = 1
        rsave = ''
        pr_time = TIM.time()
        selok = 1
        p = 0
        gok = 0
        collision = 0
        koef = 1
        skip = image.load('game/gui/skip.png').convert_alpha()
        while run:
            if self.menu:
                ok = 0
            savesurf = transform.smoothscale(self.win,(256,144))
            self.save = pygame.image.tostring(savesurf,'RGB')
            data = Descripter(go,script)
            dt = TIM.time() - pr_time
            pr_time = TIM.time()
            keys = key.get_pressed()
            mp = pygame.mouse.get_pos()
            self.win.blit(bg,(0,0))
            if cgt:
                self.win.blit(cg,(0,0))
                self.win.blit(cge,(0,0))
            if data[0] == 'audio':
                ok = 0
                tim = 0
                if data[1] == 'stop':
                    mixer.music.stop()
                else:
                    okm = 1
                    mus = 'game/bgm/'+data[1]+'.ogg'
                go += 1
            elif data[0] == "sound":
                ok = 0
                tim = 0
                if sok:
                    snd = mixer.Sound('game/sfx/'+data[1])
                    snd.set_volume(self.gromz)
                    snd.play()
                    sok = 0
                go += 1
                sok = 1
            elif data[0] == 'bg':
                ok = 0
                tim = 0
                if cgt:
                    cgt = 0
                pbg = 'game/images/bg/'+data[1]+'.png'
                bg = transform.smoothscale(image.load(pbg).convert(),self.win_size)
                go += 1
            elif data[0] == 'cg':
                ok = 0
                tim = 0
                if not cgt:
                    pcg = 'game/images/cg/'+data[1]+'.png'
                    pcge = 'game/images/cg/'+data[1]+'.png'
                else:
                    pcge = 'game/images/cg/'+data[1]+'.png'
                cg = image.load(pcg).convert_alpha()
                cge = image.load(pcge).convert_alpha()
                cgt = 1
                go += 1
            elif data[0] == 'show':
                ok = 0
                tim = 0
                if kd > 0:
                    for girl in girls:
                        girl.x = x21
                for girl in doki:
                    if data[1] == girl.name:
                        if kd > 0:
                            girl.x = x22
                        girl.spr = data[2]
                        girl.surf = girl.crspr()
                        girls.add(girl)
                kd += 1
                go += 1
            elif data[0] == 'hide':
                ok = 0
                tim = 0
                for girl in girls:
                    for i in range(len(data[1])):
                        if girl.name == data[1][i]:
                            girl.z = 0.8
                            girl.x = x11
                            girls.remove(girl)
                            kd -= 1
                go += 1
            elif data[0] == 'choice':
                ok = 0
                tim = 0
                choice = 1
            elif data[0] == 'jump':
                ok = 0
                tim = 0
                go = data[1]
            elif data[0] == 'poem':
                poem = 1
                pn = data[1]
            elif data[0] == '1':
                ok = 0
                tim = 0
                mixer.music.fadeout(1000)
                bg = image.load("game/images/bg/veinmaskb.png").convert()
                script += 1
                go = 0
            else:
                name = data[0]
                if rsave == "":
                    r = data[2]
                if data[1] != "" and gok != go:
                    for girl in girls:
                        if name == girl.name:
                            girl.spr = data[1]
                            girl.surf = girl.crspr()
                    gok = go
            for e in event.get():
                if e.type == QUIT:
                    run = 0
                    sys.exit()
                if e.type == pygame.KEYUP:
                    if e.key == K_LCTRL:
                        p = 0
                        tim = 0
                        selok = 1
                if e.type == pygame.MOUSEBUTTONUP and e.button == 1 and ok and not collision:
                    go += 1
            if okm:
                mixer.music.load(mus)
                mixer.music.play(-1)
                okm = 0
            for girl in girls:
                if name == girl.name:
                    if girl.z != 0.9:
                        girl.zoom(0.9,dt)
                else:
                    if girl.z != 0.8 and name != "Хикари" and name != "i" and girl.z != 0.8:
                        girl.zoom(0.8,dt)
            girls.update()
            girls.draw(self.win)
            if tim > 1:
                ok = 1
            else:
                ok = 0
            if tim > 1:
                if r == "" and rsave == "" and not choice and not poem:
                    go += 1
                    tim = 0
            if a:
                p = 0
                auto.col = WHITE
                if tim > 4 and not choice and not poem and rsave == "":
                    go += 1
                    tim = 0
            if keys[K_BACKSPACE] and r == "" and ok and not poem:
                rsave = ""
                tim = 0.3
            elif keys[K_BACKSPACE] and r != "" and ok and not poem:
                rsave = r
                r = ""
                tim = 0.3
            if r != '' and not poem:
                say(self.win,r,name)
                for i in butg:
                    if i.rect.collidepoint(mp):
                        collision = 1
                        if i.col == DARK: 
                            i.col = colhh
                        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                            if not p:
                                p = 0
                            if not a:
                                a = 0
                            if selok:
                                select.set_volume(self.gromz)
                                select.play()
                            if i == auto:
                                if not a:
                                    a = 1
                                else:
                                    a = 0
                            elif i == prop:
                                if not p:
                                    p = 1
                                else:
                                    p = 0
                            if i == hist:
                                self.main(0,1,0,1)
                            elif i == sohr:
                                self.main(0,1,1)
                            elif i == zagr:
                                self.main(0,1,0,0,1)
                            elif i == nast:
                                self.main(0,1,0,0,0,1)
                            selok = 0
                        else:
                            selok = 1
                    else:
                        if a and i == auto:
                            i.col = WHITE
                        elif p and i == prop:
                            i.col = WHITE
                        else:
                            i.col = DARK
                    i.update()
                else:
                     collision = 0
                butg.draw(self.win)
            if keys[K_SPACE] and ok and rsave == "":
                tim = 0
                ok = 0
                if poem:
                    poem = 0
                    pok = 1
                go += 1
            if keys[K_LCTRL] and ok:
                p = 1
            if p and not choice and not poem and tim != 0 and rsave == "":
                a = 0
                prop.col = WHITE
                go += 1
                self.win.blit(skip,(0,10))
                obvtext(self.win,60,30,"Пропуск",ft,1,BLACK)
            elif prop.col != WHITE:
                p = 0
            if keys[K_s]:
                lll = "game/screenshots/%02d-%02d-%02d_%02d-%02d-%02d.png" % (self.t[3],self.t[4],self.t[5],self.t[2],self.t[1],self.t[0])
                image.save(self.win,lll)
            if keys[K_F11]:
                if self.flags == DOUBLEBUF:
                    self.flags = FULLSCREEN | DOUBLEBUF
                    self.win = display.set_mode(self.win_size,self.flags)
                else:
                    self.flags = DOUBLEBUF
                    self.win = display.set_mode(self.win_size,self.flags)
            if poem:
                p = 0
                a = 0
                if pok:
                    flip.set_volume(self.gromz)
                    flip.play()
                    pok = 0
                self.win.blit(plist,(placepoem))
                poemdef(self.win,poems[pn][0],poems[pn][1],monikafont)
            if choice:
                tim = 0
                if not self.ifprop:
                    p = 0
                buttons.draw(csurf)
                for i in range(len(data[2])):
                    buttons.add(button_list[i])
                    justtext(csurf,640,button_list[i].y,data[2][i])
                for i in buttons:
                    if i.rect.collidepoint(mp):
                        collision = 1
                        if i.s == "idle": 
                            i.s = "hover"
                            over.set_volume(self.gromz)
                            over.play()
                        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                            select.set_volume(self.gromz)
                            select.play()
                            choice = 0
                            go = int(data[1][buttons.sprites().index(i)])
                            csurf = Surface(self.win_size, pygame.SRCALPHA)
                    else:
                        i.s = 'idle'
                        collision = 0
                buttons.update()
                self.win.blit(csurf,(0,0))
            else:
                buttons.empty()
            if ok and r != "":
                ctc.x += round(koef*20*dt,3)
                if ctc.x > 1023:
                    koef = -0.5
                elif ctc.x < 1017:
                    koef = 1
                ctcg.draw(self.win)
                ctcg.update()
            else:
                koef = 1
                ctc.x = 1015
            display.update()
            tim += dt
            self.clock.tick(60)
    def main(self,loadrun = 1,menurun = 0,sohr = 0,hist = 0,zagr = 0,setting = 0):
        words = "Вступительные слова."
        splash = image.load('game/images/bg/splash.png').convert_alpha()
        kr = image.load('game/gui/menu_bg.png').convert_alpha()
        mask = image.load('game/gui/overlay/game_menu.png').convert_alpha()
        zm = 1
        zn = 0.58
        zs = 0.68
        zy = 0.6
        xm = 1000
        ym = 640
        xn = 750
        yn = 385
        xy = 600
        yy = 335
        xs = 510
        ys = 500
        lx = 250
        ly = -200
        check = image.load('game/gui/button/check_selected_foreground.png').convert_alpha()
        linen = image.load('game/gui/scrollbar/horizontal_poem_bar.png').convert_alpha()
        line = transform.smoothscale(linen,(350,18)).convert_alpha()
        lines_list = [(420,350),(420,450),(800,350),(800,450)]
        sliders = pygame.sprite.Group()
        slider1 = OneSprite(sliders,'gui/slider/horizontal_hover_thumb.png',415+self.skort*345,350)
        slider2 = OneSprite(sliders,'gui/slider/horizontal_hover_thumb.png',415+self.skora*345,450)
        slider3 = OneSprite(sliders,'gui/slider/horizontal_hover_thumb.png',795+self.gromz*345,350)
        slider4 = OneSprite(sliders,'gui/slider/horizontal_hover_thumb.png',795+self.gromm*345,450)
        saves = pygame.sprite.Group()
        save1 = Box(saves,500,300)
        save2 = Box(saves,800,300)
        save3 = Box(saves,1100,300)
        save4 = Box(saves,500,500)
        save5 = Box(saves,800,500)
        save6 = Box(saves,1100,500)
        ss = pygame.sprite.Group()
        okon = SButton(ss,205,"Оконный")
        poln = SButton(ss,235,"Полноэкранный")
        newtext = SButton(ss,205,"Новый текст",810)
        propchoice = SButton(ss,235,"После выборов",810)
        ss.update()
        bs = pygame.sprite.Group()
        gs = pygame.sprite.Group()
        if self.g:
            hi = MButton(bs,320,"История")
            so = MButton(bs,365,"Сохранить")
            za = MButton(bs,410,"Загрузить")
            gm = MButton(bs,455,"Главное меню")
        else:
            mixer.music.load("game/bgm/1.ogg")
            mixer.music.set_volume(self.gromm)
            mixer.music.play(-1)
            bok = Menuspr(gs, 'overlay/main_menu.png', 1, 310)
            yu = Menuspr(gs, 'menu_art_y.png',zy,xy,yy)
            sa = Menuspr(gs, 'menu_art_s.png',zs,xs,ys)
            na = Menuspr(gs, 'menu_art_n.png',zn,xn,yn)
            mo = Menuspr(gs, 'menu_art_m.png',zm,xm,ym)
            logo = Menuspr(gs, 'logo.png',0.6, lx,ly)
            ng = MButton(bs,410,"Новая игра")
            za = MButton(bs,455,"Загрузить")
        se = MButton(bs,500,"Настройки")
        ex = MButton(bs,545,"Выйти")
        naz = MButton(bs,650,"Назад")
        bs.update()
        bs.remove(naz)
        aa = Surface(self.win_size,SRCALPHA)
        txt = Surface(self.win_size,SRCALPHA)
        ba = Surface(self.win_size,SRCALPHA)
        bel = Surface(self.win_size,SRCALPHA)
        sal = -31
        tal = 0
        aal = 0
        bal = 0
        txt.fill(WHITE)
        aa.fill(WHITE)
        ba.fill(WHITE)
        mon = 5
        nat = 612
        say = 1017
        yur = 1433
        kx = 0
        ky = 0
        bela = 255
        bel.fill(WHITE)
        w = text.render(words,1,BLACK,WHITE)
        pt = w.get_rect(center=(640,360))
        nazad = 0
        selok = 1
        fade = 0
        tim = 0
        stran = 1
        pr_time = TIM.time()
        self.menu = 1
        while loadrun:
            dt = TIM.time() - pr_time
            pr_time = TIM.time()
            if tim < 2:
                sal += 300*dt
            if tim > 2 and tim < 3:
                aal += 300*dt
            if tim > 3:
                tal += 300*dt
            if tim > 6:
                bal += 800*dt
            self.win.fill(WHITE)
            for e in event.get():
                if e.type == QUIT:
                    loadrun = 0
            ba.set_alpha(bal)
            if bal < 1000:
                splash.set_alpha(sal)
                txt.set_alpha(tal)
                aa.set_alpha(aal)
                txt.blit(w,(pt))
                self.win.blit(splash,(0,0))
                self.win.blit(aa,(0,0))
                self.win.blit(txt,(0,0))
                self.win.blit(ba,(0,0))
            elif bal > 1000:
                loadrun = 0
                menurun = 1
                tim = 0
            display.flip()
            tim += dt
            self.clock.tick(60)
        while menurun:
            dt = TIM.time() - pr_time
            pr_time = TIM.time()
            bel.set_alpha(bela)
            mp = pygame.mouse.get_pos()
            if bela > 0 and not fade:
                bela -= 10
            for e in pygame.event.get():
                if e.type == QUIT:
                    menurun = 0
                    sys.exit()
            self.win.blit(kr,(kx,ky))
            if not self.g:
                if tim > 0 and bok.rect.x < 0 and tim < 1:
                    bok.pos.x += 400*dt*QuinticEaseOut(tim)
                    bok.rect.x = round(bok.pos.x)
                elif tim > 1:
                    bok.rect.x = 0
                if tim > 1 and tim < 2 and logo.rect.y < -30:
                    logo.pos.y += 600*LogoB(tim-1)*dt
                    logo.rect.y = round(logo.pos.y)
                if logo.rect.y > -50:
                    logo.rect.y = -45
            if kx > -100:
                kx -= 30*dt
                ky -= 30*dt
            else:
                kx = 0
                ky = 0
            if setting or zagr or self.g:
                self.win.blit(mask,(0,0))
            if self.g:
                nazad = 1
                if hist:
                    hi.col = colhh
                    obvtext(self.win,30,30, "История", fbig, 4,col)
                    obvtext(self.win,630,165,"История диалогов пуста.",ft,1,BLACK)
                elif sohr:
                    so.col = colhh
                    obvtext(self.win,30,30,"Сохранить",fbig,4,col)
            if zagr or sohr:
                justtext(self.win,300+980//2,150,'Страница '+str(stran),text)
                saves.draw(self.win)
                for i in saves:
                    justtext(self.win,i.x,i.y+80,i.text,fl)
                    if sohr:
                        if i.rect.collidepoint(mp):
                            if e.type == pygame.MOUSEBUTTONDOWN:
                                i.image = image.fromstring(self.save,(256,144),"RGB")
            if setting:
                se.col = colhh
                obvtext(self.win,30,30, "Настройки", fbig, 4,col)
                obvtext(self.win, 420, 165, "Экран", fs,2,col)
                obvtext(self.win, 800, 165, "Пропуск", fs,2,col)
                obvtext(self.win, 420, 290, "Скорость текста", fs,2,col)
                obvtext(self.win, 420, 400, "Скорость автопрокрутки", fs,2,col)
                obvtext(self.win, 800, 290, "Громкость звуков", fs,2,col)
                obvtext(self.win, 800, 400, "Громкость музыки", fs,2,col)
                if self.flags == DOUBLEBUF:
                    self.win.blit(check,(420,200))
                else:
                    self.win.blit(check,(420,230))
                if self.ifprop:
                    self.win.blit(check,(780,230))
                if self.ifnewtext:
                    self.win.blit(check,(780,200))
                self.win.blit(line,(420,350))
                self.win.blit(line,(420,450))
                self.win.blit(line,(800,350))
                self.win.blit(line,(800,450))
                for i in sliders:
                    if line.get_rect(topleft=(lines_list[sliders.sprites().index(i)])).collidepoint(mp):
                        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                            i.x = mp[0]
                            i.update()
                sliders.draw(self.win)
                self.skort = round((slider1.x - 415)/350,1)
                self.skora = round((slider2.x - 415)/350,1)
                self.gromz = round((slider3.x - 795)/350,1)
                self.gromm = round((slider4.x - 795)/350,1)
                mixer.music.set_volume(self.gromm)
                for i in ss:
                    if i.rect.collidepoint(mp):
                        if i.col == GREY:
                            i.col = colb
                        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                            if i == okon and self.flags != DOUBLEBUF:
                                self.flags = DOUBLEBUF
                                self.win = display.set_mode(self.win_size,self.flags)
                            elif i == poln and self.flags == DOUBLEBUF:
                                self.flags = FULLSCREEN | DOUBLEBUF
                                self.win = display.set_mode(self.win_size,self.flags)
                            if i == propchoice and tim > 2.3:
                                if self.ifprop:
                                    self.ifprop = 0
                                else:
                                    self.ifprop = 1
                                tim = 2
                            if i == newtext and tim > 2.3:
                                if self.ifnewtext:
                                    self.ifnewtext = 0
                                else:
                                    self.ifnewtext = 1
                                tim = 2
                    else:
                        if (i == okon and self.flags == DOUBLEBUF) or (i == poln and self.flags != DOUBLEBUF) or (i == propchoice and self.ifprop) or (i == newtext and self.ifnewtext):
                            i.col = colb
                        else:
                            i.col = GREY
                ss.update()
                ss.draw(self.win)
                self.win.blit(fl.render("v0.0.4",1,BLACK),(1230,700))
            elif zagr:
                za.col = colhh
                obvtext(self.win,30,30, "Загрузить", fbig, 4,col)
            else:
                gs.draw(self.win)
            if nazad:
                bs.add(naz)
            else:
                bs.remove(naz)
            bs.draw(self.win)
            for i in bs:
                if i.rect.collidepoint(mp):
                    if i.col == col:
                        i.col = colh
                        over.set_volume(self.gromz)
                        over.play()
                    if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                        if selok and i.col != colhh:
                            select.set_volume(self.gromz)
                            select.play()
                        if i == za:
                            hist = 0
                            sohr = 0
                            zagr = 1
                            setting = 0
                            nazad = 1
                        elif i == se:
                            hist = 0
                            sohr = 0
                            setting = 1
                            zagr = 0
                            nazad = 1
                        elif i == naz or i == ex:
                            setting = 0
                            zagr = 0
                            nazad = 0
                            if i == ex:
                                menurun = 0
                                sys.exit()
                            if i == naz and self.g:
                                menurun = 0
                        if self.g:
                            if i == gm:
                                self.g = 0
                                self.main(0,1)
                                mixer.music.load("game/bgm/1.ogg")
                            elif i == hi:
                                hist = 1
                                sohr = 0
                                zagr = 0
                                setting = 0
                            elif i == so:
                                hist = 0
                                sohr = 1
                                zagr = 0
                                setting = 0
                            elif i == naz:
                                menurun = 0
                        else:
                            if i == ng and not fade:
                                fade = 1
                        selok = 0
                        f = open(r'game/settings.py', 'w')
                        f.write('import pygame')
                        f.write('\nfrom pygame import *')
                        f.write('\n')
                        if self.flags == DOUBLEBUF:
                            f.write('\nflags = DOUBLEBUF')
                        else:
                            f.write('\nflags = FULLSCREEN | DOUBLEBUF')
                        f.write('\nifprop = '+str(self.ifprop))
                        f.write('\nifnewtext = '+str(self.ifnewtext))
                        f.write('\nskort = '+str(self.skort))
                        f.write('\nskora = '+str(self.skora))
                        f.write('\ngromz = '+str(self.gromz))
                        f.write('\ngromm = '+str(self.gromm))
                        f.close()
                    else:
                        selok = 1
                else:
                    if (i == se and setting) or (i == za and zagr):
                        pass
                    else:
                        if self.g:
                            if (i == hi and hist) or (i == so and sohr):
                                pass
                            else:
                                i.col = col
                        else: 
                            i.col = col
            if bela > 0:
                self.win.blit(bel,(0,0))
            if fade:
                mixer.music.fadeout(1000)
                bel.fill(BLACK)
                self.win.blit(bel,(0,0))
                if bela < 300:
                    bela += 10
                else:
                    menurun = 0
                    self.menu = 0
                    self.notjustmonika(default.go)
            bs.update()
            display.flip()
            tim += dt
            if tim > 10:
                tim = 2.01
            self.clock.tick(60)