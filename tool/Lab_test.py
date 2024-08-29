import cv2
import numpy as np

image_path = 'lab-color-space.png'

def load_image(image_path):
    image_bgr = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    image_lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2Lab)
    return image_rgb, image_lab

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if x < image_lab.shape[1] and y < image_lab.shape[0]:
            lab_value = image_lab[y, x]
            print(f"Lab: L={lab_value[0]} a={lab_value[1]} b={lab_value[2]}")

image_rgb, image_lab = load_image(image_path)

cv2.imshow("Image", cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
cv2.setMouseCallback("Image", mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
