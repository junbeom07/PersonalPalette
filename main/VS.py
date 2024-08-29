import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 파일을 불러옵니다.
image_path = 'img.jpg'  # 여기에 이미지 파일 경로를 입력하세요.
frame = cv2.imread(image_path)

# 이미지가 정상적으로 불러와졌는지 확인합니다.
if frame is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# Matplotlib을 사용하여 이미지를 표시합니다.
fig, ax = plt.subplots()

# 이미지를 BGR에서 YCrCb 색 공간으로 변환합니다.
frame_ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

# YCrCb 색 공간에서 피부색 범위를 정의합니다.
lower = np.array([0, 133, 77], dtype=np.uint8)
upper = np.array([255, 173, 127], dtype=np.uint8)

# 피부색을 검출하기 위한 마스크를 생성합니다.
skin_msk = cv2.inRange(frame_ycrcb, lower, upper)

# 피부 영역만 추출합니다.
skin = cv2.bitwise_and(frame, frame, mask=skin_msk)

# 피부 영역을 HSV 색 공간으로 변환합니다.
skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

# 마스크된 영역에서 HSV 값을 추출합니다.
h, s, v = cv2.split(skin_hsv)
h_mean = cv2.mean(h, mask=skin_msk)[0]
s_mean = cv2.mean(s, mask=skin_msk)[0]
v_mean = cv2.mean(v, mask=skin_msk)[0]

if s_mean >= 226:
    color_text = "Vivid"
elif 142 <= s_mean < 226:
    if abs(v_mean - 180) < abs(v_mean - 240) and abs(v_mean - 180) < abs(v_mean - 250):
        color_text = "Deep"
    elif abs(v_mean - 240) < abs(v_mean - 180) and abs(v_mean - 240) < abs(v_mean - 250):
        color_text = "Strong"
    else:
        color_text = "Bright"
elif 57 <= s_mean < 142:
    if abs(v_mean - 31) < abs(v_mean - 102) and abs(v_mean - 31) < abs(v_mean - 182) and abs(v_mean - 31) < abs(v_mean - 225):
        color_text = "Dark"
    elif abs(v_mean - 102) < abs(v_mean - 31) and abs(v_mean - 102) < abs(v_mean - 182) and abs(v_mean - 102) < abs(v_mean - 225):
        color_text = "Dull"
    elif abs(v_mean - 182) < abs(v_mean - 31) and abs(v_mean - 182) < abs(v_mean - 102) and abs(v_mean - 182) < abs(v_mean - 225):
        color_text = "Soft"
    else:
        color_text = "Light"
else:
    if abs(v_mean - 31) < abs(v_mean - 102) and abs(v_mean - 31) < abs(v_mean - 182) and abs(v_mean - 31) < abs(v_mean - 225):
        color_text = "Dark Grayish"
    elif abs(v_mean - 102) < abs(v_mean - 31) and abs(v_mean - 102) < abs(v_mean - 182) and abs(v_mean - 102) < abs(v_mean - 225):
        color_text = "Grayish"
    elif abs(v_mean - 182) < abs(v_mean - 31) and abs(v_mean - 182) < abs(v_mean - 102) and abs(v_mean - 182) < abs(v_mean - 225):
        color_text = "Light Grayish"
    else:
        color_text = "Pale"

# BGR 이미지를 RGB로 변환 (matplotlib는 RGB 색상 형식을 사용하므로)
skin_rgb = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)

# HSV 값을 문자열로 생성 (가로 배치)
h_text = f"H: {h_mean:.2f}"
s_text = f"S: {s_mean:.2f}"
v_text = f"V: {v_mean:.2f}"

# Matplotlib의 플롯을 업데이트합니다.
ax.imshow(skin_rgb)
ax.axis('off')  # 축을 숨깁니다.
ax.set_title(f'Skin Detection - {color_text} | {h_text} | {s_text} | {v_text}', fontsize=14, color='white', pad=20, bbox=dict(facecolor='black', alpha=0.5))
plt.show()
