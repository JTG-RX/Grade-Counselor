import random
import formatter
import grade_analyzer
assignments = [
    {"name": "HW1", "score": 14, "max_score": 20, "weight": 0.1},
    {"name": "Quiz1", "score": 5, "max_score": 10, "weight": 0.05},
    {"name": "Exam1", "score": 25, "max_score": 50, "weight": 0.3},
    {"name": "Project", "score": 90, "max_score": 100, "weight": 0.55}
]


result = grade_analyzer.calculate_weighted_average(assignments)
print(formatter.CWA_Formater(result))

#make it so it can take inputs