import os
import pandas as pd
import glob

# 파일이 위치한 폴더 지정
directory = 'C:/Users/user/Desktop/Won/10월'

# 지정된 폴더 내 모든 Excel 파일을 순회
for filepath in glob.glob(os.path.join(directory, '*.xlsx')):
    filename = os.path.basename(filepath)
    # "9월 기획예산과 특별회계" 파일 제외
    if "9월 기획예산과 특별회계" not in filename:
        # Excel 파일 로드
        df = pd.read_excel(filepath)
        # "시세" 열이 있는지 확인하고 계산
        if '시세' in df.columns:
            # "시세" 열의 항목 개수
            count = df['시세'].count()
            # "시세" 열의 값 총합
            total = df['시세'].sum()
            # 숫자를 세 자리마다 쉼표로 구분하는 형식으로 변환
            formatted_total = f"{total:,}"
            # 새 파일명 생성
            new_filename = f"{filename[:-5]}_{count}건 {formatted_total}.xlsx"  # .xlsx 확장자를 고려하여 제거 후 추가
            # 파일명 변경
            os.rename(filepath, os.path.join(directory, new_filename))
        else:
            print(f"'시세' 열이 {filename}에 없습니다.")
    else:
        print(f"파일 {filename}은 변경 대상에서 제외되었습니다.")

print("파일 이름 변경 작업이 완료되었습니다.")