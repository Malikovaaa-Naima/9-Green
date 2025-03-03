# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()                 

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

    wn.mainloop()

# pip install pygame

# import pygame
# import time
# import random

# # Pygame ni boshlash
# pygame.init()

# # Ranglar
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)

# # O'yin ekranining o'lchamlari
# width = 600
# height = 400
# screen = pygame.display.set_mode((width, height))

# # O'yin nomi
# pygame.display.set_caption('Snake Game')

# # Ilon boshlanishi
# snake_block = 10
# snake_speed = 15

# # Fontlar
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)

# def your_score(score):
#     value = score_font.render("Bal: " + str(score), True, black)
#     screen.blit(value, [0, 0])

# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     screen.blit(mesg, [width / 6, height / 3])

# def gameLoop():  # O'yin tsikli
#     game_over = False
#     game_close = False

#     x1 = width / 2
#     y1 = height / 2

#     x1_change = 0
#     y1_change = 0

#     snake_List = []
#     Length_of_snake = 1

#     foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

#     while not game_over:

#         while game_close == True:
#             screen.fill(blue)
#             message("O'yin tugadi! Qayta urinish uchun C, chiqish uchun Q", red)
#             your_score(Length_of_snake - 1)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0

#         if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
#             game_close = True

#         x1 += x1_change
#         y1 += y1_change
#         screen.fill(blue)
#         pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]

#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True

#         our_snake(snake_block, snake_List)
#         your_score(Length_of_snake - 1)

#         pygame.display.update()

#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1

#         pygame.time.Clock().tick(snake_speed)

#     pygame.quit()
#     quit()

# gameLoop()

# python snake_game.py























