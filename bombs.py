import config
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random

colorama.init()

class Bombs():
    def __init__(self, rows , cols):
        self._xpos = rows
        self._ypos = cols
        self._catched = 0
        self._left = 0

    def position(self):
        arr = []
        arr.append(Fore.CYAN +'•')
        arr.append(self._xpos)
        arr.append(self._ypos)
        return arr    

    def x_pos(self):
            if(self._xpos < 26):
                self._xpos += 1
            else:
                if(self._catched == 0):
                    self._xpos = 29 
                else:
                    self._xpos = 26 

            return self._xpos 