from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard

width = 600
height = 600

game_screen = Screen()
game_screen.bgcolor("black")
game_screen.screensize(width, height)
game_screen.title("Snake Game")
game_screen.tracer(0)  # we turn of the tracer for the individual commands to be executed off screen to prevent lags in images

snake = Snake()
food = Food(width, height)
score = 0
score_text = f"Score: {score}"
score_board = ScoreBoard(score_text, 350)


def control():
    game_screen.listen()
    game_screen.onkey(fun=snake.turn_right, key="d")
    game_screen.onkey(fun=snake.turn_left, key="a")
    game_screen.onkey(fun=snake.turn_up, key="w")
    game_screen.onkey(fun=snake.turn_down, key="s")


def eat_food():
    if snake.snake_head.distance(food) < 20:
        food.refresh(width, height)
        new_snake_piece = Turtle()
        new_snake_piece.penup()
        new_snake_piece.speed("fastest")
        new_snake_piece.shape("square")
        new_snake_piece.color("green")
        snake.snake_body.append(new_snake_piece)
        return True


def collision_detection(collision_width, collision_height):
    if \
            snake.snake_head.xcor() < - collision_width or \
            snake.snake_head.xcor() > collision_width or \
            snake.snake_head.ycor() < -collision_height or \
            snake.snake_head.ycor() > collision_height:
        global game_on  # this global definition s needed to manipulate a variable outside a method
        game_over = ScoreBoard("Game Over !!!", 0)
        game_on = False


def collision_detection_snake_body():
    global game_on
    for snake_part in snake.snake_body[1:]:
        # this [number:number] method is called slicing and can be used for lists and tuples, it allows you to use a certain range of items in a list or a tuple that you designate
        # in this case the command tells that the list should start from the item with the index 1 and go on until the end
        if snake.snake_head.distance(snake_part) < 10:
            game_over = ScoreBoard("Game Over !!!", 0)
            game_on = False


game_on = True
control()

while game_on:
    game_screen.update()
    sleep(1 / 20)  # waits the indicated amount of seconds before executing the next command
    snake.move()
    if eat_food():
        score += 1
        score_text = f"Score: {score}"
        score_board.increase_score(score_text)
    collision_detection(480, 400)
    collision_detection_snake_body()

game_screen.exitonclick()
