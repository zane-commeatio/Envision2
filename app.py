from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
@app.route("/index", methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        f = request.files['file']
        return render_template('index.html', debug = str(f.filename))
        f.save(secure_filename(f.filename))
        

    return render_template('index.html', debug = None)

@app.route("/team")
def team():
    return render_template('team.html')


@app.route("/bbfu")
def bbfu():
    return render_template('bbfu.html')

