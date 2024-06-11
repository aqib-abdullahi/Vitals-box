#!/usr/bin/env python3
"""entry point"""
from PyQt6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.ui.widgets.devices_list import DevicesWindow
from app.ui.widgets.fullname import FullName


def run() -> int:
    """runs app entry point"""
    app = QApplication([])
    main_window = MainWindow()
    device_window = DevicesWindow()
    fullname_window = FullName()

    main_window.set_device_next_window(device_window)
    device_window.set_name_next_window(fullname_window)
    fullname_window.set_device_previous_window(device_window)

    main_window.show()
    return sys.exit(app.exec())


if __name__ == '__main__':
    import sys
    sys.exit(run())