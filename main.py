from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from helper import draw_expr
from sympy import symbols, lambdify

if __name__ == "__main__":
    app = QApplication([])  # Start application.
    window = QWidget()  # Create window.
    window.setWindowTitle("Function Plotter")

    # Set the window icon
    app.setWindowIcon(QIcon("icon.png"))

    static_canvas = FigureCanvas(Figure())
    plotter = static_canvas.figure.subplots()

    grid_layout = QGridLayout()  # Create a layout.
    h_layout = QHBoxLayout()  # Create a layout

    ex_entry = QLineEdit()
    ex_entry.setText("x^2")

    minV_entry = QSpinBox()
    minV_entry.setRange(-10000, 10000)
    minV_entry.setValue(-10)
    minV_entry.setSingleStep(1)  # Set the step size to 1

    maxV_entry = QSpinBox()
    maxV_entry.setRange(-10000, 10000)
    maxV_entry.setValue(10)
    maxV_entry.setSingleStep(1)  # Set the step size to 1

    grid_layout.addWidget(ex_entry, 0, 1)
    grid_layout.addWidget(minV_entry, 1, 1)
    grid_layout.addWidget(maxV_entry, 2, 1)

    expr_label = QLabel("Function")
    minV_label = QLabel("Min value")
    maxV_label = QLabel("Max value")

    ex_entry.setObjectName("ex_entry")
    minV_entry.setObjectName("minV_entry")
    maxV_entry.setObjectName("maxV_entry")
    

    grid_layout.addWidget(expr_label, 0, 0)
    grid_layout.addWidget(minV_label, 1, 0)
    grid_layout.addWidget(maxV_label, 2, 0)

    plot_button = QPushButton("Plot")
    plot_button.clicked.connect(lambda: draw_expr(plotter, ex_entry, minV_entry, maxV_entry))
    ex_entry.returnPressed.connect(lambda: draw_expr(plotter, ex_entry, minV_entry, maxV_entry))

    grid_layout.addWidget(plot_button, 3, 1)

    instructions_text = """<html>
                          <head>
                              <style>
                                  p { margin-top: 10px; margin-bottom: 10px; }
                                  b { color: #336699; }
                              </style>
                          </head>
                          <body>
                              <p><b>Instructions:</b></p>
                              <p>Enter a mathematical expression in function form, e.g., <b>5*x^3 + 2*x</b></p>
                              <p>Specify the minimum and maximum values for <b>x</b>.</p>
                              <p>Click <b>'Plot'</b> to visualize the function.</p>
                              <p><b>NOTE:</b> The following operators must be supported: <b>+</b>, <b>-</b>, <b>*</b>, <b>/</b>, <b>^</b>.</p>
                          </body>
                          </html>"""
    instructions_label = QLabel(instructions_text)
    instructions_label.setWordWrap(True)  # Allow text to wrap to multiple lines
    grid_layout.addWidget(instructions_label, 4, 0, 1, 2)  # Spanning two columns

    h_layout.addLayout(grid_layout)
    h_layout.addWidget(static_canvas)

    window.setLayout(h_layout)
    window.show()
    app.exec_()
