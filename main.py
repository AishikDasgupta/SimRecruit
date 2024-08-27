import spacy
import PyPDF2

nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
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

# Function to calculate weighted score for resume sections
def calculate_weighted_score(resume_sections, job_requirements, section_weights):
    total_score = 0
    for section, weight in section_weights.items():
        resume_keywords = extract_keywords(resume_sections.get(section, ""))
        job_keywords = extract_keywords(job_requirements.get(section, ""))
        
        # Ensure we are calculating the score based on numbers
        section_score = match_keywords(resume_keywords, job_keywords)
        
        # Multiply section score by its weight
        total_score += section_score * weight

    return total_score

if __name__ == "__main__":
    # Get the resume PDF file path from the user
    resume_path = input("Enter the path to your resume PDF (e.g., ../data/sample_resume.pdf): ")

    try:
        # Extract text from the resume PDF
        resume_text = extract_text_from_pdf(resume_path)
        
        # Get the job description from the user
        job_description = input("Enter the job description: ")

        # Simulate splitting the resume and job description into sections
        resume_sections = {
            "experience": resume_text,  # Simulate extracting "experience" section
            "skills": resume_text,       # Simulate extracting "skills" section
            "education": resume_text     # Simulate extracting "education" section
        }
        
        job_requirements = {
            "experience": job_description,  # Simulate matching job experience
            "skills": job_description,      # Simulate matching job skills
            "education": job_description    # Simulate matching education requirements
        }
        
        # Weights for different sections (example: experience is more important)
        section_weights = {
            "experience": 0.5,
            "skills": 0.3,
            "education": 0.2
        }

        # Calculate the weighted score for the resume
        total_score = calculate_weighted_score(resume_sections, job_requirements, section_weights)
        print(f"Total Weighted Keyword Match Score: {total_score:.2f}%")
        
    except FileNotFoundError:
        print(f"Error: The file '{resume_path}' was not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
