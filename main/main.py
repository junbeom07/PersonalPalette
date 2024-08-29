import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'img.jpg'
frame = cv2.imread(image_path)

if frame is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

fig, ax = plt.subplots()

frame_ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

lower = np.array([0, 133, 77], dtype=np.uint8)
upper = np.array([255, 173, 127], dtype=np.uint8)

skin_msk = cv2.inRange(frame_ycrcb, lower, upper)

skin = cv2.bitwise_and(frame, frame, mask=skin_msk)

skin_hsv = cv2.cvtColor(skin, cv2.COLOR_BGR2HSV)

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

skin_rgb = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)

h_text = f"H: {h_mean:.2f}"
s_text = f"S: {s_mean:.2f}"
v_text = f"V: {v_mean:.2f}"

ax.imshow(skin_rgb)
ax.axis('off')
ax.set_title(f'Skin Detection - {color_text} | {h_text} | {s_text} | {v_text}', fontsize=14, color='white', pad=20, bbox=dict(facecolor='black', alpha=0.5))
plt.show()
