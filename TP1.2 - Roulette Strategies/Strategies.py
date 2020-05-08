# -*- coding: utf-8 -*-

import numpy as np

class Strategies(object):
    # Constructor and Instance Attributes
    def __init__(self, roulette, stratName):
        self.roulette = roulette
        self.modified = ""
        # Number Selection
        if(stratName == "number"):
            num = -1
            while(num < 0 or num > 36):
                num = int(float(input('Please choose a number (from 0 to 36): ')))
            self.number = num
        # Color Selection
        if(stratName in ["color", "martingale", "dalembert", "fibonacci"]):
            color = ""
            while(color != 'red' and color != 'black'):
                color = str(input('Please choose a color ("red" or "black"): '))
            self.color = color
        
        # Martingale Specifications
        if(stratName == "martingale"):
            modified = ""
            while(modified != 'Y' and modified != 'N'):
                modified = str.upper(str(input('There are two types of Martingale. Classic and Modified. The default is Classic. Do you want to change to Modified? (Y/N): ')))
            self.modified = modified
        # Sofovich Specifications
        elif(stratName == "sofovich"):
            notChosenNum_1 = notChosenNum_2 = -1
            while(notChosenNum_1 < 0 or notChosenNum_1 > 36):
                notChosenNum_1 = int(float(input('Choose your NOT chosen number 1: ')))
            while(notChosenNum_2 < 0 or notChosenNum_2 > 36):
                notChosenNum_2 = int(float(input('Choose your NOT chosen number 2: ')))
            self.notChosenNumber1 = notChosenNum_1
            self.notChosenNumber2 = notChosenNum_2
        # santE Specifications
        elif(stratName == "sante"):
            notChosenCol = 0
            while(notChosenCol not in [1, 2, 3]):
                notChosenCol = int(float(input('Please choose your NOT CHOSEN column: (1, 2 or 3): ')))
            self.notChosenColumn = notChosenCol

    # Only Number
    def betToNumber(self):
        capital = self.roulette.getInitCapital()
        betValue = self.roulette.getBetValue()
        fr = 0
        zeroCapital = False
        graphsLimited = {"capital": [capital], "frec": []}
        graphsUnlimited = {"capital": [capital], "frec": []}

        for i in range(1, self.roulette.getGames()):
            capital -= betValue
            rand = np.random.randint(0, len(self.roulette.getNumbers()))
            if(rand == self.number):
                capital += betValue * 36
                fr += 1

            graphsUnlimited["capital"].append(capital)
            graphsUnlimited["frec"].append(fr/i)

            if (capital <= 0):
                zeroCapital = True
            
            if (zeroCapital):
                graphsLimited["capital"].append(0)
                graphsLimited["frec"].append(0)
            else:
                graphsLimited["capital"].append(capital)
                graphsLimited["frec"].append(fr/i)

        print('Final capital: ', capital)
        print("Your total play time would be about: " + str(self.roulette.getGames() * self.roulette.getBetTime() // 60) + " min")
        print()

        # Array conversion
        graphsLimited["capital"] = np.array(graphsLimited["capital"])
        graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
        graphsLimited["frec"] = np.array(graphsLimited["frec"])
        graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

        return graphsLimited, graphsUnlimited

    # Only Color
    def betToColor(self):
        capital = self.roulette.getInitCapital()
        betValue = self.roulette.getBetValue()
        fr = 0
        zeroCapital = False
        graphsLimited = {"capital": [capital], "frec": []}
        graphsUnlimited = {"capital": [capital], "frec": []}

        for i in range(1, self.roulette.getGames()):
            capital -= betValue
            rand = np.random.randint(0, 37)
            color = self.roulette.getNumbers()[rand].color
            if(color == self.color):
                capital += betValue * 2
                fr += 1

            graphsUnlimited["capital"].append(capital)
            graphsUnlimited["frec"].append(fr/i)

            if (capital <= 0):
                zeroCapital = True
            
            if (zeroCapital):
                graphsLimited["capital"].append(0)
                graphsLimited["frec"].append(0)
            else:
                graphsLimited["capital"].append(capital)
                graphsLimited["frec"].append(fr/i)

        print('Final capital: ', capital)
        print("Your total play time would be about: " + str(self.roulette.getGames() * self.roulette.getBetTime() // 60) + " min")
        print()

        # Array conversion
        graphsLimited["capital"] = np.array(graphsLimited["capital"])
        graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
        graphsLimited["frec"] = np.array(graphsLimited["frec"])
        graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

        return graphsLimited, graphsUnlimited

    # Gerardo Sofovich's Strategy
    def betAsSofovich(self):
        capital = self.roulette.getInitCapital()
        betValue = self.roulette.getBetValue()
        fr = 0
        zeroCapital = False
        graphsLimited = {"capital": [capital], "frec": []}
        graphsUnlimited = {"capital": [capital], "frec": []}
        
        for i in range(1, self.roulette.getGames()):
            capital -= (betValue * 35)
            rand = np.random.randint(0, len(self.roulette.getNumbers()))
            
            if(rand != self.notChosenNumber1 and rand != self.notChosenNumber2):
                capital += betValue * 36
                fr += 1
            
            graphsUnlimited["capital"].append(capital)
            graphsUnlimited["frec"].append(fr/i)

            if (capital <= 0):
                zeroCapital = True
            
            if (zeroCapital):
                graphsLimited["capital"].append(0)
                graphsLimited["frec"].append(0)
            else:
                graphsLimited["capital"].append(capital)
                graphsLimited["frec"].append(fr/i)

        print('Final capital: ', capital)
        print("Your total play time would be about: " + str(self.roulette.getGames() * self.roulette.getBetTime() // 60) + " min")
        print()
        
        # Array conversion
        graphsLimited["capital"] = np.array(graphsLimited["capital"])
        graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
        graphsLimited["frec"] = np.array(graphsLimited["frec"])
        graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

        return graphsLimited, graphsUnlimited

    # Classic and Modified Martingale
    def betMartingale(self):
        capital = self.roulette.getInitCapital()
        betValue = self.roulette.getBetValue()
        fr = 0
        zeroCapital = False
        graphsLimited = {"capital": [capital], "frec": []}
        graphsUnlimited = {"capital": [capital], "frec": []}

        for i in range(1, self.roulette.getGames()):   
            capital -= betValue
            rand = np.random.randint(0, 37)
            color = self.roulette.getNumbers()[rand].color
            if(color == self.color):
                capital += betValue * 2
                fr += 1

            # Duplicate previous bet (modified: adds +1 units)
            if(color != self.color):
                if (self.modified == 'Y'):
                    betValue = betValue * 2 + 1
                else:
                    betValue = betValue * 2
            else:
                # Reinitialize betValue to the starting value
                betValue = self.roulette.getBetValue()
            
            graphsUnlimited["capital"].append(capital)
            graphsUnlimited["frec"].append(fr/i)

            if (capital <= 0):
                zeroCapital = True

            if (zeroCapital):
                graphsLimited["capital"].append(0)
                graphsLimited["frec"].append(0)
            else:
                graphsLimited["capital"].append(capital)
                graphsLimited["frec"].append(fr/i)

        print('Final capital: ', capital)
        print("Your total play time would be about: " + str(self.roulette.getGames() * self.roulette.getBetTime() // 60) + " min")
        print()
        
        # Array conversion
        graphsLimited["capital"] = np.array(graphsLimited["capital"])
        graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
        graphsLimited["frec"] = np.array(graphsLimited["frec"])
        graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

        return graphsLimited, graphsUnlimited

    # D'Alembert Strategy
    def betDalembert(self):
        capital = self.roulette.getInitCapital()
        betValue = self.roulette.getBetValue()
        fr = 0
        zeroCapital = False
        graphsLimited = {"capital": [capital], "frec": []}
        graphsUnlimited = {"capital": [capital], "frec": []}

        for i in range(1, self.roulette.getGames()):
            capital -= betValue
            rand = np.random.randint(0, 37)
            color = self.roulette.getNumbers()[rand].color
            if(color == self.color):
                capital += betValue * 2
                fr += 1
                if(betValue > self.roulette.getBetValue()):
                    betValue -= 1
                else:
                    # Reinitialize betValue to the starting value
                    betValue = self.roulette.getBetValue()
            else:
                betValue += 1
            
            graphsUnlimited["capital"].append(capital)
            graphsUnlimited["frec"].append(fr/i)

            if (capital <= 0):
                zeroCapital = True
            
            if (zeroCapital):
                graphsLimited["capital"].append(0)
                graphsLimited["frec"].append(0)
            else:
                graphsLimited["capital"].append(capital)
                graphsLimited["frec"].append(fr/i)

        print('Final capital: ', capital)
        print("Your total play time would be about: " + str(self.roulette.getGames() * self.roulette.getBetTime() // 60) + " min")
        print()
        
        # Array conversion
        graphsLimited["capital"] = np.array(graphsLimited["capital"])
        graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
        graphsLimited["frec"] = np.array(graphsLimited["frec"])
        graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

        return graphsLimited, graphsUnlimited

    # Fibonacci Strategy
    def betFibonacci(self):
        fibonacci = [1, 1]
        capital = self.roulette.getInitCapital()
        betValue = fibonacci[-1]
        zeroCapital = False
        fr = 0
        graphsLimited = {"capital": [capital], "frec": []}
        graphsUnlimited = {"capital": [capital], "frec": []}

        for i in range(1, self.roulette.getGames()):
            capital -= betValue
            rand = np.random.randint(0, 37)
            color = self.roulette.getNumbers()[rand].color
            if(color == self.color):
                capital += betValue * 2
                fr += 1
                if(len(fibonacci) <= 3):
                    # Reset secuence
                    fibonacci = [1, 1]
                else:
                    # Erase last two numbers of the secuence
                    fibonacci.pop()
                    fibonacci.pop()
            else:
                # New number to the secuence
                fibonacci.append(fibonacci[-2] + fibonacci[-1])
            
            # Bet always in Fibonacci Secuence's last position
            betValue = fibonacci[-1]

            graphsUnlimited["capital"].append(capital)
            graphsUnlimited["frec"].append(fr/i)

            if (capital <= 0):
                zeroCapital = True
            
            if (zeroCapital):
                graphsLimited["capital"].append(0)
                graphsLimited["frec"].append(0)
            else:
                graphsLimited["capital"].append(capital)
                graphsLimited["frec"].append(fr/i)

        print('Final capital: ', capital)
        print("Your total play time would be about: " + str(self.roulette.getGames() * self.roulette.getBetTime() // 60) + " min")
        print()
        
        # Array conversion
        graphsLimited["capital"] = np.array(graphsLimited["capital"])
        graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
        graphsLimited["frec"] = np.array(graphsLimited["frec"])
        graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

        return graphsLimited, graphsUnlimited

    # SantE's Strategy (Original)
    def betASSantE(self):
        capital = self.roulette.getInitCapital()
        betValue = self.roulette.getBetValue()
        fr = 0
        zeroCapital = False
        graphsLimited = {"capital": [capital], "frec": []}
        graphsUnlimited = {"capital": [capital], "frec": []}

        for i in range(1, self.roulette.getGames()):
            capital -= betValue * 2 # Two Columns for bet
            rand = np.random.randint(0, 37)
            if(rand == 0):
                # Zero doesn't have any valid column
                column = 0
            else:
                # Column calculation with integer division
                column = ((rand - 1) // 12) + 1
            
            # Winning
            if(column != self.notChosenColumn):
                capital += betValue * 3
                fr += 1

            if(column == self.notChosenColumn):
                # Duplicate previous bet
                betValue = betValue * 2
            else:
                # Reinitialize betValue to the starting value
                betValue = self.roulette.getBetValue()

            graphsUnlimited["capital"].append(capital)
            graphsUnlimited["frec"].append(fr/i)

            if (capital <= 0):
                zeroCapital = True
            
            if (zeroCapital):
                graphsLimited["capital"].append(0)
                graphsLimited["frec"].append(0)
            else:
                graphsLimited["capital"].append(capital)
                graphsLimited["frec"].append(fr/i)

        print('Final capital: ', capital)
        print("Your total play time would be about: " + str(self.roulette.getGames() * self.roulette.getBetTime() // 60) + " min")
        print()
        
        # Array conversion
        graphsLimited["capital"] = np.array(graphsLimited["capital"])
        graphsUnlimited["capital"] = np.array(graphsUnlimited["capital"])
        graphsLimited["frec"] = np.array(graphsLimited["frec"])
        graphsUnlimited["frec"] = np.array(graphsUnlimited["frec"])

        return graphsLimited, graphsUnlimited

    # Getters and Setters (Only the ones that we could use)
    def getModified(self):
        return self.modified

    def setModified(self, modified):
        self.modified = modified
    