import streamlit as st
import spacy
import PyPDF2
import time

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract keywords from text using spaCy
def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return keywords

# Function to match keywords between resume and job description
def match_keywords(resume_keywords, job_keywords):
    matched_keywords = set(resume_keywords).intersection(set(job_keywords))
    return len(matched_keywords) / len(job_keywords) * 100 if job_keywords else 0

# Streamlit app title and description
st.title("📝 ATS Keyword Matching Simulator")
st.subheader("- Created by AISHIK DASGUPTA")
st.subheader("Evaluate your resume against job descriptions with AI.")
st.markdown("Upload your resume as a PDF and enter the job description below to get a keyword match score. 🎯")

# Layout with columns for resume and job description input
col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader("📄 Upload your resume", type="pdf")

with col2:
    job_description = st.text_area("💼 Paste the job description")

# Button to trigger the analysis
if st.button("Analyze"):
    if resume and job_description:
        with st.spinner("🔍 Extracting and matching keywords..."):
            # Progress bar to simulate processing
            progress_bar = st.progress(0)
            
            for i in range(100):
                time.sleep(0.01)  # Simulate processing time
                progress_bar.progress(i + 1)

            # Extract text and keywords
            resume_text = extract_text_from_pdf(resume)
            resume_keywords = extract_keywords(resume_text)
            job_keywords = extract_keywords(job_description)

            # Calculate keyword match score
            score = match_keywords(resume_keywords, job_keywords)

        # Display the match score with color-coded feedback
        if score < 50:
            st.markdown(f"❌ **Keyword Match Score: <span style='color:red'>{score:.2f}%</span>**", unsafe_allow_html=True)
        elif 50 <= score < 75:
            st.markdown(f"⚠️ **Keyword Match Score: <span style='color:yellow'>{score:.2f}%</span>**", unsafe_allow_html=True)
        else:
            st.markdown(f"✅ **Keyword Match Score: <span style='color:green'>{score:.2f}%</span>**", unsafe_allow_html=True)

        # Display extracted keywords
        st.markdown("### 📝 Extracted Keywords from Resume:")
        st.write(", ".join(resume_keywords[:20]))  # Display first 20 keywords

        st.markdown("### 💼 Extracted Keywords from Job Description:")
        st.write(", ".join(job_keywords[:20]))  # Display first 20 keywords

    else:
        st.error("⚠️ Please upload a resume and enter a job description.")

# Sidebar for settings
st.sidebar.title("📊 ATS Simulator Settings")
st.sidebar.markdown("Use the options below to customize the ATS simulator.")
matching_algorithm = st.sidebar.selectbox("Choose matching algorithm", ["Basic Match", "Weighted Match", "Synonym Match"])

# to run the first load into the virtual environment that has been  setup using the bash command:
# source /home/malfoy2003/Desktop/projects/ATS_Simulator/venv/bin/activate (for my device)
# then run the WebApp using the bash command: streamlit run /home/malfoy2003/Desktop/projects/ATS_Simulator/src/app.py (again for my device specifically)

