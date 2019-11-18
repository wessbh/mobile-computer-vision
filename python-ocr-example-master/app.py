import os
import cv2
import numpy as np
from flask import Flask, render_template, request
import pytesseract
from ocr_core import ocr_core
import json

UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_page():
        message = 'result : ok'
        # check if the post request has the file part
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename

        if file and allowed_file(file.filename):
            img = cv2.imread(file.filename)

            alpha = 2.0
            beta = -160
            """""
            cv2.imshow('ok', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            """""
            new = alpha * img + beta
            new = np.clip(new, 0, 255).astype(np.uint8)
            text = pytesseract.image_to_string(new, lang="Arabic")
            print("text:"+text)
            # extract the text and display it
            response = app.response_class(
                response=json.dumps(text),
                status=200,
                mimetype='application/json'
            )
        return text

if __name__ == '__main__':
    app.run(host='192.168.0.106')
