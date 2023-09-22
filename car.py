from turtle import Turtle,Screen
import random
color = ["red","green","black","purple","blue","yellow"]
INITIAL_SPEED=5
MOVE_INCREMENT=5
class Car:

    def __init__(self):
      self.car_list=[]
      self.speed=INITIAL_SPEED
    def manager(self):
        if random.randint(1,6)==1:
            car_obj = Turtle("square")
            car_obj.shapesize(stretch_len=2,stretch_wid=1)
            car_obj.color(random.choice(color))
            car_obj.penup()
            car_obj.goto(420,random.randrange(-250,250))
            self.car_list.append(car_obj)

    def move(self):
        for cars in self.car_list:
            cars.backward(self.speed)

    def speed_up(self):
        self.speed+=MOVE_INCREMENT


