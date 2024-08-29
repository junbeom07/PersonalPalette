import cv2
import numpy as np
import matplotlib.pyplot as plt

face_img = cv2.imread("img.jpg")
face_img_ycrcb = cv2.cvtColor(face_img, cv2.COLOR_BGR2YCrCb)
lower = np.array([0, 133, 77], dtype=np.uint8)
upper = np.array([255, 173, 127], dtype=np.uint8)
skin_msk = cv2.inRange(face_img_ycrcb, lower, upper)
skin = cv2.bitwise_and(face_img, face_img, mask=skin_msk)
skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(skin_hsv)
h_mean = cv2.mean(h, mask=skin_msk)[0]
s_mean = cv2.mean(s, mask=skin_msk)[0]
v_mean = cv2.mean(v, mask=skin_msk)[0]

print(f"평균 HSV 값: H={h_mean:.2f}, S={s_mean:.2f}, V={v_mean:.2f}")

skin_rgb = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)
plt.imshow(skin_rgb)
plt.axis('off')
plt.title('Skin Detection')
plt.show()
