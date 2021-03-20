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
        self._design = [['|','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','|'],
        ['|','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','=','|'],
        ['\\','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','/']] 
        

        self._health = 10
 

    def get_boss(self, i , j):
        return (self._design[i][j] + Fore.CYAN)
    
    def move_right(self, i ):
        self._start += i

    def move_left(self, i ):
        self._start -= i

    def reduce_health(self):
        self._health -= 1

class bombdrop():
    def __init__(self, rows , cols):
        self._xpos = rows
        self._ypos = cols
        self._catched = 0
        self._design = [['|','=','=','=','=','=','=','=','=','|'],['|','=','=','=','=','=','=','=','=','|'],['\\','-','-','-','-','-','-','-','-','/']]
        
        
    def x_pos(self):
        if(self._xpos < 26):
            self._xpos += 1
        else:
            if(self._catched == 0):
                self._xpos = 29 
            else:
                self._xpos = 26 

        return self._xpos 
