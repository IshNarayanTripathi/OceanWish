import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, 'Up')


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car_manager.create_new()
    car_manager.move_car()


    for cars in car_manager.all_cars:
        if cars.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_Line():
        player.go_to_start()
        car_manager.increse_speed()
        scoreboard.increase_level()
        scoreboard.update()

screen.exitonclick()
