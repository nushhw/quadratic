# Quadratic Equation Solver with Graph Visualization

This project is a web-based quadratic equation solver built using Python's Flask framework and Matplotlib. It allows users to input coefficients `a`, `b`, and `c` of a quadratic equation of the form: ax^2 + bx +c.


The application determines the nature of the roots using the discriminant, applies Vieta's formulas, and plots the corresponding quadratic curve.

---

## Features

- Computes the discriminant and determines the type of roots (real and distinct, real and equal, or complex).
- Calculates sum and product of roots, as well as higher-order expressions such as:
  - \( x_1^2 + x_2^2 \)
  - \( x_1^3 + x_2^3 \)
  - \( x_1^4 + x_2^4 \)
- Dynamically generates a plot of the quadratic function.
- Simple and intuitive web interface using HTML forms.

---

## Requirements

- Python 3.7 or later
- pip (Python package manager)

Python packages used:

- Flask
- Matplotlib
- NumPy

Install them with:

```bash
pip install -r requirements.txt
