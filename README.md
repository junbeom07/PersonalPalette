# PersonalPalette
설치해야할것

--------------------------------------

pip install opencv-python

pip install numpy

pip install -U matplotlib

--------------------------------------
main.py

tone.py

이 프로그램은 OpenCV를 사용하여 이미지에서 피부 영역을 추출하고, 해당 영역의 평균 Lab 색상 공간의 b 값을 계산하는 기능을 제공합니다. Lab 색상 공간에서 b 값은 색상의 노랑-파랑 축을 나타내며, 이를 통해 피부 톤의 색상 특성을 분석할 수 있습니다.

피부 영역 추출 (Skin Detection):

이미지를 YCrCb 색상 공간으로 변환한 후, 피부 색상 범위에 해당하는 픽셀을 마스크로 추출합니다.
추출된 마스크를 사용하여 이미지에서 피부 영역만을 남깁니다.


Lab 색상 공간의 b 값 평균 계산:

추출된 피부 영역을 Lab 색상 공간으로 변환합니다.
피부 영역에 해당하는 b 값의 평균을 계산하여 출력합니다.


이미지의 제목에 계산된 평균 Lab b 값을 표시합니다.
img.jpg라는 이름의 이미지 파일을 준비합니다. 이 파일은 프로그램과 같은 디렉토리에 위치해야 합니다.





VS.py

이 프로그램은 이미지에서 피부 영역을 추출하고, 해당 영역의 색상을 분석하여 그 색상의 특징을 설명하는 기능을 수행합니다. HSV 색상 공간을 사용하여 이미지 처리와 색상 분석을 수행합니다.



피부 영역 추출 (Skin Detection):

이미지를 YCrCb 색상 공간으로 변환한 후, 피부 색상 범위에 해당하는 픽셀을 마스크로 추출합니다.
추출된 마스크를 사용하여 이미지에서 피부 영역만을 남깁니다.


HSV 색상 공간의 평균 값 계산:

추출된 피부 영역을 HSV 색상 공간으로 변환합니다.
HSV 색상 공간에서 H(색상), S(채도), V(명도) 채널을 분리하고, 각 채널의 평균값을 계산합니다.


색상 특징 분석:

계산된 S(채도)와 V(명도) 값을 기반으로 색상 특징을 분류합니다.


이미지에 분석된 피부 영역과 함께 해당 영역의 HSV 평균값 및 색상 특징이 표시됩니다.
img.jpg라는 이름의 이미지 파일을 준비합니다. 이 파일은 프로그램과 같은 디렉토리에 위치해야 합니다.




--------------------------------------
hsv_test.py

vs색공간 이미지를 불러오고, 마우스 커서가 이미지 위를 이동할 때 해당 위치의 HSV(Hue, Saturation, Value) 색상 값을 실시간으로 출력하는 프로그램입니다.


Lab_test.py

Lab색공간 이미지를 불러오고, 마우스 커서가 이미지 위를 이동할 때 해당 위치의 Lab 색상 공간 값을 실시간으로 출력하는 프로그램입니다.


LAB2RGB.py

Lab 색상 값을 기반으로 단색 이미지를 생성하는 프로그램입니다.


skin.py

이미지에서 피부 영역을 탐지하고, 그 영역의 HSV(색상, 채도, 명도) 평균 값을 계산한다.