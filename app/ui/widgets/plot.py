#!/usr/bin/env python3
"""Plots with matplotlip"""
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib import pyplot


matplotlib.use('QtAgg')
# matplotlib.style.use('dark_background')
pyplot.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "black",
    "axes.facecolor": "white",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})

class GraphCanvas(FigureCanvasQTAgg):
    """Plot canvas"""
    def __init__(self, parent=None, width=None, height=None, dpi=None):
        """initializes canvas"""
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout(pad=0)
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        # self.axes = None
        super().__init__(fig)
        self.axes = fig.add_subplot(111)
        self.axes.grid(True)
        # self.axes.axis('off')