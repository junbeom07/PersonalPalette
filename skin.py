import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 불러옵니다.
face_img = cv2.imread("img.jpg")

# 이미지를 BGR에서 YCrCb 색 공간으로 변환합니다.
face_img_ycrcb = cv2.cvtColor(face_img, cv2.COLOR_BGR2YCrCb)

# YCrCb 색 공간에서 피부색 범위를 정의합니다.
lower = np.array([0, 133, 77], dtype=np.uint8)
upper = np.array([255, 173, 127], dtype=np.uint8)

# 피부색을 검출하기 위한 마스크를 생성합니다.
skin_msk = cv2.inRange(face_img_ycrcb, lower, upper)

# 피부 영역만 추출합니다.
skin = cv2.bitwise_and(face_img, face_img, mask=skin_msk)

# 피부 영역을 HSV 색 공간으로 변환합니다.
skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

# 마스크된 영역에서 HSV 값을 추출합니다.
h, s, v = cv2.split(skin_hsv)
h_mean = cv2.mean(h, mask=skin_msk)[0]
s_mean = cv2.mean(s, mask=skin_msk)[0]
v_mean = cv2.mean(v, mask=skin_msk)[0]

# 평균 HSV 값을 출력합니다.
print(f"평균 HSV 값: H={h_mean:.2f}, S={s_mean:.2f}, V={v_mean:.2f}")

# BGR 이미지를 RGB로 변환 (matplotlib는 RGB 색상 형식을 사용하므로)
skin_rgb = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)

# 결과를 화면에 출력합니다.
plt.imshow(skin_rgb)
plt.axis('off')  # 축을 숨깁니다.
plt.title('Skin Detection')
plt.show()
