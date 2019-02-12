# -*- coding: utf-8 -*-
"""
Created on Fri May 25 08:42:31 2018

@author: Niccolo` Tubini, Giovanna Dalpiaz Riccardo Rigon
@license: creative commons 4.0
"""

import pandas as pd
import numpy as np

import rasterio
import rasterio.plot as rsplot

import shapefile as shp

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

from mpl_toolkits.axes_grid1 import make_axes_locatable

import datetime as datetime

from netCDF4 import Dataset

labelSize = 20
titleSize = 20
legendSize = 18
axisTicksSize = 18

lineWidth = 3
lineStyle =''

markerSize = 3
markerType = 'o'

figureSizeHeigth = 12
figureSizeWidth = 10


def openRasterAsNpArray(fileName, noValue):
    """
    Read raster map .asc
    
    :param str fileName: The name of the file including extension
    :param int noValues: Map no values to set to Nan
    :param boolean info: Print a concise summary of a DataFrame
    :param boolean head: Print the first 5 rows
    :return: raster map
    :rtype: array
    """
    
    with rasterio.open(fileName) as src: 
        rasterMap=src.read(1)
    rasterMap=np.asfarray(rasterMap)
    rasterMap[rasterMap <= noValue]='NAN'
    
    return rasterMap

    
    
def plotRaster(rasterMap, colorMap, title, bartitle):
    """
    plot raster map 
    
    :param str rasterMap: The variable containing the raster map (numpy array)
    :param str colorMap: The name of the color map
    :param str title: The title of the figure
    """
    fig,ax=plt.subplots(figsize=(figureSizeHeigth,figureSizeWidth))
    ax.imshow(rasterMap,cmap=colorMap)
    ax.set_aspect(1)
    #ax.set_axis_off()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="4%", pad=0.2)
    ax.set_title(title,fontsize=titleSize)
    cbar=plt.colorbar(ax.imshow(rasterMap,cmap=colorMap),cax=cax)
    cbar.set_label(bartitle, rotation=270)
    cbar.ax.get_yaxis().labelpad = 15
    plt.show()
    
    return
    
    
    
def plotMap(RasterList, ColormapList, Alpha,ShpList, ShpColors, labels, title):
    """
    plot map (rasters and shpefiles)    
    :param str RasterList: The variable containing the list of raster map
    :param str ColormapList: The name of the list of color maps
    :param str Alpha: The name of the list of transparencies 
    :param str ShpList: The variable containing the list of shapefile to plot
    :param str ShpColors: The name of the list of colors
    :param str labels: The name of the list of labels
    :param str title: The title of the figure
    """
        
    fig,ax=plt.subplots(figsize=(figureSizeHeigth,figureSizeWidth))    
    ax.set_aspect(1)
    ax.set(xlabel = "Latitude",ylabel="Longitude")
    ax.set_title(title,fontsize=titleSize)
    
    # plotting rasters (if any)
    if len(RasterList) > 0:
        index = 0;
        while index < len(RasterList):
            rasterio.plot.show((RasterList[index], 1),ax=ax, cmap=ColormapList[index],alpha=Alpha[index])
            #rsplot.show(RasterList[index],ax=ax, cmap=ColormapList[index],alpha=Alpha[index])
            index += 1
            
    # plotting shapefiles (if any)
    if len(ShpList) > 0:
        index = 0;
        while index < len(ShpList):
            if ShpList[index].geom_type[1] == 'LineString':
                ShpList[index].plot(ax=ax,facecolor='none',edgecolor=ShpColors[index],label=labels[index])
            if ShpList[index].geom_type[1] == 'Point':
                ShpList[index].plot(ax=ax,facecolor=ShpColors[index],edgecolor="black",label=labels[index])
            index += 1
    
    plt.legend()
    plt.show()
    
    return