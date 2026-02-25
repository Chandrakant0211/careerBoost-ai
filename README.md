# 🚀 CareerBoost AI – Resume Analyzer

CareerBoost AI is a Machine Learning based Resume Analyzer built using Python and Streamlit.  
It compares a resume with a job description and provides:

- 📊 Match Score
- 📈 ATS Score
- ✅ Detected Skills
- ❌ Missing Skills
- 💡 Improvement Suggestions

---

## 🔥 Features

- Upload Resume (PDF)
- Extract text from PDF
- Compare with Job Description
- TF-IDF based similarity score
- Skill gap detection
- Clean Streamlit dashboard

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn (TF-IDF)
- RapidFuzz
- PyMuPDF
- spaCy



## 📂 Project Structure
ResumeAnaliseML/
│
├── careerBoostAi.py # Main app
├── utils.py # Analysis logic
├── db.py # Database (optional)
├── requirements.txt
└── README.md

---

## ⚙️ Run Locally

### 1️⃣ Clone Repository

### 2️⃣ Create Virtual Environment


## Activate (Windows):
**..venv\Scripts\Activate.ps1**

 
### 3️⃣ Install Dependencies
**pip install -r requirements.txt**


### 4️⃣ Run App
**streamlit run careerboostai.py**


---

## ☁️ Deploy on Streamlit Cloud

1. Push project to GitHub
2. Go to https://share.streamlit.io
3. Select repository
4. Choose `careerBoostAi.py`
5. Deploy 🚀

---

## 📌 How It Works

1. Extract resume text
2. Clean text using NLP
3. Convert text to vectors (TF-IDF)
4. Calculate similarity score
5. Detect skill gaps
6. Show improvement suggestions

---

## 🎯 Future Improvements

- Deep Learning Model
- AI-based Resume Rewriting
- User Feedback Learning
- Database Storage
- Authentication System

---

## 👨‍💻 Author

Developed by **Chandrakant kumar**

---

⭐ If you like this project, give it a star!
