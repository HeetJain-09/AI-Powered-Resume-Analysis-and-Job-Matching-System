# 🤖 AI-Powered Resume Analysis & Job Matching System

> A Generative AI-powered web application that analyzes resumes against job descriptions and provides match scores, strengths, missing skills, and personalized improvement recommendations.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange)
![PyPDF2](https://img.shields.io/badge/PDF-PyPDF2-green)

---

## 📌 Overview

The **AI-Powered Resume Analysis & Job Matching System** helps candidates evaluate how well their resume matches a specific job role.

Users can:

* Upload a resume in PDF format
* Enter a target job title and description
* Generate an AI-based match score
* Identify resume strengths and missing skills
* Get personalized improvement suggestions
* Ask questions using the AI Resume Assistant
* Download the analysis report

The project demonstrates the practical use of **Generative AI, prompt engineering, PDF processing, API integration, and Streamlit development**.

---

## ✨ Key Features

### 📄 Resume Analysis

* PDF resume upload
* Text extraction using **PyPDF2**
* Resume content analysis

### 💼 Job Matching

* Target job title and description input
* AI-based resume-to-job comparison
* Match score generation

### 🧠 AI Insights

* Resume strengths
* Missing skills
* Improvement recommendations
* Job-specific feedback

### 💬 AI Resume Assistant

Interactive AI assistant for questions related to:

* Resume improvements
* Missing skills
* Match score
* Job requirements
* ATS optimization

### 📥 Report Generation

Download the generated resume analysis report.

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Web Interface
  │
  ├── Resume PDF ──► PyPDF2 ──► Resume Text
  │
  └── Job Title + Description
                │
                ▼
        Prompt Engineering
                │
                ▼
       Google Gemini 2.5 Flash
                │
                ▼
          AI Resume Analysis
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
    Match    Missing   Improvement
     Score    Skills   Suggestions
                │
                ▼
        Results + AI Assistant
```

Detailed architecture: [`assets/architecture.md`](assets/architecture.md)

---

## 🛠️ Technology Stack

| Technology                  | Purpose                    |
| --------------------------- | -------------------------- |
| **Python**                  | Application development    |
| **Streamlit**               | Web application UI         |
| **Google Gemini 2.5 Flash** | AI-powered resume analysis |
| **google-generativeai**     | Gemini API integration     |
| **PyPDF2**                  | PDF text extraction        |
| **HTML/CSS**                | UI customization           |
| **Git & GitHub**            | Version control            |

---

## 🧠 AI & Prompt Engineering

The application sends structured context to **Gemini 2.5 Flash**, including:

* Target job role
* Job description
* Extracted resume content
* User's analysis query

The model generates:

1. Match Score
2. Resume Strengths
3. Missing Skills
4. Improvement Recommendations

This demonstrates practical **LLM integration and prompt engineering** in a career-focused application.

---

## 🎥 Demo

A complete walkthrough demonstrates:

* Resume upload and text extraction
* Job description input
* Gemini-powered analysis
* Match score
* Strengths and missing skills
* Improvement recommendations
* AI Resume Assistant

**Demo Video:** `demo/Resume_Analyzer_GitHub.mp4`

---

## 📑 Project Presentation

The project presentation is available in:

`docs/AI_RESUME_JOB_MATCHING.pptx`

---

## 🎓 Internship Project

### AI & Machine Learning Intern — Edunet Foundation

**Duration:** January 2026 – February 2026
**Mode:** Remote

This project was developed as part of an **Artificial Intelligence & Machine Learning internship**, applying Generative AI concepts to a practical resume analysis and job-matching use case.

### Key Contributions

* Developed an AI-powered resume analysis application using **Python, Streamlit, and Google Gemini API**.
* Implemented PDF resume text extraction using **PyPDF2**.
* Built AI-based resume and job-description matching functionality.
* Generated match scores, strengths, missing skills, and improvement recommendations.
* Integrated an interactive **AI Resume Assistant**.
* Applied prompt engineering and API integration techniques.
* Documented and presented the project as part of the internship.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/HeetJain-09/AI-Powered-Resume-Analysis-and-Job-Matching-System.git
cd AI-Powered-Resume-Analysis-and-Job-Matching-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Navigate to the folder containing `resume_analyzer.py` and run:

```bash
streamlit run resume_analyzer.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 🔑 Gemini API Configuration

The application requires a **Google Gemini API key**.

The API key is provided through the application interface.

⚠️ **Never commit real API keys, passwords, or credentials to GitHub.**

For public demonstrations, use sample or anonymized resume data.

---

## 📁 Project Structure

```text
AI-Powered-Resume-Analysis-and-Job-Matching-System/
│
├── AI-Resume-Analyzer-main/
│   └── resume_analyzer.py
│
├── assets/
│   └── architecture.md
│
├── demo/
│   └── Resume_Analyzer_GitHub.mp4
│
├── docs/
│   └── AI_RESUME_JOB_MATCHING.pptx
│
├── .devcontainer/
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚠️ Limitations

The generated match score is an **AI-based estimate**, not an official ATS score or hiring decision.

Results may vary depending on:

* Resume quality and formatting
* Job description quality
* PDF text extraction
* AI model interpretation

The system should be used as a **resume improvement and job-matching assistant**, not as a definitive recruitment evaluation tool.

---

## 🚀 Future Scope

* ATS keyword analysis
* Resume section-wise scoring
* Automatic job recommendations
* AI-powered resume rewriting
* Skill-gap visualization
* Multiple job comparison
* Cloud deployment

---

## 👨‍💻 Author

### Heet Jain

**B.E. — Artificial Intelligence & Data Science**

Interested in **Data Science, Generative AI, and AI-powered applications**.

**Project developed during:**
AI & Machine Learning Internship — **Edunet Foundation**

---

⭐ If you find this project useful, consider starring the repository.
