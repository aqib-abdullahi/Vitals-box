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

        # devices list window
        self.device_window = DevicesWindow()

        # window specs
        self.setWindowTitle(AppConfig.APP_NAME)
        self.setGeometry(0, 0, 800, 600)

        # start button
        self.start_button = QPushButton("START")
        # start button action
        self.start_button.clicked.connect(self.show_window)

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

    def show_window(self) -> None:
        """shows the device list window when start is clicked"""
        if not self.device_window.isVisible():
            self.hide()
            self.device_window.show()