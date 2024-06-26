#!/usr/bin/env python3
"""entry point"""
from PyQt6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.ui.widgets.devices_list import DevicesWindow
from app.ui.widgets.fullname import FullName
from app.ui.widgets.date_of_birth import DateOfBirth
from app.ui.widgets.gender import Gender
from app.ui.widgets.weight import Weight
from app.ui.widgets.information import Information
from app.ui.widgets.measurement import Measurement


class Initializer:
    """Instantiates all windows"""
    def __init__(self):
        """initializes windows"""
        self.app = QApplication([])
        self.main_window = MainWindow()
        self.device_window = DevicesWindow()
        self.fullname_window = FullName()
        self.date_of_birth_window = DateOfBirth()
        self.gender_window = Gender()
        self.weight_window = Weight()
        self.information_window = Information()

    def run(self) -> int:
        """runs app entry point"""
        self.main_window.set_device_next_window(self.device_window)
        self.device_window.set_name_next_window(self.fullname_window)
        self.fullname_window.set_device_previous_window(self.device_window)
        self.fullname_window.set_date_next_window(self.date_of_birth_window, self.information_window)
        self.date_of_birth_window.set_fullname_previous_window(self.fullname_window)
        self.date_of_birth_window.set_gender_next_window(self.gender_window, self.information_window)
        self.gender_window.set_date_previous_window(self.date_of_birth_window)
        self.gender_window.set_weight_next_window(self.weight_window, self.information_window)
        self.weight_window.set_gender_previous_window(self.gender_window)
        self.weight_window.set_information_next_window(self.information_window, self.information_window)
        self.information_window.set_weight_previous_window(self.weight_window)

        self.main_window.show()
        return sys.exit(self.app.exec())


if __name__ == '__main__':
    import sys
    start = Initializer()
    sys.exit(start.run())