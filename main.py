## Geo-Scripting WUR
## Erwin van den Berg, Joris Wever
## 20-Jan-2016
## Lesson 13
## Exercise: NDWI and reprojection in pythonRaster handling with Python

# -*- coding: utf-8 -*-

# import modules
from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
import numpy as np
from py.ndwi import NDWI # function to calculate NDWI and write to file

# Initialize variables
fileArray = []
dataArray = []
bandArray = []

for i in range(4,6):
    
    # Open data
    index = i-4
    fileArray.append('data/LC81980242014260LGN00_sr_band' + str(i) + '.tif')   
    dataArray.append(gdal.Open(fileArray[index], GA_ReadOnly))

    # View Information 
    print '-------------------\nINFORMATION ABOUT "' + fileArray[index] + '"\n-------------------'
    print "Driver: ", dataArray[index].GetDriver().ShortName,"/", \
         dataArray[index].GetDriver().LongName
    print "Size is ",dataArray[index].RasterXSize,"x",dataArray[index].RasterYSize, \
          'x',dataArray[index].RasterCount
    print '\nProjection is: ', dataArray[index].GetProjection()
    print "\nInformation about the location of the image and the pixel size:"
    geotransform = dataArray[index].GetGeoTransform()
    if not geotransform is None:
        print 'Origin = (',geotransform[0], ',',geotransform[3],')'
        print 'Pixel Size = (',geotransform[1], ',',geotransform[5],')'
    print '-------------------\nEND OF INFORMATION\n-------------------\n'

    # Read data
    bandArray.append(dataArray[index].ReadAsArray(0,0,dataArray[index].RasterXSize, dataArray[index].RasterYSize))
    bandArray[index] = bandArray[index].astype(np.float32)
    
# function to calculate NDWI and write to file (*.tif i.e. Geotif file)
NDWI(bandArray[0], bandArray[1], dataArray[0])





