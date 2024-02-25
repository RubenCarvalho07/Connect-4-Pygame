import pygame, time

colors = {
    "white" : (255, 255, 255),
    "blue" : (0, 0, 255  ),
    "red" : (255, 0, 0),
    "yellow" : (255, 255, 0)
}

game = [
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"],
    ["white", "white", "white", "white", "white", "white", "white"]
]

player = "red"

screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption('Connect 4')

def draw():
    pygame.display.update()
    screen.fill(colors["blue"])
    for i in range(6):
        for j in range(7):
            pygame.draw.circle(screen, colors[game[i][j]], (j * 100 + 75, i * 75 + 75), 25)

def play(pl):
    row = pygame.mouse.get_pos()[0] // 100
    time.sleep(.25)
    i = 5
    while i >= 0 and game[i][row] != "white":
            i -= 1
    if game[i][row] == "white":
        game[i][row] = pl
        if pl == "red":
            pl  = "yellow"
        else:
            pl = "red"
    return pl

def end():
    for i in range(6):
        for j in range(4):
            if game[i][j] == game[i][j+1] == game[i][j+2] == game[i][j+3] != "white":
                print("\n\n=======================\n" + game[i][j] + " ganhou!!!\n=======================\n\n")
                return True

    for j in range(7):
        for i in range(3):
            if game[i][j] == game[i+1][j] == game[i+2][j] == game[i+3][j] != "white":
                print("\n\n=======================\n" + game[i][j] + " ganhou!!!\n=======================\n\n")
                return True

    for i in range(3, 6):
        for j in range(4):
            if game[i][j] == game[i-1][j+1] == game[i-2][j+2] == game[i-3][j+3] != "white":
                print("\n\n=======================\n" + game[i][j] + " ganhou!!!\n=======================\n\n")
                return True

    for i in range(3):
        for j in range(4):
            if game[i][j] == game[i+1][j+1] == game[i+2][j+2] == game[i+3][j+3] != "white":
                print("\n\n=======================\n" + game[i][j] + " ganhou!!!\n=======================\n\n")
                return True
    return False

while not end():
    draw()
    if pygame.mouse.get_pressed()[0]:
        player = play(player) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit()