from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import re
from search import find_similar

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/upload'

@app.route("/", methods = ['GET', 'POST'])
@app.route("/index", methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        try:
            files = request.files.to_dict()
            f = files['uploaded_picture']
            extension = re.findall(r'.*(\..*)',f.filename)[0]
            f.save('static/uploaded_picture.jpg')
            response = find_similar('static/uploaded_picture.jpg')
            return render_template('uploaded.html', resp = response, picture_path = 'static/uploaded_picture.jpg'  )
        except Exception as e:
            print(e)
            return render_template('index.html', debug = e)
        

    return render_template('index.html')

@app.route("/team")
def team():
    return render_template('team.html')


@app.route("/bbfu")
def bbfu():
    return render_template('bbfu.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
