import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import cv2


def transfer_style(content_image, style_image, model_path):

   

    print("Loading images...")
    # Load content and style images
    content_image = cv2.imread(content_image)
    style_image = cv2.imread(style_image)
    print("Resizing and Normalizing images...")
    # Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]. Example using numpy:
    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.

    # Optionally resize the images. It is recommended that the style image is about
    # 256 pixels (this size was used when training the style transfer network).
    # The content image can be any size.
    style_image = tf.image.resize(style_image, (256, 256))

    print("Loading pre-trained model...")
    # The hub.load() loads any TF Hub model
    hub_module = hub.load(model_path)

    print("Generating stylized image now...wait a minute")
    # Stylize image.
    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0]

    # reshape the stylized image
    stylized_image = np.array(stylized_image)
    stylized_image = stylized_image.reshape(
        stylized_image.shape[1], stylized_image.shape[2], stylized_image.shape[3])

    print("Stylizing completed...")
    return stylized_image

