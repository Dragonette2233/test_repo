import sys
import os
from abc import ABC

class CutstomExc(Exception): ...

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

def main():
    raise CutstomExc()

if __name__ == '__main__': main()

