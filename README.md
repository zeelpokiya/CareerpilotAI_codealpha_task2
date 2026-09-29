# CareerPilot AI – Intelligent Career & Skill Roadmap Assistant

CareerPilot AI is an AI-powered career guidance and skill roadmap system designed to help students understand their career readiness, identify skill gaps, explore suitable career paths, and generate personalized career development plans.

The system uses an agent-based workflow to analyze a student's profile and generate a structured career plan containing career recommendations, skill gaps, learning roadmaps, projects, and interview preparation guidance.

## 📌 Project Information

* **Project Code:** CareerPilot AI – Intelligent Career & Skill Roadmap Assistant
* **Project Title:** CareerPilot AI – Intelligent Career & Skill Roadmap Assistant
* **Project Type:** AI Agent / Intelligent Web Application
* **Domain:** Artificial Intelligence & Career Guidance
* **Interface:** Web Application
* **AI Model:** Local/Open-Source LLM
* **Workflow:** Multi-Agent AI Workflow

## 🎯 Objective

The main objective of CareerPilot AI is to provide students with an intelligent and personalized career planning assistant.

The system aims to:

* Analyze a student's profile.
* Identify suitable career paths.
* Detect skill gaps.
* Recommend skills to learn.
* Generate a structured learning roadmap.
* Recommend suitable AI/software projects.
* Provide interview preparation guidance.
* Generate a final personalized career plan.

## ✨ Key Features

* Student profile analysis
* Career matching
* Career readiness score
* Skill gap analysis
* Skill recommendations
* Personalized learning roadmap
* AI project recommendations
* Interview preparation
* AI Career Coach
* Career report generation
* Multi-agent workflow
* Validation of generated career plans
* Interactive dashboard
* Modern glassmorphism-based UI

## 🤖 AI Agent Workflow

CareerPilot AI uses multiple specialized agents for different stages of career planning.

```text
Student Profile
       ↓
Career Matching Tool
       ↓
Career Agent
       ↓
Skill Gap Agent
       ↓
Roadmap Agent
       ↓
Project Agent
       ↓
Interview Agent
       ↓
Validation Agent
       ↓
Final Career Plan
```

Each agent performs a specific task instead of generating the complete career plan in a single step.

## 🧠 Main AI Components

### 1. Career Agent

Analyzes the student's profile and identifies potentially suitable career paths.

### 2. Skill Gap Agent

Compares the student's existing skills with the skills required for the selected career path.

### 3. Roadmap Agent

Creates a structured learning roadmap based on the identified skill gaps.

### 4. Project Agent

Recommends practical projects that can help the student improve skills and build a portfolio.

### 5. Interview Agent

Provides interview preparation topics, questions, and guidance related to the selected career.

### 6. Validation Agent

Checks the generated career plan for:

* Required sections
* Relevance
* Completeness
* Consistency
* Practicality

The validation stage is a quality-control mechanism and does not guarantee absolute correctness.

## 🏗️ System Architecture

```text
User
 ↓
Student Profile
 ↓
Career Analysis
 ↓
AI Agent Workflow
 ↓
┌──────────────────────┐
│ Career Agent         │
│ Skill Gap Agent      │
│ Roadmap Agent        │
│ Project Agent        │
│ Interview Agent      │
└──────────────────────┘
 ↓
Validation Agent
 ↓
Final Career Plan
 ↓
Dashboard / Report
```

## 📊 Career Analysis

The Career Analysis module processes the student's information and provides:

* Career readiness score
* Career recommendations
* Skill analysis
* Skill gaps
* Learning priorities
* Development suggestions

After the analysis is completed, the user can access the main dashboard.

## 📈 Dashboard

The dashboard provides a centralized view of the generated career information.

It can include:

* Career readiness score
* Recommended career path
* Skill gap information
* Recommended skills
* Learning roadmap
* Project recommendations
* Interview preparation

## 💡 AI Career Coach

The AI Career Coach provides interactive career-related guidance.

Students can use it to ask questions about:

* Career paths
* Skills
* Learning
* Projects
* Interviews
* Career preparation

## 📄 Career Report

CareerPilot AI can generate a structured career report based on the student's profile and AI-generated career plan.

The report can contain:

```text
Student Profile
      ↓
Career Recommendation
      ↓
Career Readiness
      ↓
Skill Gap
      ↓
Learning Roadmap
      ↓
Project Recommendations
      ↓
Interview Preparation
      ↓
Final Career Plan
```

## 🛠️ Technologies Used

### Programming Language

* Python

### AI / LLM

* Ollama
* Llama 3.2
* Open-source Large Language Model

### Agent Workflow

* LangGraph / Graph-based agent workflow

### Web Application

* Python
* HTML/CSS
* Streamlit or Flask-based application components

### Other Components

* Report generation utilities
* Skill analysis utilities
* Roadmap generation utilities

## 📁 Project Structure

```text
504/
│
├── app.py
│
├── assets/
│   └── style.css
│
├── agent/
│   ├── graph.py
│   └── nodes.py
│
├── utils/
│   ├── roadmap.py
│   ├── report_generator.py
│   └── skill_analyzer.py
│
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd 504
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

Install the required Python packages using the project's dependency file if provided:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not included, install the required packages used by the project.

## 🧠 Ollama Setup

CareerPilot AI uses a local LLM through Ollama.

After installing Ollama, download the required model:

```bash
ollama pull llama3.2
```

Make sure the Ollama service is running before starting the application.

## ▶️ Running the Application

Run the application using:

```bash
python app.py
```

If the project is configured as a Streamlit application, use:

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal.

## 🔄 Application Workflow

```text
Start Application
       ↓
Enter Student Profile
       ↓
Career Analysis
       ↓
Calculate Career Readiness
       ↓
Identify Skill Gaps
       ↓
Generate Career Roadmap
       ↓
Recommend Projects
       ↓
Interview Preparation
       ↓
Validate Career Plan
       ↓
Display Final Career Plan
```

## 🎨 User Interface

The application provides a modern interface with:

* Career Analysis section
* Dashboard
* Skill Gap visualization
* Career readiness information
* Project recommendations
* AI Coach
* Career report
* Modern glassmorphism design

## 🔐 Responsible AI

CareerPilot AI is designed as a career guidance and educational assistant.

AI-generated recommendations should be treated as guidance rather than guaranteed career outcomes. Users should verify important information and consider their personal goals, skills, interests, and current industry requirements.

## 🚀 Future Enhancements

Possible future improvements include:

* Integration with live job-market data
* Resume analysis
* LinkedIn profile analysis
* Skill certification recommendations
* Job matching
* Real-time labor-market information
* Voice-based AI Career Coach
* Cloud deployment
* User authentication
* Database integration
* Progress tracking
* Personalized learning notifications

## 📚 Academic Purpose

This project was developed as part of the codealpha_task2  project work.

---

**CareerPilot AI – Intelligent Career & Skill Roadmap Assistant**
