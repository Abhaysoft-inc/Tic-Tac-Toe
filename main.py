import pygame as pg
import sys
import time
from pygame.locals import *

# Declaring the global variables

# For storing 'x' or 'o' value as character

XO = 'x'

# storing the winner's value at any instant of code
winner = None

# To check if game is draw
draw = None

# Width
width = 400

# Height 
height = 400

# Background color
white = (255, 255, 255)

# Color LIne
line_color = (0, 0, 0)

# INIT pygame window
pg.init()

# Setting FPS
fps = 30

# Clock
CLOCK = pg.time.Clock()

# Pygame Screen
screen = pg.display.set_mode((width, height + 100 ), 0, 32)

#  Game Title
pg.display.set_caption("Tic Tac Toe Online Multiplayer")

# Loding Images
initiating_window = pg.image.load("cover.png")
x_img = pg.image.load("x.png")
o_img = pg.image.load("o.png")

# Resizing Image
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))


def game_initiating_window():

    # Displaying over the screen
    screen.blit(initiating_window, (0, 0))

    # updating the display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    # Drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2 , height), 7)

    # Drawing horizontal line
    pg.draw.line(screen, line_color, (0, height/ 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2 ), 7 )
    draw_status()

def draw_status():
    # getting global variable
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + "won !"
    if draw:
        message = "Game Draw !"

    # setting a font object
    font = pg.font.Font(None, 30)

    # Setting font properties
    text = font.render(message, 1, ( 255, 255, 255))

    # Copy the rendered message 
    screen.fill ((0, 0, 0,), (0, 400, 500, 100))
    text_rect = text.get_rect(center =(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update() 

def check_win():
    global board, winner, draw

    # Checking for winning rows
    for row in range(0, 3 ):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1)*height / 3 - height / 6), (width, (row + 1) * height / 3 - height /6 ), 4)
            break
    # Checking for winning columns

    for col in range(0, 3 ):
        if((board[o][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line (screen, (250, 0, 0), ((col + 1)* width / 3 - width / 6, 0), ((col + 1)* width / 3 - width / 6, height), 4)
        break
        # Check for diagonal winner
        if (board[0][0] == board[1][1] == board[2][2]) and (board [0][0] is not None):
            winner = board[0][0]
            pg.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4)

        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            winner = board[0][2]
            pg.draw.line (screen, (250, 70, 70), (350,50), (50, 350),4)

        if(all([all(row) for row in board]) and winner is None):
            draw = True
        draw_status()

def drawXO(row, col):
    global board, XO
    # For first row
    if row == 1:
        posx = 30

    # for second row
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30
    if col == 1 :
        posy == 30
    if col == 2:
        posy == height / 3 + 30
    if col == 3:
        posy = height / 3 * 2 + 30

    #  Setting up required board
    board[row-1][col-1] = XO

    if(XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'

    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()

def user_click():
    x, y = pg.mouse.get_pos()

    if(x<width / 3):
        col=1
    elif (x<width / 3 * 2):
        col = 2 
    elif(x<width):
        col = 3
    else:
        col = None

    if (y<height / 3):
        row = 1
    elif(y<height / 3 * 2):
        row = 2
    elif(y<height):
        row= 3
    else:
        row=None


    if(row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row, col)
        check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]
game_initiating_window()

while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            user_click()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)                


