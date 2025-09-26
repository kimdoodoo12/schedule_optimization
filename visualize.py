import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Rectangle
# Windows: 'Malgun Gothic'
plt.rcParams['font.family'] = 'Malgun Gothic'

# macOS: 'AppleGothic'
# plt.rcParams['font.family'] = 'AppleGothic'
# Linux (예: Ubuntu): 나눔폰트가 설치되어 있다면
# plt.rcParams['font.family'] = 'NanumGothic'

# 마이너 경고 제거 (음수 기호 깨짐 방지)
plt.rcParams['axes.unicode_minus'] = False

def visualize_timetable(timetable):
    # 요일과 교시 범위 정의
    days = ["월", "화", "수", "목", "금"]
    periods = list(range(1, 13))  # 1교시 ~ 12교시
    
    #그래프 크기 설정 (가로 10, 세로 6)
    fig, ax = plt.subplots(figsize=(10, 6))

    # x축 요일 설정, y축 교시 설정
    ax.set_xlim(0, len(days))
    ax.set_ylim(0, len(periods))
    
    # 가로 세로 격자선 그리기 (요일별, 교시별 구분선)
    for x in range(len(days) + 1):
        ax.axvline(x, color='gray', linewidth=0.5)
    for y in range(len(periods) + 1):
        ax.axhline(y, color='gray', linewidth=0.5)

    # x축 눈금 위치와 레이블 설정
    ax.set_xticks([i + 0.5 for i in range(len(days))])
    ax.set_xticklabels(days)
    # x축 레이블과 눈금을 위쪽으로 이동
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()
    # y축 눈금 위치와 레이블 설정
    ax.set_yticks([i + 0.5 for i in range(len(periods))])
    ax.set_yticklabels([f"{p}교시" for p in periods])

    # 시간표에 강의 정보 배치
    for lecture in timetable:
        day_idx = days.index(lecture["요일"])
        start = lecture["시작교시"] - 1
        end = lecture["종료교시"]

        height = end - start # 강의가 차지하는 교시 수

        # 강의 시간에 맞게 사각형 블록 생성
        rect = Rectangle(
            (day_idx, start),   # 위치 (요일 인덱스, 시작 교시)
            1,                  # 폭: 1일 (요일 1칸)
            height,             # 높이: 수업 길이(교시 수)
            facecolor='skyblue',# 배경색
            edgecolor='black',  # 테두리 색
            linewidth=1         # 테두리 굵기
        )
        ax.add_patch(rect)      #그래프 사각형 추가

        # 텍스트 중앙에 배치
        ax.text(
            day_idx + 0.5,                              # x 좌표: 칸 중앙
            start + height / 2,                         # y 좌표: 강의 시간 절반 위치 (중앙)
            f"{lecture['강의명']}\n{lecture['교수명']}",  # 텍스트 내용
            ha='center',                                # 가로 정렬 중앙
            va='center',                                # 세로 정렬 중앙
            fontsize=9                                  # 글자 크기
        )

    # y축 방향 뒤집기 (1교시가 위로 오도록)
    ax.invert_yaxis()
    # 그래프 제목 설정
    ax.set_title("최적 시간표", fontsize=16)
    #레이아웃 자동 조정 (여백 등)
    plt.tight_layout()
    #화면에 그래프 출력
    plt.show()
