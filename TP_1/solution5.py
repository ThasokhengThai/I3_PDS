def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90 or score<=96.9:
        return "A"
    elif score >= 80 or score<=89.9:
        return "B"
    elif score >= 70 or score<=79.9:
        return "C"
    elif score >= 60 or score<=69.9:
        return "D"
    else:
        return "F"

scores = [99, 90, 85.5, 72, 60, 59.9, -5, 101]

for score in scores:
    print(f"{score} -> {letter_grade(score)}")




#Methode2 using try and except  and for loop (for score in scores: to handle invalid input
def letter_grade(score):
    try:
        score = float(score)
        if score < 0 or score > 100:
            return "Invalid"
        elif score >= 97:
            return "A+"
        elif score >= 90 or score<=96.9:
            return "A"
        elif score >= 80 or score<=89.9:
            return "B"
        elif score >= 70 or score<=79.9:
            return "C"
        elif score >= 60 or score<=69.9:
            return "D"
        else:
            return "F"
    except ValueError:
        return "Invalid"
scores = [99, 90, 85.5, 72, 60, 59.9, -5, 101]
for score in scores:
    print(f"{score} -> {letter_grade(score)}")



