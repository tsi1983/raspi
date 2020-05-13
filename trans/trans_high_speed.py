import numpy as np
from numpy import deg2rad
from siteradar import siteradar
from platecaree import platecaree

WGS84_A    = 6378137.000
WGS84_E2   = 0.00669437999019758
WGS84_MNUM = 6335439.32729246

def convertRadarToPlateCaree( destgis:platecaree ,jmaxy:siteradar):
    latSize = destgis.sizelat
    lonSize = destgis.sizelon
    my = np.array( np.zeros(latSize), dtype=float) # new double[ latSize]
    dx = np.array( np.zeros(lonSize), dtype=float) # new double[ lonSize]
    dy = np.array( np.zeros(latSize), dtype=float) # new double[ latSize]
    dlon     = destgis.dlon 
    dlat     = destgis.dlat 
    dlonhalf = destgis.dlon / 2 
    dlathalf = destgis.dlat / 2 
    westlon  = destgis.wlon  
    northlat = destgis.nlat 
    for i in range(0, lonSize):
        lon1 = westlon + dlon * i  + dlonhalf 
        dx[i]=deg2rad( lon1 - jmaxy.sitelon )
    for i in range(0, latSize):
        lat1 = (northlat) - dlat * i + dlathalf
        my[i]=deg2rad(( lat1 + jmaxy.sitelat)/2)
        dy[i]=deg2rad(  lat1 - jmaxy.sitelat   )
    sizex = jmaxy.sizex
    sizey = jmaxy.sizey
    destgisdata = destgis.data
    for latint in range(0, latSize):
        sin = np.sin(my[ latint]) 
        w   = np.sqrt(1.0 - WGS84_E2 * sin * sin)
        m   = WGS84_MNUM / (w * w * w) 
        n   = WGS84_A / w 
        dym = dy[ latint] * m 
        for lonint in range(0, lonSize):
            dxncos = dx[ lonint] * n * np.cos(my[ latint])
            x = jmaxy.getX( dxncos) 
            y = jmaxy.getY( dym   ) 
            if (x < 0 or x >= sizex or y < 0 or y >= sizey):
                continue 
            destgisdata[ latint * lonSize + lonint] = jmaxy.getValue(x,y)

if __name__ == "__main__":
    sradar = siteradar()
    data = np.array(np.zeros(500*500), dtype = float)
    data = np.full(500*500,30.0)
    print("length = ",len(data),":",data)
    sradar.data = data
    data = np.zeros(500 * 500)
    gis = platecaree(sizelon=500,sizelat=500,data=data)
    print("start")
    convertRadarToPlateCaree(gis, sradar)
    print("end")
