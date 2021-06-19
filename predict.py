import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

def predict(image):
    model = load_model("mnist.h5")

    return np.argmax(model.predict(image))
