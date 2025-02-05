import pandas as pd
import glob

# "processed_"로 시작하는 모든 .xlsx 파일 찾기
files = glob.glob("processed_*.xlsx")

# 전체 합계를 저장할 변수 초기화
global_total1 = 0
global_total2 = 0

# 각 파일의 합계 결과를 저장할 리스트 초기화
results = []

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

    # 파일 이름과 두 합계를 딕셔너리 형태로 저장
    results.append({"파일명": file, "total1": total1, "total2": total2})

    print(f"{file} -> 실적시간 합계: {total1}, Unnamed: 18 합계: {total2}")

    # 전체 합계에 누적
    global_total1 += total1
    global_total2 += total2

# 결과 리스트를 데이터프레임으로 변환합니다.
summary_df = pd.DataFrame(results)

# 데이터프레임 내용 확인 (원하는 경우)
print(summary_df)

# summary_totals.xlsx라는 이름으로 결과 엑셀 파일을 생성합니다.
summary_df.to_excel("summary_totals.xlsx", index=False)

print("전체 파일의 실적시간 총합:", global_total1)
print("전체 파일의 Unnamed: 18 총합:", global_total2)