# System Architecture

```text
                    ┌──────────────────────┐
                    │      User             │
                    │ Resume + Job Details │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │    Web Interface     │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌──────────────────┐       ┌──────────────────┐
       │   PDF Resume     │       │ Job Description  │
       │    Upload        │       │      Input       │
       └────────┬─────────┘       └────────┬─────────┘
                │                          │
                ▼                          │
       ┌──────────────────┐                │
       │     PyPDF2       │                │
       │  Text Extraction │                │
       └────────┬─────────┘                │
                │                          │
                └────────────┬─────────────┘
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
              │       AI Analysis            │
              │                              │
              │ • Match Score                │
              │ • Strengths                  │
              │ • Missing Skills             │
              │ • Improvement Suggestions    │
              └──────────────┬───────────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │  Results Dashboard   │
                  │  + Resume Assistant  │
                  └──────────────────────┘
