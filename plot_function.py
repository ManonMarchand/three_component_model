from mpl_toolkits.axes_grid1 import Divider, Size
from mpl_toolkits.axes_grid1.mpl_axes import Axes
from itertools import cycle
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
from math import log10, floor
import numpy as np

import warnings


def create_plot(two_sided=False, colors = ['#6F4C9B', '#5568B8', '#4D8AC6',
               '#60AB9E', '#77B77D', '#A6BE54',
               '#D1B541', '#E49C39', '#DF4828', '#990D38'], markers = ['o', 'v', '^', 's', 'D', '*'], figsize=(5, 3.4)):
    """
    Makes a plot environnement. The only interest of this tool is that now
    figsize dictates the size of the rectangle and not the size of the full
    figure, which I find annoying.

    Parameters
    ----------
    twosided : bool
        allows to change the size of the figure accordingly.
    colors : list of strings
        a default list exists but this allows to change it if u want
    markers : list of strings
        a default list of markers exists, but u can change it if needed
    Returns
    -------
    fig, ax : matplotlib objects to be used as normal
    colors, markers : itertools cycles of colors and markers

    """
    color = cycle(colors)
    marker = cycle(markers)
    if two_sided :
        fig = plt.figure(figsize=(3.4, 3.4))
    else :
        fig = plt.figure(figsize=figsize)
    # The first & third items are for padding and the second items are for the
    # axes. Sizes are in inches.
    h = [Size.Fixed(1.0), Size.Scaled(1.), Size.Fixed(.2)]
    v = [Size.Fixed(0.7), Size.Scaled(1.), Size.Fixed(.5)]

    divider = Divider(fig, (0.0, 0.0, 1., 1.), h, v, aspect=False)
    # the width and height of the rectangle is ignored.

    ax = Axes(fig, divider.get_position())
    ax.set_axes_locator(divider.new_locator(nx=1, ny=1))

    fig.add_axes(ax)
    return fig, ax, color, marker




def legend_modulus(ax, loc='lower right', second_legend=False, bbox_to_anchor=0):
    """
    Function to automatically add a legend in oscillatory rheology tests
    empty symbols are loss modulus and full symbols are storage modulus
    
    Parameters
    ----------
    ax : matplotlib axis object
            to be modified
    loc : string 
        position for the legend             
    second_legend : boolean
        True if there is already a legend on the axis to be modified 
    bbox_to_anchor : tuple
        add a tuple with desired position here 

    Returns
    -------
    nothing, but draws the legend on ax
    """
    handles = [mpl.lines.Line2D([], [], c='k', label=r'$\mathrm{loss~modulus}$'),
              mpl.lines.Line2D([], [], c='k', mfc='k', label=r'$\mathrm{storage~modulus}$')]


    if second_legend :

        if bbox_to_anchor != 0:
            legend = plt.legend(handles=handles, loc=loc, bbox_to_anchor=bbox_to_anchor)
            ax.add_artist(legend)
        else:
            legend = plt.legend(handles=handles, loc=loc)
            ax.add_artist(legend)
    else:
        if bbox_to_anchor != 0:
            ax.legend(loc=loc, handles=handles, bbox_to_anchor=bbox_to_anchor)
        else :
            ax.legend(loc=loc, handles=handles)