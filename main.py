import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.onkey(player.move_up, key="Up")
screen.onkey(player.move_down, key="Down")


sleep_time = 0.1
level = 1

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    if car_manager.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()

    if player.ycor() >= 280:
        player.reset_position()
        sleep_time *= 0.7
        level += 1
        scoreboard.update_score(level)



screen.exitonclick()