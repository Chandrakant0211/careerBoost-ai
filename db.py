# db.py

ROLE_SKILLS = {
    "web development": [
        "html", "css", "javascript", "react",
        "node", "git", "sql", "rest api",
        "agile", "communication", "teamwork"
    ],
    "android app development": [
        "java", "kotlin", "android studio",
        "xml", "firebase", "rest api",
        "git", "sqlite", "material design",
        "problem solving"
    ],
    "data science": [
        "python", "machine learning",
        "pandas", "numpy", "statistics",
        "sql", "data visualization",
        "communication"
    ],
    "java developer": [
        "java", "spring boot", "hibernate",
        "sql", "rest api", "git",
        "agile", "problem solving"
    ]
}

# Master Skill List
ALL_SKILLS = set(skill for skills in ROLE_SKILLS.values() for skill in skills)