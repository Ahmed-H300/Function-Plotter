from PySide2.QtWidgets import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from sympy import symbols, lambdify, SympifyError

def draw_expr(plotter, ex_entry, minV_entry, maxV_entry):
    # Clear the previous plot
    plotter.clear()

    # Get the expression, min value, and max value from the input fields
    expr = ex_entry.text()
    min_value = minV_entry.value()
    max_value = maxV_entry.value()

    if min_value >= max_value:
        # Display an error message for invalid range
        error_message = "Invalid range. Please ensure that the minimum value is less than the maximum value."
        QMessageBox.critical(None, "Invalid Range", error_message)
        return

    # Create a numpy array of x values within the given range
    x = np.linspace(min_value, max_value, 1000)

    # Create symbols for the expression
    symbol_x = symbols('x')

    try:
        # Validate the expression
        lambdify(symbol_x, expr)

        # Replace the ^ operator with ** for exponentiation
        expr = expr.replace('^', '**')

        # Create a lambdify function from the modified expression
        expr_func = lambdify(symbol_x, expr, modules=['numpy'])

        # Evaluate the expression function for the given x values
        y = expr_func(x)

        # Plot the function
        plotter.plot(x, y, color='blue')
        plotter.set_xlabel('x')
        plotter.set_ylabel('f(x)')
        plotter.set_title('Function Plot')

    except SympifyError:
        # Display an error message for invalid expression
        error_message = "Invalid expression. Please enter a valid mathematical expression like the examples provided in the instructions."
        QMessageBox.critical(None, "Invalid Expression", error_message)

    except Exception as e:
        # Display a generic error message for other exceptions
        error_message = "Invalid expression. Please enter a valid mathematical expression like the examples provided in the instructions."
        QMessageBox.critical(None, "Error", error_message)

    # Refresh the canvas to display the updated plot
    static_canvas = plotter.get_figure().canvas
    static_canvas.draw()