"""

# 문제 정의
파일명에 한글이 사용된 경우, 유니코드 정규화 문제로 인해 자음과 모음이 분리되는 현상이 발생할 수 있음.
이 문제는 유니코드의 두 가지 정규화 형식, 즉 NFD(Normalization Form Decomposition)와 NFC(Normalization Form Composition) 간의 차이 때문에 발생.

# 문제 발생 예시
주로 macOS와 같이 NFD를 사용하는 운영 체제와 Windows와 같이 NFC를 사용하는 운영 체제 간의 파일 공유에서 발생.
Windows에서는 일반적으로 NFC를 사용하기 때문에, macOS에서 생성된 한글 파일명이 Windows에서 분리되어 보이는 경우가 이에 해당.

# 개념 설명
1. NFD (Normalization Form Decomposition): 이 형식은 문자를 기본 구성 요소로 분해.
예를 들어, 한글에서는 하나의 글자를 여러 자음과 모음으로 분리.
2. NFC (Normalization Form Composition): 이 형식은 분해된 문자를 가능한 한 본래의 형태로 조합.
일부 운영 체제나 애플리케이션은 NFD를 사용해 파일명을 저장하고, 다른 시스템에서는 NFC를 사용하는 경우가 있음. 
이로 인해 한 시스템에서는 정상적으로 보이는 파일명이 다른 시스템에서는 자음과 모음이 분리되어 보일 수 있음.

# 문제 해결 방법
이 문제를 해결하려면 파일명을 NFC 형식으로 변환하는 것이 필요. 
이를 위해 특정 소프트웨어나 스크립트를 사용할 수 있으며, 이를 통해 파일명을 정상적으로 볼 수 있게 함.

"""

# 문제 해결 코드
import sys
from unicodedata import normalize
import os

def change_nfc_all_dir(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        os.rename(before_filename, after_filename)
        
        if os.path.isdir(before_filename):    
            change_nfc_all_dir(before_filename)
            
change_nfc_all_dir(r'C:\Users\selena\Desktop') # <- 현재 Desktop 하위 폴더에 대해 모두 적용


