# WhatsApp Reader Agent

A contextual web navigation agent built with Google's Agent Development Kit (ADK) that can navigate the web using contextual clues to achieve end objectives. The agent supports both cloud-based (Gemini) and local LLM models.

## Features

- **Contextual Web Navigation**: Expert at finding and following contextual clues on web pages
- **Flexible LLM Support**: Works with both cloud-based (Gemini) and local models (Ollama)
- **Browser Automation**: Uses Playwright MCP tools for web interaction
- **Adaptive Approach**: Interprets ambiguous instructions and adapts strategies to reach goals

## Prerequisites

- Python 3.11 or higher
- Node.js and npm (for Playwright MCP tools)
- [Ollama](https://ollama.com/) (optional, for local LLM usage)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "Whatsapp Reader"
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install google-adk litellm python-dotenv
```

### 4. Install Node.js Dependencies

```bash
# Install Playwright MCP tools globally
npm install -g @playwright/mcp
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# For Google Gemini (cloud-based)
GOOGLE_API_KEY="your_google_api_key_here"

# For local LLM (optional)
OLLAMA_API_BASE="http://localhost:11434"
```

## Usage

### Using Cloud-Based Gemini Model (Default)

The agent is configured by default to use Google's Gemini 2.5 Flash model:

```python
# In agent.py - already configured
model="gemini-2.5-flash"
```

### Using Local LLM with Ollama

1. **Install and Start Ollama**:
   ```bash
   # Install Ollama (follow instructions at https://ollama.com/)
   # Pull a model (example with Gemma 3)
   ollama pull gemma3:12b
   # Start Ollama server
   ollama serve
   ```

2. **Modify the Agent Configuration**:
   ```python
   # In agent.py, uncomment the local model line and comment out the Gemini line:
   # model="gemini-2.5-flash",
   model=LiteLlm(model="ollama_chat/gemma3:12b"),
   ```

3. **Set Environment Variable**:
   ```bash
   export OLLAMA_API_BASE="http://localhost:11434"
   ```

### Running the Agent

#### Option 1: Using ADK Web Interface
```bash
adk web
```

#### Option 2: Using ADK CLI
```bash
adk run Whatsapp_agent.agent
```

#### Option 3: Programmatic Usage
```python
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from Whatsapp_agent.agent import root_agent

# Set up session and runner
session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="whatsapp_reader",
    user_id="user_1",
    session_id="session_1"
)

runner = Runner(
    agent=root_agent,
    app_name="whatsapp_reader",
    session_service=session_service
)

# Run the agent
content = types.Content(role='user', parts=[types.Part(text="Navigate to example.com and find the contact information")])
events = runner.run(user_id="user_1", session_id="session_1", new_message=content)

for event in events:
    if event.is_final_response():
        print("Agent Response:", event.content.parts[0].text)
```

## Configuration

### Available Models

#### Cloud-Based Models
- `gemini-2.5-flash` (default) - Fast and efficient
- `gemini-2.5-pro` - More powerful for complex tasks
- `gemini-2.0-flash` - Stable version

#### Local Models (via Ollama)
- `ollama_chat/gemma3:12b` - Google's open-source model
- `ollama_chat/llama3:8b` - Meta's Llama 3
- `ollama_chat/mistral:7b` - Mistral AI's model
- `ollama_chat/codellama:7b` - Specialized for coding tasks

### Tool Configuration

The agent uses Playwright MCP tools for web automation:
- `browser_navigate` - Navigate to web pages
- `browser_screenshot` - Take screenshots
- `browser_fill` - Fill forms
- `browser_click` - Click elements

You can filter specific tools by uncommenting the `tool_filter` line in the agent configuration.

## Troubleshooting

### Common Issues

1. **Ollama Connection Issues**:
   - Ensure Ollama is running: `ollama serve`
   - Check if the model is downloaded: `ollama list`
   - Verify API endpoint: `curl http://localhost:11434/api/tags`

2. **Playwright MCP Issues**:
   - Ensure Node.js and npm are installed
   - Reinstall Playwright MCP: `npm install -g @playwright/mcp@latest`

3. **Python UTF-8 Issues (Windows)**:
   ```powershell
   $env:PYTHONUTF8 = "1"
   ```

4. **Tool Calling Issues with Ollama**:
   - Use `ollama_chat/` provider instead of `ollama/`
   - Ensure you're using the latest version of `litellm`

### Debug Mode

The agent includes debug logging for LiteLLM. To see detailed request/response logs, the debug mode is already enabled in the code:

```python
import litellm
litellm._turn_on_debug()
```

## Project Structure

```
Whatsapp Reader/
├── Whatsapp_agent/
│   ├── __init__.py
│   └── agent.py          # Main agent configuration
├── README.md             # This file
└── .env                  # Environment variables (create this)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with both cloud and local models
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions:
- Check the [Google ADK documentation](https://google.github.io/adk-docs/)
- Review [LiteLLM documentation](https://docs.litellm.ai/)
- Check [Ollama documentation](https://ollama.com/docs) 