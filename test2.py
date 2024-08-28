import cv2
import numpy as np

# 이미지 파일 경로
image_path = 'd.jpg'

# 이미지를 BGR 색상 공간으로 읽기
image_bgr = cv2.imread(image_path)

# 이미지를 BGR에서 HSV 색상 공간으로 변환
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

# 마우스 콜백 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # 마우스 위치의 HSV 값 추출
        if x >= 0 and x < image_hsv.shape[1] and y >= 0 and y < image_hsv.shape[0]:
            hsv_value = image_hsv[y, x]
            h, s, v = hsv_value
            print(f"Mouse position: ({x}, {y}) - H={h}, S={s}, V={v}")
            
            # 이미지에 마우스 포인터 표시 (원)
            image_display = image_bgr.copy()
            cv2.circle(image_display, (x, y), 5, (0, 255, 0), -1)
            cv2.imshow('Image', image_display)

# 윈도우 이름
window_name = 'Image'

# 윈도우 생성 및 마우스 콜백 함수 설정
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, mouse_callback)

# 이미지 표시
cv2.imshow(window_name, image_bgr)

# 키를 누를 때까지 대기
cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()
