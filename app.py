from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    info = ""
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            if a == 0:
                info = "Invalid input: a cannot be 0 for a quadratic equation."
                return render_template('index.html', plot_url=None, info=info)

            discriminant = b**2 - 4*a*c

            if discriminant > 0:
                info += f"Two real roots since Δ = {discriminant:.2f}<br>"
            elif discriminant < 0:
                info += f"Two imaginary roots since Δ = {discriminant:.2f}<br>"
            else:
                info += f"One real root since Δ = {discriminant:.2f}<br>"

            sum_ = -b / a
            product = c / a
            info += f"Sum of roots (x₁ + x₂) = {sum_:.2f}<br>"
            info += f"Product of roots (x₁·x₂) = {product:.2f}<br>"

            x1_sq_plus_x2_sq = sum_**2 - 2 * product
            x1_cub_plus_x2_cub = x1_sq_plus_x2_sq * sum_ - (product * sum_)
            x1_4 = x1_cub_plus_x2_cub * sum_ - product * x1_sq_plus_x2_sq
            info += f"x₁² + x₂² = {x1_sq_plus_x2_sq:.2f}<br>"
            info += f"x₁³ + x₂³ = {x1_cub_plus_x2_cub:.2f}<br>"
            info += f"x₁⁴ + x₂⁴ = {x1_4:.2f}<br>"

            # Plot the quadratic function
            x = np.linspace(-10, 10, 400)
            y = a * x**2 + b * x + c

            plt.figure()
            plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.title("Graph of the Quadratic Function")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.grid(True)
            plt.legend()

            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            plot_url = f'data:image/png;base64,{image_base64}'
            plt.close()

        except Exception as e:
            info = f"Error: {e}"

    return render_template('index.html', plot_url=plot_url, info=info)

if __name__ == '__main__':
    app.run(debug=True)
