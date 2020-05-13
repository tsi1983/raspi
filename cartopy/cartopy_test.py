
#!python
# coding: UTF-8

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature #県境・川

#都道府県着色---
import cartopy.io.shapereader as shapereader
import itertools

# tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Natural Earthから州データセットを取得する
shpfilename = shapereader.natural_earth(resolution='10m',
                                        category='cultural',
                                        name='admin_1_states_provinces')

# get shapefile records
reader = shapereader.Reader(shpfilename)
provinces = reader.records()

# 日本の国をフィルタリングする
provinces_of_japan = itertools.ifilter(lambda province: province.attributes['admin'] == 'Japan', provinces)

# plot
colors = itertools.cycle(['red', 'blue', 'green', 'lime', 'orange', 'cyan', 'purple','gray','yellow','violet','magenta'])
#都道府県着色---

fig = plt.figure(figsize=[5,5])

states_10m  = cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces_lines', '10m', #県境
                                           edgecolor='gray',
                                           facecolor='none')  # no filled color
## 10m resolution
ax1 = plt.axes(projection=ccrs.PlateCarree())
ax1.coastlines(resolution='10m')

#都道府県着色---
for province in provinces_of_japan:
    geometry = province.geometry
    ax1.add_geometries(geometry, ccrs.PlateCarree(), facecolor=next(colors))
#都道府県着色---

ax1.set_extent([120,150,20,50], ccrs.PlateCarree())
ax1.add_feature(states_10m) #県境
ax1.set_title('10m coastline')

# plt.show()

# When windows is closed.
def _destroyWindow():
    root.quit()
    root.destroy()

# Tkinter Class
root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)  # When you close the tkinter window.

# Canvas
canvas = FigureCanvasTkAgg(fig, master=root)  # Generate canvas instance, Embedding fig in root
canvas.draw()
canvas.get_tk_widget().pack()
#canvas._tkcanvas.pack()

# root
root.update()
root.deiconify()
root.mainloop()
