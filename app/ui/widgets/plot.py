#!/usr/bin/python3
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
    """graph canvas"""
    def __init__(self, parent=None, width=None, height=None, dpi=None):
        """initializes canvas"""
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.tight_layout(pad=0)
        fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        super().__init__(fig)
        self.axes = fig.add_subplot(111)
        self.axes.grid(True)

class TempCanvas(FigureCanvasQTAgg):
    """Temperature bar canvas"""
    def __init__(self, parent=None, width=None, height=None, dpi=None):
        """initializes class"""
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor('lightgray')
        self.axes = fig.add_subplot(111)
        fig.subplots_adjust(left=0.3, right=0.7, top=0.95, bottom=0.05)
        super().__init__(fig)

        self.bar = None
        self.initial_height()
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(0, 80)
        self.axes.xaxis.set_visible(False)
        self.axes.tick_params(axis='y', colors='black')

    # Initial bar plot
    def initial_height(self):
        """initial temp bar height"""
        self.bar = self.axes.bar([0], [0], width=2, color="cyan")[0]

    def update_height(self, value):
        """updates temp bar height"""
        new_temperature = abs(value)
        self.bar.set_height(new_temperature)
        self.draw()