import numpy as np
import os
import matplotlib.pyplot as ppl
import matplotlib.ticker as mticker
import cartopy.crs as ccrs
from cartopy.mpl.ticker import (LongitudeFormatter, LatitudeFormatter)
from tkinter import filedialog as fd

"""This file contains methods for cleaning and processing .ict and .csv files 
for data analysis and input, as well as plotting flight paths"""

# TODO: Streamline data input of large quantity of files as well as flight plotting
# TODO: Move main to other file

# creates a dictionary of data from a file
# TODO: Include no data values in dict
def readFile(fileIn):
    with open(fileIn, newline="") as file:
        while True:
            title = file.readline()
            # check if we have reached the data
            # note: maybe change this if not all files have lat/longs
            # TODO: make this more universal/modular
            if "Latitude,Longitude" in title:
                break
        title = title.strip().split(",")
        fileData = {}
        for i in title:
            fileData[i] = []
        for line in file:
            line = line.strip().split(",")
            for i, j in enumerate(title):
                fileData[j].append(line[i])
    return fileData


# takes dict data, isolates and cleans lat/long, and plots flight path

def plotFlightMap(dataList):

    # values indicating no data
    noDataVals = [-9999, -8888]

    # meta list of lats/longs of different flights
    lats = []
    longs = []

    # creates nan list of flight locations for a single data dict at a time
    for data in dataList:
        # converts list to numpy array
        latsArray = np.asarray(data["Latitude"], dtype=float)
        longsArray = np.asarray(data["Longitude"], dtype=float)

        # replaces no data vals with nan for clean plot
        for i, j in enumerate(latsArray):
            if j in noDataVals:
                latsArray[i] = np.nan

        for i, j in enumerate(longsArray):
            if j in noDataVals:
                longsArray[i] = np.nan

        # add to meta list
        lats.append(latsArray)
        longs.append(longsArray)

    # plot size and map type (easiest map to implement, no need for excessive accuracy)
    ppl.figure(figsize=(12,7))
    ax = ppl.axes(projection=ccrs.PlateCarree())

    # plot individual flights on the same graph
    for i, j in enumerate(lats):
        ax.plot(longs[i], lats[i])

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True)
    ax.coastlines()
    ax.set_xmargin(0.75)
    ax.set_ymargin(1)
    ppl.show()


def main():

    # finds all files in a directory
    dataPath = fd.askdirectory()
    dataList = os.listdir(dataPath)

    # list of flight paths
    subData = []

    # iterate through files and adds to subData
    for x in range(len(dataList)):
        try:
            subData.append(readFile(dataPath + '/' + dataList[x]))
        except:

            print(dataList[x])

    # plot list of flights together
    plotFlightMap(subData)

if __name__ == '__main__':
    main()