import math
import random
from state_and_evaluation import create_initial_state, evaluate, get_neighbor

#초기 온도 100, 감소비율 0.95, 반복 1000회
def simulated_annealing(lecture_dict, initial_temp=100.0, cooling_rate=0.95, iteration=1000):
    current = create_initial_state(lecture_dict)
    current_score = evaluate(current)
    temp = initial_temp
    best = current
    best_score = current_score

    for step in range(iteration):
        # 이웃 상태 생성 및 평가
        neighbor = get_neighbor(current, lecture_dict)
        neighbor_score = evaluate(neighbor)

        # 이웃 상태 갱신 조건
        delta = neighbor_score - current_score
        # 이웃상태가 더 좋은경우 수락, 나쁜 해여도 확률적으로 수락 
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = neighbor
            current_score = neighbor_score
            # 현재까지 최고의 상태를 저장
            if current_score < best_score:
                best = current
                best_score = current_score

        # 온도 감소
        temp *= cooling_rate
    # 최적해 및, 점수 반환
    return best, best_score