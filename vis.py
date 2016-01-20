%matplotlib inline
from osgeo import gdal
import matplotlib.pyplot as plt

# Open image
dsll = gdal.Open("ouput/ndwi_ll.tif")

# Read raster data
ndwi = dsll.ReadAsArray(0, 0, dsll.RasterXSize, dsll.RasterYSize)

# Now plot the raster data using gist_earth palette
plt.imshow(ndwi, interpolation='nearest', vmin=0, cmap=plt.cm.gist_earth)
plt.show()

dsll = None
