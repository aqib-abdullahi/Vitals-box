#!/bin/usr/python3
"""Main Application window"""
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QFont, QColor, QPalette
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QLabel,
                             QMenu,
                             QLineEdit,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QPushButton,
                             )


class MainWindow(QMainWindow):
    """QMainWindow subclass
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("IoT-Health Checker")
        self.setGeometry(200, 200, 620, 410)

        self.start_button = QPushButton("START")
        self.head_label = QLabel("IoT-health Checker")
        self.subhead_label = QLabel("Welcome to the IoT-health checker app. \n"
                               "Click Start to Proceed")
        vbox = QVBoxLayout()

        self.start_button.setFont(QFont('Arial', 17))
        self.start_button.setStyleSheet(" font-size: 30px; qproperty-alignment: AlignCenter; font-family: Arial Black;")
        self.start_button.setFixedSize(150, 60)

        self.head_label.setFont(QFont('Arial', 20))
        self.head_label.setStyleSheet(" font-size: 40px; qproperty-alignment: AlignCenter; font-family: Arial Black;")

        self.subhead_label.setFont(QFont('Arial', 16))
        self.subhead_label.setStyleSheet(" font-size: 20px; qproperty-alignment: AlignCenter; font-family: Arial Black;")

        vbox.addWidget(self.head_label)
        vbox.addWidget(self.subhead_label)
        vbox.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setAutoFillBackground(True)
        widget_palette = widget.palette()
        widget_palette.setColor(widget.backgroundRole(), QColor('beige'))
        widget.setPalette(widget_palette)
        widget.setLayout(vbox)

        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()
sys.exit(app.exec())