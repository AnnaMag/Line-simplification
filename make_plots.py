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

def lines_multiplot(list_in, list_out, out_name):
    line_in = LineString(list_in)
    line_out = LineString(list_out)

    fig = pyplot.figure(1, figsize=(10, 4), dpi=140)
    fig.suptitle('Results of the Douglas-Peucker algorithm', fontsize=14, fontweight='bold')
    ax = fig.add_subplot(111)

    x1, y1 = line_in.xy
    x2, y2 = line_out.xy
    ax.plot(x1, y1, 'r^--',x2,y2, 'bs-' ,solid_capstyle='round', zorder=1, linewidth=1.5)
    ax.legend(['original route','simplified route'], loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=2)

    dilated = line_in.buffer(0.005)
    patch1 = PolygonPatch(dilated, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
    ax.add_patch(patch1)

    ax.tick_params(direction='out', length=2, width=0.8, pad = 0.05)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

    #make some space around the plots
    start, end = ax.get_xlim()
    xrange = [start-0.005, end+0.005]
    ax.set_xlim(*xrange)
    ax.xaxis.set_tick_params(labelsize=8)

    start, end = ax.get_ylim()
    yrange = [start-0.005, end+0.005]
    ax.set_ylim(*yrange)
    ax.set_aspect(1)
    ax.yaxis.set_tick_params(labelsize=8)

    #pyplot.show()
    fig.savefig(str(out_name)+'.png')   # save the figure to file
