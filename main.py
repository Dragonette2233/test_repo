import sys
import os
from abc import ABC

class Warrior(ABC):
    def __init__(self):
        self.type = 'ancient'

    def roar(self):
        print(f'in warrior class: {self.type}')

class Viking(Warrior):
    def __init__(self) -> None:
        self.type = 'ancient_child'
        self.name = 'Unknown viking'
    
    def roar(self):
        super().roar()
        print('In VIking class')

    def kill(self):
        raise AttributeError()


new_warrior = Viking()
new_warrior.roar()
new_warrior.kill()