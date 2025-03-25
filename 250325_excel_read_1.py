import pandas as pd
import glob

# "processed_"로 시작하는 모든 엑셀 파일 목록 가져오기
file_pattern = "processed_*.xlsx"
files = glob.glob(file_pattern)

# 결과 리스트 초기화
results = []

for file in files:
    # 엑셀 파일 읽기 (첫 번째 시트 사용)
    df = pd.read_excel(file)
    
    # 헤더를 제외한 행의 개수(데이터 행 수)
    count = len(df)
    
    # "실적시간" 열의 합계 (숫자형 변환 후 합산)
    if "실적시간" in df.columns:
        total1 = pd.to_numeric(df["실적시간"], errors="coerce").sum()
    else:
        total1 = 0
    
    # "Unnamed: 18" 열의 합계 (숫자형 변환 후 합산)
    if "Unnamed: 18" in df.columns:
        total2 = pd.to_numeric(df["Unnamed: 18"], errors="coerce").sum()
    else:
        total2 = 0
    
    # 결과를 딕셔너리 형태로 리스트에 저장
    result_dict = {
        "파일명": file,
        "행개수": count,
        "total1": total1,
        "total2": total2
    }
    results.append(result_dict)

# 리스트를 데이터프레임으로 변환
df = pd.DataFrame(results)

# 결과를 엑셀 파일로 저장
df.to_excel("summary_totals.xlsx", index=False)
print("결과를 엑셀 파일로 저장했습니다.")
