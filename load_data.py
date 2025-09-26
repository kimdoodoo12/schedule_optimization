import pandas as pd
import random
import math

# 데이터 처리
def load_data(filepath):
    # 액셀 파일 불러오기
    df = pd.read_excel(filepath, engine="openpyxl")
    df = df.dropna(subset=["시작교시", "종료교시"])
    df["시작교시"] = df["시작교시"].astype(int)
    df["종료교시"] = df["종료교시"].astype(int)

    # 강의에 대해 요일, 교시 형태의 슬롯 리스트 생성
    def get_slots(row):
        return [f"{row['요일']}-{i}" for i in range(row["시작교시"], row["종료교시"] + 1)]
    # 요일과 시간대를 슬롯으로서 교체
    df["슬롯"] = df.apply(get_slots, axis=1)

    lecture_dict = {}
    for _, row in df.iterrows():
        entry = {
            "강의명": row["강의명"],
            "분반": row["분반"],
            "교수명": row["교수명"],
            "요일": row["요일"],
            "시작교시": row["시작교시"],
            "종료교시": row["종료교시"],
            "슬롯": row["슬롯"],
            "학점": row["학점"]
        }
        # 강의명을 기준으로 그룹화
        lecture_dict.setdefault(row["강의명"], []).append(entry)
    
    # 강의정보 반환
    return lecture_dict