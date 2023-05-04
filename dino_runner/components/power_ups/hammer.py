import pygame
from dino_runner.components.power_ups.power_upH import PowerUpH
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hammer(PowerUpH):
    def __init__(self):
         super().__init__(HAMMER, HAMMER_TYPE)