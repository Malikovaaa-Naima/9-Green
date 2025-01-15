from turtle import *
import random
speed("fast")
colormode(255)

bgcolor('black')
HungryRegal =  200

color ('green')

while HungryRegal > 0:
    left(HungryRegal)
    forward(HungryRegal * 3)
    HungryRegal = HungryRegal-1