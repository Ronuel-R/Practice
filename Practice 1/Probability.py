import math
import random
from fractions import Fraction
class Probability:
    all = []
    def __init__(self, x,y,z,result=0):
        self.x = red
        self.y = blue
        self.z = green
        self.result = result
        Probability.all.append(self)
    def __repr__(self):
        return f"{self.result}"'\n'

class balls_probability(Probability):
    def calculate(self):
        total_ball = red + blue + green
        total_ball_base = red + blue + green
        red1 = random.randint(0,red)
        total_ball1 = total_ball - red1
        blue1 = random.randint(0,blue)
        total_ball2 = total_ball1 - green
        green1 = random.randint(0,green)
        total = red1 + blue1 + green1
        prob_red = Fraction(red,total_ball_base)
        prob_blue = Fraction(blue,total_ball_base)
        prob_green = Fraction(green,total_ball_base)
        self.result = 'Number of red ball: '+str(int(red1)),'Number of green ball: '+str(int(blue1)),'Number of blue ball: '+str(int(green1)),'Total number of balls drawn: '+str(int(total))+'/'+str(int(total_ball))+' Probability of drawing red: '+str(prob_red)+' Probability of drawing blue: '+str(prob_blue)+' Probability of drawing green: '+str(prob_green)

while True:
    print("Press 1 to start")
    calc = int(input("Type Here: "))

    if calc == 1:
        print("How many balls for red?")
        red = int(input("Type Here: "))
        print("How many balls for blue?")
        blue = int(input("Type Here: "))
        print("How many balls for green?")
        green = int(input("Type Here: "))
        compute = balls_probability(red,green,blue)
        compute.calculate()
        print(balls_probability.all)


    check = input("Do you want to calculate again? Y or N: ")
    if check.upper() == "Y":
        continue
    elif check.upper() == "N":
        print("Bye...")
        break