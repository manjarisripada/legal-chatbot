# Legal Chatbot with Gradio and GPT-2

This project is an interactive AI chatbot designed to provide general legal advice using Gradio for the user interface and the GPT-2 language model for text generation. The chatbot allows users to engage in a conversation, save chat history, and retrieve previous interactions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Conversational AI using GPT-2 for generating responses.
- Interface built with Gradio for easy interaction.
- Saves chat history to a JSON file (`chat_history.json`).
- Allows users to retrieve previous conversation history using the command `"oldconv"`.

## Installation

### Requirements

- Python 3.6 or higher
- Libraries: Gradio, Transformers

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/manjarisripada/legal-chatbot.git
   cd legal-chatbot
2. Install the required libraries:
   ```bash
   pip install gradio
   pip install transformers

## Usage

1. Run the chatbot script:
   ```bash
   python chatbot.py
2. Open the Gradio interface in your browser, where you can start chatting with the bot.
3. To stop the chat session and save the conversation, type stop or quit.

### Commands
oldconv: Displays the conversation history.

stop or quit: Ends the chat session and saves the conversation to chat_history.json
