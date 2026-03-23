# Student Performance Analysis

## Project Overview

Exploratory data analysis of 1,000 student records to identify key factors
influencing academic performance across math, reading, and writing.

**Tools Used:** Python · Pandas · Matplotlib · Seaborn · Jupyter Notebook · VS Code

---

## Dataset

**Source:** [Students Performance Dataset – Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

**Size:** 1,000 rows × 8 columns

| Feature | Description|
|---|---|
| gender | Male / Female |
| race/ethnicity | Group A, B, C, D, E |
| parental level of education | Highest education level of parent |
| lunch | Standard or Free/Reduced |
| test preparation course | Completed or None |
| math score | Score out of 100 |
| reading score | Score out of 100 |
| writing score | Score out of 100 |

✅ No missing values found in this dataset.

---

## Key Findings

> **Note:** Gender and race/ethnicity columns were present in the dataset
> but were intentionally excluded from this analysis.
> This project focuses on academic and socioeconomic factors only.

**1. Test Preparation Course**
Students who completed the test prep course scored higher in all three subjects.
The benefit was strongest in reading and writing.

**2. Gender Differences**
Female students outperformed male students in reading and writing.
Male students had a slight advantage in math.

**3. Subject Correlations**
Reading and writing scores are strongly correlated (~0.95).
Math shows a moderate correlation with both (~0.80–0.82),
suggesting language skills share a common foundation.

**4. Parental Education**
Students whose parents held higher degrees scored slightly higher
across all subjects, especially in reading and writing.

**5. Lunch Type (Socioeconomic Indicator)**
Students with standard lunch consistently scored higher than
students on free/reduced lunch — suggesting economic background
influences academic outcomes.

---

## Project Structure
```
Student-Performance-Analysis/
│
├── data/
│   └── student_performance.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Naaz-Parween786/Student-Performance-Analysis.git
cd Student-Performance-Analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Open the notebook**
```bash
jupyter notebook notebooks/analysis.ipynb
```

---

## Requirements
```
pandas
matplotlib
seaborn
jupyter
```

---

## Author

**Naaz Parween** · BCA Honours, Ranchi University
[GitHub](https://github.com/Naaz-Parween786)
