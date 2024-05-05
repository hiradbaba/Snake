import os
import sys
import time
import random
import keyboard
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# Constants
WIDTH = 60
HEIGHT = 30
SNAKE_CHAR = 'ø'
FOOD_CHAR = 'ó'
BLOCK_CHAR = '█'
EMPTY_CHAR = ' '
DELAY = 0.1  # Reduced delay
BORDER_COLOR = Fore.WHITE
GAME_OVER = False
score = 0

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'



snake = [(4, 3), (3, 3), (2, 3)]
direction = None
food = (random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1))
blocks = [(random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1)) for _ in range(20)]


def init():
    global snake, direction, food, blocks
    snake = [(4, 3), (3, 3), (2, 3)]
    direction = None
    food = (random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1))
    blocks = [(random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1)) for _ in range(20)]



def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def draw():
    global score
    clear_screen()
    print(BORDER_COLOR + '+' + '-' * WIDTH + '+')
    for y in range(HEIGHT):
        print(BORDER_COLOR + '|' + EMPTY_CHAR * WIDTH + BORDER_COLOR + '|')
    print(BORDER_COLOR + '+' + '-' * WIDTH + '+')

    for x, y in snake:
        print_at(x, y, Fore.GREEN + SNAKE_CHAR)
    print_at(food[0], food[1], Fore.RED + FOOD_CHAR)
    for block in blocks:
        print_at(block[0], block[1], Fore.BLUE + BLOCK_CHAR)
    
    print_at(0,32, f"SCORE: {score}")
    #print_at(0,33, f"snake: {snake}")

def print_at(x, y, char):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y+2, x+2, char))
    sys.stdout.flush()

def move():
    global direction
    global food
    global GAME_OVER
    global score
    if direction is None:
        return
    x, y = snake[0]
    if direction == UP:
        y -= 1
    elif direction == DOWN:
        y += 1
    elif direction == LEFT:
        x -= 1
    elif direction == RIGHT:
        x += 1
    x %= WIDTH
    y %= HEIGHT 
    # Check for collisions with food and blocks
    if (x, y) == food:
        food = (random.randint(1, WIDTH - 1), random.randint(1, HEIGHT - 1))
        score += 1

    elif (x,y) in snake[1:]:
        GAME_OVER = True
        return
    elif (x, y) in blocks :
        GAME_OVER = True
        return
    else:
        snake.pop()  # Remove the last segment of the snake to maintain its length

    snake.insert(0, (x, y))

def load_game_over_screen():
    global score
    clear_screen()
    print(Fore.RED + r"   ____                         ___                   ")
    print(Fore.RED + r"  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __  ")
    print(Fore.RED + r" | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__| ")
    print(Fore.RED + r" | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |    ")
    print(Fore.RED + r"  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|    ")
    _ = [print() for i in range(3)]
    print(Fore.GREEN +   f"                Score: {score}                ")

def menu():
    
    clear_screen()
    print(Fore.RED   +   r"  _________ _______      _____   ____  __ó___________")
    print(Fore.GREEN +   r" /   _____/ \      \    /  _  \ |    |/ _|\_   _____/")
    print(Fore.YELLOW +  r" \_____  \  /   |   \  /  /_\  \|      <   |    __)_  ")
    print(Fore.BLUE +    r" /        \/    |    \/    |    \    |  \  |        \ ")
    print(Fore.MAGENTA + r"/_______  /\____|__  /\____|__  /____|__ \/_______  / ")
    print(Fore.CYAN +    r"        \/         \/         \/        \/        \/  ")
    _ = [print() for i in range(3)]
    print(Fore.GREEN +   "                 Press Any Key To PLAY                ")
    input()


def game():
    global GAME_OVER, UP, DOWN, RIGHT, LEFT, direction
    while True:
        if GAME_OVER:
            #load_game_over_screen()
            break
        
        # Handle keyboard input
        if direction != DOWN and keyboard.is_pressed('w'):
            direction = UP
        elif direction != UP and keyboard.is_pressed('s'):
            direction = DOWN
        elif direction != RIGHT and keyboard.is_pressed('a'):
            direction = LEFT
        elif direction != LEFT and keyboard.is_pressed('d'):
            direction = RIGHT
        draw()
        move()
        time.sleep(DELAY)

def game_over():
    global GAME_OVER
    load_game_over_screen()
    input()
    GAME_OVER = False

def main_loop():
    while True:
        menu()
        init()
        game()
        game_over()

if __name__ == '__main__':
    main_loop()


