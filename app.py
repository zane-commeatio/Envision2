from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/upload'

@app.route("/", methods = ['GET', 'POST'])
@app.route("/index", methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        try:
            #f = request.files['uploaded_picture']
            #f.save(secure_filename(f.filename))
            files = request.files.to_dict()
            f = files['uploaded_picture']
            extension = re.findall(r'.*(\..*)',f.filename)[0]
            f.save('uploaded_picture')
            return render_template('index.html', debug = str(extension))
        except Exception as e:
            print(e)
            return render_template('index.html', debug = e)
        

    return render_template('index.html', debug = None)

@app.route("/team")
def team():
    return render_template('team.html')


@app.route("/bbfu")
def bbfu():
    return render_template('bbfu.html')

