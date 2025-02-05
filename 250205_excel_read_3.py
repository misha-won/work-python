import pandas as pd
import glob

# 파일명이 "processed_"로 시작하고 파일명에 "사서"가 포함된 엑셀 파일 목록 가져오기
file_pattern = "processed_*사서*.xlsx"
files = glob.glob(file_pattern)

# 전체 필터링된 행 개수와 "실적시간" 합계를 누적할 변수 초기화
total_row_count = 0
total_time_sum = 0

# 각 파일별로 처리
for file in files:
    df = pd.read_excel(file)
    
    # 문자열 비교를 위해 해당 열들을 문자열로 변환한 후, na 값은 False 처리
    cond_edu = df["교육기관명"].astype(str).str.contains("도서관", na=False)
    cond_title = df["제목"].astype(str).str.contains("사서", na=False)
    cond_content = df["내용"].astype(str).str.contains("사서", na=False)
    
    # 조건: "교육기관명"에 "도서관"이 포함되거나, "제목" 또는 "내용"에 "사서"가 포함되는 행
    condition = cond_edu | cond_title | cond_content
    filtered_df = df[condition]
    
    # 필터링된 행 개수와 "실적시간" 열의 합계 계산
    row_count = len(filtered_df)
    time_sum = pd.to_numeric(filtered_df["실적시간"], errors="coerce").sum()
    
    total_row_count += row_count
    total_time_sum += time_sum

# 전체 결과 출력
print("전체 필터링된 행의 개수:", total_row_count)
print("전체 실적시간 합계:", total_time_sum)

# 결과를 하나의 엑셀 파일로 저장 (예: summary_filtered.xlsx)
result_df = pd.DataFrame({
    "필터링된 행 개수": [total_row_count],
    "실적시간 합계": [total_time_sum]
})
result_df.to_excel("summary_filtered.xlsx", index=False)