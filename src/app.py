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

# Load custom CSS
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load custom HTML
def load_html(html_file):
    with open(html_file, 'r') as f:
        html_content = f.read()
    st.markdown(html_content, unsafe_allow_html=True)

# Load the CSS and HTML files
load_css("/home/malfoy2003/Desktop/projects/ATS_Simulator/src/style.css")
load_html("/home/malfoy2003/Desktop/projects/ATS_Simulator/src/index.html")

# Streamlit app content
st.markdown("## Upload Your Resume and Job Description")

col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader("📄 Upload your resume", type="pdf", key="resume_upload")

with col2:
    job_description = st.text_area("💼 Paste the job description", key="job_description")

# HTML button
analyze_button_html = """
<div style='text-align: center;'>
    <button type="button" class="button" id="analyze-button">Analyze</button>
</div>
"""

# Inject HTML button into Streamlit app
st.markdown(analyze_button_html, unsafe_allow_html=True)

# JavaScript to trigger Streamlit's rerun when the button is clicked
st.markdown("""
    <script>
    document.getElementById("analyze-button").addEventListener("click", function() {
        window.parent.document.querySelector("button").click();
    });
    </script>
    """, unsafe_allow_html=True)

# Button interaction handling (detecting Streamlit's show score button click)
if st.button("show score", key="analyze_button"):
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
            st.markdown(f"<div class='error'>❌ Keyword Match Score: <span>{score:.2f}%</span></div>", unsafe_allow_html=True)
        elif 50 <= score < 75:
            st.markdown(f"<div class='warning'>⚠️ Keyword Match Score: <span>{score:.2f}%</span></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result'>✅ Keyword Match Score: <span>{score:.2f}%</span></div>", unsafe_allow_html=True)

        # Display extracted keywords
        st.markdown("### 📝 Extracted Keywords from Resume:")
        st.write(", ".join(resume_keywords[:20]))  # Display first 20 keywords

        st.markdown("### 💼 Extracted Keywords from Job Description:")
        st.write(", ".join(job_keywords[:20]))  # Display first 20 keywords

    else:
        st.markdown("<div class='error'>⚠️ Please upload a resume and enter a job description.</div>", unsafe_allow_html=True)
