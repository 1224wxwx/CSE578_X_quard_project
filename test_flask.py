from flask import Flask, render_template
from matplotlib.figure import Figure
import random
import io   
from flask import Flask, Response, request
from matplotlib.backends.backend_svg import FigureCanvasSVG

app = Flask(__name__)


@app.route("/")
def hello(name="X Squad" ):

    return render_template("index.html",name=name,x = 100)



@app.route("/<int:x>")
def return_number(x=2):

    return f'hello {x}'


@app.route("/img-<int:x>.svg")
def plot_svg(x=10):
    """ renders the plot on the fly.
    """
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x_points = range(x)
    axis.plot(x_points, [random.randint(1, 30) for i in x_points])

    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")

if __name__ == "__main__":
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)