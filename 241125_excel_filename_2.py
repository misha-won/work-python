import os
import re  # 정규 표현식 모듈 추가
import pandas as pd
from openpyxl import load_workbook

# 파일이 위치한 폴더 지정
directory = 'C:/Users/user/Desktop/Won/9월'

# 지정된 폴더 내 모든 Excel 파일을 순회하면서 파일명 변경
for filename in os.listdir(directory):
    if filename.endswith('.xlsx') and "기획예산과" in filename and not filename.startswith("2024"):
        # 파일명에서 날짜와 관련된 정보를 추출
        match = re.match(r'(\d{6})-(\d{6})기획예산과(\(카드\))?_(\d+)건 (\d+,\d+).xlsx', filename)
        if match:
            # 추출된 정보를 바탕으로 새로운 날짜 형식을 생성
            start_date = '2024' + match.group(1)[2:]  # '240904'의 '2409'를 제외하고 '2024'를 추가
            end_date = '2024' + match.group(2)[2:]    # '240913'의 '2409'를 제외하고 '2024'를 추가
            card = match.group(3) if match.group(3) else ''
            count = match.group(4)
            amount = match.group(5)

            new_filename = f"{start_date}-{end_date}기획예산과{card}_{count}건 {amount}.xlsx"

            # 파일명 변경
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed '{filename}' to '{new_filename}'")

print("All eligible files have been renamed.")