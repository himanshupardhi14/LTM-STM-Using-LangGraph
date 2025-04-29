# LangGraph Memory Chatbot with Gemini

This project implements a conversational AI chatbot using LangChain, LangGraph, FAISS, and Google's Gemini model. It simulates human-like conversation with both short-term and long-term memory, allowing it to recall context and past user interactions.

---

## 🚀 Features

- 🤖 Conversational AI using **Gemini (Google Generative AI)**
- 🧠 Short-Term Memory with `ConversationBufferMemory`
- 🗃️ Long-Term Memory using **FAISS Vector Store**
- 🔁 Graph-based control flow using `StateGraph` from LangGraph
- 🔍 Memory retrieval enhances prompts based on past context

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/himanshupardhi14/LTM-STM-Using-LangGraph.git
   cd LTM-STM-Using-LangGraph
   ```
2. **Install Dependencies**
   ```bash
   pip install langchain langchain-google-genai langchain-community langgraph faiss-cpu
   ```
3. **Set Your API Key**
     ```bash
   os.environ["GOOGLE_API_KEY"] = "Insert your API key here"
   ```
4. **Run the Chatbot**
   ```bash
   python main.py
   ```
---
## 📁 Project Structure
   ```bash
   LTM-STM-Using-LangGraph/
   ├── main.py        # Main Python script
   └── README.md      # Project documentation
   ```
---
## Sample Output
   ```bash
  --- Step 1---
{'chat_history': '...'}
--- Step 2---
{'chat_history': '...'}
--- Step 3---
{'chat_history': '...'}

   ```
---
## 🧾 Requirements

- Python 3.8+

### Dependencies

- [langchain](https://pypi.org/project/langchain/)
- [langchain-google-genai](https://pypi.org/project/langchain-google-genai/)
- [langchain-community](https://pypi.org/project/langchain-community/)
- [langgraph](https://pypi.org/project/langgraph/)
- [faiss-cpu](https://pypi.org/project/faiss-cpu/)

   
   
