import cv2
import numpy as np
import matplotlib.pyplot as plt

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

def calculate_average_lab_b(image, mask):
    """
    피부 영역의 평균 Lab B 값을 계산합니다.

    Parameters:
    - image: 피부 영역 이미지 (BGR 형식)
    - mask: 피부 영역 마스크 (binary mask)

    Returns:
    - 평균 Lab B 값
    """
    # 피부 영역만 남기기 위해 마스크를 적용
    skin_masked = cv2.bitwise_and(image, image, mask=mask)
    
    # 피부 영역의 Lab 색 공간으로 변환
    skin_lab = cv2.cvtColor(skin_masked, cv2.COLOR_BGR2Lab)
    
    # 마스크가 적용된 피부 영역의 Lab B 값만 추출
    b_values = skin_lab[:, :, 2][mask > 0]
    
    # Lab B 값의 평균 계산
    average_b = np.mean(b_values)
    
    return average_b

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
    # 피부 영역의 평균 Lab B 값 계산
    average_b = calculate_average_lab_b(skin, skin_msk) -128
    
    # BGR 이미지를 RGB로 변환 (matplotlib은 RGB를 사용합니다)
    skin_rgb = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)
    
    # Plotting the image
    fig, ax = plt.subplots()
    ax.imshow(skin_rgb)
    ax.set_title(f'Skin Detection - Average Lab B value: {average_b:.2f}')
    
    plt.show()
