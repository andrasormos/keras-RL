from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





# LOAD DATA
dateParse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %I-%p")
df = pd.read_csv("Gdax_BTCUSD_1h_close.csv", parse_dates=["Date"], date_parser=dateParse, index_col=0)


dataSize = len(df.index)
initialTimeRange = 84               # How long the game should go on
gameLength = 84                     # How many data increment should be shown as history. Could be hours, month
print("Data Size:", dataSize)

def randomChart():

    startIndex = randint((initialTimeRange + gameLength), (dataSize-1))  # self.initialTimeRange # self.dataSize
    endIndex = startIndex - initialTimeRange

    print("Random Chart:", startIndex, " - ", endIndex)
    startDate = df.index[startIndex]
    endDate = df.index[endIndex]


    startDateStr = startDate.strftime("%Y-%m-%d %H:%M:%S")
    endDateStr = endDate.strftime("%Y-%m-%d %H:%M:%S")

    return startDateStr, endDateStr, startIndex, endIndex



startDateStr, endDateStr, startIndex, endIndex = randomChart()


print("\n")
print(startDateStr, "-", endDateStr)

  # 9441