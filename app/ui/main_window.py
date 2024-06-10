#!/usr/bin/env python3
"""Main Application window"""
from ..utils.config import AppConfig
from app.ui.widgets.devices_list import DevicesWindow
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QFont, QColor, QPalette, QScreen
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

        self.device_window = DevicesWindow()

        self.setWindowTitle(AppConfig.APP_NAME)
        self.setGeometry(0, 0, 800, 600)

        self.start_button = QPushButton("START")
        # start button action
        self.start_button.clicked.connect(self.show_window)

        self.head_label = QLabel("IoT-health Checker")
        self.subhead_label = QLabel("Welcome to the IoT-health checker app.\n"
                               "Click Start to Proceed")
        vbox = QVBoxLayout()

        self.start_button.setStyleSheet(" font-size: 20px; qproperty-alignment: AlignCenter; font-family: Arial Black;")
        self.start_button.setFixedSize(150, 60)

        self.head_label.setStyleSheet(" font-size: 40px; qproperty-alignment: AlignCenter; font-family: Arial Black;")

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



        # Center screen
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def show_window(self) -> None:
        """shows the device list window"""
        if not self.device_window.isVisible():
            self.device_window.show()