#!/usr/bin/env python3
"""Plots with matplotlip"""
import sys
import matplotlib
from PyQt6 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


matplotlib.use('QtAgg')


class GraphCanvas(FigureCanvasQTAgg):
    """Plot canvas"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """initializes canvas"""
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(GraphCanvas, self).__init__(fig)