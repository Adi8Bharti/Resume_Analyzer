Resume_Analyzer/
├── Resume_Analyzer.ipynb      # Main Colab notebook / Python script
├── requirements.txt           # Python dependencies
├── flowchart.png              # Project flow diagram
└── README.md                  # Project description & instructions

Flow Diagram:

+-----------------+
|  Upload Resume  |
+--------+--------+
         |
         v
+-----------------+
| Extract Text    | (PDF/TXT)
+--------+--------+
         |
         v
+-----------------+
| Detect Skills   | (spaCy NLP)
+--------+--------+
         |
         v
+-----------------+
| Score Education |
+-----------------+
         |
         v
+-----------------+
| Score Experience|
+-----------------+
         |
         v
+-----------------+
|  Total Score    |
+--------+--------+
         |
         v
+-----------------+
| Candidate Class |
| Strong/Moderate |
| Weak            |
+-----------------+
