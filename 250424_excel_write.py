import pandas as pd

file_name = "2025년 폭력예방교육 이수명단(시립도서관).xlsx"

# 세 번째 행을 헤더로 지정하여 파일 읽기
df = pd.read_excel(file_name, header=2)

# 기존 열 이름 리스트 가져오기
cols = list(df.columns)

# 이후 처리 작업 수행 (예: 데이터 총합 계산 등)
print(f"파일 {file_name} 처리 완료. 열 이름: {df.columns.tolist()}")

# 처리한 결과를 새로운 파일로 저장
df.to_excel("processed_" + file_name, index=False)