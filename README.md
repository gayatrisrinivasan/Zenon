# Zenon - A Friendly Therapist Telegram Bot

Zenon is an AI-powered chatbot created to offer therapeutic support for individuals in need. Accessible anytime through Telegram, Zenon provides a safe, non-judgmental space for users to express their feelings, receive insights, and enhance self-awareness through natural language conversations.

## Table of Contents

- [Abstract](#abstract)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)

---

## Abstract

Zenon aims to guide individuals toward well-being and self-discovery by creating a secure space for meaningful conversations. It is designed to help users enhance self-awareness and self-reflection while providing emotional support in a convenient, cost-effective way.

## Features

- **24/7 Availability**: Zenon offers round-the-clock support, providing relief and guidance whenever needed.
- **Sentiment Analysis**: Analyzes the user's emotional tone to provide contextually relevant responses.
- **Insight Generation**: Utilizes machine learning algorithms to identify patterns in user thoughts and feelings, generating personalized insights and recommendations.
- **Telegram Integration**: Ensures accessibility, privacy, and anonymity through a familiar messaging platform.

## Technologies Used

- **Telegram Bot API**: For Telegram-based user interactions.
- **Python**: Primary programming language.
- **OpenAI API**: For NLP and response generation.

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/zenon-therapist-bot.git
   cd zenon-therapist-bot
2. **Install required packages:**
    ```bash
    pip install -r requirements.txt

3. **Set up your environment variables:**
Add your Telegram Bot Token and OpenAI API Key in the environment or in a .env file as follows:

    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    OPENAI_API_KEY=your_openai_api_key

4. **Run the bot:**
    ```bash
    python main.py

## Usage

1. Open Telegram and search for your bot using its username.
2. Start a conversation with Zenon to receive emotional support and insights.
3. Type messages freely; Zenon will respond based on sentiment and context, providing support and recommendations.

## Architecture

Zenon is structured as follows:

- **Natural Language Processing:** Enables Zenon to understand and interpret user messages.
- **Sentiment Analysis:** Determines emotional tone to adjust responses.
- **Insight Generation:** Uses machine learning algorithms to analyze user input and provide personalized feedback.

---
