import random
from game.resources import nonunicode
def Descripter(i,scr):
    data = open('game/'+str(scr), "r", encoding="utf8").readlines()
    for x in range(len(data[i])):
        if data[i][0] == 'a':
            an = ''
            for d in range(2,len(data[i].rstrip("\n"))):
                an += str(data[i][d])
            return 'audio', an
        elif data[i][0] == 'b':
            bgn = ''
            for d in range(3,len(data[i].rstrip("\n"))):
                bgn += str(data[i][d])
            return 'bg', bgn
        elif data[i][0] == 'c':
            cgn = ''
            for d in range(3,len(data[i].rstrip("\n"))):
                cgn += str(data[i][d])
            return 'cg', cgn
        elif data[i][0] == '"':
            s = ''
            for d in range(1,len(data[i].rstrip("\n"))-1):
                s += str(data[i][d])
            return 'i', 0, s
        elif data[i][1] == 'h':
            a = str(data[i][5])
            if a == "m":
                name = "Моника"
            elif a == "y":
                name = "Юри"
            elif a == "s":
                name = "Сайори"
            elif a == "n":
                name = "Нацуки"
            b = ''
            pos = ""
            if data[i][7] == "x":
                for o in range(7,10):
                    pos += data[i][o]
                for lp in range(11,len(data[i].rstrip("\n"))):
                    b += data[i][lp]
                return 'show', name, pos, b
            else:
                for lp in range(7,len(data[i].rstrip("\n"))):
                    b += data[i][lp]
                return 'show', name, b
        elif data[i][1] == 'i':
            a = ""
            an = 0
            if data[i].rstrip("\n")[-1] == "0":
                an = 1
            for o in range(5,len(data[i].rstrip("\n"))):
                a += data[i][o]
            d = ""
            if "m" in a:
                d = "Моника"
            if "y" in a:
                d = "Юри"
            if "s" in a:
                d = "Сайори"
            if "n" in a:
                d = "Нацуки"
            if "a" in a:
                d = "all"
            return 'hide', d, an
        elif data[i][0] == '%':
            c = ['']
            r = []
            n = 1
            l = 0
            b = ''
            for o in range(1,len(data[i].rstrip("\n"))):
                if data[i][o] =='-':
                    c.append('')
            for o in range(len(c)):
                for e in range(n,len(data[i].rstrip("\n"))):
                    if data[i][e] =='-':
                        n = e+1
                        break
                    else:
                        c[o]+=data[i][e]
            for o in range(len(c)):
                a = ''
                for e in range(l,len(data[i+1].rstrip("\n"))):
                    if data[i+1][e] == '|':
                        l = e+1
                        for pp in range(l, len(data[i+1].rstrip("\n"))):
                            b += data[i+1][pp]
                        break
                    if data[i+1][e] == '/':
                        l = e+1
                        break
                    else:
                        a+=data[i+1][e]
                r.append(a)
            return 'choice',c,r,b
        elif data[i][0] == "I":
            return 'if',data[i][3], int(data[i][4])
        elif data[i][0] == '-':
            d = ''
            for o in range(1,len(data[i].rstrip('\n'))):
                d += data[i][o]
            return 'jump',int(d)
        elif data[i][0] == 'p':
            return 'poem', int(data[i][2]), str(data[i][3])
        elif data[i][0] == 'S':
            d = data[i][2:].rstrip('\n')
            return 'sound',d
        elif data[i][0] == "F":
            d = data[i][1:].rstrip('\n')
            return 'flag',d
        elif data[i][0] == "=":
            return data[i].rstrip('\n')
        elif data[i][2] == "=":
            return "lp",str(data[i][0]),str(data[i][1]),int(data[i][3:].rstrip('\n'))
        else:
            if data[i][2] =='"':
                a = ''
                b = ''
                for o in range(2,len(data[i].rstrip("\n"))):
                    b += data[i][o]
            else:
                a = ''
                for d in range(2,len(data[i].rstrip("\n"))):
                    if data[i][d] == ' ':
                        break
                    else:
                        a += data[i][d]
                b = ''
                for o in range(3+len(a),len(data[i].rstrip("\n"))):
                    b += data[i][o]
            if b == '"g"':
                ran = random.randint(8,60)
                r = ""
                for l in range(ran):
                    r += random.choice(nonunicode)
                b = r
            if data[i][0] == 'm':
                return 'Моника', a, b
            elif data[i][0] == 's':
                return 'Сайори', a, b
            elif data[i][0] == 'y':
                return 'Юри', a, b
            elif data[i][0] == 'n':
                return 'Нацуки', a, b
            elif data[i][0] == 'o':
                return 'Хикари', a, b
            elif data[i][0] == "i":
                return "???", a,b