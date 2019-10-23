import pickle

import cv2
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras


def getData():
    image = cv2.imread('img.png')
    image = cv2.resize(image, (64, 64))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    val = [image, ]
    image = np.array(val)
    image = image / 255.0
    model = keras.models.load_model('model.h5')
    predictions = model.predict(image)

    id_to_label_file = open('id_to_label_file', 'rb')
    id_to_label = pickle.load(id_to_label_file)
    id_to_label_file.close()

    res = plt.xlabel(id_to_label[np.argmax(predictions)])
    print(res)
    return res.get_text()

# getData()
