'''
Created on 2019/08/09

@author: Takanori Sakanashi
'''
#import numpy as np

class Meta(object):
    nx = None
    ny = None
    wlon = None
    nlat = None
    dlon = None
    dlat = None
    def __init__(self, nx=nx,ny=ny,wlon=wlon,nlat=nlat,dlon=dlon,dlat=dlat):
        self.nx = int(nx)
        self.ny = int(ny)
        self.wlon = float(wlon)
        self.nlat = float(nlat)
        self.dlon = float(dlon)
        self.dlat = float(dlat)

class GPVData(object):
    wlon = 118.0
    nlat = 48.0
    dlon = 0.012500000
    dlat = 0.008333333

    nx = 2560
    ny = 3360
    meta = None
    data = None # numpy array
    def __init__(self, meta=meta, data=data):
        self.meta = meta
        self.nx = int(self.meta.nx)
        self.ny = int(self.meta.ny)
        self.wlon = float(self.meta.wlon)
        self.nlat = float(self.meta.nlat)
        self.dlon = float(self.meta.dlon)
        self.dlat = float(self.meta.dlat)
        self.data = data.reshape( self.ny, self.nx)

    def get_value(self, lat, lon):
        px = (lon - self.wlon) / self.dlon # lon
        py = (self.nlat - lat) / self.dlat # lat
        x0 = int(px - 0.5)
        y0 = int(py - 0.5)
        return(self.data[y0,x0])
    def get_pointdata_dict(self, latloncsvList):
        dict={}
        for latlon in latloncsvList:
            lat = float( latlon.split(",")[0])
            lon = float( latlon.split(",")[1])
            dict[latlon] = self.get_value(lat, lon)
        return dict
    def get_gpv(self):
        '''
        return numpy array [y,x]
        '''
        return self.data

class MetaRd(object):
    metastr = ""
    metadict = {}
    def __init__(self, metastr):
        self.metastr = metastr
        metalist = metastr.replace("\r\n","\n").split("\n")
        for meta in metalist:
            if len(meta) < 1:
                continue
            if str(meta).startswith("=") or str(meta).index(",") < 1:
                continue
            strs = meta.split(",")
            self.metadict[strs[0]] = strs[1].replace(" " ,"")
    def get_value(self, element):
        return self.metadict[element]
    def get_number_of_x_grids(self):
        return self.get_value("number of x grids")
    def get_number_of_y_grids(self):
        return self.get_value("number of y grids")
    def get_base_point_x(self):
        return self.get_value("base point x")
    def get_base_point_y(self):
        return self.get_value("base point y")
    def get_base_point_lat(self):
        return self.get_value("base point lat")
    def get_base_point_lon(self):
        return self.get_value("base point lon")
    def get_grid_interval_x(self):
        return self.get_value("grid interval x")
    def get_grid_interval_y(self):
        return self.get_value("grid interval y")
    def getMeta(self):
        nx = self.get_number_of_x_grids()
        ny = self.get_number_of_y_grids()
        wlon = self.get_base_point_lon()
        nlat = self.get_base_point_lat()
        dlon = self.get_grid_interval_x()
        dlat = self.get_grid_interval_y()
        meta = Meta(nx=nx,ny=ny,wlon=wlon,nlat=nlat,dlon=dlon,dlat=dlat)
        return meta


