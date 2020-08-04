import os
import random
import pygame

pygame.init()
Width, Height = [700, 400]
screen = pygame.display.set_mode((Width, Height))
running = True
start_screen = True
all_sprites = pygame.sprite.Group()
helper_sprites = pygame.sprite.Group()
attackers_sprites = pygame.sprite.Group()
borders = pygame.sprite.Group()
clock = pygame.time.Clock()
pygame.mixer.music.load('data/1.mp3')
pygame.mixer.music.play()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Clock_image(pygame.sprite.Sprite):
    image = load_image("clock2.png", -1)
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Clock_image.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Erythrocytes(pygame.sprite.Sprite):
    image = load_image("red.png", -1)
    image = pygame.transform.scale(image, (70, 70))

    def __init__(self, x, y):
        super().__init__(all_sprites, helper_sprites)
        self.image = Erythrocytes.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # self.image = pygame.Surface((50, 50), pygame.SRCALPHA, 32)
        # pygame.draw.rect(self.image, pygame.Color("grey"), (0, 0, 50, 50))

    def update(self):
        pass


class Leukocytes(pygame.sprite.Sprite):
    image = load_image("white.png", -1)
    image = pygame.transform.scale(image, (60, 60))

    def __init__(self, x, y):
        super().__init__(all_sprites, helper_sprites)
        self.image = Leukocytes.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Thrombocyte(pygame.sprite.Sprite):
    image = load_image("platelet.png", -1)
    image = pygame.transform.scale(image, (60, 60))

    def __init__(self, x, y):
        super().__init__(all_sprites, helper_sprites)
        self.image = Thrombocyte.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Oxygen(pygame.sprite.Sprite):
    image = load_image("oxygen.png", -1)
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites, attackers_sprites)
        self.image = Oxygen.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Virus(pygame.sprite.Sprite):
    image = load_image("virus1.png", -1)
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites, attackers_sprites)
        self.image = Virus.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Cut(pygame.sprite.Sprite):
    image = load_image("cut.png", -1)
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites, attackers_sprites)
        self.image = Cut.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Red_curcor(pygame.sprite.Sprite):
    image = load_image("cursor1.png", -1)
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Red_curcor.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Blue_curcor(pygame.sprite.Sprite):
    image = load_image("cursor2.png", -1)
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Blue_curcor.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Pink_curcor(pygame.sprite.Sprite):
    image = load_image("cursor3.png", -1)
    image = pygame.transform.scale(image, (50, 50))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Pink_curcor.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Heart(pygame.sprite.Sprite):
    image = load_image("heart.png", -1)
    image = pygame.transform.scale(image, (25, 25))

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Heart.image
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


class Platform():
    def __init__(self, surface):
        pygame.draw.rect(surface, (161, 0, 0), (0, 75, Width, 230))

        pygame.draw.rect(surface, (73, 66, 61), (85, 325, 75, 80), 10)
        pygame.draw.rect(surface, (161, 0, 0), (85, 325, 75, 80))

        pygame.draw.rect(surface, (73, 66, 61), (185, 325, 75, 80), 10)
        pygame.draw.rect(surface, (161, 0, 0), (185, 325, 75, 80))

        pygame.draw.rect(surface, (73, 66, 61), (285, 325, 75, 80), 10)
        pygame.draw.rect(surface, (161, 0, 0), (285, 325, 75, 80))


def clock_update(value):
    font = pygame.font.Font(None, 30)
    minute = str(value // 60).rjust(2, '0')
    seconds = str(value % 60).rjust(2, '0')
    time = "{}:{}".format(minute, seconds)
    text = font.render(time, 1, (0, 127, 235))
    text_x = 630
    text_y = 15
    screen.blit(text, (text_x, text_y))


info = False
while start_screen:
    fon = pygame.transform.scale(load_image('start_info.jpg'), (626, 400))
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    if info:
        screen.blit(fon, (50, 0))
    else:
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 80)
        string_start = font.render('START', 1, pygame.Color('red'))
        start_rect = string_start.get_rect()
        start_rect.top = 100
        start_rect.x = 250
        screen.blit(string_start, start_rect)

        string_info = font.render('INFO', 1, pygame.Color('red'))
        info_rect = string_info.get_rect()
        info_rect.top = 160
        info_rect.x = 270
        screen.blit(string_info, info_rect)

        string_exit = font.render('EXIT', 1, pygame.Color('red'))
        exit_rect = string_exit.get_rect()
        exit_rect.top = 220
        exit_rect.x = 267
        screen.blit(string_exit, exit_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            start_screen = False
        if event.type == pygame.MOUSEBUTTONUP:
            if info:
                info = False
                continue
            x, y = event.pos
            if start_rect.x <= x <= 430 and start_rect.top <= y <= 140:
                start_screen = False
                pygame.mixer.music.load('data/2.mp3')
                pygame.mixer.music.play()
            elif info_rect.x <= x <= 400 and info_rect.top <= y <= 200:
                info = True

            elif exit_rect.x <= x <= 400 and exit_rect.top <= y <= 260:
                running = False
                start_screen = False
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    pygame.display.update()

first_cursor = pygame.transform.scale(load_image("cursor1.png", -1), (30, 30))
second_cursor = pygame.transform.scale(load_image("cursor2.png", -1), (30, 30))
third_cursor = pygame.transform.scale(load_image("cursor3.png", -1), (25, 25))
main_display = Platform(screen)
main_e = Erythrocytes(82, 325)
main_l = Leukocytes(193, 329)
main_t = Thrombocyte(292, 330)
Clock_image(580, 0)
Health = [Heart(600, 40), Heart(630, 40), Heart(660, 40)]
gameover_image = pygame.transform.scale(load_image("gameover.png"), (700, 400))
mouse_type = 0
tick_object = 0
tick_time = 999
seconds = 0
while running:
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            current_x, current_y = event.pos
            if 85 <= current_x <= 180 and 315 <= current_y <= 405:
                mouse_type = 1
            elif 185 <= current_x <= 270 and 315 <= current_y <= 405:
                mouse_type = 2
            elif 285 <= current_x <= 370 and 315 <= current_y <= 405:
                mouse_type = 3
            for box in attackers_sprites:

                if box.rect.collidepoint(current_x, current_y):
                    if mouse_type == 1:
                        if isinstance(box, Oxygen):
                            box.kill()
                            continue
                        else:
                            Health.pop(0).kill()
                            continue

                    if mouse_type == 2:
                        if isinstance(box, Virus):
                            box.kill()
                            continue
                        else:
                            Health.pop(0).kill()
                            continue
                    if mouse_type == 3:
                        if isinstance(box, Cut):
                            box.kill()
                            continue
                        else:
                            Health.pop(0).kill()
                            continue

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_focused():
                if mouse_type != 0:
                    if mouse_type == 1:
                        pygame.mouse.set_visible(False)
                        current_x, current_y = event.pos
                        screen.blit(first_cursor, (current_x - 10, current_y - 10))
                        pygame.display.update()
                    elif mouse_type == 2:
                        pygame.mouse.set_visible(False)
                        current_x, current_y = event.pos
                        screen.blit(second_cursor, (current_x - 10, current_y - 10))
                        pygame.display.update()
                    elif mouse_type == 3:
                        pygame.mouse.set_visible(False)
                        current_x, current_y = event.pos
                        screen.blit(third_cursor, (current_x - 10, current_y - 10))
                        pygame.display.update()

    tick_time += 1
    if tick_time == 1000:
        seconds += 1
        tick_time = 0
    screen.fill((0, 0, 0))
    clock_update(seconds)
    tick_object += 1
    if tick_object == 500:
        varient = random.randint(1, 3)
        if varient == 1:
            Oxygen(random.randint(0, Width - 50), random.randint(75, 250))
        elif varient == 2:
            Virus(random.randint(0, Width - 50), random.randint(75, 250))
        elif varient == 3:
            Cut(random.randint(0, Width - 50), random.randint(75, 250))

        tick_object = 0
    Platform(screen)
    all_sprites.draw(screen)
    if mouse_type == 1:
        screen.blit(first_cursor, (current_x - 10, current_y - 10))
        pygame.display.update()
    elif mouse_type == 2:
        screen.blit(second_cursor, (current_x - 10, current_y - 10))
        pygame.display.update()
    elif mouse_type == 3:
        screen.blit(third_cursor, (current_x - 10, current_y - 10))
        pygame.display.update()
    pygame.display.update()
    pygame.display.flip()
    if len(Health) == 0:
        rect = gameover_image.get_rect()
        rect.x = -700
        rect.y = 0
        while rect.x < 0:
            screen.blit(gameover_image, (rect.x, rect.y))
            rect = rect.move(2, 0)
            pygame.time.wait(5)
            pygame.display.update()
        pygame.time.wait(5000)
        running = False
        continue
