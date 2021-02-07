def calculate_grade(score):
    grade = (
        "A"
        if score >= 80
        else "B+"
        if score >= 75
        else "B"
        if score >= 70
        else "C+"
        if score >= 65
        else "C"
        if score >= 60
        else "D+"
        if score >= 55
        else "D"
        if score >= 50
        else "F"
    )
    return grade


score = int(input("Enter your score: "))
print("grade: " + calculate_grade(score))
