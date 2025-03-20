# LangchainApp

A Python application demonstrating the use of LangChain with OpenAI's GPT models.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Project Structure

- `1_chat_models/`: Contains examples of using chat models with LangChain
  - `1_chat_models_starter.py`: Basic example of using GPT-4 with LangChain

## Usage

Run the example script:
```bash
python 1_chat_models/1_chat_models_starter.py
``` 