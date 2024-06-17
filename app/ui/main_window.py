#!/usr/bin/env python3
"""Main Application window"""
from ..utils.config import AppConfig
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QLabel,
                             QWidget,
                             QVBoxLayout,
                             QPushButton,
                             )


class MainWindow(QMainWindow):
    """QMainWindow subclass
    """
    def __init__(self):
        super().__init__()

        # window specs
        self.setWindowTitle(AppConfig.APP_NAME)
        self.setGeometry(0, 0, 800, 600)

        # start button
        self.start_button = QPushButton("START")

        # Font styling
        self.head_label = QLabel("IoT-health Checker")
        self.subhead_label = QLabel("Welcome to the IoT-health checker app.\n"
                               "Click Start to Proceed")


        self.start_button.setStyleSheet(" font-size: 20px; font-weight: bold;"
                                        " qproperty-alignment: AlignCenter; font-family: Arial;")
        self.start_button.setFixedSize(150, 60)

        self.head_label.setStyleSheet(" font-size: 40px; font-weight: bold;"
                                      " qproperty-alignment: AlignCenter; font-family: Arial;")

        self.subhead_label.setStyleSheet(" font-size: 20px; font-weight: bold;"
                                         " qproperty-alignment: AlignCenter; font-family: Arial;")

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.head_label)
        vbox.addWidget(self.subhead_label)
        vbox.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()

        # Background color change
        # widget.setAutoFillBackground(True)
        # widget_palette = widget.palette()
        # widget_palette.setColor(widget.backgroundRole(), QColor('white'))
        # widget.setPalette(widget_palette)

        # sets widget
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        # Center screen
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        self.next_device_window = None

    def set_device_next_window(self, next_device_window):
        """sets the next window
        """
        self.next_device_window = next_device_window
        self.start_button.clicked.connect(self.show_device_next_window)

    def show_device_next_window(self):
        """shows the devices as next window
        """
        self.hide()
        self.next_device_window.show()