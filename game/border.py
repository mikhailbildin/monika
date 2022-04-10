import pygame
from game.resources import *

def _circlepoints(r):
    _circle_cache = {}
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

def render(text, font,opx=2, col = WHITE, ocolor=col):
    textsurface = font.render(text, True, col).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = textsurface.get_height()
    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))
    surf = osurf.copy()
    osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))
    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))
    surf.blit(textsurface, (opx, opx))
    return surf