import pandas as pd
import glob

# "processed_"로 시작하는 모든 .xlsx 파일 찾기
files = glob.glob("processed_*.xlsx")

# 전체 합계를 저장할 변수 초기화
global_total1 = 0
global_total2 = 0

for file in files:
    # 엑셀 파일 읽기 (header는 첫 번째 행)
    df = pd.read_excel(file, header=0)
    
    # "실적시간" 열의 데이터를 숫자형으로 변환 후 합계 계산 (오류 발생 시 NaN은 무시)
    if "실적시간" in df.columns:
        total1 = pd.to_numeric(df["실적시간"], errors='coerce').sum()
    else:
        total1 = 0
    
    # "Unnamed: 18" 열의 데이터를 숫자형으로 변환 후 합계 계산
    if "Unnamed: 18" in df.columns:
        total2 = pd.to_numeric(df["Unnamed: 18"], errors='coerce').sum()
    else:
        total2 = 0

    print(f"{file} -> 실적시간 합계: {total1}, Unnamed: 18 합계: {total2}")

    # 전체 합계에 누적
    global_total1 += total1
    global_total2 += total2

print("전체 파일의 실적시간 총합:", global_total1)
print("전체 파일의 Unnamed: 18 총합:", global_total2)
