import random;

# 초기상태 랜덤으로 생성
def create_initial_state(lecture_dict):
    selected_courses = []
    used_slots = set()
    total_credits = 0

    course_names = list(lecture_dict.keys())
    random.shuffle(course_names)

    for course_name in course_names:
        # 시간슬롯 중복 하드 제약 체크
        valid_sections = [sec for sec in lecture_dict[course_name] if not any(slot in used_slots for slot in sec["슬롯"])]
        if not valid_sections:
            continue
        chosen = random.choice(valid_sections)

        # 학점 초과 시 스킵
        if total_credits + chosen["학점"] > 18:
            continue
        
        # 선택한 강의 시간표 추가, 시간슬롯 업데이트, 누적학점 반영
        selected_courses.append(chosen)
        used_slots.update(chosen["슬롯"])
        total_credits += chosen["학점"]

        # 최소 15학점을 넘으면 초기상태 생성 완료 및 루프 종료
        if total_credits >= 15:
            break 
    #초기 시간표가 학점 15점이 못채워질 경우 예외
    if total_credits < 15:
        raise Exception("충분한 학점의 초기 상태 생성 실패")

    return selected_courses

# 평가함수
def evaluate(state):

    schedule = {}
    fatigue_penalty = 0 # 하루 피로도 페널티
    gap_penalty = 0 # 공강 페널티

    for course in state:
        day = course["요일"]
        start = course["시작교시"]
        end = course["종료교시"]
        schedule.setdefault(day, []).extend(range(start, end + 1))

    for periods in schedule.values():
        periods.sort()
        for i in range(len(periods) - 1):
            gap = periods[i + 1] - periods[i] - 1
            # 공강이 1교시이상 생기면 페널티 점수
            if gap > 0:
                gap_penalty += gap
        span = periods[-1] - periods[0] + 1
        # 하루 시간표가 6교시 이상이면 패널티 점수
        if span > 5:
            fatigue_penalty += (span - 5)
    # 총 평가점수 반환
    return gap_penalty + fatigue_penalty

# 이웃상태 생성
def get_neighbor(state, lecture_dict):
    for _ in range(100):  # 최대 100번 시도
        neighbor = state.copy()

        # 강의 하나를 랜덤 제거
        removed = random.choice(neighbor)
        neighbor.remove(removed)

        # 현재 상태에 없는 강의 목록
        used_courses = set(s["강의명"] for s in neighbor)
        candidate_courses = [c for c in lecture_dict if c not in used_courses]
        if not candidate_courses:
            continue

        # 아무 강의 하나 선택
        new_course = random.choice(candidate_courses)
        candidate_sections = lecture_dict[new_course]

        # 시간중복 체크
        used_slots = set(slot for s in neighbor for slot in s["슬롯"])
        valid_sections = [
            sec for sec in candidate_sections
            if not any(slot in used_slots for slot in sec["슬롯"])
        ]
        if not valid_sections:
            continue

        # 강의 하나 추가
        new_section = random.choice(valid_sections)
        neighbor.append(new_section)

        # 학점 조건
        total_credits = sum(s["학점"] for s in neighbor)
        if 15 <= total_credits <= 18:
            return neighbor

    return state  # 적절한 이웃 없으면 그대로 반환