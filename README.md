# 🎤 LangChain Orchestrator AI App

A **production-ready, modular LLM orchestration framework** leveraging **FastAPI**, **LangChain**, and **Streamlit**.  
This system integrates multiple powerful LLMs—**Google GEMMA**, **Groq’s Gemma2**, and **Ollama’s LLaMA2**—with **speech recognition for natural voice input**, making it ideal for essay and poetry generation in AI-driven applications.

This stack is designed for **AI researchers, backend engineers, and data scientists** who want a production-grade setup that demonstrates secure API design, multi-model orchestration, and a lightweight UI aligned with enterprise standards.

------------------------------------------------------------------------

## 🚀 Features

-   🎙️ **Voice-to-Text Input** for essay/poem generation using Google
    Speech Recognition.\
-   📝 **Essay Generation** powered by **Groq's Gemma-2-9b-it** model.\
-   🎵 **Poem Generation** powered by **LLaMA2 via Ollama**.\
-   ⚡ **FastAPI + LangServe backend** to serve AI models.\
-   🌐 **Streamlit frontend** for easy interaction.

------------------------------------------------------------------------

## 🛠️ Installation

1.  Clone the repository:

    ``` bash
    git clone https://github.com/your-username/langchain-orchestrator-ai-app.git
    cd langchain-orchestrator-ai-app
    ```

2.  Create and activate virtual environment:

    ``` bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate    # Windows
    ```

3.  Install dependencies:

    ``` bash
    pip install -r requirements.txt
    ```

4.  Set up environment variables in `.env` file:

    ``` env
    LANGCHAIN_API_KEY=your_langchain_api_key
    GROQ_API_KEY=your_groq_api_key
    GOOGLE_API_KEY=your_google_api_key
    ```

------------------------------------------------------------------------

## ▶️ Running the App

### 1. Start FastAPI backend:

``` bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Start Streamlit frontend:

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 📂 Project Structure

    ├── app.py              # Streamlit frontend (UI with text + voice input)
    ├── main.py             # FastAPI backend with LangServe routes
    ├── requirements.txt    # Python dependencies
    ├── .env                # API Keys and environment variables
    └── README.md           # Project documentation

------------------------------------------------------------------------

## 🎤 Example Usage

### Essay Generation

-   Enter a topic manually OR speak into the mic → Generates a
    **100-word essay**.

### Poem Generation

-   Enter a topic manually OR speak into the mic → Generates a
    **100-word poem**.

------------------------------------------------------------------------

## 🔧 Tech Stack

-   [LangChain](https://www.langchain.com/)
-   [Ollama](https://ollama.ai/)
-   [Groq](https://groq.com/)
-   [Google Generative AI](https://ai.google/)
-   [FastAPI](https://fastapi.tiangolo.com/)
-   [Streamlit](https://streamlit.io/)
-   [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

------------------------------------------------------------------------

## 📝 License

This project is licensed under the MIT License.

------------------------------------------------------------------------

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first
to discuss what you would like to change.

------------------------------------------------------------------------


