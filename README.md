# SimRecruit(ATS Simulator) 🌟

ATS Keyword Matching Simulator is a Python-based tool designed to analyze and match resume keywords with job descriptions, simulating how Applicant Tracking Systems (ATS) process resumes. This project allows users to optimize their resumes for specific job applications, enhancing their chances of passing through ATS filters.

## Features 🚀

- **Keyword Matching**: Analyze resume content against job descriptions using NLP techniques to calculate a match score.
- **Interactive UI**: Built with **Streamlit**, the app provides a user-friendly interface for uploading resumes and job descriptions.
- **Dynamic Feedback**: Real-time, color-coded scoring to indicate match quality (red, yellow, green).
- **Customizable UI**: Enhanced with **HTML** and **CSS** for a visually appealing experience.
- **Real-time Progress Indicators**: Shows the processing status and feedback on the keyword matching process.

## Installation 🔧

1. Clone this repository:
   ```bash
   git clone https://github.com/AishikDasgupta/ATS_Keyword_Matching_Simulator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ATS_Keyword_Matching_Simulator
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🎯

1. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```

2. Access the app at `http://localhost:8501`.

3. Upload your resume (PDF format) and paste the job description to get an instant keyword match score.

## Backend Modules 📦

- `streamlit`: For building the web app interface.
- `spacy`: Used for natural language processing and keyword extraction.
- `PyPDF2`: Handles PDF parsing and text extraction.
- `time`: Simulates real-time progress indicators.

## Frontend Modules 🌐

- **HTML**: Used for custom layout and content structure.
- **CSS**: Styles the app interface for a polished look.
- **JavaScript**: Enhances interactivity for button actions.

## Screenshots 📸

![Screenshot from 2024-08-29 22-29-05](https://github.com/user-attachments/assets/51d078c9-9542-41ec-b3f3-dd2dcd5405cb)

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📬

For any inquiries or feedback, please contact:

- **Aishik Dasgupta**
- Email: [itsdg19@gmail.com](mailto:itsdg19@gmail.com)
- GitHub: [AishikDasgupta](https://github.com/AishikDasgupta)

## Acknowledgments 🙏

- Special thanks to the contributors of the libraries used in this project.
- Thanks to the community for their support and feedback.

## Contributing 🤝

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
