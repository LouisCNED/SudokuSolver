import pygame

WIDTH = 550
background_color = (255, 255, 255)
original_grid_element_color = (52, 31, 151)
buffer = 5
pygame.init()
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku")
menu_bg_color = (52, 31, 151)
win.fill(menu_bg_color)
myfont = pygame.font.SysFont('Comic Sans MS', 35)
play_btn_img = pygame.image.load('images/play.png').convert_alpha()
settings_btn_img = pygame.image.load('images/settings.png').convert_alpha()
back_btn_img = pygame.image.load('images/back.png').convert_alpha()
red_button_img = pygame.image.load('images/red.png').convert_alpha()
blue_image_img = pygame.image.load('images/blue.png').convert_alpha()
green_image_img = pygame.image.load('images/green.png').convert_alpha()




class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        win.blit(self.image, self.rect)

        return action



grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

]
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]


def insert(win, position, background_color):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid_original[i - 1][j - 1] != 0):
                    return
                if (event.key == 48):
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(win, background_color, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10):
                    pygame.draw.rect(win, background_color, (
                    position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    value = myfont.render(str(event.key - 48), True, (0, 0, 0))
                    win.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return

def verif():
    listem = []
    listep = []
    fg = 0
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if grid[i][j] != 0:
                listem = []
                listep = []
                fg = 0
                for m in range(0, 9):
                    countm = grid[m].count(grid[i][j])
                    for u in range(0, 9):
                        listem.append(grid[u][m])
                    listemcount = listem.count(grid[i][j])
                    if listemcount > 1:
                        print(listemcount, listem)
                        return False
                    if countm > 1:
                        print(countm, grid[m])
                        return False
                    listem = []
                for l in range(0, 9):
                    countl = grid[l].count(grid[i][j])
                    if countl > 1:
                        print(countl, grid[l])
                        return False
                    for p in range(0, 9):
                        listep.append(grid[p][l])
                    listepcount = listep.count(grid[i][j])
                    if listepcount > 1:
                        return False
                    listep = []
                x = i // 9
                y = j // 9
                for f in range (0, 3):
                    for g in range(0, 3):
                        if grid[x+f][y+g] == grid[i][j]:
                            fg += 1
                            print(grid[x+f][y+g], x+f, y+g)
                            if fg > 1:
                                return False
    return True

def main(background_color):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    original_grid_element_color = (255, 255, 255)
    for i in range(0, 10):
        if (i % 3 == 0):
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0] // 50, pos[1] // 50), background_color)
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if verif():
                        grid_draw(background_color)
        pygame.display.update()
    pygame.display.update()




def isEmpty(num):
    if num == 0:
        return True
    return False


def isValid(position, num):



    for i in range(0, len(grid[0])):
        if (grid[position[0]][i] == num):
            return False


    for i in range(0, len(grid[0])):
        if (grid[i][position[1]] == num):
            return False


    x = position[0] // 3 * 3
    y = position[1] // 3 * 3


    for i in range(0, 3):
        for j in range(0, 3):
            if (grid[x + i][y + j] == num):
                return False
    return True


solved = 0


def sudoku_solver(win, background_color):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (isEmpty(grid[i][j])):
                for k in range(1, 10):
                    if isValid((i, j), k):
                        grid[i][j] = k
                        pygame.draw.rect(win, background_color, (
                        (j + 1) * 50 + buffer, (i + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                        value = myfont.render(str(k), True, (0, 0, 0))
                        win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
                        pygame.display.update()
                        pygame.time.delay(25)

                        sudoku_solver(win, background_color)


                        global solved
                        if (solved == 1):
                            return


                        grid[i][j] = 0
                        pygame.draw.rect(win, background_color, (
                        (j + 1) * 50 + buffer, (i + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                        pygame.display.update()

                return
    solved = 1


def grid_draw(background_color):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)
    original_grid_element_color = (255, 255, 255)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    for i in range(0, 10):
        if (i % 3 == 0):
            pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    sudoku_solver(win, background_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return



def settings():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    background_color = (255, 255, 255)
    menu_bg_color = (52, 31, 151)
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    back_btn = Button(10, 0, back_btn_img)
    green_btn = Button(60, 250, green_image_img)
    blue_btn = Button(250, 250, blue_image_img)
    red_button = Button(450, 250, red_button_img)


    while True:
        win.fill(menu_bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        if back_btn.draw():
            menu(menu_bg_color)
        if red_button.draw():
            background_color = (192, 9, 9)
            original_grid_element_color = (192, 9, 9)
            menu_bg_color = (192, 9, 9)
        if blue_btn.draw():
            background_color = (5, 6, 200)
            original_grid_element_color = (5, 6, 200)
            menu_bg_color = (5, 6, 200)
        if green_btn.draw():
            background_color = (19, 168, 29)
            original_grid_element_color = (19, 168, 29)
            menu_bg_color = (19, 168, 29)
        pygame.display.update()




def menu(menu_bg_color):
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    #menu_bg_color = (52, 31, 151)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    play_btn_img = pygame.image.load('images/play.png').convert_alpha()
    play_btn = Button(215, 125, play_btn_img)
    settings_btn = Button(215, 300, settings_btn_img)


    while True:
        win.fill(menu_bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        if play_btn.draw():
            main(menu_bg_color)
        if settings_btn.draw():
            settings()
            print('zz')
        pygame.display.update()

menu(menu_bg_color)
pygame.display.update()
