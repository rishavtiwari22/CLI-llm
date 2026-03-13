# 🤖 Python AI Chat

A simple terminal-based chatbot that lets you chat with either **ChatGPT** or **Google Gemini** directly from the command line.

---

## 📋 Features

- Chat with **OpenAI GPT-3.5 Turbo**
- Chat with **Google Gemini**
- Simple terminal interface
- Easy LLM switching at startup

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-ai-chat.git
cd python-ai-chat
```

### 2. Install Dependencies

```bash
pip install openai google-genai
```

### 3. Set API Keys

Set your API keys as environment variables:

```bash
# OpenAI
export OPENAI_API_KEY="your-openai-api-key"

# Google Gemini
export GEMINI_API_KEY="your-gemini-api-key"
```

> 💡 **Tip:** Add these lines to your `~/.zshrc` to make them persistent.

### 4. Run the App

```bash
python main.py
```

---

## 🖥️ Usage

1. When prompted, choose your LLM:
   - Press `1` for **ChatGPT**
   - Press `2` for **Gemini**
2. Start chatting!
3. Type `quit`, `exit`, or `close` to stop.

```
Chat with LLM's press 1 or 2

1. Chat-GPT
2. Gemini
Choose LLM 1/2: 1
You : Hello!
Bot:  Hi there! How can I help you today?
```

---

## 📁 Project Structure

```
python-ai-chat/
├── main.py       # Main application file
└── README.md     # Project documentation
```

---

## 🔑 API Keys

| Service | Where to get it |
|---|---|
| OpenAI | [platform.openai.com](https://platform.openai.com/api-keys) |
| Google Gemini | [aistudio.google.com](https://aistudio.google.com/app/apikey) |

> ⚠️ **Never hardcode your API keys in the source code or commit them to version control.**

---

## 📦 Dependencies

- [`openai`](https://pypi.org/project/openai/) >= 1.0.0
- [`google-genai`](https://pypi.org/project/google-genai/)
