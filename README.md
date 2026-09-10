# 🤖 AI-Powered Resume Analysis & Job Matching System

> An AI-powered web application that analyzes resumes against job descriptions and provides intelligent insights such as match score, strengths, missing skills, and personalized improvement recommendations.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-orange)
![PyPDF2](https://img.shields.io/badge/PDF-PyPDF2-green)
![GitHub](https://img.shields.io/badge/Version%20Control-GitHub-black?logo=github)

---

## 📌 Overview

The **AI-Powered Resume Analysis & Job Matching System** is a Generative AI-based application designed to help candidates understand how well their resume aligns with a specific job description.

The system allows users to:

* Upload a resume in PDF format
* Enter a target job title
* Enter a complete job description
* Analyze the resume using Google Gemini AI
* Generate a job match score
* Identify resume strengths
* Detect missing skills
* Receive personalized improvement recommendations
* Ask follow-up questions through an AI Resume Assistant
* Download the generated analysis report

The project demonstrates the practical application of **Generative AI, prompt engineering, API integration, PDF processing, and Streamlit application development**.

---

## 🎯 Problem Statement

Candidates often apply for multiple jobs without knowing how closely their resume matches the requirements of a particular role.

They may struggle to:

* Evaluate resume relevance for a specific job
* Identify missing skills
* Understand their strengths and weaknesses
* Optimize their resume for different job roles
* Tailor their resume according to job requirements

Manual resume evaluation can be time-consuming and subjective.

Therefore, this project provides an **AI-powered solution for resume analysis and job matching** that generates actionable feedback based on the resume and target job description.

---

## ✨ Key Features

### 📄 Resume PDF Processing

* Upload resumes directly in PDF format
* Extract resume text using **PyPDF2**
* Display extracted resume information
* Show page count and extracted character count

### 💼 Job Description Analysis

Users can provide:

* Target Job Title
* Complete Job Description

The system uses these inputs to evaluate how relevant the uploaded resume is for the selected role.

### 🧠 AI-Powered Resume Evaluation

Using **Google Gemini 2.5 Flash**, the application generates:

* 📊 Job Match Score
* ✅ Resume Strengths
* ❌ Missing Skills
* 💡 Improvement Recommendations

### 📊 Match Analysis

The application provides an AI-generated compatibility score based on factors such as:

* Skills
* Experience
* Qualifications
* Job requirements
* Relevant resume content

### 💡 Personalized Recommendations

The system provides suggestions to help candidates improve and tailor their resumes according to the target job.

### 💬 Interactive AI Resume Assistant

Users can ask follow-up questions about:

* Resume content
* Job description
* Match score
* Missing skills
* Resume improvements
* Career-related suggestions

### 📥 Download Analysis Report

Users can download the generated resume analysis as a text report for future reference.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │        User          │
                    │ Resume + Job Details │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Streamlit Web UI  │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌──────────────────┐         ┌──────────────────┐
       │   Resume PDF     │         │ Job Description  │
       │     Upload       │         │      Input       │
       └────────┬─────────┘         └────────┬─────────┘
                │                            │
                ▼                            │
       ┌──────────────────┐                  │
       │     PyPDF2       │                  │
       │  Text Extraction │                  │
       └────────┬─────────┘                  │
                │                            │
                └─────────────┬──────────────┘
                              ▼
                   ┌──────────────────────┐
                   │   Prompt Engineering │
                   │ Resume + Job Context │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │   Google Gemini AI   │
                   │   Gemini 2.5 Flash   │
                   └──────────┬───────────┘
                              │
                              ▼
              ┌──────────────────────────────┐
              │        AI Analysis           │
              │                              │
              │ • Match Score                │
              │ • Strengths                  │
              │ • Missing Skills             │
              │ • Improvement Suggestions    │
              └──────────────┬───────────────┘
                             │
                             ▼
                   ┌──────────────────────┐
                   │ Results + AI Chat    │
                   └──────────────────────┘
```

A detailed architecture reference is available in:

`assets/architecture.md`

---

## 🔄 How It Works

### Step 1 — Upload Resume

The user uploads a resume in PDF format through the Streamlit interface.

### Step 2 — Extract Resume Text

**PyPDF2** extracts textual information from the uploaded PDF.

### Step 3 — Enter Job Information

The user provides:

* Target Job Title
* Job Description

### Step 4 — Send Data to Gemini

The extracted resume content and job requirements are provided to the **Gemini 2.5 Flash** model through the Google Generative AI API.

### Step 5 — AI Analysis

Gemini analyzes the relationship between the candidate's resume and the target job requirements.

### Step 6 — Generate Insights

The system generates:

```text
Resume
   +
Job Description
   ↓
AI Analysis
   ↓
Match Score
   ↓
Strengths
   ↓
Missing Skills
   ↓
Improvement Suggestions
```

### Step 7 — Interactive Chat

After analysis, users can ask additional questions through the built-in AI Resume Assistant.

---

## 🛠️ Technology Stack

| Technology                  | Purpose                             |
| --------------------------- | ----------------------------------- |
| **Python**                  | Core application development        |
| **Streamlit**               | Web application interface           |
| **Google Gemini 2.5 Flash** | Generative AI analysis              |
| **google-generativeai**     | Gemini API integration              |
| **PyPDF2**                  | PDF text extraction                 |
| **HTML/CSS**                | UI customization                    |
| **Git & GitHub**            | Version control and project hosting |
| **Visual Studio Code**      | Development environment             |
| **Google AI Studio**        | Gemini API access                   |

---

## 🧠 AI & Prompt Engineering

The project uses **Generative AI and prompt engineering** to evaluate resumes against job descriptions.

The application provides the AI model with structured information containing:

* Target job role
* Job description
* Extracted resume content
* User's analysis question

The model is instructed to generate structured insights including:

1. Match Score
2. Strengths
3. Missing Skills
4. Resume Improvement Suggestions

This demonstrates how Large Language Models can be integrated into a practical career-oriented application.

---

## 📊 Sample Analysis Output

Example:

```text
MATCH SCORE: 82%

✅ STRENGTHS
- Strong Python knowledge
- Relevant data analysis experience
- Experience with machine learning
- Good technical project exposure

❌ MISSING SKILLS
- SQL optimization
- Advanced Excel
- Business intelligence tools

💡 IMPROVEMENT SUGGESTIONS
- Add SQL-based projects
- Highlight measurable project outcomes
- Include relevant analytical tools
- Tailor technical skills to the job description
```

> Note: The actual output varies depending on the uploaded resume and job description.

---

## 💬 AI Resume Assistant

The application includes an interactive chatbot that allows users to ask contextual questions after the resume analysis.

Example questions:

```text
What skills am I missing for this job?

How can I improve my resume?

Which skills should I highlight?

Why is my match score low?

What projects should I add?

How can I make my resume more ATS-friendly?
```

The assistant uses the relevant resume information and generated analysis to provide contextual responses.

---

## 🎥 Project Demo

A complete walkthrough of the application is available in the project demo video.

### Demo Includes

1. Resume PDF upload
2. Resume text extraction
3. Job title and job description input
4. Gemini-powered resume analysis
5. Match score generation
6. Strength identification
7. Missing skill detection
8. Improvement recommendations
9. Interactive AI Resume Assistant

> **Security Note:** API keys and other credentials should never be included in public screenshots, videos, source code, or GitHub commits.

---

## 📑 Project Presentation

Project presentation files can be added to the `docs/` folder when available.

Recommended structure:

```text
docs/
├── AI_Resume_Analyzer_Presentation.pdf
└── AI_Resume_Analyzer_Presentation.pptx
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/HeetJain-09/AI-Powered-Resume-Analysis-and-Job-Matching-System.git
```

### 2. Navigate to the Project

```bash
cd AI-Powered-Resume-Analysis-and-Job-Matching-System
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Configuration

This application requires a **Google Gemini API key**.

The application accepts the API key through the Streamlit interface.

### ⚠️ Security

**Never commit your real API key to GitHub.**

Avoid hard-coding secrets such as:

```python
api_key = "YOUR_REAL_API_KEY"
```

Do not upload:

* API keys
* Passwords
* Authentication tokens
* Private credentials
* Sensitive personal information

For public demonstrations, use sample or anonymized resume data.

---

## ▶️ Running the Application

Run the Streamlit application using:

```bash
streamlit run resume_analyzer.py
```

After starting the application, open the local Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

---

## 📁 Project Structure

```text
AI-Powered-Resume-Analysis-and-Job-Matching-System/
│
├── .devcontainer/
│
├── AI-Resume-Analyzer-main/
│   └── resume_analyzer.py
│
├── assets/
│   └── architecture.md
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Optional Portfolio Assets

The repository can also include:

```text
├── demo/
│   └── Resume_Analyzer_GitHub.mp4
│
├── screenshots/
│   ├── home.png
│   ├── resume-upload.png
│   ├── analysis-results.png
│   └── chatbot.png
│
└── docs/
    ├── AI_Resume_Analyzer_Presentation.pdf
    └── AI_Resume_Analyzer_Presentation.pptx
```

---

## 💼 Internship Project Context

### Artificial Intelligence & Machine Learning Intern

**Edunet Foundation — Remote**
**January 2026 – February 2026**

This project was developed during an Artificial Intelligence and Machine Learning internship as a practical application of Generative AI concepts.

### Key Contributions

* Developed an AI-powered Resume Analysis and Job Matching System using Python, Streamlit, and Google Gemini API.
* Built an end-to-end application to extract resume content from PDF files and evaluate candidate profiles against job descriptions.
* Implemented AI-driven resume evaluation for match scoring, strengths identification, missing-skill detection, and personalized improvement recommendations.
* Integrated an interactive AI Resume Assistant for resume and career-related queries.
* Applied prompt engineering and API integration techniques.
* Developed a practical AI web application under industry mentorship.

---

## 🎓 Learning Outcomes

Through this project, the following concepts were practically implemented:

* Generative AI Application Development
* Large Language Model Integration
* Prompt Engineering
* Google Gemini API Integration
* PDF Text Extraction
* Python Application Development
* Streamlit Web Application Development
* Session State Management
* API Error Handling
* AI-powered Chatbot Development
* Git & GitHub
* Project Documentation

---

## 🚀 Future Enhancements

Potential future improvements include:

* 🎯 ATS keyword analysis
* 📑 Resume section-wise scoring
* 🔎 Automatic job recommendations
* 📝 AI-powered resume rewriting
* 📊 Skill-gap visualization
* 🔗 LinkedIn profile integration
* 📚 Skill and course recommendations
* 📈 Multiple job comparison
* 📄 Professional resume generation
* ☁️ Cloud deployment
* 🔐 Secure environment-based API configuration
* 🗃️ Resume history and comparison

---

## 🔐 Privacy & Security

This project is intended for educational and demonstration purposes.

Users should avoid uploading resumes containing highly sensitive personal information when using publicly accessible deployments.

### Important

* Do not commit API keys.
* Do not upload passwords or credentials.
* Do not include sensitive personal data in screenshots or demo videos.
* Use sample or anonymized resumes for public demonstrations.

---

## 📌 Limitations

The generated match score is an **AI-generated estimate**, not an official ATS score or hiring decision.

Results may vary depending on:

* Resume quality
* Job description quality
* Extracted PDF text
* Prompt context
* AI model interpretation

The system should therefore be used as a **resume improvement and job-matching assistant**, rather than as a definitive recruitment evaluation system.

---

## 📈 Project Impact

The system provides candidates with a quick way to understand the alignment between their resume and a target job description.

The overall workflow can be summarized as:

```text
Resume
   ↓
Job Description
   ↓
AI Comparison
   ↓
Match Score
   ↓
Skill Gap Analysis
   ↓
Personalized Recommendations
   ↓
Better Resume
```

---

## 🏆 Project Highlights

* 🤖 Generative AI-powered application
* 🧠 Google Gemini 2.5 Flash integration
* 📄 Automated PDF resume processing
* 📊 AI-based job matching
* 💡 Personalized recommendations
* 💬 Interactive AI Resume Assistant
* 🌐 Streamlit web interface
* 🔌 Google Gemini API integration
* 🐍 Python-based application
* 📚 Developed during AI & ML internship

---

## 👨‍💻 Author

### Heet Jain

**Artificial Intelligence & Machine Learning Enthusiast**

**Project:** AI-Powered Resume Analysis & Job Matching System

Developed during an **AI & Machine Learning Internship at Edunet Foundation**.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
