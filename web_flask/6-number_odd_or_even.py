#!/usr/bin/python3
"""
script starts Flask web app with more custom routes for c and python and int
depending if int is odd or even
"""

from flask import Flask, render_template, abort
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom text given"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """display text if given int"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_if_int(n):
    """display html page if given int"""
    return render_template('5-number.html', n=n)a


@app.route('/number_odd_or_even/<int:n>')
def oddoreven(n):
    """display html page only if int given, depends if int is odd or even"""
   if n.isnumeric():
        if int(n) % 2 == 0:
            return render_template("6-number_odd_or_even.html",
                                   number=n, oddeven='even')
        else:
            return render_template("6-number_odd_or_even.html",
                                   number=n, oddeven='odd')
    else:
        return abort(404) 


if __name__ == "__main__":
    app.run()
