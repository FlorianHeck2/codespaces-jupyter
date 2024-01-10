def get_grade(score): 
    if score >= 60:
        if score >= 70:
            if score >= 80:
                if score >= 90:
                    return "A"
                return "B"
            return "C"
        return "D"

    print(get_grade(90))