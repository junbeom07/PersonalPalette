import cv2
import numpy as np

def extract_skin(image, lower_bound, upper_bound):
    """
    주어진 이미지에서 피부 영역을 추출합니다.

    Parameters:
    - image: 입력 이미지 (BGR 형식)
    - lower_bound: YCrCb 색 공간에서의 하한값 (np.array)
    - upper_bound: YCrCb 색 공간에서의 상한값 (np.array)

    Returns:
    - 피부 영역이 추출된 이미지 (BGR 형식)
    - 피부 마스크 (binary mask)
    """
    # 이미지를 BGR에서 YCrCb 색 공간으로 변환합니다.
    image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # 피부색을 검출하기 위한 마스크를 생성합니다.
    skin_mask = cv2.inRange(image_ycrcb, lower_bound, upper_bound)

    # 피부 영역만 추출합니다.
    skin = cv2.bitwise_and(image, image, mask=skin_mask)

    return skin, skin_mask

def on_mouse(event, x, y, flags, param):
    """
    마우스 이벤트 처리 함수
    """
    if event == cv2.EVENT_MOUSEMOVE:
        if x >= 0 and y >= 0 and x < skin.shape[1] and y < skin.shape[0]:
            # 피부 영역의 Lab 색 공간으로 변환
            lab_color = cv2.cvtColor(skin, cv2.COLOR_BGR2Lab)
            lab_b_value = lab_color[y, x, 2]
            text = f'Lab B value: {lab_b_value:.2f}'
            
            # 결과 이미지에 Lab B 값 표시
            display_image = skin.copy()
            cv2.putText(display_image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("Skin Detection", display_image)

# 이미지를 불러옵니다.
face_img = cv2.imread("img.jpg")

# YCrCb 색 공간에서 피부색 범위를 정의합니다.
lower = np.array([0, 133, 77], dtype=np.uint8)
upper = np.array([255, 173, 127], dtype=np.uint8)

# 피부 영역 추출
skin, skin_msk = extract_skin(face_img, lower, upper)

# 피부 영역이 없는 경우 예외 처리
if cv2.countNonZero(skin_msk) == 0:
    print("피부 영역이 검출되지 않았습니다.")
else:
    # 원본 이미지를 보여주면서 마우스 이벤트 처리 설정
    cv2.imshow("Skin Detection", skin)
    cv2.setMouseCallback("Skin Detection", on_mouse)
    
    # 사용자 입력 대기
    cv2.waitKey(0)
    cv2.destroyAllWindows()
