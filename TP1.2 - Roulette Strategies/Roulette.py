# -*- coding: utf-8 -*-

import numpy as np
import random
from RouletteNumber import RouletteNumber


class Roulette(object):

    # Constructor and Instance Attributes
    def __init__(self):
        self.numbers = np.zeros(37, dtype=RouletteNumber)

        # Roulette's numbers initialization
        self.numbers[0] = RouletteNumber(0, 'green')
        for i in range(1, len(self.numbers), 2):
            if (i <= 10):
                self.numbers[i] = RouletteNumber(i, 'red')
                self.numbers[i+1] = RouletteNumber(i+1, 'black')
            elif (i <= 18):
                self.numbers[i] = RouletteNumber(i, 'black')
                self.numbers[i+1] = RouletteNumber(i+1, 'red')
            elif (i <= 28):
                self.numbers[i] = RouletteNumber(i, 'red')
                self.numbers[i+1] = RouletteNumber(i+1, 'black')
            else:
                self.numbers[i] = RouletteNumber(i, 'black')
                self.numbers[i+1] = RouletteNumber(i+1, 'red')

    # Player parameters
    def configurePlayer(self):
        self.GAMES = int(float(input('How many games do you want to play?: ')))
        self.INITCAPITAL = int(float(input('Define your initial capital: ')))
        self.BETVALUE = int(float(input('Bet Value?: ')))
        self.BETTIME = 180 # average of 3 minutes for the bet time and spinning

    # Getters and Setters
    def getNumbers(self):
        return self.numbers

    def setNumbers(self, numbers):
        self.numbers = numbers

    def getGames(self):
        return self.GAMES
    
    def setGames(self, games):
        self.GAMES =  games

    def getInitCapital(self):
        return self.INITCAPITAL
    
    def setInitCapital(self, initC):
        self.INITCAPITAL = initC
    
    def getBetValue(self):
        return self.BETVALUE

    def setBetValue(self,betV):
        self.BETVALUE = betV

    def getBetTime(self):
        return self.BETTIME

    def setBetTime(self,betT):
        self.BETTIME = betT
