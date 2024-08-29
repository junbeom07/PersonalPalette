import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_skin(image, lower_bound=None, upper_bound=None):
    if lower_bound is None:
        lower_bound = np.array([0, 133, 77], dtype=np.uint8)
    if upper_bound is None:
        upper_bound = np.array([255, 173, 127], dtype=np.uint8)

    image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    skin_mask = cv2.inRange(image_ycrcb, lower_bound, upper_bound)
    skin = cv2.bitwise_and(image, image, mask=skin_mask)
    return skin, skin_mask

def calculate_average_lab_b(image, mask):
    skin_masked = cv2.bitwise_and(image, image, mask=mask)
    skin_lab = cv2.cvtColor(skin_masked, cv2.COLOR_BGR2Lab)
    b_values = skin_lab[:, :, 2][mask > 0]
    return np.mean(b_values)

face_img = cv2.imread("img.jpg")

skin, skin_mask = extract_skin(face_img)

if cv2.countNonZero(skin_mask) == 0:
    print("피부 영역이 검출되지 않았습니다.")
else:
    average_b = calculate_average_lab_b(skin, skin_mask)
    skin_rgb = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)
    plt.imshow(skin_rgb)
    plt.title(f'Lab B value: {average_b:.2f}')
    plt.axis('off')
    plt.show()
