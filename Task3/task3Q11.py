#Q11)  Given a dictionary of student names and their scores, write a program to find the 
#student with the highest score and return their name and score. 

def highest_scoring_student(scores_dict):
    if not scores_dict:
        return "No students"
    
    highest_student = max(scores_dict, key=scores_dict.get)
    return highest_student, scores_dict[highest_student]

students_scores = {
    "Novel": 85,
    "Kushal": 92,
    "Ashutosh": 88,
    "Nitin": 79
}

name, score = highest_scoring_student(students_scores)
print(f"Highest scoring student: {name} with score {score}")
