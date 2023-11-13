from turtle import Screen, Turtle
from player import Player
from block import Block
from time import sleep
from random import randint


def create_blocks():
    blocks = []
    for _ in range(randint(10, 15)):
        block = Block()
        blocks.append(block)

    return blocks


def collision_checks():
    for block in blocks_container:
        if player.distance(block) < 25:
            global game_on
            game_on = False


screen_width = 800
screen_height = 600

game_screen = Screen()
game_screen.tracer(0)
game_screen.setup(screen_width, screen_height)


player = Player(0, 20 - screen_height/2)
player.game_control(game_screen)

end_line = screen_height/2
game_on = True
need_new_blocks = True

blocks_container = create_blocks()
blocks_on_road = len(blocks_container)


while game_on:
    sleep(0.1)
    game_screen.update()

    collision_checks()

    for created_block in blocks_container:
        if created_block.xcor() > -420:
            created_block.move()
        else:
            blocks_container.remove(created_block)
            blocks_on_road -= 1
            need_new_blocks = True

        if len(blocks_container) < 30 and created_block.xcor() < 0 and need_new_blocks:
            blocks_container.extend(create_blocks())
            blocks_on_road = len(blocks_container)
            need_new_blocks = False

    if player.ycor() >= end_line:
        game_on = False

if player.ycor() >= end_line:
    print("You won")

game_screen.exitonclick()
