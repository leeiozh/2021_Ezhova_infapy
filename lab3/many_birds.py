import pygame, sys
import numpy as np
from pygame.draw import *


def draw_background(surf):
    rect(surf, (33, 33, 120), (0, 0, 550, 72))
    rect(surf, (141, 95, 211), (0, 72, 550, 39))
    rect(surf, (205, 135, 222), (0, 111, 550, 67))
    rect(surf, (222, 135, 170), (0, 178, 550, 93))
    rect(surf, (255, 153, 85), (0, 271, 550, 77))
    rect(surf, (0, 102, 128), (0, 348, 550, 359))


def draw_seabirds(surface, color):
    arc(surface, color, (51, 26, 100, 128), np.pi / 3, 7 * np.pi / 9)
    arc(surface, color, (51, 27, 100, 128), np.pi / 3, 7 * np.pi / 9)
    arc(surface, color, (114, 14, 100, 128), np.pi / 3, 7 * np.pi / 9)
    arc(surface, color, (114, 15, 100, 128), np.pi / 3, 7 * np.pi / 9)


def draw_wings(screen, w_surf, x_0, y_0):
    foo = []
    soo = []
    doo = []
    b_foo = []  # for black line near wing
    b_doo = []
    b_soo = []

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

    polygon(screen, white, ((190, 480), (140, 440), (125, 500), (190, 510)))


def draw_legs(leg1_surf, leg_surf, d, l):
    ellipse(leg1_surf, white, (45, 10, 20, 50))
    ellipse(leg_surf, white, (0, 0, 30, 60))
    polygon(leg1_surf, black,
            [(l - 1, d), (l - 16, d + 10), (l - 31, d + 29), (l - 5, d + 11), (l - 1, d + 36), (l + 4, d + 19),
             (l + 1, d + 11),
             (l + 1, d + 9), (l + 19, d + 34), (l + 18, d + 19),
             (l + 11, d + 11), (l + 7, d + 4), (l + 36, d + 30), (l + 29, d + 14), (l + 11, d)])
    polygon(leg1_surf, (234, 211, 114),
            [(l + 0, d), (l - 15, d + 10), (l - 30, d + 28), (l - 5, d + 10), (l, d + 35), (l + 3, d + 20), (l, d + 10),
             (l + 2, d + 8), (l + 20, d + 33), (l + 17, d + 20),
             (l + 10, d + 10), (l + 7, d + 4), (l + 35, d + 29), (l + 28, d + 14), (l + 10, d)])


def draw_fish(screen, x_f, y_f, x_ff, y_ff, x_tail, y_tail, x_big_fin, y_big_fin, d_fish, l_fish):
    r = (d_fish ** 2 + l_fish ** 2) / (2 * d_fish)
    z = 2 * r - 2 * d_fish

    # body
    circle(surf3, black, (250, 200), int(r) + 1)
    circle(surf4, black, (250, 200 + int(z)), int(r) + 1)
    circle(surf1, fishy, (250, 200), int(r))
    circle(surf2, fishy, (250, 200 + int(z)), int(r))

    # plavnics and tail
    circle(screen, black, (x_big_fin + 49, y_big_fin + 13), 6)
    polygon(screen, black,
            [(x_big_fin - 2, y_big_fin - 1), (x_big_fin + 46, y_big_fin + 6), (x_big_fin + 47, y_big_fin + 19),
             (x_big_fin + 24, y_big_fin + 17)])

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
    polygon(screen, fins,
            [(13 + x_f, y_f), (x_f + 22, y_f), (x_f + 22, y_f + 11), (18 + x_f, y_f + 14), (x_f, 14 + y_f)])


def print_seabirds():
    draw_seabirds(surface, white)

    surface2 = pygame.transform.rotate(surface, -20)
    surface3 = pygame.transform.rotate(surface, 0)
    big_seabird = pygame.transform.rotate(surface2, -20)
    medium_seabird = pygame.transform.scale(surface2, (200, 200))
    small_seabird = pygame.transform.scale(surface2, (150, 150))
    roten_small_seabird = pygame.transform.rotate(small_seabird, 20)

    screen.blit(surface3, (0, 0))
    screen.blit(big_seabird, (40, 30))
    screen.blit(surface2, (-62, 157))

    screen.blit(medium_seabird, (400, 100))
    screen.blit(medium_seabird, (420, 200))
    screen.blit(medium_seabird, (350, 150))
    screen.blit(medium_seabird, (300, 170))
    screen.blit(medium_seabird, (150, 130))
    screen.blit(medium_seabird, (50, 80))
    screen.blit(medium_seabird, (-70, 70))
    screen.blit(medium_seabird, (320, 50))
    screen.blit(medium_seabird, (200, 10))

    screen.blit(roten_small_seabird, (100, 100))
    screen.blit(roten_small_seabird, (50, 140))
    screen.blit(roten_small_seabird, (30, 100))
    screen.blit(roten_small_seabird, (230, 220))

    screen.blit(small_seabird, (-30, 130))
    screen.blit(small_seabird, (100, 230))
    screen.blit(small_seabird, (200, 70))
    screen.blit(small_seabird, (200, 200))


def print_albatross():
    draw_wings(screen, w_surf, x_0, y_0)
    draw_legs(leg1_surf, leg_surf, 58, 50)

    w_surf2 = pygame.transform.rotate(w_surf, -15)
    leg2_surf = pygame.transform.rotate(leg1_surf, 25)
    leg0_surf = pygame.transform.rotate(leg_surf, 12)

    polygon(alba_surf, white, ((190, 480), (140, 440), (125, 500), (190, 510)))

    # albatross' wings & body
    alba_surf.blit(w_surf2, (-20, -45))
    alba_surf.blit(w_surf, (30, 0))
    ellipse(alba_surf, white, (x_0 + 130, y_0 + 50, 160, 80))

    # albatross' legs
    alba_surf.blit(leg_surf, (240, 510))
    alba_surf.blit(leg0_surf, (260, 390))
    alba_surf.blit(leg2_surf, (230, 330))
    alba_surf.blit(leg2_surf, (200, 335))

    # rest albatross' parts
    polygon(alba_surf, black, [(435, 462), (480, 454), (491, 469), (480, 486), (435, 478)])
    polygon(alba_surf, (255, 221, 85), [(435, 463), (480, 455), (490, 470), (480, 485), (435, 477)])
    ellipse(alba_surf, white, (126, 485, 60, 30))
    polygon(alba_surf, black, [(435, 470), (450, 471), (490, 470)])
    ellipse(alba_surf, white, (x_0 + 270, y_0 + 70, 80, 40))
    ellipse(alba_surf, white, (x_0 + 330, y_0 + 50, 60, 40))
    circle(alba_surf, black, (x_0 + 375, y_0 + 70), 5)
    screen.blit(alba_surf, (0, 0))
    alba_screen2 = pygame.transform.scale(alba_surf, (150, 150))
    screen.blit(alba_screen2, (250, 270))
    alba_screen3 = pygame.transform.flip(alba_screen2, 1, 0)
    screen.blit(alba_screen3, (400, 300))


def print_fishes():
    draw_fish(screen, x_f, y_f, x_ff, y_ff, x_tail, y_tail, x_big_fin, y_big_fin, d_fish, l_fish)

    surf3.blit(surf4, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    screen.blit(surf3, (89, 382))
    surf1.blit(surf2, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    circle(surf1, (7, 60, 184), (280, 270), 6)
    circle(surf1, black, (280, 270), 3)
    circle(surf1, black, (x_ff + 7, y_ff + 13), 8)
    circle(surf1, fins, (x_ff + 7, y_ff + 13), 7)
    polygon(surf1, black,
            [(x_ff - 1, y_ff), (x_ff + 11, y_ff), (x_ff + 26, y_ff + 11), (x_ff + 11, y_ff + 15), (x_ff, y_ff + 12)])
    polygon(surf1, fins,
            [(x_ff, y_ff), (x_ff + 10, y_ff), (x_ff + 24, y_ff + 10), (x_ff + 11, y_ff + 15), (x_ff, y_ff + 12)])
    polygon(surf1, black,
            [(x_tail + 42, y_tail + 14), (x_tail + 42, y_tail + 12), (x_tail, y_tail), (x_tail + 7, y_tail + 29)])
    polygon(surf1, fishy, [(x_tail + 41, y_tail + 13), (x_tail + 1, y_tail + 1), (x_tail + 8, y_tail + 28)])
    circle(surf1, black, (x_big_fin + 49, y_big_fin + 13), 6)
    polygon(surf1, black,
            [(x_big_fin - 2, y_big_fin - 1), (x_big_fin + 46, y_big_fin + 6), (x_big_fin + 47, y_big_fin + 19),
             (x_big_fin + 24, y_big_fin + 17)])
    polygon(surf1, fins, [(x_big_fin, y_big_fin), (x_big_fin + 45, y_big_fin + 7), (x_big_fin + 47, y_big_fin + 19),
                          (x_big_fin + 25, y_big_fin + 17)])
    circle(surf1, fins, (x_big_fin + 48, y_big_fin + 13), 6)
    circle(surf1, fins, (20 + x_f, 12 + y_f), 3)
    polygon(surf1, black,
            [(12 + x_f, y_f), (x_f + 23, y_f), (x_f + 23, y_f + 11), (18 + x_f, y_f + 15), (x_f - 2, 15 + y_f)])
    polygon(surf1, fins,
            [(13 + x_f, y_f), (x_f + 22, y_f), (x_f + 22, y_f + 11), (18 + x_f, y_f + 14), (x_f, 14 + y_f)])
    screen.blit(surf1, (89, 382))
    fliped_fish = pygame.transform.flip(surf3, 1, 0)
    screen.blit(fliped_fish, (-150, 370))
    fliped_fish = pygame.transform.flip(surf1, 1, 0)
    screen.blit(fliped_fish, (-150, 370))
    screen.blit(surf3, (220, 300))
    screen.blit(surf1, (220, 300))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((550, 707))
alba_surf = pygame.Surface((550, 707), pygame.SRCALPHA, 32)
surface = pygame.Surface((320, 240), pygame.SRCALPHA, 32)
surface.convert_alpha()
surf1 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
surf2 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
surf3 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
surf4 = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
w_surf = pygame.Surface((550, 707), pygame.SRCALPHA, 32)
leg_surf = pygame.Surface((550, 707), pygame.SRCALPHA, 32)
leg1_surf = pygame.Surface((550, 707), pygame.SRCALPHA, 32)

black = (0, 0, 0)
white = (255, 255, 255)
fishy = (71, 136, 147)

d_fish = 15
l_fish = 48
r = (d_fish ** 2 + l_fish ** 2) / (2 * d_fish)
z = 2 * r - 2 * d_fish
fins = (102, 99, 112)
red = (180, 50, 50)
size = (0, 0, 300, 200)
x_big_fin = 215
y_big_fin = 235
x_f = 210
y_f = 280
x_tail = 160
y_tail = 255
x_ff = 255
y_ff = 283
y_0 = 400
x_0 = 50

pygame.display.update()
clock = pygame.time.Clock()
done = False

while not done:
    clock.tick(FPS)

    draw_background(screen)

    print_seabirds()

    print_albatross()

    print_fishes()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
