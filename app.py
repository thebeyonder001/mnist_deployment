from flask import Flask, render_template, request
from PIL import Image
import numpy as np

from predict import predict

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name


@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['POST'])
def upload_image_file():    
    if request.method == 'POST':
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28,28))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1,28,28,1)/255

        return 'Predicted Number: ' + str(predict(im2arr))

@app.route('/home/')
def home():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)