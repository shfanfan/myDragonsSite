from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route('/real')
def real():
    return render_template("real.html")

@app.route('/cultures')
def cultures():
    return render_template("cultures.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
    