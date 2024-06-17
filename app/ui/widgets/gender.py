#!/usr/bin/env python3
"""Gender option window"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QWidget,
                             QComboBox,
                             QVBoxLayout,
                             QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QFormLayout
                             )


class Gender(QWidget):
    """Gneder option to select
    """
    def __init__(self):
        """initializes the window"""
        super().__init__()

        self.setWindowTitle("Select Gender")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.form = QFormLayout()
        # dropdown list of gender
        gender = QComboBox()
        # test  genders
        gender.addItem('---')
        gender.addItem('Male')
        gender.addItem('Female')

        # combobox style (dropdown list styling)
        gender.setStyleSheet(" font-size: 17px; font-weight: bold; "
                              "qproperty-alignment: AlignCenter; font-family: Arial;")
        gender.setFixedSize(150,20)

        self.form.addRow("Gender:   ", gender)
        self.form.setFormAlignment(Qt.AlignmentFlag.AlignCenter)

        # adds name edit to layout
        layout.addLayout(self.form)

        # buttons (backward and forward)
        self.nav_buttons = QHBoxLayout()
        self.nav_buttons.addStretch(3)
        self.back_button = QPushButton("< Back")
        self.next_button = QPushButton("Next >")
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

        self.prev_window = None
        self.next_weight_window = None

    def set_date_previous_window(self, prev_window):
        """set devices window
        """
        self.prev_window = prev_window
        self.back_button.clicked.connect(self.show_dob_previous_window)

    def show_dob_previous_window(self):
        """shows previous window"""
        self.hide()
        self.prev_window.show()

    def set_weight_next_window(self, next_weight_window):
        """sets the gender window"""
        self.next_weight_window = next_weight_window
        self.next_button.clicked.connect(self.show_weight_next_window)

    def show_weight_next_window(self):
        """show the date window as next"""
        self.hide()
        self.next_weight_window.show()