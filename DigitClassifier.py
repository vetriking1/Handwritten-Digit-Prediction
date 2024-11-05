import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

def predict_image(img_location, plot=False):
        # Load the model
    model = tf.keras.models.load_model("./mnist_model.h5")
    
    # Load and preprocess the image using OpenCV
    img = cv2.imread(img_location, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img_array = np.array(img, dtype='float32') / 255.0
    if plot:
        # Check the preprocessed image
        plt.imshow(img_array, cmap='gray')
        plt.title('Preprocessed Image')
        plt.show()
    
    # Expand dimensions to match model input
    img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension
    """make the image 3d (size, size, 1) 1 for grayscale"""
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make predictions
    predictions_array = model.predict(img_array)
    predictions = np.array(predictions_array)[0]
    result = np.argmax(predictions)
    
    print('The image name:', img_location, 'Predicted:', result)
    return result

#!Extra  code
def predict_image_24x(img_location):
    # Load the model
    model = tf.keras.models.load_model("./mnist_model.h5")
    
    # Load and preprocess the image using OpenCV
    img = cv2.imread(img_location)[:,:,0]
    img = np.invert(np.array([img]))

    predictions_array = model.predict(img)
    result = np.argmax(predictions_array)
    
    print('The image name:', img_location, 'Predicted:', result)
    return result


