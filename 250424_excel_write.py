import os
import openpyxl

base_directory = "C:/Users/user/Desktop/Workspace/교육훈련/폭력예방교육"
file_name = "2025년 폭력예방교육 이수명단(시립도서관).xlsx"
file_path = os.path.join(base_directory, file_name)

# 엑셀 파일 로드
wb = openpyxl.load_workbook(file_path)

for row in wb[0].iter_rows(min_row=3):  # 4번째 행부터 시작
    temp = str(row[4].value)  # 5번째 열 데이터 선택
    temp += "."
    row[4].value = temp