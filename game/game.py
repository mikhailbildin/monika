import pygame, sys, os.path, random, time as TIM
from pygame import *
from game.fonts import *
from game.descript import Descripter
from game.draw import *
from game.definitions import *
from game.easings import *
from game.poems import *
from game.resources import *
import game.settings as settings
import game.border as border

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.flags = settings.flags
        self.ifprop = settings.ifprop
        self.ifnewtext = settings.ifnewtext
        self.skort = settings.skort
        self.skora = settings.skora
        self.gromm = settings.gromm
        self.gromz = settings.gromz
        self.lp = settings.lp
        self.win_size = (1280,720)
        self.win = display.set_mode(self.win_size,self.flags)
        display.set_icon(image.load('game/gui/app.png'))
        display.set_caption("DLC of DDLC")
        self.clock = time.Clock()
        self.t = TIM.localtime()
        self.g = 0
        self.oksurf = pygame.Surface(self.win_size,SRCALPHA)
        self.oksurf.blit(image.load('game/gui/overlay/confirm.png').convert_alpha(),(0,0))
        Confirm(self.oksurf,"kek")
        self.menu = 1
        self.sav = []
    def notjustmonika(self,go,zagruzka = 0):
        self.g = 1
        self.menu = 0
        run = 1
        dspr = '1forma'
        girls = pygame.sprite.Group()
        Monika = Girl(dspr,m,"Моника",'monika/',0)
        Sayori = Girl(dspr,s,"Сайори",'sayori/',0)
        Yuri = Girl(dspr,y,"Юри",'yuri/',0)
        Natsuki = Girl(dspr,n,"Нацуки",'natsuki/',0)
        doki = []
        doki.append(Monika)
        doki.append(Sayori)
        doki.append(Yuri)
        doki.append(Natsuki)
        flagg = [0,0,0]
        if zagruzka != 0:
            zagdat = open('game/saves/'+str(zagruzka), "r").readlines()
            mus = zagdat[2].rstrip("\n")
            pbg = zagdat[3].rstrip("\n")
            pcg = zagdat[4].rstrip("\n")
            pcge = zagdat[5].rstrip("\n")
            script = zagdat[6].rstrip("\n")
            Monika.lp = int(zagdat[7][0])
            Sayori.lp = int(zagdat[7][1])
            Yuri.lp = int(zagdat[7][2])
            Natsuki.lp = int(zagdat[7][3])
            for fla in range(len(zagdat[8].rstrip('\n'))):
                flagg[fla] = int(zagdat[8][fla])
            if len(zagdat) != 8:
                for a in range(9,len(zagdat)):
                    for girl in doki:
                        if zagdat[a][0] == girl.ras[0]:
                            x = ""
                            spr = ""
                            for b in range(1,len(zagdat[a])):
                                if zagdat[a][b] == "-":
                                    break
                                else:
                                    x += zagdat[a][b]
                            for c in range(len(x)+2,len(zagdat[a].rstrip("\n"))):
                                spr += zagdat[a][c]
                            girl.alpha = 255
                            girl.z = 0.8
                            girl.x = int(x)
                            girl.spr = spr
                            girl.surf = girl.crspr()
                            girls.add(girl)
        else:
            mus = "game/bgm/morning.ogg"
            pbg = "game/images/bg/bedroom_evening.png"
            pcg = ""
            pcge = ""
            script = 0
        bg = transform.smoothscale(image.load(pbg).convert(),self.win_size)
        name = ''
        r = ''
        okm = 1
        a = 0
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
        gok = -1
        collision = 0
        koef = 1
        skip = image.load('game/gui/skip.png').convert_alpha()
        while run:
            self.sav = []
            if self.menu:
                tim = 0
                ok = 0
            savesurf = transform.smoothscale(self.win,(256,144))
            self.save = pygame.image.tostring(savesurf,'RGB')
            data = Descripter(go,script)
            dt = TIM.time() - pr_time
            pr_time = TIM.time()
            keys = key.get_pressed()
            mp = pygame.mouse.get_pos()
            mpr = pygame.mouse.get_pressed()
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
            elif data[0] != "sound" and sok == 0:
                sok = 1
            elif data[0] == "sound":
                ok = 0
                p = 0
                if sok:
                    snd = mixer.Sound('game/sfx/'+data[1])
                    snd.set_volume(self.gromz)
                    snd.play()
                    sok = 0
                if tim > snd.get_length() or tim > 0.5:
                    sok = 1
                    tim = 0
                    go += 1
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
                for girl in doki:
                    if data[1] == girl.name:
                        if gok != go:
                            if girl in girls:
                                girls.remove(girl)
                            if data[2][0] == "x":
                                girl.x = xlist[data[2]]
                                girl.spr = data[3]
                            else:
                                girl.spr = data[2]
                            girl.surf = girl.crspr()
                            girls.add(girl)
                            gok = go
                        if girl.z < 0.79:
                            girl.alpha += 150*dt
                            girl.z += 0.1*dt
                        elif girl.z > 0.83:
                            girl.alpha = 255
                            girl.z = 0.8*1.05
                            go += 1
                        else:
                            girl.alpha = 255
                            girl.z = 0.8
                            go += 1
            elif data[0] == 'hide':
                ok = 0
                tim = 0
                for girl in girls:
                    if girl.name == data[1] or data[1] == "all":
                        if girl.z > 0.74 and data[2] == 0:
                            girl.alpha -= 900*dt
                            girl.z -= 0.6*dt
                        else:
                            girls.remove(girl)
                            girl.x = 640
                            girl.z = 0.8*0.95
                            girl.alpha = 150
                            if data[1] != "all":
                                go += 1
                            else:
                                if len(girls) == 0:
                                    go += 1
            elif data[0] == 'choice':
                ok = 0
                tim = 0
                choice = 1
            elif data[0] == 'jump':
                ok = 0
                tim = 0
                go = data[1]
            elif data[0] == "flag":
                ok = 0
                tim = 0
                if data[1][0] == "=":
                    flagg[int(data[1][1])] = 1
                    go += 1
                else:
                    if flagg[int(data[1][0])]:
                        go += 1
                    else:
                        go += 2
            elif data[0] == 'if':
                ok = 0
                tim = 0
                for girl in doki:
                    if girl.ras[0] == data[1]:
                        if girl.lp == data[2]:
                            go += 1
                        else:
                            go += 2
            elif data[0] == 'poem':
                r = ""
                ok = 0
                tim = 0
                poem = 1
                pn = data[1]
                pf = data[2]
            elif data[0] == 'lp':
                for girl in doki:
                    if girl.ras[0] == data[1]:
                        if data[2] == "+":
                            girl.lp += data[3]
                        elif data[2] == "-":
                            girl.lp -= data[3]
                        else:
                            girl.lp = data[3]
                go += 1
            elif data[0] == '=':
                ok = 0
                tim = 0
                mixer.music.fadeout(1000)
                script = data[1:]
                go = 0
            else:
                if gok != go:
                    name = data[0]
                    if data[1] != "":
                        for girl in girls:
                            if name == girl.name:
                                girl.spr = data[1]
                                girl.surf = girl.crspr()
                    r = data[2]
                    gok = go
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = 0
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == K_LCTRL:
                        p = 0
                        tim = 0
                        selok = 1
                    elif event.key == K_ESCAPE:
                        ok = 0
                        tim = 0
                        lpo = str(Monika.lp)+str(Sayori.lp)+str(Yuri.lp)+str(Natsuki.lp)
                        flo = ''
                        for imo in range(len(flagg)):
                            flo += str(flagg[imo])
                        self.menu = 1
                        self.sav.append(go)
                        self.sav.append(mus)
                        self.sav.append(pbg)
                        self.sav.append(pcg)
                        self.sav.append(pcge)
                        self.sav.append(script)
                        self.sav.append(lpo)
                        self.sav.append(flo)
                        if len(girls) > 0:
                            for girl in girls:
                                self.sav.append(str(girl.ras[0])+str(girl.x)+"-"+str(girl.spr))
                        self.main(0,1,1)
                if mpr[0] and ok and not collision and not poem and r != "":
                    ok = 0
                    tim = 0
                    go += 1
                if mpr[0] and poem and not placepoem.collidepoint(mp):
                    ok = 0
                    tim = 0
                    poem = 0
                    pok = 1
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
                    if girl.z != 0.8 and name != "Хикари" and name != "i":
                        girl.zoom(0.8,dt)
            girls.update()
            girls.draw(self.win)
            if tim > 1:
                ok = 1
                if rsave == "" and data[2] == "" and not choice and not poem:
                    tim = 0
                    if data[0] == "sound":
                        sok = 1
                    go += 1
            else:
                ok = 0
            if a:
                p = 0
                auto.col = WHITE
                if tim > 4 and not choice and not poem and rsave == "":
                    tim = 0
                    go += 1
            if keys[K_BACKSPACE] and r == "" and ok and not poem:
                r = rsave
                rsave = ""
                tim = 0.3
                ok = 0
            elif keys[K_BACKSPACE] and r != "" and ok and not poem:
                rsave = r
                r = ""
                tim = 0.3
                ok = 0
            if r != '' and not poem:
                say(self.win,r,name)
                for i in butg:
                    if i.rect.collidepoint(mp):
                        collision = 1
                        if i.col == DARK: 
                            i.col = colhh
                        if mpr[0]:
                            if p or a:
                                p = 0
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
                            if i == hist or i == sohr or i == zagr or i == nast:
                                ok = 0
                                tim = 0
                                lpo = str(Monika.lp)+str(Sayori.lp)+str(Yuri.lp)+str(Natsuki.lp)
                                flo = ''
                                for imo in range(len(flagg)):
                                    flo += str(flagg[imo])
                                self.menu = 1
                                self.sav.append(go)
                                self.sav.append(mus)
                                self.sav.append(pbg)
                                self.sav.append(pcg)
                                self.sav.append(pcge)
                                self.sav.append(script)
                                self.sav.append(lpo)
                                self.sav.append(flo)
                                if len(girls) > 0:
                                    for girl in girls:
                                        self.sav.append(str(girl.ras[0])+str(girl.x)+"-"+str(girl.spr))
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
            if (keys[K_SPACE] or keys[K_RETURN]) and ok and rsave == "":
                ok = 0
                tim = 0
                go += 1
            if keys[K_LCTRL] and ok:
                p = 1
            if p and not choice and not poem and tim != 0 and rsave == "":
                a = 0
                prop.col = WHITE
                self.win.blit(skip,(0,10))
                obvtext(self.win,50,20,"Пропуск",ft,1,BLACK)
                go += 1
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
                if data[2] == "m":
                    poemdef(self.win,poems[pn][0],poems[pn][1],monikafont)
                if data[2] == "s":
                    poemdef(self.win,poems[pn][0],poems[pn][1],sayorifont)
                if data[2] == "y":
                    poemdef(self.win,poems[pn][0],poems[pn][1],yurifont)
                if data[2] == "n":
                    poemdef(self.win,poems[pn][0],poems[pn][1],natsukifont)
                if len(poems[pn][1]) > 18:
                    self.win.blit(skip,(500,200))
            if choice:
                tim = 0
                if not self.ifprop:
                    p = 0
                buttons.draw(csurf)
                for i in range(len(data[2])):
                    buttons.add(button_list[i])
                    if button_list[i].hov:
                        justtext(csurf,640,button_list[i].y,data[2][i],ft,colh)
                    else:
                        justtext(csurf,640,button_list[i].y,data[2][i])
                for i in buttons:
                    if i.rect.collidepoint(mp):
                        collision = 1
                        if i.s == "idle": 
                            i.s = "hover"
                            i.hov = 1
                            over.set_volume(self.gromz)
                            over.play()
                        if mpr[0]:
                            if data[3] != "":
                                for girl in doki:
                                    if data[3][buttons.sprites().index(i)] == girl.ras[0]:
                                        girl.lp += 1
                            select.set_volume(self.gromz)
                            select.play()
                            choice = 0
                            go = int(data[1][buttons.sprites().index(i)])
                            csurf = Surface(self.win_size, pygame.SRCALPHA)
                    else:
                        i.s = 'idle'
                        i.hov = 0
                        collision = 0
                buttons.update()
                self.win.blit(csurf,(0,0))
            else:
                buttons.empty()
            if ok and r != "":
                if self.menu == 0:
                    ctc.x = round(ctc.x+koef*15*dt,3)
                if ctc.x > 1023:
                    koef = -0.75
                elif ctc.x < 1017:
                    koef = 1
                if koef < 0:
                    if ctc.alpha > 120:
                        ctc.alpha -= round(100*dt)
                else:
                    if ctc.alpha < 260:
                        ctc.alpha += round(100*dt)
                ctcg.update()
                ctcg.draw(self.win)
            else:
                koef = 1
                ctc.x = 1015
            if self.lp:
                pygame.draw.rect(self.win,(100,100,100),[850,5,400,25],0,5)
                justtext(self.win,900,20,"Сайори: "+str(Sayori.lp),fl,WHITE)
                justtext(self.win,1000,20,"Моника: "+str(Monika.lp),fl,WHITE)
                justtext(self.win,1100,20,"Юри: "+str(Yuri.lp),fl,WHITE)
                justtext(self.win,1200,20,"Нацуки: "+str(Natsuki.lp),fl,WHITE)
            #self.win.blit(self.oksurf,(0,0))
            #Console(self.win,r,sok)
            display.update()
            if not self.menu:
                tim += dt
            self.clock.tick(60)
    def main(self,loadrun = 1,menurun = 0,sohr = 0,hist = 0,zagr = 0,setting = 0):
        self.menu = 1
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
        save1 = Box(saves,500,300,1)
        save2 = Box(saves,800,300,2)
        save3 = Box(saves,1100,300,3)
        save4 = Box(saves,500,500,4)
        save5 = Box(saves,800,500,5)
        save6 = Box(saves,1100,500,6)
        stranl = pygame.sprite.Group()
        for ir in range(9):
            LButton(stranl,600+ir*50,str(ir+1),650,GREY)
        stranl.update(text)
        ss = pygame.sprite.Group()
        okon = SButton(ss,205,"Оконный")
        poln = SButton(ss,235,"Полноэкранный")
        newtext = SButton(ss,205,"Новый текст",810)
        propchoice = SButton(ss,235,"После выборов",810)
        lpyes = SButton(ss,550,"Виджет ЛП")
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
        stran = "1"
        pr_time = TIM.time()
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
            mpr = pygame.mouse.get_pressed()
            if bela > 0 and not fade:
                bela -= 10
            for e in pygame.event.get():
                if e.type == QUIT:
                    menurun = 0
                    sys.exit()
                if self.g:
                    if e.type == KEYDOWN and e.key == "K_ESCAPE":
                        time.delay(100)
                        menurun = 0
                        self.menu = 0
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
                if tim > 2:
                    logo.rect.y = -45
            if kx > -100:
                kx -= 50*dt
                ky -= 50*dt
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
                stranl.draw(self.win)
                justtext(self.win,300+980//2,150,'Страница '+stran,text)
                for ir in stranl:
                    if ir.rect1.collidepoint(mp):
                        if ir.col == GREY:
                            ir.col = col
                        if mpr[0]:
                            stran = ir.name
                    else:
                        if ir.name == stran:
                            ir.col = colb
                        else:
                            ir.col = GREY
                stranl.update(text)
                saves.draw(self.win)
                for i in saves:
                    justtext(self.win,i.x,i.y+80,i.text,fl)
                    if os.path.isfile("game/saves/"+stran+str(i.number)) and os.path.isfile("game/saves/"+stran+str(i.number)+".png"):
                        i.image = pygame.image.load("game/saves/"+stran+str(i.number)+".png")
                        i.text = open('game/saves/'+stran+str(i.number), "r").readlines()[0]
                    else:
                        i.image = Surface((256,144))
                        i.image.fill(PINK)
                        i.text = "пустой слот"
                    if i.rect.collidepoint(mp):
                        i.line(self.win)
                        if mpr[0]:
                            if sohr:
                                self.t = TIM.localtime()
                                i.image = image.fromstring(self.save,(256,144),"RGB")
                                i.text = str(days[self.t[6]]+", "+months[self.t[1]-1]+" "+str(self.t[2])+" "+str(self.t[0])+", "+("%02d:%02d" % (self.t[3],self.t[4])))
                                pygame.image.save(i.image,"game/saves/"+stran+str(i.number)+".png")
                                f = open("game/saves/"+stran+str(i.number),"w+")
                                f.write(i.text+"\n")
                                for sss in range(len(self.sav)):
                                    f.write(str(self.sav[sss])+"\n")
                                f.close()
                            if zagr:
                                if i.text != "пустой слот":
                                    if selok:
                                        select.play()
                                        selok = 0
                                    zagruzka = int(stran+str(i.number))
                                    fade = 1
            if setting:
                se.col = colhh
                obvtext(self.win,30,30, "Настройки", fbig, 4,col)
                obvtext(self.win, 420, 165, "Экран", fs,2,col)
                obvtext(self.win, 800, 165, "Пропуск", fs,2,col)
                obvtext(self.win, 420, 290, "Скорость текста", fs,2,col)
                obvtext(self.win, 420, 400, "Скорость автопрокрутки", fs,2,col)
                obvtext(self.win, 420, 500, "Дополнительно", fs,2,col)
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
                if self.lp:
                    self.win.blit(check,(420,545))
                self.win.blit(line,(420,350))
                self.win.blit(line,(420,450))
                self.win.blit(line,(800,350))
                self.win.blit(line,(800,450))
                for i in sliders:
                    if line.get_rect(topleft=(lines_list[sliders.sprites().index(i)])).collidepoint(mp):
                        if mpr[0]:
                            i.x = mp[0]-5
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
                        if mpr[0]:
                            if i == okon and self.flags != DOUBLEBUF:
                                self.flags = DOUBLEBUF
                                self.win = display.set_mode(self.win_size,self.flags)
                            elif i == poln and self.flags == DOUBLEBUF:
                                self.flags = FULLSCREEN | DOUBLEBUF
                                self.win = display.set_mode(self.win_size,self.flags)
                            if i == lpyes and tim > 2.3:
                                if self.lp:
                                    self.lp = 0
                                else:
                                    self.lp = 1
                                tim = 2
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
                        if (i == okon and self.flags == DOUBLEBUF) or (i == poln and self.flags != DOUBLEBUF) or (i == propchoice and self.ifprop) or (i == newtext and self.ifnewtext) or (i == lpyes and self.lp):
                            i.col = colb
                        else:
                            i.col = GREY
                ss.update()
                ss.draw(self.win)
                self.win.blit(fl.render("v0.0.6",1,BLACK),(1230,700))
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
                    if mpr[0] and tim > 1:
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
                                sys.exit()
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
                                time.delay(500)
                                menurun = 0
                                self.menu = 0
                        else:
                            if i == ng:
                                zagr = 0
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
                        f.write('\nlp = '+str(self.lp))
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
                    if zagr:
                        self.notjustmonika(int(open('game/saves/'+str(zagruzka), "r").readlines()[1].rstrip("\n")),zagruzka)
                    else:
                        self.notjustmonika(0)
            bs.update()
            display.flip()
            tim += dt
            if tim > 10:
                tim = 2.01
            self.clock.tick(60)