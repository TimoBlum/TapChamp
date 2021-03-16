import pygame

wx = 600
wy = 200
win = pygame.display.set_mode((wx, wy))
pygame.display.set_caption("Tap Championship!")
clock = pygame.time.Clock()
bvalue = 2
rvalue = 2
winpoints = rvalue - bvalue
bcounter = 0
rcounter = 0
winner = False
Frame = 0


def redrawWin():
    global Frame, winpoints
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (230, 230, 230), (10, 10, wx - 20, wy - 20))
    pygame.draw.rect(win, (255, 0, 0), (20, 20, (wx // 2) - 20 + winpoints * 2, wy - 40))
    pygame.draw.rect(win, (0, 0, 255), ((wx // 2) + winpoints * 2, 20, (wx // 2) - 20 - winpoints * 2, wy - 40))

    if not winner:
        tweak()
        winpoints = rvalue - bvalue
        detectCheat()
        pygame.draw.line(win, (230, 230, 230), (wx/2, 20), (wx/2, wy-20))
        pygame.draw.line(win, (230, 230, 230), (wx/2+200, 20), (wx/2+200, wy-20))
        pygame.draw.line(win, (230, 230, 230), (wx/2-200, 20), (wx/2-200, wy-20))
        checkWin()
        pygame.display.update()
        Frame += 1


def checkWin():
    global winner
    if winpoints > 100:
        win.fill((255, 0, 0))
        winner = True
    elif winpoints < -100:
        winner = True
        win.fill((0, 0, 255))


def tweak():
    global bvalue, rvalue, bcounter, rcounter
    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        bvalue += 1
        bcounter += 1
    else:
        bcounter = 0
    if keys[pygame.K_a]:
        rvalue += 1
        rcounter += 1
    else:
        rcounter = 0


def detectCheat():
    global rcounter, bcounter, rvalue, bvalue
    # No human taps faster than 60 times a second so if this code sees you having a 60 press streak
    # it will punish you
    if rcounter >= 10 and rvalue >= 3:
        rvalue -= 2
    if bcounter >= 10 and bvalue >= 3:
        bvalue -= 2


def yn(a, c):
    # decide if something, whether float or int is the same number
    b = a // c
    bb = a / c
    if b - bb == 0:
        return True
    else:
        return False


def main():
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWin()
        print(winpoints)


main()
