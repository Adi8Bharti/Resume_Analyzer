!pip install spacy
!python -m spacy download en_core_web_md

!pip install PyPDF2

from google.colab import files

uploaded = files.upload()  # Opens file picker
filename = list(uploaded.keys())[0]  # Get uploaded PDF name

import PyPDF2

resume_text = ""

with open(filename, "rb") as f:  # "rb" = read binary
    reader = PyPDF2.PdfReader(f)
    for page in reader.pages:
        text = page.extract_text()
        if text:  # sometimes extract_text() can return None
            resume_text += text + "\n"

print(resume_text[:5000])  # preview first 500 characters

import spacy
nlp = spacy.load("en_core_web_md")
resume_doc = nlp(resume_text)

skills = [
    "python", "sql", "aws", "java", "machine learning",
    "power bi", "excel", "tableau", "javascript", "react",
    "html", "css", "docker", "kubernetes", "git", "linux",
    "c++", "c#", "node.js", "django", "flask", "tensorflow",
    "pytorch", "nlp", "data analysis", "data visualization",
    "big data", "hadoop", "spark", "rest api", "cloud",
    "problem solving", "deep learning", "sql server", "oracle",
    "mongodb", "postgresql", "jira", "agile", "scrum", "ci/cd"
]

matched_skills = []

for skill in skills:
    skill_doc = nlp(skill)
    similarity = resume_doc.similarity(skill_doc)
    if similarity > 0.75:
        matched_skills.append(skill)

print("Matched skills:", matched_skills)

education_scores = {'phd': 10, 'masters': 7, 'bachelors': 5, 'diploma': 3}
education_level = input("Enter education level: ")
edu_score = education_scores.get(education_level.lower(), 0)

experience_years = float(input("Enter years of experience: "))
if experience_years >= 5: exp_score = 10
elif experience_years >= 3: exp_score = 7
elif experience_years >= 1: exp_score = 5
else: exp_score = 2

skill_score = len(matched_skills) * 5
total_score = skill_score + edu_score + exp_score

print("\nTotal Score:", total_score)

if total_score >= 35:
    print("Decision: Strong Candidate ✅")
elif total_score >= 20:
    print("Decision: Moderate Candidate ⚠️")
else:
    print("Decision: Weak Candidate ❌")
