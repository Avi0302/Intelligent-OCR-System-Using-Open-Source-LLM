import cv2
import numpy as np


def preprocess_image(image):

    img = np.array(image.convert("RGB"))

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    denoised = cv2.fastNlMeansDenoising(gray)

    thresh = cv2.threshold(
        denoised,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    thresh_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

    return thresh_rgb