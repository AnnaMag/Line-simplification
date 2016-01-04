#! /usr/bin/env python
"""
Created on Mon Jan 4 2016
Anna M. Kedzierska
"""
from matplotlib import pyplot
from shapely.geometry import LineString
from descartes.patch import PolygonPatch

BLUE = '#6699cc'
GRAY = '#999999'

def plot_lines(ax,ob1,ob2):
     x1, y1 = ob1.xy
     x2, y2 = ob2.xy
     ax.plot(x1, y1, 'r^--',x2,y2, 'bs-' ,solid_capstyle='round', zorder=1, linewidth=1.5)

def lines_multiplot(list_in, list_out):
    line_in = LineString(list_in)
    line_out = LineString(list_out)

    fig = pyplot.figure(1, figsize=(10, 4), dpi=140)

    # 1
    ax = fig.add_subplot(111)
    plot_lines(ax, line_in,line_out)
    dilated = line_in.buffer(0.01)
    patch1 = PolygonPatch(dilated, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
    ax.add_patch(patch1)
    ax.tick_params(direction='out', length=2, width=0.8, pad = 0.05)

    #make some space around the plots
    start, end = ax.get_xlim()
    xrange = [start-0.005, end+0.005]
    ax.set_xlim(*xrange)
    start, end = ax.get_ylim()
    print(start, end)
    yrange = [start-0.005, end+0.005]

    ax.set_ylim(*yrange)
    ax.set_aspect(1)

    pyplot.show()
