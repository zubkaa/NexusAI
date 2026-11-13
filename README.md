# NexusAI 🤖

An AI-powered Discord assistant built with Python.

NexusAI is a personal project designed to bring AI-powered conversations directly into Discord. It uses an AI language model through an API to generate helpful, conversational responses.

## 🚀 Features

- **AI Conversations:** Ask NexusAI questions using Discord.
- **Mention Detection:** Mention the bot to receive an AI-generated response.
- **Reply Detection:** Reply directly to NexusAI's messages to continue a conversation.
- **Discord Commands:** Includes a `!ping` command to check whether the bot is online and a `!ask` command for direct AI questions.
- **Asynchronous Processing:** Uses Python's asynchronous programming features to handle requests efficiently.

## 🛠️ Technologies Used

- Python
- discord.py
- OpenAI Python SDK
- Groq API
- python-dotenv
- Git & GitHub

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/detective-cc/NexusAI.git
cd NexusAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project directory:

```env
discord_token=YOUR_DISCORD_BOT_TOKEN
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Replace the placeholders with your own credentials.

**Never share or upload your `.env` file.**

### 6. Run NexusAI

```bash
python bot.py
```

## 💬 Commands

| Command | Description |
|---|---|
| `!ping` | Checks whether NexusAI is online. |
| `!ask <question>` | Sends a question to the AI. |
| `@NexusAI <message>` | Starts an AI conversation. |

## 🗺️ Development Roadmap

- [x] Discord bot integration
- [x] AI API integration
- [x] Mention-based AI responses
- [x] Reply detection
- [ ] Persistent conversation memory
- [ ] Database integration
- [ ] Advanced AI automation features

## 👨‍💻 About the Project

NexusAI is an ongoing learning and development project focused on Python, AI integration, APIs, Discord bot development, and automation.

Built as part of my journey into software development and cybersecurity.

---

**Project Status:** Active Development