# Schedule Optimization

University timetable optimization project using **Simulated Annealing**.  
The goal is to generate valid schedules with **15–18 credits** while minimizing **gaps between classes** and improving daily time distribution.

---

## Features
- Random initial schedule generation without overlapping classes
- Evaluation function based on:
  - Daily gaps (공강 최소화)
  - Time span of lectures (시간 분포 최소화)
- Neighbor state generation:
  - Remove one lecture and replace with a non-conflicting lecture
- Hybrid approach:
  - Duplicate handling with penalty in evaluation

---
