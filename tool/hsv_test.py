import cv2
import numpy as np

image_path = 'hsv.jpg'
image_bgr = cv2.imread(image_path)
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if x >= 0 and x < image_hsv.shape[1] and y >= 0 and y < image_hsv.shape[0]:
            hsv_value = image_hsv[y, x]
            h, s, v = hsv_value
            print(f"Mouse position: ({x}, {y}) - H={h}, S={s}, V={v}")
            image_display = image_bgr.copy()
            cv2.circle(image_display, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow('Image', image_display)

window_name = 'Image'
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, mouse_callback)
cv2.imshow(window_name, image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
