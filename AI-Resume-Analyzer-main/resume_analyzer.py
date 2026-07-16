import streamlit as st
import PyPDF2
import google.generativeai as genai
import time

st.set_page_config(page_title="Resume Checker", page_icon="📄", layout="wide")

if 'resume_text' not in st.session_state: st.session_state.resume_text=""
if 'result' not in st.session_state: st.session_state.result=""
if 'chat_history' not in st.session_state: st.session_state.chat_history=[]

st.markdown("""
<style>
.result-box{
padding:18px;
background:#f8fff8;
border-left:6px solid #4CAF50;
border-radius:10px;
margin-top:10px;
margin-bottom:20px;
}
div.stButton>button{
width:100%;
height:45px;
border-radius:8px;
font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

def extract_pdf(pdf_file):
    reader=PyPDF2.PdfReader(pdf_file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()+"\n"
    return text

@st.cache_resource
def load_ai(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")

def get_ai_response(model,prompt):
    for i in range(3):
        try:
            return model.generate_content(prompt).text
        except:
            if i<2: time.sleep(2)
            else: return "❌ API error - check quota or key"

st.markdown("""
<div style="padding:15px;border-radius:10px;background:#f5f7fa;border:1px solid #ddd;">
<h2>🔍 AI Resume Matcher</h2>
<p style="color:gray;">Upload your resume, paste a job description and check your ATS match instantly.</p>
</div>
""",unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Setup")
    api_key=st.text_input("Gemini API Key",type="password")
    if api_key:
        try:
            st.session_state.model=load_ai(api_key)
            st.success("✅ Ready!")
        except:
            st.error("❌ Invalid key")

col1,col2=st.columns(2)

with col1:
    st.subheader("📄 Upload Resume")
    pdf_file=st.file_uploader("Choose PDF",type="pdf")
    if pdf_file:
        st.session_state.resume_text=extract_pdf(pdf_file)
        pages=len(PyPDF2.PdfReader(pdf_file).pages)
        chars=len(st.session_state.resume_text)
        st.success("✅ Resume Extracted!")
        a,b=st.columns(2)
        a.metric("Pages",pages)
        b.metric("Characters",chars)
        with st.expander("Preview"):
            st.text_area("",st.session_state.resume_text[:500],height=180)

with col2:
    st.subheader("💼 Job Details")
    job_title=st.text_input("Job Title",value="Data Analyst Intern")
    job_desc=st.text_area("Job Description",height=180)

if st.button("🚀 ANALYZE RESUME"):
    model=st.session_state.get("model")
    if model and st.session_state.resume_text and job_desc:
        with st.spinner("🤖 Gemini is analyzing your resume..."):
            prompt=f"""Job:{job_title}
Description:{job_desc[:700]}
Resume:{st.session_state.resume_text[:1400]}

Please give:
1.MATCH SCORE (0-100%)
2.✅ STRENGTHS
3.❌ MISSING
4.➤ FIXES
"""
            st.session_state.result=get_ai_response(model,prompt)
            st.markdown(f'<div class="result-box">{st.session_state.result}</div>',unsafe_allow_html=True)
    else:
        st.error("⚠️ Need: API Key + PDF + Job Description")

tab2,tab3=st.tabs(["📊 Results","💬 Chat"])

with tab2:
    if st.session_state.result:
        st.markdown("### 📊 Analysis Results")
        st.markdown(st.session_state.result)
        st.download_button("📥 Download Analysis Report",st.session_state.result,"resume_analysis.txt","text/plain")

with tab3:
    st.markdown("### 💬 Resume Assistant")
    st.caption("Ask questions about your analysis.")
    if st.session_state.result and st.session_state.get("model"):
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["text"])
        q=st.chat_input("Ask anything about the analysis...")
        if q:
            st.session_state.chat_history.append({"role":"user","text":q})
            with st.chat_message("user"):
                st.write(q)
            prompt=f"Analysis:{st.session_state.result}\nResume:{st.session_state.resume_text[:600]}\nQuestion:{q}"
            with st.chat_message("assistant"):
                with st.spinner():
                    ans=get_ai_response(st.session_state.model,prompt)
                    st.write(ans)
                    st.session_state.chat_history.append({"role":"assistant","text":ans})
