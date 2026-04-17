# Just Eat It

A web app that eliminates meal decision fatigue. Tell it your energy level, time available, and mood — it gives you one meal. No options. No overthinking.

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask
- AI: Groq API (LLaMA 3.3 70B)

## How to Run Locally
1. Clone the repo
2. Install dependencies: `pip install flask flask-cors groq python-dotenv`
3. Create a `.env` file with your Groq API key: `GROQ_API_KEY=your-key-here`
4. Run the server: `python app.py`
5. Open `index.html` in your browser