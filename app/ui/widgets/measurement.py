#!/usr/bin/env python3
"""Measurement Window"""
from app.ui.widgets.plot import GraphCanvas
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QGroupBox
                             )


class Measurement(QWidget):
    """meeasurement reading window
    """
    def __init__(self):
        """initializes the window"""
        super().__init__()

        self.setWindowTitle("IoT Health Checker")
        self.setGeometry(0, 0, 1200, 800)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        # self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        group_v = QGroupBox('graph')
        group_h = QGroupBox('temp')
        group_h.setMaximumWidth(400)
        hbox.addWidget(group_v)
        hbox.addWidget(group_h)

        graph_layout = QVBoxLayout()
        group_v.setLayout(graph_layout)

        #top graph (dummy data)
        self.canvas_one = GraphCanvas(self, width=4, height=3, dpi=100)
        self.canvas_one.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        #bottom graph (dummy data)
        self.canvas_two = GraphCanvas(self, width=4, height=3, dpi=100)
        self.canvas_two.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        graph_layout.addWidget(self.canvas_one)
        graph_layout.addWidget(self.canvas_two)

        #to be edited
        # buttons (backward and forward)
        self.nav_buttons = QHBoxLayout()
        self.nav_buttons.addStretch(3)
        self.back_button = QPushButton("< Back")
        self.next_button = QPushButton("End measurement")
        self.nav_buttons.addWidget(self.back_button)
        self.nav_buttons.addWidget(self.next_button)

        # style buttons
        self.next_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")
        self.back_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")

        # adds button to layout
        layout.addLayout(self.nav_buttons)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        #end app
        self.next_button.clicked.connect(self.end_measurement)

    def end_measurement(self):
        """ends app"""
        self.close()