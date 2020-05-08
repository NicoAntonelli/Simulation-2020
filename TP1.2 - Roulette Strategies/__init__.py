# -*- coding: utf-8 -*-

'''
UTN FRRO - Simulation 2020
TP1.2 - Roulette: Economic and Mathematical Analysis

Authors: Joshua Acciarri (44823) & Nicolás Antonelli (44852)
Professor: Torres, Juan
Final Date: 01/05/2020

Python Libraries/Modules Used:
    - Numpy: Random Numbers and Array Manipulation
    - Pyplot: Matplotlib Module for Graph Plotting

Classes/Other Files:
    -RouletteNumber: Object with a value from 0 to 36, and a color
    -Roulette: Object (European Roulette) that contains 37 RouletteNumbers and Strategy methods
    -Strategies: Object with the configurations and definitions of all strategies we use
    -Graphing: File with common Plotting functions and the complete saving route
'''

from Roulette import Roulette
from Strategies import Strategies
from graphing import letsGraph
import matplotlib.pyplot as plt

# Global Configs
save = {"mode": True, "route": "graphs/" } # If mode is False, the graph won't be sabed


# Main
if __name__ == '__main__':
    roulette = Roulette()
    opt = -1
    while (opt != 0):
        # Menu
        print('ROULETTE SIMULATOR')
        print('Welcome. Do you want to play?')
        print()
        inputMsg = 'Please choose a strategy: (number from 1 to 8)\n'
        inputMsg += '1: Bet to a single number\n2: Bet to a color\n3: Bet AS Sofovich\n4: Bet Martingale (Classic and Modified)\n'
        inputMsg += '5: Bet D\'Alambert\n6: Bet Fibonacci (Bet fixed to 1)\n7: Bet AS SantE (Original Strategy)\n8: Don\'t Play \n\n0: Exit Game\n'
        while(opt not in [0, 1, 2, 3, 4, 5, 6, 7, 8]):
            opt = int(float(input(inputMsg)))
        print()

        # Exit Game
        if (opt == 0):
            print('Good Bye!\n')
            exit()
        elif (opt == 8):
            print('You made the best choice and didn\'t play\n')
            exit()
    
        # Roulette Settings
        roulette.configurePlayer()

        # Strategy Name selection from a Strategies' Names array
        allStrategies = ["exit", "number", "color", "sofovich", "martingale", "dalembert", "fibonacci", "sante", "noplay"]
        stratName = allStrategies[opt]
    
        # Configuring strategy parameters
        strat = Strategies(roulette, stratName)
        print()

        # Arrays for multiple Game Results (Recommended: 5 to 10)
        results = 6
        resultsLimited = []
        resultsUnlimited = []

        # Simulating the Strategy
        for i in range(results):
            if (opt == 1): graphsLim, graphsUnlim = strat.betToNumber() 
            elif (opt == 2):
                graphsLim, graphsUnlim = strat.betToColor()
            elif (opt == 3):
                graphsLim, graphsUnlim = strat.betAsSofovich()
            elif (opt == 4):
                graphsLim, graphsUnlim = strat.betMartingale()
            elif (opt == 5):
                graphsLim, graphsUnlim = strat.betDalembert()
            elif (opt == 6):
                graphsLim, graphsUnlim = strat.betFibonacci()
            elif (opt == 7):
                graphsLim, graphsUnlim = strat.betASSantE()
            else:
                print('Good Bye!\n')
                exit()

            # Adding current results to the array of results
            resultsLimited.append(graphsLim)
            resultsUnlimited.append(graphsUnlim)
    
        # Call graphing's function for the first game results
        info = {"title": "Roulette Strategy Analysis, one result game", "type": "one_result", "strategy": stratName, "modified": strat.getModified()}
        letsGraph(resultsLimited[0], resultsUnlimited[0], roulette, info, save)

        # Averages Calculation
        graphsLim["capital"]   = (resultsLimited[0]["capital"]   + resultsLimited[1]["capital"]   + resultsLimited[2]["capital"]   + resultsLimited[3]["capital"]   + resultsLimited[4]["capital"]   + resultsLimited[5]["capital"])   / results
        graphsUnlim["capital"] = (resultsUnlimited[0]["capital"] + resultsUnlimited[1]["capital"] + resultsUnlimited[2]["capital"] + resultsUnlimited[3]["capital"] + resultsUnlimited[4]["capital"] + resultsUnlimited[5]["capital"]) / results
        graphsLim["frec"]      = (resultsLimited[0]["frec"]      + resultsLimited[1]["frec"]      + resultsLimited[2]["frec"]      + resultsLimited[3]["frec"]      + resultsLimited[4]["frec"]      + resultsLimited[5]["frec"])      / results
        graphsUnlim["frec"]    = (resultsUnlimited[0]["frec"]    + resultsUnlimited[1]["frec"]    + resultsUnlimited[2]["frec"]    + resultsUnlimited[3]["frec"]    + resultsUnlimited[4]["frec"]    + resultsUnlimited[5]["frec"])    / results

        # Call graphing's function for every game result
        info = {"title": "Roulette Strategy Analysis, all results games", "type": "all_results_average", "strategy": stratName, "modified": strat.getModified()}
        letsGraph(graphsLim, graphsUnlim, roulette, info, save)

        # Visualize all the graphics
        plt.show()
        
        # Default Strat to -1 for re-start game simulator correctly
        opt = -1
