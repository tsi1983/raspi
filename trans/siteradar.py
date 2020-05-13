import numpy as np
from datetime import datetime as dt

class siteradar:
    NO_VALUE = float('-inf')
    data = np.zeros(500*500)
    def __init__( self, name="", sitelon=139.5735,sitelat=35.5135,sizex=500, sizey=500, dx=1000,dy=1000,offx=0,offy=0,B=200,beta=1.6, noEcho=False,noOpe=False,data=data):
        self.sitelon = sitelon
        self.sitelat = sitelat
        self.name = name
        self.sizex = sizex
        self.sizey = sizey
        self.dx = dx
        self.dy = dy
        self.offx = offx
        self.offy = offy
        self.B = B
        self.beta = beta
        self.noEcho = noEcho
        self.noOpe = noOpe
        if len(data) != sizex * sizey:
            raise ValueError( " data size must be sizelon * sizelat")
        self.data = data # float nparray [sizex * sizey]
    def getX( self, disX):
        return int( disX / self.dx + self.sizex / 2 - 0.5  + self.offx )
    def getY( self, disY):
        return int(-disY / self.dy + self.sizey / 2 + 0.5  - self.offy )
    def getValue( self, x, y):
        if x>=self.sizex or x < 0:
             return NO_VALUE
        if y>=self.sizey or y < 0:
             return NO_VALUE
        return self.data[y * self.sizex + x]

if __name__ == "__main__":
    sradar = siteradar()
    print(sradar.sizex)
    print(sradar.sizey)
    print( sradar.getX(50000))
    print(np.array( np.zeros(3360), dtype=float))
