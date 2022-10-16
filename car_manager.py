from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.car_list = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            temp_car = Turtle("square")
            temp_car.shapesize(stretch_wid=1, stretch_len=2)
            temp_car.penup()
            temp_car.color(random.choice(COLORS))
            #set its random position on y coordinate
            temp_car.setpos(300, random.randint(-280, 280))
            self.car_list.append(temp_car)


    def move_car(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)


    def detect_collision(self, player):

        for car in self.car_list:
            if player.distance(car) < 30:
                return True












