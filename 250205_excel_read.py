import pandas as pd
import glob
import warnings

# 특정 경고 메시지를 무시하도록 설정
warnings.filterwarnings("ignore", message="Workbook contains no default style, apply openpyxl's default")

# "교육훈련실적 내역"으로 시작하는 모든 .xlsx 파일 목록을 가져옵니다.
file_pattern = "교육훈련실적 내역*.xlsx"
file_list = glob.glob(file_pattern)

for file in file_list:
    # 두 번째 행을 헤더로 지정하여 파일을 읽어옵니다.
    df = pd.read_excel(file, header=1)
    
    # 기존 열 이름 리스트를 가져와서 새 이름을 생성합니다.
    cols = list(df.columns)
    new_cols = []
    prev_col = None
    suffix = 2

    for col in cols:
        if pd.isna(col):
            # 이전 유효한 열 이름이 없으면 기본 이름 사용, 있으면 이전 이름에 숫자(suffix)를 붙입니다.
            if prev_col is None:
                new_col = f"Unnamed{suffix}"
            else:
                new_col = f"{prev_col}{suffix}"
            suffix += 1
        else:
            new_col = col
            prev_col = col  # 유효한 열 이름을 저장
            suffix = 2     # 새 그룹 시작 시 suffix 초기화
        new_cols.append(new_col)

    # 새로 생성한 열 이름을 데이터프레임에 할당합니다.
    df.columns = new_cols
    
    # 이후 처리 작업 수행 (예: 데이터 총합 계산 등)
    print(f"파일 {file} 처리 완료. 열 이름: {df.columns.tolist()}")

    # 필요한 경우, 처리한 결과를 새로운 파일로 저장할 수 있습니다.
    df.to_excel("processed_" + file, index=False)
