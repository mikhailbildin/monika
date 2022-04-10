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
            for o in range(7,len(data[i].rstrip("\n"))):
                b += data[i][o]
            return 'show', name, b
        elif data[i][1] == 'i':
            a = ""
            for o in range(5,len(data[i].rstrip("\n"))):
                a += data[i][o]
            d = []
            if "m" in a:
                d.append("Моника")
            if "y" in a:
                d.append("Юри")
            if "s" in a:
                d.append("Сайори")
            if "n" in a:
                d.append("Нацуки")
            return 'hide', d
        elif data[i][0] == '%':
            c = ['']
            r = []
            n = 1
            l = 0
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
                    if data[i+1][e] == '/':
                        l = e+1
                        break
                    else:
                        a+=data[i+1][e]
                r.append(a)
            return 'choice',c,r
        elif data[i][0] == '-':
            d = ''
            for o in range(1,len(data[i].rstrip('\n'))):
                d+= data[i][o]
            return 'jump',int(d)
        elif data[i][0] == 'p':
            return 'poem', int(data[i][2])
        elif data[i][0] == 'S':
            d = ''
            for o in range(2,len(data[i].rstrip('\n'))):
                d+= data[i][o]
            return 'sound',d
        elif data[i][0] == "=":
            return '123'
        else:
            if data[i][2] =='"':
                a = ''
                b = ''
                for o in range(2,len(data[i].rstrip("\n"))):
                    b += data[i][o]
            else:
                a = ''
                for d in range(2,len(data[i])):
                    if data[i][d] == ' ':
                        break
                    else:
                        a += data[i][d]
                b = ''
                for o in range(3+len(a),len(data[i].rstrip("\n"))):
                    b += data[i][o]
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