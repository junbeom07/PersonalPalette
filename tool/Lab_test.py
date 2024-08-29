import cv2
import numpy as np

# 이미지 파일 경로 설정
image_path = 'lab-color-space.png'

# 이미지와 Lab 색상 공간으로 변환하는 함수
def load_image(image_path):
    # 이미지를 BGR 형식으로 로드
    image_bgr = cv2.imread(image_path)
    # 이미지를 RGB 형식으로 변환
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    # 이미지를 Lab 색상 공간으로 변환
    image_lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2Lab)
    return image_rgb, image_lab

# 마우스 이벤트 핸들러 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if x < image_lab.shape[1] and y < image_lab.shape[0]:  # Ensure coordinates are within image bounds
            # Lab 값 추출
            lab_value = image_lab[y, x]
            print(f"Lab: L={lab_value[0]} a={lab_value[1]} b={lab_value[2]}")

# 이미지 로드
image_rgb, image_lab = load_image(image_path)

# OpenCV 윈도우 생성
cv2.imshow("Image", cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
cv2.setMouseCallback("Image", mouse_callback)

# 이미지 창을 닫기 전까지 대기
cv2.waitKey(0)
cv2.destroyAllWindows()
