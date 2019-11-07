from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/team")
def elements():
    return render_template('team.html')


@app.route("/bbfu")
def bbfu():
    return render_template('bbfu.html')

