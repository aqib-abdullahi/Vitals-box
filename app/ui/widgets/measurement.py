#!/usr/bin/env python3
"""Measurement Window"""
import sys
import random
from PyQt6 import QtCore
from app.ui.widgets import summary
from app.ui.widgets.plot import GraphCanvas, TempCanvas
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QGroupBox,
                             QFormLayout,
                             QMessageBox
                             )


class Measurement(QWidget):
    """meeasurement reading window
    """
    def __init__(self):
        """initializes the window"""
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowType.WindowMinimizeButtonHint |
            QtCore.Qt.WindowType.WindowMaximizeButtonHint
        )
        self.setWindowTitle("IoT Health Checker")
        self.setGeometry(0, 0, 1200, 800)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)

        layout = QVBoxLayout()
        self.setLayout(layout)

        hbox = QHBoxLayout()
        layout.addLayout(hbox)
        group_v = QGroupBox('Graph')
        group_h = QGroupBox('Temperature and Summary')
        group_h.setMaximumWidth(500)
        hbox.addWidget(group_v)
        hbox.addWidget(group_h)

        graph_layout = QVBoxLayout()
        group_v.setLayout(graph_layout)

        temp_layout = QHBoxLayout()
        group_h.setLayout(temp_layout)
        second_group_h = QGroupBox('Temperature Bar')
        temp_layout.addWidget(second_group_h)

        # user info section
        summary_v = QVBoxLayout()
        summary_box = QGroupBox('User Info')
        summary_v.addWidget(summary_box)
        temp_layout.addLayout(summary_v)

        #info
        form_lay = QVBoxLayout()
        self.form = QFormLayout()
        self.form.addRow("Name:   ", summary.fullname)
        self.form.addRow("Date of birth:   ", summary.dob)
        self.form.addRow("Gender:   ", summary.gender)
        self.form.addRow("Weight:   ", summary.weight)
        form_lay.addLayout(self.form)
        summary_box.setLayout(form_lay)

        # summary
        info = QGroupBox('Summary')
        sum_layout = QVBoxLayout()
        sum_layout.addWidget(info)
        summary_v.addLayout(sum_layout)

        #top graph (dummy data)
        self.canvas_one = GraphCanvas(self, width=4, height=3, dpi=100)
        # self.canvas_one.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        #bottom graph (dummy data)
        self.canvas_two = GraphCanvas(self, width=4, height=3, dpi=100)
        # self.canvas_two.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        graph_layout.addWidget(self.canvas_one)
        graph_layout.addWidget(self.canvas_two)

        #temperature bar
        self.temp_canvas = TempCanvas(width=1, height=8, dpi=100)
        bar = QVBoxLayout()
        second_group_h.setLayout(bar)
        bar.addWidget(self.temp_canvas)
        second_group_h.setMaximumWidth(200)

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
        self.next_button.setFixedWidth(180)
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
        self.next_button.clicked.connect(self.question_exit)

        #dummy data clear and redraw
        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_graph_plot)
        self.timer.timeout.connect(self.update_bar_chart)

        #dummy
        self.temperature = 0

    def update_graph_plot(self):
        """updates the graph motion"""
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas_one.axes.cla()  # Clear the canvas.
        self.canvas_one.axes.plot(self.xdata, self.ydata, 'r')
        self.canvas_one.axes.grid(True)
        self.canvas_one.draw()

        # canvas_two
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas_two.axes.cla()
        self.canvas_two.axes.plot(self.xdata, self.ydata, 'r')
        self.canvas_two.axes.grid(True)
        self.canvas_two.draw()

    def update_bar_chart(self):
        """updates the temperature bar"""
        new_value = random.uniform(-1.0, 1.0)
        self.temperature += new_value
        self.temp_canvas.update_height(self.temperature)

    def question_exit(self):
        """initiates dialog to ask exit confirmation"""
        answer = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to end measurement?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.end_measurement()
        else:
            QMessageBox.StandardButton.Abort
        return

    def end_measurement(self):
        """ends app"""
        self.destroy()
        sys.exit()