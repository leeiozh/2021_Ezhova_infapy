import pygame, sys
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((550, 707))
surface = pygame.Surface((320, 240), pygame.SRCALPHA, 32)
surface.convert_alpha()
surf1 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
surf2 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
surf3 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
surf4 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
d_fish = 15
l_fish = 48
black = (0, 0, 0)
white = (255, 255, 255)
r = (d_fish ** 2 + l_fish ** 2) / (2 * d_fish)
z = 2 * r - 2 * d_fish
fishy = (71, 136, 147)
circle(surf3, black, (250, 200), int(r) + 1)
circle(surf4, black, (250, 200 + int(z)), int(r) + 1)
circle(surf1, fishy, (250, 200), int(r))
circle(surf2, fishy, (250, 200 + int(z)), int(r))

rect(screen, (33, 33, 120), (0, 0, 550, 72))
rect(screen, (141, 95, 211), (0, 72, 550, 39))
rect(screen, (205, 135, 222), (0, 111, 550, 67))
rect(screen, (222, 135, 170), (0, 178, 550, 93))
rect(screen, (255, 153, 85), (0, 271, 550, 77))
rect(screen, (0, 102, 128), (0, 348, 550, 359))

arc(screen, white, (236, 120, 100, 100), np.pi / 4, 7 * np.pi / 9)
arc(screen, white, (236, 121, 100, 100), np.pi / 4, 7 * np.pi / 9)
arc(screen, white, (310, 117, 100, 100), np.pi / 4, 7 * np.pi / 9)
arc(screen, white, (310, 118, 100, 100), np.pi / 4, 7 * np.pi / 9)

running = True

fins = (102, 99, 112)
red = (180, 50, 50)
size = (0, 0, 300, 200)
x_big_fin = 307
y_big_fin = 617
x_f = 298
y_f = 658
x_tail = 253
y_tail = 637
x_ff = 339
y_ff = 664
circle(screen, (0, 0, 0), (x_big_fin + 49, y_big_fin + 13), 6)
polygon(screen, (0, 0, 0),
        [(x_big_fin - 2, y_big_fin - 1), (x_big_fin + 46, y_big_fin + 6), (x_big_fin + 47, y_big_fin + 19),
         (x_big_fin + 24, y_big_fin + 17)])

arc(surface, white, (51, 26, 100, 128), np.pi / 3, 7 * np.pi / 9)
arc(surface, white, (51, 27, 100, 128), np.pi / 3, 7 * np.pi / 9)
arc(surface, white, (114, 14, 100, 128), np.pi / 3, 7 * np.pi / 9)
arc(surface, white, (114, 15, 100, 128), np.pi / 3, 7 * np.pi / 9)
# Fish
circle(screen, black, (x_ff + 7, y_ff + 13), 8)
circle(screen, fins, (x_ff + 7, y_ff + 13), 7)
polygon(screen, black,
        [(x_ff - 1, y_ff), (x_ff + 11, y_ff), (x_ff + 26, y_ff + 11), (x_ff + 11, y_ff + 15), (x_ff, y_ff + 12)])
polygon(screen, fins,
        [(x_ff, y_ff), (x_ff + 10, y_ff), (x_ff + 24, y_ff + 10), (x_ff + 11, y_ff + 15), (x_ff, y_ff + 12)])
polygon(screen, black,
        [(x_tail + 42, y_tail + 14), (x_tail + 42, y_tail + 12), (x_tail, y_tail), (x_tail + 7, y_tail + 29)])
polygon(screen, fishy, [(x_tail + 41, y_tail + 13), (x_tail + 1, y_tail + 1), (x_tail + 8, y_tail + 28)])
polygon(screen, fins, [(x_big_fin, y_big_fin), (x_big_fin + 45, y_big_fin + 7), (x_big_fin + 47, y_big_fin + 19),
                       (x_big_fin + 25, y_big_fin + 17)])
circle(screen, fins, (x_big_fin + 48, y_big_fin + 13), 6)
circle(screen, fins, (20 + x_f, 12 + y_f), 3)
polygon(screen, black,
        [(12 + x_f, y_f), (x_f + 23, y_f), (x_f + 23, y_f + 11), (18 + x_f, y_f + 15), (x_f - 2, 15 + y_f)])
polygon(screen, fins, [(13 + x_f, y_f), (x_f + 22, y_f), (x_f + 22, y_f + 11), (18 + x_f, y_f + 14), (x_f, 14 + y_f)])

# wing
foo = []
soo = []
doo = []
b_foo = []  # for black line near wing
b_doo = []
b_soo = []
y_0 = 400
x_0 = 50
w_surf = pygame.Surface((550, 707), pygame.SRCALPHA, 32)
leg_surf = pygame.Surface((550, 707), pygame.SRCALPHA, 32)

for x in range(0, 142, 1):
    re = [x + x_0, y_0 - 6 + (93 / (3 * np.pi)) * (np.sin(3 * x * np.pi / 142) + 3 * x * np.pi / 142)]
    b_re = [x + x_0 - 1, y_0 - 6 + (93 / (3 * np.pi)) * (np.sin(3 * x * np.pi / 142) + 3 * x * np.pi / 142)]
    foo.append(re)
    b_foo.append(b_re)
    ra = [x + x_0 + 50, y_0 + 93 * (x ** 4) / (142 ** 4)]
    b_ra = [x + x_0 + 51, y_0 + 93 * (x ** 4) / (142 ** 4)]
    soo.insert(0, ra)
    b_soo.insert(0, b_ra)
    ry = [x + x_0, y_0 - 20 + 10000000 * 1.7 * 93 * (x ** (1 / 2)) / (142 ** 4)]
    b_ry = [x + x_0 + 1, y_0 - 20 + 10000000 * 1.7 * 93 * (x ** (1 / 2)) / (142 ** 4)]
    b_doo.insert(0, b_ry)
    doo.insert(0, ry)
foo.append([192, 87 + y_0])
foo.append([192, 86 + y_0])

for x in range(0, 141, 1):
    if x < 38:
        foo.append(soo[x])
        b_foo.append(b_soo[x])
    else:
        foo.append(doo[x])
        b_foo.append(b_doo[x])
polygon(w_surf, black, b_foo)
polygon(w_surf, white, foo)

# Legs

leg1_surf = pygame.Surface((550, 707), pygame.SRCALPHA, 32)
ellipse(leg1_surf, white, (45, 10, 20, 50))
ellipse(leg_surf, white, (0, 0, 30, 60))
d = 58
l = 50
polygon(leg1_surf, black,
        [(l - 1, d), (l - 16, d + 10), (l - 31, d + 29), (l - 5, d + 11), (l - 1, d + 36), (l + 4, d + 19),
         (l + 1, d + 11),
         (l + 1, d + 9), (l + 19, d + 34), (l + 18, d + 19),
         (l + 11, d + 11), (l + 7, d + 4), (l + 36, d + 30), (l + 29, d + 14), (l + 11, d)])
polygon(leg1_surf, (234, 211, 114),
        [(l + 0, d), (l - 15, d + 10), (l - 30, d + 28), (l - 5, d + 10), (l, d + 35), (l + 3, d + 20), (l, d + 10),
         (l + 2, d + 8), (l + 20, d + 33), (l + 17, d + 20),
         (l + 10, d + 10), (l + 7, d + 4), (l + 35, d + 29), (l + 28, d + 14), (l + 10, d)])

surface2 = pygame.transform.rotate(surface, -20)
surface3 = pygame.transform.rotate(surface, 0)
w_surf2 = pygame.transform.rotate(w_surf, -15)
leg2_surf = pygame.transform.rotate(leg1_surf, 25)
leg0_surf = pygame.transform.rotate(leg_surf, 12)

polygon(screen, white, ((190, 480), (140, 440), (125, 500), (190, 510)))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    # seabirds
    screen.blit(surface3, (0, 0))
    screen.blit(surface2, (-62, 157))

    # albatross' wings & body
    screen.blit(w_surf2, (-20, -45))
    screen.blit(w_surf, (30, 0))
    ellipse(screen, white, (x_0 + 130, y_0 + 50, 160, 80))

    # albatross' legs
    screen.blit(leg_surf, (240, 510))
    screen.blit(leg0_surf, (260, 390))
    screen.blit(leg2_surf, (230, 330))
    screen.blit(leg2_surf, (200, 335))
    # rest albatross' parts
    polygon(screen, black, [(435, 462), (480, 454), (491, 469), (480, 486), (435, 478)])
    polygon(screen, (255, 221, 85), [(435, 463), (480, 455), (490, 470), (480, 485), (435, 477)])
    ellipse(screen, white, (126, 485, 60, 30))
    polygon(screen, black, [(435, 470), (450, 471), (490, 470)])
    ellipse(screen, white, (x_0 + 270, y_0 + 70, 80, 40))
    ellipse(screen, white, (x_0 + 330, y_0 + 50, 60, 40))
    circle(screen, black, (x_0 + 375, y_0 + 70), 5)

    # fish
    surf3.blit(surf4, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(surf3, (89, 382))
    surf1.blit(surf2, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(surf1, (89, 382))
    circle(screen, (7, 60, 184), (368, 650), 6)
    circle(screen, black, (369, 650), 3)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()