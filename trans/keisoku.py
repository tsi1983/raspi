import numpy as np
from siteradar import siteradar
from platecaree import platecaree
from trans_high_speed import convertRadarToPlateCaree
import time

print("start")
start = time.time()

sradar = siteradar()
data = np.array(np.zeros(500*500), dtype = float)
data = np.full(500*500,30.0)
print("length = ",len(data),":",data)
sradar.data = data
data = np.zeros(500 * 500)
gis = platecaree(sizelon=500,sizelat=500,data=data)
convertRadarToPlateCaree(gis, sradar)
print("end")
end = time.time()
ellapssed = end - start
print("ellapssed",ellapssed)
