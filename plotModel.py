import plotly.express as px
import pandas as pd


class Plot():

    def __init__(self, dfResult, a, b, gridInfo):
       self.modelDf = dfResult
       self.a = a
       self.b = b
       self.gridInfo = gridInfo

    def print_title(self):

        start = str(self.gridInfo[0])
        end = str(self.gridInfo[1])
        step = str(self.gridInfo[2])

        return "Linear function ( y = " + str(self.a) + "x + " + str(self.b) + ") from: "+ start + "up untill to: " + end + "with a step of: " + step


    def plot(self):
        fig = px.scatter(self.modelDf, x="x", y="y", trendline="ols")
        return fig