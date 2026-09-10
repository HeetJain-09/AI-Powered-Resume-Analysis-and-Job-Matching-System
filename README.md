# 🤖 AI-Powered Resume Analysis & Job Matching System

> An AI-powered web application that analyzes resumes against job descriptions and provides intelligent insights such as match score, strengths, missing skills, and personalized improvement recommendations.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Gemini AI](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-orange)
![PyPDF2](https://img.shields.io/badge/PDF-PyPDF2-green)
![AI](https://img.shields.io/badge/AI-Generative%20AI-purple)
![GitHub](https://img.shields.io/badge/Version%20Control-GitHub-black?logo=github)

---

## 📌 Overview

The **AI-Powered Resume Analysis & Job Matching System** is a Generative AI-based application designed to help candidates understand how well their resume aligns with a specific job description.

The system allows users to upload a resume in PDF format, enter a target job title and job description, and receive an AI-generated evaluation.

Using **Google Gemini 2.5 Flash**, the application analyzes the candidate's resume and identifies:

* 📊 Job Match Score
* ✅ Resume Strengths
* ❌ Missing Skills
* 💡 Resume Improvement Suggestions
* 💬 AI-powered Resume Assistant

The project demonstrates the practical application of **Generative AI, prompt engineering, API integration, PDF processing, and Streamlit application development**.

---

## 🎯 Problem Statement

In today's competitive job market, candidates often apply to multiple positions without knowing how closely their resumes match the requirements of a particular role.

Candidates may struggle to:

* Evaluate resume relevance for a specific job role
* Identify skills missing from their resume
* Understand their strengths and weaknesses
* Optimize resumes according to job requirements
* Tailor their resume for different job applications

Manual resume evaluation can be time-consuming and subjective.

Therefore, this project aims to provide an **automated AI-powered solution** that compares resume content with job requirements and generates actionable feedback.

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

The system uses these inputs to evaluate the relevance of the uploaded resume.

### 🧠 AI-Powered Resume Evaluation

Google's **Gemini 2.5 Flash** model analyzes the resume and job description to generate:

* Match Score
* Candidate Strengths
* Missing Skills
* Improvement Recommendations

### 📊 Match Analysis

The application provides an AI-generated compatibility score between the candidate profile and the target job.

The analysis considers factors such as:

* Skills
* Experience
* Job requirements
* Relevant qualifications
* Resume content

### 💡 Personalized Recommendations

The AI provides suggestions that can help candidates improve their resume for the selected job role.

### 💬 Interactive AI Resume Assistant

The application includes a chatbot that allows users to ask follow-up questions about:

* Resume
* Job description
* Analysis results
* Missing skills
* Career-related improvements

### 📥 Download Analysis Report

Users can download the generated resume analysis as a text report for future reference.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Streamlit Web UI   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Resume PDF Upload │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       PyPDF2        │
                    │  Text Extraction    │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │ Resume + Job Description       │
              │ + Job Title                    │
              └───────────────┬────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Google Gemini API   │
                    │ Gemini 2.5 Flash    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   AI Analysis        │
                    ├─────────────────────┤
                    │ Match Score          │
                    │ Strengths            │
                    │ Missing Skills       │
                    │ Improvement Tips     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Results + AI Chat    │
                    └─────────────────────┘
```

---

## 🔄 How It Works

### Step 1 — Upload Resume

The user uploads a resume in PDF format through the Streamlit interface.

### Step 2 — Extract Resume Text

The application uses **PyPDF2** to extract textual information from the uploaded PDF.

### Step 3 — Enter Job Information

The user enters:

* Job Title
* Job Description

### Step 4 — Send Data to Gemini

The extracted resume content and job requirements are provided to the **Gemini 2.5 Flash** model through the Google Generative AI API.

### Step 5 — AI Analysis

Gemini analyzes the relationship between the candidate's profile and the target job requirements.

### Step 6 — Generate Insights

The system generates:

```text
Match Score
     ↓
Strengths
     ↓
Missing Skills
     ↓
Improvement Suggestions
```

### Step 7 — Interactive Chat

The user can ask additional questions about the analysis through the built-in AI assistant.

---

## 🛠️ Technology Stack

| Technology                  | Purpose                             |
| --------------------------- | ----------------------------------- |
| **Python**                  | Core application development        |
| **Streamlit**               | Web application interface           |
| **Google Gemini 2.5 Flash** | Generative AI analysis              |
| **google-generativeai**     | Gemini API integration              |
| **PyPDF2**                  | Resume PDF text extraction          |
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

This approach demonstrates how Large Language Models can be integrated into practical career-oriented applications.

---

## 📊 Sample Analysis Output

The system generates an analysis similar to:

```text
MATCH SCORE: 82%

✅ STRENGTHS
- Strong Python knowledge
- Relevant data analysis experience
- Experience with machine learning
- Good technical project exposure

❌ MISSING
- SQL optimization
- Advanced Excel
- Business intelligence tools

➤ FIXES
- Add SQL-based projects
- Highlight measurable project outcomes
- Include relevant analytical tools
- Tailor technical skills to the job description
```

> Note: The actual output varies depending on the uploaded resume and job description.

---

## 💬 AI Resume Assistant

After the resume analysis is generated, users can interact with the built-in chatbot.

Example questions:

```text
What skills am I missing for this job?

How can I improve my resume?

Which skills should I highlight?

Why is my match score low?

What projects should I add?

How can I make my resume more ATS-friendly?
```

The chatbot uses the generated analysis and relevant resume information to provide contextual responses.

---


## 🎥 Project Demo

A complete walkthrough of the application is available below.

### ▶️ Demo Video

https://drive.google.com/file/d/1THIFxvg2eZzNVXhtbgEWB-wj28K1uHFx/view

The demonstration covers:

1. Gemini API configuration
2. Resume PDF upload
3. Resume text extraction
4. Job title and job description input
5. AI-powered resume analysis
6. Match score generation
7. Strength identification
8. Missing skill detection
9. Improvement recommendations
10. Interactive AI chatbot

---

## 📑 Project Presentation

The complete project presentation is available in the `docs` folder.

### Presentation

* [📄 Project Presentation – PDF](./docs/AI_Resume_Analyzer_Presentation.pdf)
* [📊 Project Presentation – PPTX](./docs/AI_Resume_Analyzer_Presentation.pptx)

The presentation covers:

* Problem Statement
* System Approach
* Technology Stack
* Algorithm & Working
* Deployment
* Results
* Future Scope

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd AI-RESUME-ANALYZER
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

You can obtain an API key through **Google AI Studio**.

After obtaining the key, enter it into the **Gemini API Key** field in the application's sidebar.

### ⚠️ Security Warning

**Never upload your API key to GitHub.**

Do not hard-code the API key inside Python files or commit it to the repository.

For example, avoid:

```python
api_key = "YOUR_REAL_API_KEY"
```

The current application accepts the API key through the Streamlit interface, helping prevent the key from being stored directly in the source code.

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run resume_analyzer.py
```

After starting the application, Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your web browser.

---

## 📁 Project Structure

```text
AI-RESUME-ANALYZER/
│
├── resume_analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
│
├── assets/
│   ├── project-banner.png
│   └── architecture.png
│
├── screenshots/
│   ├── home.png
│   ├── resume-upload.png
│   ├── analysis-results.png
│   └── chatbot.png
│
├── demo/
│   └── demo.mp4
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

During the internship, this project was developed as a practical application of Artificial Intelligence and Generative AI concepts.

Key contributions included:

* Developed an AI-powered Resume Analysis and Job Matching System using Python, Streamlit, and Google Gemini 2.5 Flash API.
* Built an end-to-end application to extract resume content from PDF files and evaluate candidate profiles against job descriptions.
* Implemented AI-driven resume evaluation for match scoring, missing-skill detection, strengths identification, and personalized improvement recommendations.
* Integrated an interactive AI chatbot for resume and career-related queries.
* Applied prompt engineering and API integration techniques.
* Developed a production-style AI web application under industry mentorship.

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

The project can be extended with additional features such as:

* 🎯 ATS keyword analysis
* 📑 Resume section-wise scoring
* 🔎 Automatic job recommendation
* 📝 AI-powered resume rewriting
* 📊 Skill-gap visualization
* 🔗 LinkedIn profile integration
* 📚 Skill/course recommendations
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

Results can vary depending on:

* Resume quality
* Job description quality
* Extracted PDF text
* Prompt context
* AI model interpretation

The system should therefore be used as a **resume improvement and job-matching assistant**, rather than as a definitive recruitment evaluation system.

---

## 📈 Project Impact

The system provides candidates with a quick way to understand the alignment between their resume and a target job description.

It helps users:

**Understand → Identify → Improve → Tailor**

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
* 🧠 Gemini 2.5 Flash integration
* 📄 Automated PDF resume processing
* 📊 AI-based job matching
* 💡 Personalized recommendations
* 💬 Interactive AI chatbot
* 🌐 Streamlit web interface
* 🔌 Google Gemini API integration
* 🐍 Python-based backend
* 📚 Developed during AI & ML internship

---

## 👨‍💻 Author

### Heet Jain

**Artificial Intelligence & Machine Learning Enthusiast**

### Project

**AI-Powered Resume Analysis & Job Matching System**

Developed during **AI & Machine Learning Internship at Edunet Foundation**.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

