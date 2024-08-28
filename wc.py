import cv2
import numpy as np

def classify_tone(lab_color):
    _, _, B = lab_color

    # b 값이 음수면 쿨톤, 양수면 웜톤으로 분류
    if B < 0:
        return 'Cool Tone'
    else:
        return 'Warm Tone'

def classify_image_tone(image_path, use_average=True):
    # 이미지를 읽어옵니다.
    image = cv2.imread(image_path)
    
    # 이미지를 LAB 색 공간으로 변환합니다.
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    if use_average:
        # 이미지 전체의 평균 b 값을 계산
        average_lab_color = np.mean(lab_image, axis=(0, 1))
        tone = classify_tone(average_lab_color)
        return tone, average_lab_color
    else:
        # 이미지의 중앙 부분의 b 값을 사용
        h, w, _ = lab_image.shape
        center_lab_color = lab_image[h//2, w//2]
        tone = classify_tone(center_lab_color)
        return tone, center_lab_color

# 이미지 경로를 설정합니다.
image_path = 'dbwotjr.jpg'

# 이미지의 톤을 분류합니다. 전체 평균을 사용할지 중앙 픽셀을 사용할지 결정
tone, lab_color = classify_image_tone(image_path, use_average=True)

print(f"The image is classified as: {tone}")
print(f"LAB color: {lab_color}")
