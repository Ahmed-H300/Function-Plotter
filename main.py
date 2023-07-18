from PySide2.QtWidgets import *
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from helper import *
import matplotlib.pyplot as plt


def draw_expr(*arg):
    pass

if __name__ == "__main__":

    # Initialize a window and title
    app = QApplication([]) # Start application.
    window = QWidget() # Create window.
    window.setWindowTitle("Function Plotter")

    # Initialize the canvas that contains the figure
    static_canvas = FigureCanvas(Figure())
    plotter = static_canvas.figure.subplots()

    # Initialize a grid layout
    grid_layout = QGridLayout() # Create a layout.
    h_layout = QHBoxLayout() # Create a layout

    # Entries
    ex_entry = QLineEdit()
    ex_entry.setText("x^2")

    # minV_entry = QSpinBox()
    # minV_entry.setValue(0)
    # minV_entry.setRange(-10000, 10000)
    # maxV_entry = QSpinBox()
    # maxV_entry.setValue(1000)
    # maxV_entry.setRange(-10000, 10000)

    minV_entry = QSpinBox()
    minV_entry.setRange(-10000, 10000)
    minV_entry.setValue(-10)
    minV_entry.setSingleStep(1)  # Set the step size to 1

    maxV_entry = QSpinBox()
    maxV_entry.setRange(-10000, 10000)
    maxV_entry.setValue(10)
    maxV_entry.setSingleStep(1)  # Set the step size to 1

    # Add Entries to grid
    grid_layout.addWidget(ex_entry, 0, 1)
    grid_layout.addWidget(minV_entry, 1, 1)
    grid_layout.addWidget(maxV_entry, 2, 1)

    # Labels
    expr_label = QLabel("Function")
    minV_label = QLabel("Min value")
    maxV_label = QLabel("Max value")

    # Add labels to grid
    grid_layout.addWidget(expr_label, 0, 0)
    grid_layout.addWidget(minV_label, 1, 0)
    grid_layout.addWidget(maxV_label, 2, 0)

    # Button
    plot_button = QPushButton("Plot")
    plot_button.clicked.connect(draw_expr)
    ex_entry.returnPressed.connect(draw_expr)

    # Add button to grid
    grid_layout.addWidget(plot_button, 3, 1)

     # Add instructions label with styling
    instructions_text = """<html>
                          <head>
                              <style>
                                  p { margin-top: 10px; margin-bottom: 10px; }
                                  b { color: #336699; }
                              </style>
                          </head>
                          <body>
                              <p><b>Instructions:</b></p>
                              <p>Enter a mathematical expression in function form, e.g., <b>5*x^3 + 2*x</b>.</p>
                              <p>Specify the minimum and maximum values for <b>x</b>.</p>
                              <p>Click <b>'Plot'</b> to visualize the function.</p>
                              <p><b>NOTE:</b> The following operators must be supported: <b>+</b>, <b>-</b>, <b>*</b>, <b>/</b>, <b>^</b>.</p>
                          </body>
                          </html>"""
    instructions_label = QLabel(instructions_text)
    instructions_label.setWordWrap(True)  # Allow text to wrap to multiple lines
    grid_layout.addWidget(instructions_label, 4, 0, 1, 2)  # Spanning two columns



    # combine layouts and add canvas
    h_layout.addLayout(grid_layout)
    h_layout.addWidget(static_canvas)


    window.setLayout(h_layout) # Pass the layout to the window
    window.show() # Show window
    app.exec_() # Execute the App