import numpy as np
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import sys
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        
    def predict(self):
        try:
            # load model
            model = load_model("model.h5")
            
            imagename = self.filename
            test_image = image.load_img(imagename, target_size=(224, 224))
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            result = np.argmax(model.predict(test_image), axis=1)
            print(f"{result}")
            
            if result[0] == 1:
                prediction = "Healthy"
                return [{"image": prediction}]
            else:
                prediction = "Coccidiosis"
                return [{"image": prediction}]
            
            logging.info(f"The prediction pipeline is working and the result is {prediction}")
            
        except Exception as e:
            logging.info("Error in performing predict operation")
            raise CustomException(e, sys)