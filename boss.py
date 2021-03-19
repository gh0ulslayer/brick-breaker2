import config
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
from board import board

colorama.init()

class boss():
    def __init__(self, rows , cols):
        self._start = rows
        self._paddlelen = cols
        self._design = ([[Fore.RED + '@' for col in range(self._paddlelen)]
                       for row in range(2)])

 

    def get_boss(self, i , j):
        return self._design[i][j]
    
    def move_right(self, i ):
        self._start += i

    def move_left(self, i ):
        self._start -= i



    

