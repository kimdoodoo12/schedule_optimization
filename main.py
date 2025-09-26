from load_data import load_data
from simulated_annealing import simulated_annealing
from visualize import visualize_timetable

if __name__ == "__main__":
    filepath = "C:\\Users\\User\\Downloads\\schedule_optimization\\scheduleTable.xlsx"  # 여기에 엑셀 파일 경로 넣기
    lecture_dict = load_data(filepath)
    best_schedule, best_score = simulated_annealing(lecture_dict)

    print(f"평가함수 점수 {best_score}")
    for info in best_schedule:
        print(f"{info['강의명']} ({info['분반']}): {info['요일']} {info['시작교시']}-{info['종료교시']}, {info['학점']}학점")

    visualize_timetable(best_schedule)