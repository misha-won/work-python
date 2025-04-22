# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
import sys
from pathlib import Path

import pandas as pd

def detect_engine(path: Path, mode: str):
    ext = path.suffix.lower()
    if mode == 'read':
        if ext == '.xls':
            return 'xlrd'
        elif ext in ('.xlsx', '.xlsm', '.xlsb', '.odf', '.ods', '.odt'):
            return 'openpyxl'
    else:  # write
        if ext == '.xls':
            return 'xlwt'
        else:
            return 'openpyxl'
    raise ValueError(f"Unsupported file extension: {ext}")

def replace_first_col(val: str, new_ym: str) -> str:
    """
    "YYYY-MM-DD" 패턴의 맨 앞 'YYYY-MM' 부분만 new_ym 으로 바꿉니다.
    """
    if not isinstance(val, str):
        return val
    m = re.match(r'^(\d{4}-\d{2})-(\d{2})$', val)
    if m:
        day = m.group(2)
        return f"{new_ym}-{day}"
    return val

def fill_column7(row: pd.Series) -> str:
    """
    6번째 컬럼(0-based index=5) 값에 따라 7번째 컬럼(0-based index=6)에 채울 코드를 반환.
    """
    name = row.iat[5]
    if name == "고광용":
        return "A3000349"
    elif name == "정성환":
        return "A2103865"
    elif name == "황임중":
        return "A2601203"
    else:
        return row.iat[6]  # 원래 값 유지

def main():
    p = argparse.ArgumentParser(
        description="Excel 파일의 첫 열 날짜 변경 및 6→7열 코드 매핑"
    )
    p.add_argument("input_file",  help="입력할 Excel 파일 (.xls 또는 .xlsx)")
    p.add_argument("output_file", help="변경 후 저장할 Excel 파일 경로")
    p.add_argument(
        "new_year_month",
        help="새 연도‑월 (YYYY-MM 형식, 예: 2025-04)",
        type=str
    )
    args = p.parse_args()

    in_path  = Path(args.input_file)
    out_path = Path(args.output_file)
    new_ym   = args.new_year_month

    if not re.match(r'^\d{4}-\d{2}$', new_ym):
        print("ERROR: new_year_month는 YYYY-MM 형식이어야 합니다.", file=sys.stderr)
        sys.exit(1)

    # 1) 파일 읽기
    engine_read = detect_engine(in_path, mode='read')
    df = pd.read_excel(in_path, engine=engine_read, dtype=str)

    # 2) 첫 번째 열 날짜 치환
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda v: replace_first_col(v, new_ym))

    # 3) 6→7열 매핑
    df.iloc[:, 6] = df.apply(fill_column7, axis=1)

    # 결과 저장
    engine_write = detect_engine(out_path, mode='write')
    df.to_excel(out_path, index=False, engine=engine_write)

    print(f"✔ 변경 완료: {out_path}")

if __name__ == "__main__":
    main()
