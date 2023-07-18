import pytest
from pytest_mock import mocker
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest
from PySide2.QtWidgets import QApplication, QLineEdit, QSpinBox, QPushButton, QMessageBox
from PySide2 import QtWidgets

from main import *
from helper import *


@pytest.fixture(scope='session')
def qapp():
    app = QApplication([])
    yield app
    app.quit()


@pytest.fixture
def app_window(qapp):
    window = QWidget()
    yield qapp, window
    window.close()


def test_plot_button_clicked(app_window):
    app, window = app_window

    ex_entry = QLineEdit()
    ex_entry.setText("x^2")

    minV_entry = QSpinBox()
    minV_entry.setRange(-10000, 10000)
    minV_entry.setValue(-10)

    maxV_entry = QSpinBox()
    maxV_entry.setRange(-10000, 10000)
    maxV_entry.setValue(10)

    plot_button = QPushButton("Plot")

    layout = QGridLayout()
    layout.addWidget(ex_entry, 0, 0)
    layout.addWidget(minV_entry, 1, 0)
    layout.addWidget(maxV_entry, 2, 0)
    layout.addWidget(plot_button, 3, 0)

    window.setLayout(layout)
    window.show()

    # Click the "Plot" button
    QTest.mouseClick(plot_button, Qt.LeftButton)

    # Check if the plot is generated
    static_canvas = window.layout().itemAt(1).widget()
    assert static_canvas is not None
