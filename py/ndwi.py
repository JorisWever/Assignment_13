## Geo-Scripting WUR
## Erwin van den Berg, Joris Wever
## 20-Jan-2016

from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly, GDT_Float32
import numpy as np

def NDWI(band4Arr, band5Arr, dataSource_band4):

    # create a mask
    mask = np.greater(band4Arr+band5Arr,0)

    # set np.errstate to avoid warning of invalid values (i.e. NaN values) in the divide 
    with np.errstate(invalid='ignore'):
        ndwi = np.choose(mask,(-99,(band4Arr-band5Arr)/(band4Arr+band5Arr)))
    print "NDWI min and max values", ndwi.min(), ndwi.max()
    print "Check the real minimum value"
    print ndwi[ndwi>-99].min()

    # write the result to disk
    driver = gdal.GetDriverByName('GTiff')
    outDataSet=driver.Create('output/ndwi.tif', dataSource_band4.RasterXSize, dataSource_band4.RasterYSize, 1, GDT_Float32)
    outBand = outDataSet.GetRasterBand(1)
    outBand.WriteArray(ndwi,0,0)
    outBand.SetNoDataValue(-99)

    # set the projection and extent information of the dataset
    outDataSet.SetProjection(dataSource_band4.GetProjection())
    outDataSet.SetGeoTransform(dataSource_band4.GetGeoTransform())

    # finally let's save it... or like in the OGR example flush it
    outBand.FlushCache()
    outDataSet.FlushCache()
    print "NDWI written to a tif file: 'output/ndwi.tif'"
    return None
