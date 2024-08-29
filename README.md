```markdown:src/code-fusion/readme.md
# CodeFusion: LLM Code Chooser

CodeFusion is a handy Python tool that allows you to compare the output of different AI models for your coding questions. The app supports models from major players like Google, Anthropic, OpenAI, and Meta, and neatly displays their answers side by side.

## Setup

1. Clone the repo and navigate to the project folder:
   ```bash
   git clone https://github.com/s-smits/code-fusion
   cd code-fusion
   ```

2. Create a virtual environment and activate it:
   - **Mac and Linux:**
     ```bash
     python3 -m venv venv_codefusion
     source venv_codefusion/bin/activate
     ```
   - **Windows:**
     ```bash
     python -m venv venv_codefusion
     venv_codefusion\Scripts\activate
     ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root of your project and add your API keys:
   ```plaintext
   GOOGLE_API_KEY=your_google_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   OPENAI_API_KEY=your_openai_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

   You only need to add the keys for the models you want to use.

## Getting Started

Run the script:
```bash
python codefusion.py
```

The app does the following:
1. Asks you to choose at least two AI models
2. Checks if you've filled in your API keys (or asks for them if they're missing)
3. Lets you ask programming questions
4. Shows the answers from the chosen models in real-time
5. Provides a summary of the differences between the answers
6. Briefly advises which model seems best for your question

Type 'quit' to exit the app.

## Features

- Parallel querying of multiple AI models
- Live display of answers
- Automatic retry for API errors
- Summary and advice via GPT-4o-mini
- Fancy console interface with colored output

## --best Option

With the `--best` option, you can select the most advanced and expensive models for your AI comparisons. When this option is enabled, the following models are used:

- **Google**: `gemini/gemini-1.5-pro-latest`
- **Anthropic**: `anthropic/claude-3-5-sonnet-20240620`
- **OpenAI**: `openai/gpt-4o`
- **Meta**: `openrouter/meta-llama/llama-3.1-405b-instruct`

Without the `--best` option, the cheaper models are used:

- **Google**: `gemini/gemini-1.5-flash`
- **Anthropic**: `anthropic/claude-3-haiku-20240307`
- **OpenAI**: `openai/gpt-4o-mini`
- **Meta**: `openrouter/meta-llama/llama-3.1-8b-instruct`

## Use Cases

1. **Developer Productivity Enhancement:**  
   CodeFusion can significantly boost developer productivity by allowing them to quickly compare outputs from multiple AI models for coding questions. This saves time in researching and cross-referencing different AI assistants, enabling developers to find the most accurate or useful code snippets faster.

2. **AI Model Evaluation for Enterprise:**  
   For companies considering integrating AI coding assistants into their development workflow, CodeFusion provides an easy way to evaluate and compare different models. This can help decision-makers choose the most suitable AI service for their specific needs and use cases, potentially saving significant costs in the long run.

3. **Educational Tool for AI and Programming:**  
   CodeFusion can serve as an excellent educational resource for students and professionals learning about AI in programming. By comparing outputs from different models side-by-side, users can gain insights into how various AI models approach coding problems, understand their strengths and weaknesses, and learn best practices from multiple sources simultaneously.

## Requirements

Check `requirements.txt` for the complete list. The main libraries are:
- litellm
- rich
- python-dotenv

## License

[MIT License](LICENSE)

## Demo
[<video src="https://github.com/user-attachments/assets/-" controls="controls" style="max-width: 730px;"></video>](https://github.com/user-attachments/assets/9aa20948-4ddf-4447-b8ab-607ad2ea10da)
```
