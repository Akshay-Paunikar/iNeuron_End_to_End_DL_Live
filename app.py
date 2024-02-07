from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils import decodeImage
from predict import PredictionPipeline
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException
from ensure import ensure_annotations
import base64

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

@ensure_annotations
def decodeImage(imgstring, fileName):
    """
    to decode the binary string into normal form.
    
    Returns:
        Return the decoded string.    
    """
    try:
        imgdata = base64.b64decode(imgstring)
        with open(fileName, "wb") as f:
            f.write(imgdata)
            f.close()
            logging.info("image data decoded successfully using decodeImage function")
    except Exception as e:
        logging.info("Error in performing operation decodeImage")
        raise CustomException(e,sys)

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    # app.run(host='0.0.0.0', port=80) #for AZURE