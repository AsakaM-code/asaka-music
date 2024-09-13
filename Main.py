import random
import time
import pygame.mixer
from time import sleep
import tkinter
from tkinter import messagebox
from turtle import Screen
from snake import Snake
from harricane import Harricane
from harricane import Harricane2
from harricane import Harricane3
from data import quetions
from data import quetions2
from data import quetions3
import tkinter.messagebox as tmsg
from scoreboard import Scoreboard
from asaka_shoukai import hajime

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor('white')
screen.title('ハリケーンクイズゲーム!!')
screen.tracer(0)
screen.update()
screen.listen()
snake = Snake()
harricane = Harricane()
harricane2 = Harricane2()
harricane3 = Harricane3()
scoreboard=Scoreboard()
asaka_shoukai=hajime()

pygame.mixer.init()
pygame.mixer.music.load("kansei1.mp3")
pygame.mixer.music.play(1)

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(harricane)<20:
        print('collided')
        harricane.refresh()
        screen.update()
        for i in range(1):
            mondai=random.choice(quetions)
            sitsumon=tmsg.askquestion("クイズ",f"{mondai[0]}")

            if sitsumon==mondai[1]:
                tmsg.showinfo("クイズ","大正解!")
                scoreboard.increase_scoreboard()
                snake.move()
                pygame.mixer.init()
                pygame.mixer.music.load("Quiz-Correct_Answer02-1.mp3")
                pygame.mixer.music.play(1)
            else:
                tmsg.showinfo("クイズ", "残念不正解!")
                scoreboard.decrease_scoreboard()
                snake.move()
                pygame.mixer.init()
                pygame.mixer.music.load("Quiz-Wrong_Buzzer01-1.mp3")
                pygame.mixer.music.play(1)

    if snake.head.distance(harricane2)<20:
        print('collided')
        harricane2.refresh()
        screen.update()
        for i in range(1):
            mondai=random.choice(quetions2)
            sitsumon=tmsg.askquestion("クイズ",f"{mondai[0]}")
            print(sitsumon)

            if sitsumon==mondai[1]:
                tmsg.showinfo("クイズ","大正解")
                scoreboard.increase_scoreboard()
                snake.move()
                pygame.mixer.init()
                pygame.mixer.music.load("Quiz-Correct_Answer02-1.mp3")
                pygame.mixer.music.play(1)
            else:
                tmsg.showinfo("クイズ", "残念不正解")
                scoreboard.decrease_scoreboard()
                snake.move()
                pygame.mixer.init()
                pygame.mixer.music.load("Quiz-Wrong_Buzzer01-1.mp3")
                pygame.mixer.music.play(1)


    if snake.head.distance(harricane3)<20:
        print('collided')
        harricane3.refresh()
        screen.update()
        for i in range(1):
            mondai=random.choice(quetions3)
            sitsumon=tmsg.askquestion("クイズ",f"{mondai[0]}")
            print(sitsumon)

            if sitsumon==mondai[1]:
                tmsg.showinfo("クイズ","大正解")
                scoreboard.increase_scoreboard()
                snake.move()
                pygame.mixer.init()
                pygame.mixer.music.load("Quiz-Correct_Answer02-1.mp3")
                pygame.mixer.music.play(1)
            else:
                tmsg.showinfo("クイズ", "残念不正解")
                scoreboard.decrease_scoreboard()
                snake.move()
                pygame.mixer.init()
                pygame.mixer.music.load("Quiz-Wrong_Buzzer01-1.mp3")
                pygame.mixer.music.play(1)




    if snake.head.xcor() > 600 or snake.head.xcor() < -600 or snake.head.ycor() > 600 or snake.head.ycor() < -600:
            print('Game over')
            game_is_on = False
            scoreboard.game_over()

    if scoreboard.score >= 5:
            print('Game Clear')
            game_is_on = False
            scoreboard.game_clear()

    if scoreboard.score <= -5:
            print('Game Over')
            game_is_on = False
            scoreboard.game_over2()

screen.exitonclick()