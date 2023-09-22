from turtle import Turtle,Screen
from turtle_object import turtle_obj
from car import Car
from score_bord import Score
import time

screen = Screen()
screen.title("TURTLE CROSSING GAME")
screen.setup(width=800,height=600)
screen.tracer(0)


timmy = turtle_obj()
screen.listen()
screen.onkeypress(timmy.move_up,"Up")
screen.onkeypress(timmy.move_down,"Down")

car_obj = Car()
levels = Score()

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_obj.manager()
    car_obj.move()
    for new_car in car_obj.car_list:
        if new_car.distance(timmy)<20:
            levels.game_over()
            game_on=False
        if timmy.is_finsih_line():
            timmy.goto_start()
            levels.level_up()
            car_obj.speed_up()


screen.exitonclick()