def calculate_ats_score(skills):

    score = 0

    if len(skills) >= 15:
        score = 100
    elif len(skills) >= 12:
        score = 90
    elif len(skills) >= 10:
        score = 80
    elif len(skills) >= 8:
        score = 70
    elif len(skills) >= 5:
        score = 60
    elif len(skills) >= 3:
        score = 50
    else:
        score = 30

    return score