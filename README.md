Resume Analyzer

AI-powered Python tool to analyze resumes, detect skills, score education & experience, and classify candidate strength.

Project Overview

The Resume Analyzer is a practical, AI-driven Python application designed to automate the resume screening process. Recruiters often spend hours manually reviewing resumes to identify suitable candidates. This project leverages Natural Language Processing (NLP) and Python programming to extract relevant information from resumes, calculate a candidate’s competency score, and classify them into strength categories: Strong, Moderate, or Weak.

The tool supports resumes in PDF and TXT formats and is capable of detecting both technical and soft skills. It calculates weighted scores for education, experience, and skills to produce an overall evaluation. By doing so, it simulates a real-world AI application for HR automation and improves efficiency in the candidate screening process.

This project demonstrates practical applications of AI in HR, along with advanced Python programming skills, file handling, and NLP implementation.

Features

Resume Parsing: Extract text content from PDF or TXT files.

Skill Detection: Detects technical and soft skills using NLP (spaCy).

Education & Experience Scoring: Assigns weighted scores based on predefined criteria.

Candidate Classification: Categorizes candidates as Strong, Moderate, or Weak.

Flexible Handling: Can process different resume formats and layouts with keyword fallback.

Real-world Application: Useful for HR automation in organizations, reducing manual effort.

#Tech Stack:

Python – Core programming language

spaCy – NLP for skill detection

PyPDF2 – PDF text extraction

pandas / NumPy – Data processing and scoring

Jupyter Notebook / Google Colab – Project execution environment

Project Structure
Resume_Analyzer/
├── Resume_Analyzer.ipynb      # Main Colab notebook / Python script
├── requirements.txt           # Python dependencies
└── README.md                  # Project description & instructions
