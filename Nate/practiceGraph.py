import numpy as np
import os
import matplotlib.pyplot as ppl
import cartopy
import cartopy.crs as ccrs
"""
This is a practice program to read and clean data from an .ict file, convert it into a single .csv file
and plot flight paths
"""

# all .ict files will be stored in the same directory
dataPath = "../Data/Raw/"
dataList = os.listdir(dataPath)

# list of values that indicate no data
# TODO: learn this from file
noDataVals = [-9999, -8888]

# creates a dictionary of data from a file
def readFile(fileName):
    with open(dataPath + fileName, newline="") as file:
        while True:
            title = file.readline()

            # check if we have reached the data
            # note: maybe change this if not all files have lat/longs
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

                # this doesn't work :(
                #if line[i] in noDataVals:
                #    fileData[j].append(np.nan)
                #else:
                #    fileData[j].append(line[i])
    return fileData

# takes dict data, isolates and cleans lat/long, and plots flight path
# currently only works for a single file dict, can change params to take
# multiple dicts/data to plot multiple flights
def plotFlightMap(data):

    # converts list to numpy array
    latsArray = np.asarray(data["Latitude"], dtype=float)
    longsArray = np.asarray(data["Longitude"], dtype=float)

    # replaces no data vals with nan for clean plot
    for i,j in enumerate(latsArray):
        if j in noDataVals:
            latsArray[i] = np.nan

    for i,j in enumerate(longsArray):
        if j in noDataVals:
            longsArray[i] = np.nan

    ppl.figure(figsize=(12,7))
    ax = ppl.axes(projection=ccrs.PlateCarree())
    ax.plot(longsArray, latsArray)
    ax.gridlines(draw_labels=True)
    ax.coastlines()
    ax.set_xmargin(0.75)
    ax.set_ymargin(1)
    ppl.show()

def main():
    data = readFile("FIREXAQ-MetNav_DC8_20190905_R0.ict")
    plotFlightMap(data)

if __name__ == '__main__':
    main()