import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_lab_image(L, a, b, size=(100, 100)):
    lab_image = np.full((size[0], size[1], 3), [L, a, b], dtype=np.uint8)
    bgr_image = cv2.cvtColor(lab_image, cv2.COLOR_Lab2BGR)
    return bgr_image

def display_image(image, title=''):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_image)
    plt.title(title)
    plt.axis('off')
    plt.show()

L = 100
a = 128
b = 128

color_image = create_lab_image(L, a, b)
display_image(color_image, f'Lab(L: {L}, a: {a}, b: {b})')
