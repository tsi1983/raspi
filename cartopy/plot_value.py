import cartopy.crs as ccrs
import matplotlib.pyplot as plt

import xarray as xray
#import xray
import numpy as np
import numpy.random as random
from datetime import datetime

# toy weather data
lon = 136.5 + np.arange(20)*0.25
lat = 38. - np.arange(20)*0.25
time = datetime(2016,1,1,0)
data = random.rand(len(lat), len(lon))*100
rain = xray.DataArray(data, coords={'time': time, 'lat': lat, 'lon': lon}, dims=['lat', 'lon'])

# prepare data for annotation
darray = rain
ylab, xlab = rain.dims
xval = darray[xlab].values
yval = darray[ylab].values
zval = darray.to_masked_array(copy=False)
xval, yval = np.meshgrid(xval, yval)

# for colormap
colorlist = ['#FFFFFF', '#00FFFF', '#00B0FF', '#0070FF', '#228B22', '#00FF00', '#FFFF00', '#FF8000', '#FF0000', '#FF00FF']
levels = [1,3,5,10,20,30,40,50,80]

# plot
plt.figure(figsize=(8,6))
ax = plt.axes(projection=ccrs.PlateCarree())
rain.plot(ax=ax, levels=levels, colors=colorlist, extend='both')
for x, y, val in zip(xval.flat, yval.flat, zval.flat):
    val = '{}'.format(int(val))
    ax.text(x, y, val, ha='center', va='center')
ax.coastlines(resolution='10m')
plt.show()