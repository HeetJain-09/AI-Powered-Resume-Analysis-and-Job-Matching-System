import streamlit as st
import PyPDF2
import google.generativeai as genai

st.set_page_config(page_title="AI Resume Matcher",page_icon="📄",layout="wide")

if "resume_text" not in st.session_state: st.session_state.resume_text=""
if "result" not in st.session_state: st.session_state.result=""
if "chat_history" not in st.session_state: st.session_state.chat_history=[]

st.markdown("""
<style>
.result-box{padding:20px;background:#e8f5e8;border-left:5px solid #4CAF50;border-radius:8px;}
</style>
""",unsafe_allow_html=True)

def extract_pdf(pdf_file):
    reader=PyPDF2.PdfReader(pdf_file)
    text=""
    for page in reader.pages:
        if page.extract_text():
            text+=page.extract_text()+"\n"
    return text

@st.cache_resource
def load_ai(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")

def get_ai_response(model,prompt):
    try:
        response=model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Gemini Error:\n\n{str(e)}"

st.title("🔍 AI Resume Matcher")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ Setup")
    api_key=st.text_input("Gemini API Key",type="password")
    if api_key:
        try:
            st.session_state.model=load_ai(api_key)
            st.success("✅ Ready!")
        except Exception:
            st.error("❌ Invalid API Key")

col1,col2=st.columns([1,1])

with col1:
    st.subheader("📄 Upload Resume")
    pdf_file=st.file_uploader("Choose PDF",type="pdf")
    if pdf_file:
        st.session_state.resume_text=extract_pdf(pdf_file)
        st.success("✅ Extracted!")
        with st.expander("Preview"):
            st.text(st.session_state.resume_text[:500])

with col2:
    st.subheader("💼 Job Details")
    job_title=st.text_input("Job Title",value="Data Analyst Intern")
    job_desc=st.text_area("Job Description",height=180)

if st.button("🚀 ANALYZE RESUME"):
    model=st.session_state.get("model")

    if model and st.session_state.resume_text and job_desc:
        with st.spinner("AI analyzing..."):
            prompt=f"""
Analyze this resume for the job.

Job Title:
{job_title}

Job Description:
{job_desc[:1000]}

Resume:
{st.session_state.resume_text[:2000]}

Give:
1. MATCH SCORE (0-100%)
2. STRENGTHS
3. MISSING SKILLS
4. IMPROVEMENT SUGGESTIONS
5. FINAL RECOMMENDATION
"""
            st.session_state.result=get_ai_response(model,prompt)
    else:
        st.error("⚠️ Need API Key + Resume + Job Description")

tab1,tab2=st.tabs(["📊 Results","💬 Chat"])

with tab1:
    if st.session_state.result:
        st.markdown("### 📊 Analysis Results")
        st.markdown(f'<div class="result-box">{st.session_state.result}</div>',unsafe_allow_html=True)

with tab2:
    st.markdown("### 💬 Ask about your analysis")

    model=st.session_state.get("model")

    if model and st.session_state.result:

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["text"])

        user_q=st.chat_input("Ask anything about analysis...")

        if user_q:
            st.session_state.chat_history.append({"role":"user","text":user_q})

            with st.chat_message("user"):
                st.write(user_q)

            prompt=f"""
Analysis:
{st.session_state.result}

Resume:
{st.session_state.resume_text[:1000]}

Question:
{user_q}

Answer clearly.
"""

            with st.chat_message("assistant"):
                answer=get_ai_response(model,prompt)
                st.write(answer)
                st.session_state.chat_history.append({"role":"assistant","text":answer})

    else:
        st.info("Analyze resume first.")