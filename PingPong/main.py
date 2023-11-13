from turtle import Screen, Turtle
from racket import Racket
from ball import Ball
from time import sleep
from random import randint
from score import ScoreBoard

screen_width = 800
screen_height = 600
game_screen = Screen()
game_screen.setup(screen_width, screen_height)
game_screen.bgcolor("black")
game_screen.tracer(0)

player_racket = Racket(pos_x=-380, pos_y=0, screen_height=screen_height)
player_racket.racket_control(game_screen, True)

opponent_racket = Racket(pos_x=380, pos_y=0, screen_height=screen_height)
opponent_racket.racket_control(game_screen, False)

ball = Ball(10)

player_score_board = ScoreBoard(-40,  252)
opponent_score_board = ScoreBoard(40,  252)


def starting_direction():
    ball.setheading(randint(-60, 60))


def check_racket_ball_collision():
    if ball.xcor() > screen_width / 2 - 50 or ball.xcor() < 50 - screen_width / 2:
        if ball.distance(player_racket) < 60 or ball.distance(opponent_racket) < 60:
            ball.bounce()


def track_score():
    if ball.xcor() > screen_width / 2:
        player_score_board.increase_score()
        player_racket.refresh()
        opponent_racket.refresh()
        ball.refresh(10)
        starting_direction()
    elif ball.xcor() < -screen_width / 2:
        opponent_score_board.increase_score()
        player_racket.refresh()
        opponent_racket.refresh()
        ball.refresh(10)
        starting_direction()


game_on = True
starting_direction()
while game_on:
    game_screen.update()
    sleep(1 / 30)
    ball.move()
    ball.check_boundary_collision(screen_height)
    check_racket_ball_collision()
    track_score()
    if player_score_board.score == 10 or opponent_score_board.score == 10:
        break

if player_score_board.score == 10:
    player_win = Turtle()
    player_win.color("white")
    player_win.hideturtle()
    player_win.penup()
    player_win.write(arg="Player Wins!!!", align="center", font=("Arial", 32, "normal"))

if opponent_score_board.score == 10:
    opponent_win = Turtle()
    opponent_win.color("white")
    opponent_win.hideturtle()
    opponent_win.penup()
    opponent_win.write(arg="Opponent Wins!!!", align="center", font=("Arial", 32, "normal"))

game_screen.exitonclick()

# TODO: devise a score system where the person scores o point when the ball passes behind the racket line of the opponent's and restarts the screen composition
