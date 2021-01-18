import pygame

pygame.init()

largeFont = pygame.font.SysFont("timesnewromanttf", 115)
mediumFont = pygame.font.SysFont("timesnewromanttf", 40)
smallFont = pygame.font.SysFont("timesnewromanttf", 30)

displayWidth = 800
displayHeight = 600

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 128)
red = (200, 0, 0)
green = (0, 200, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
purple = (146, 55, 226)
brightRed = (255, 0, 0)
brightGreen = (0, 255, 0)
lightBlue = (173, 238, 255)
darkBlue = (43, 166, 210)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('The Story of the Call Story--by Aditi & Jess')
clock = pygame.time.Clock()

score = 0
prophet = "isaiah"
prophet_nums = {"isaiah": 6, "jeremiah": 5, "ezekiel": 6}
num = -1

complete = {
    "structure": False,
    "isaiah": False,
    "jeremiah": False,
    "ezekiel": False
}


def text_box(text, font, colour):
    textSurf = font.render(text, True, colour)
    return textSurf, textSurf.get_rect()


def load_image(imagename, sizex, sizey):
    image = pygame.image.load(imagename)
    image = pygame.transform.scale(image, (sizex, sizey))
    return image


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h), 1)
        if click[0] and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h), 1)
    textSurf, textRect = text_box(msg, smallFont, black)
    textRect.center = (x + w / 2, y + h / 2)
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame()


def display_score():
    textSurf, textRect = text_box(str(score), smallFont, black)
    textRect.center = (95, 582)
    gameDisplay.blit(textSurf, textRect)


def score_increase():
    global score
    score += 1


def display_background(image_name):
    background = load_image(image_name, displayWidth, displayHeight)
    gameDisplay.blit(background, (0, 0))


def display_star(position):
    star = load_image("star.png", 70, 65)
    gameDisplay.blit(star, position)


def game_intro():
    while True:
        check_quit()

        display_background('main_page.png')

        button("",25,287,200,220, black, darkBlue, structure0)
        button("", 524, 256, 200, 63, black, brightRed, setisaiah)
        button("", 592, 348, 200, 63, black, orange, setjeremiah)
        button("", 555, 440, 200, 63, black, green, setezekiel)
        if complete["structure"]:
            display_star((200, 470))
        if complete["isaiah"]:
            display_star((445, 255))
        if complete["jeremiah"]:
            display_star((510, 345))
        if complete["ezekiel"]:
            display_star((475, 435))
        if all(value for value in complete.values()):
            congratsSurf, congratsRect = text_box(
                "Congratulations! You finished the game :)", mediumFont, white)
            congratsRect.center = (displayWidth / 2, 565)
            gameDisplay.blit(congratsSurf, congratsRect)
            final_score = round((score + 1) / (30) * 100)
            congratsSurf, congratsRect = text_box(
                f"Final score: {final_score}%", smallFont, white)
            congratsRect.center = (displayWidth / 2, 590)
            gameDisplay.blit(congratsSurf, congratsRect)

        pygame.display.update()
        clock.tick(15)


total_score = 0


def structure0():
    while True:
        check_quit()

        display_background('structure_imgs/structure0.png')
        display_score()
        button("", 615, 560, 183, 40, black, purple, structure1)

        pygame.display.update()
        clock.tick(15)


def structure1():
    background = "structure_imgs/structure1_noanswers.png"
    complete = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    score_increase()
                background = "structure_imgs/structure1_answers.png"
                complete = True

        display_background(background)
        display_score()

        if complete:
            button("", 615, 560, 183, 40, black, purple, structure2)
        pygame.display.update()
        clock.tick(15)


def structure2():
    background = "structure_imgs/structure2_noanswers.png"
    complete = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    score_increase()
                background = "structure_imgs/structure2_answers.png"
                complete = True

        display_background(background)
        display_score()
        if complete:
            button("", 615, 560, 183, 40, black, purple, structure3)

        pygame.display.update()
        clock.tick(15)


def structure3():
    background = "structure_imgs/structure3_noanswers.png"
    complete = False
    word = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    word += "I"
                elif event.key == pygame.K_s:
                    word += "s"
                elif event.key == pygame.K_r:
                    word += "r"
                elif event.key == pygame.K_a:
                    word += "a"
                elif event.key == pygame.K_e:
                    word += "e"
                elif event.key == pygame.K_l:
                    word += "l"
                else:
                    word += "m"

        if len(word) >= 6:
            if word == "Israel":
                score_increase()
            background = "structure_imgs/structure3_answers.png"
            complete = True
            word = ""

        display_background(background)
        display_score()
        if complete:
            button("", 615, 560, 183, 40, black, purple, structure4)

        pygame.display.update()
        clock.tick(15)


def structure4():
    background = "structure_imgs/structure4_noanswers.png"
    complete = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    score_increase()
                background = "structure_imgs/structure4_answers.png"
                complete = True

        display_background(background)
        display_score()
        if complete:
            button("", 615, 560, 183, 40, black, purple, structure5)

        pygame.display.update()
        clock.tick(15)


def structure5():
    background = "structure_imgs/structure5_noanswers.png"
    complete = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    score_increase()
                background = "structure_imgs/structure5_answers.png"
                complete = True

        display_background(background)
        display_score()
        if complete:
            button("", 615, 560, 183, 40, black, purple, structure6)

        pygame.display.update()
        clock.tick(15)


def structure6():
    background = "structure_imgs/structure6_noanswers.png"
    complete["structure"] = True
    while True:
        check_quit()

        display_background(background)
        display_score()
        button("", 412, 348, 173, 115, black, purple, structure6_correct)
        button("", 593, 348, 173, 115, black, purple, structure6_incorrect)

        pygame.display.update()
        clock.tick(15)


def structure6_correct():
    score_increase()
    background = "structure_imgs/structure6_answers.png"
    while True:
        check_quit()

        display_background(background)
        display_score()
        button("", 615, 560, 183, 40, black, purple, game_intro)

        pygame.display.update()
        clock.tick(15)


def structure6_incorrect():
    background = "structure_imgs/structure6_answers.png"
    while True:
        check_quit()

        display_background(background)
        display_score()
        button("", 615, 560, 183, 40, black, purple, game_intro)

        pygame.display.update()
        clock.tick(15)


def setisaiah():
    global prophet, num
    prophet = "isaiah"
    num = -1
    next_slide_prophet()


def setjeremiah():
    global prophet, num
    prophet = "jeremiah"
    num = -1
    next_slide_prophet()


def setezekiel():
    global prophet, num
    prophet = "ezekiel"
    num = -1
    next_slide_prophet()


def next_slide_prophet():
    global num, score
    num += 1
    if num <= prophet_nums[prophet]:
        score += 1
        prophet_slide()
    else:
        complete[prophet] = True
        game_intro()


def prophet_slide():
    complete = False
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                complete = True

        display_background(f'{prophet}_imgs/{prophet}{num}.png')
        display_score()
        if complete and num <= 6:
            button("", 615, 560, 183, 40, black, purple, next_slide_prophet)

        pygame.display.update()
        clock.tick(15)

game_intro()
