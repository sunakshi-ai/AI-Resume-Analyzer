JOB_SKILLS = {
    "Data Scientist": [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Statistics",
        "Power BI",
        "Git"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "NLP",
        "Git",
        "AWS"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Statistics",
        "Pandas"
    ]
}


def get_missing_skills(job_role, user_skills):

    required = JOB_SKILLS[job_role]

    missing = []

    for skill in required:

        if skill not in user_skills:
            missing.append(skill)

    return missing