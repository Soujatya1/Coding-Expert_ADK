# Multi-Agent Coding Assistant 🚀

A powerful coding assistant built with **Streamlit** and **Google ADK**, orchestrating specialized expert agents for Python, Java, and C++.

## Features

- **🧠 Orchestrator:** Intelligent routing of user queries to the appropriate language expert.
- **🐍 Python Expert:** Specialized in clean, idiomatic, and efficient Python code.
- **☕ Java Expert:** Focuses on Enterprise Java and Spring Boot development.
- **⚙️ C++ Expert:** Expert in memory management and modern C++ practices.
- **🎨 Modern UI:** A sleek, dark-themed Streamlit interface for seamless interaction.

## Prerequisites

- Python 3.9+
- A Google Gemini API Key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Soujatya1/Coding-Expert_ADK.git
   cd Coding-Expert_ADK
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your API key:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

Open your browser and navigate to the address shown in the terminal (usually `http://localhost:8501`).

## Project Structure

- `app.py`: The main Streamlit interface.
- `agents.py`: Definition of the specialized agents and the orchestrator.
- `requirements.txt`: Project dependencies.
- `.gitignore`: Files and directories to be excluded from version control.
