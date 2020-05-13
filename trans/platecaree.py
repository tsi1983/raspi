import numpy as np
class platecaree:
    data = np.zeros(2560*3360)
    def __init__( self, wlon=118,elon=150, 
        nlat=48.0, slat=20.0, sizelon=2560, sizelat=3360, data=data):
        self.wlon = wlon
        self.elon = elon
        self.nlat = nlat
        self.slat = slat
        self.sizelon = sizelon
        self.sizelat = sizelat
        self.dlat = (nlat - slat) / sizelat
        self.dlon = (elon - wlon) / sizelon 
        if len(data) != self.sizelon * self.sizelat:
            raise ValueError( " data size must be sizelon * sizelat")
        self.data = data

if __name__ == "__main__":
    map = platecaree()
    print(map.sizelat)
    print(map.sizelon)

