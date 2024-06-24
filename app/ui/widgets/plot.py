#!/usr/bin/env python3
"""Plots with matplotlip"""
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot


matplotlib.use('QtAgg')
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
        super().__init__(fig)
        self.axes = fig.add_subplot(111)
        self.axes.grid(True)

class TempCanvas(FigureCanvasQTAgg):
    """Temperature bar plotting"""
    def __init__(self, parent=None, width=None, height=None, dpi=None):
        """initializes class"""
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.fig.subplots_adjust(left=0.3, right=0.7, top=0.95, bottom=0.05)
        super().__init__(self.fig)
        # Initial bar plot
        self.bar = self.axes.bar([0], [70], width=2, color="cyan")[0]
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(0, 80)