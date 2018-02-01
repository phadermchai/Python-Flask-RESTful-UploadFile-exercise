from flask import Flask, render_template
from flask_restful import Resource , Api,reqparse
import os,json

app = Flask(__name__)
api = Api(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, filename])
        file.save(destination)
        print("Upload Complete")
        return render_template("complete.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5500)
