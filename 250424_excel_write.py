import pandas as pd

file_name = "2025년 폭력예방교육 이수명단(시립도서관).xlsx"

# 세 번째 행을 헤더로 지정하여 파일 읽기
df = pd.read_excel(file_name, header=2)

# 생년월일 열 데이터를 리스트 변수로 초기화
prev_births = df["생년월일"].tolist()
new_births = []

# 생년월일 열 데이터 수정 후 새 리스트에 저장
for prev_birth in prev_births:
    new_birth = prev_birth + "."
    new_births.append(new_birth)

# 기존 열 이름 리스트 가져오기
cols = list(df.columns)

# 이후 처리 작업 수행 (예: 데이터 총합 계산 등)
print(f"파일 {file_name} 처리 완료. 열 이름: {df.columns.tolist()}")

# 처리한 결과를 새로운 파일로 저장
df.to_excel("processed_" + file_name, index=False)