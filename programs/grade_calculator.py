def get_grade(maths_mark, chemistry_mark, physics_mark):

    total_marks = sum((maths_mark, chemistry_mark, physics_mark))
    percentage = round(total_marks / 3, 2)

    results = {70: "A", 60: "B", 50: "C", 40: "D"}

    for boundary, result in results.items():
        if percentage >= boundary:
            return result

    else:
        return "You failed"
