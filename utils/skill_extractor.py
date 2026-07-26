SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "SQL",
    "MySQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node.js",
    "Git",
    "GitHub",
    "Excel",
    "Power BI",
    "TensorFlow",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "NLP",
    "AI",
    "AWS"
]

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills