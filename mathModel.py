import pandas as pd
import numpy as np

'''
Generate LinearFunction (y = ax + b)
:parameter
    :param b: num - intercept
    :param a: num - slope 
    :param gridInfo: list - n - [Start End Steps], includes end number
:return
    pd dataframe: column 1: x, column 2: y
'''
def linearFunction(b=0.0, a= 1.0, gridInfo = [0, 10, 1]):
    ## Create grid based on GridInfo
    grid = np.arange(gridInfo[0], gridInfo[1]+1, gridInfo[2])
    y = np.add(np.multiply(grid, a), b)

    dfResult = pd.DataFrame({'x':grid, 'y':y})

    return dfResult


