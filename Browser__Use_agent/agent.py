from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters
from google.adk.models.lite_llm import LiteLlm
#import litellm
#litellm._turn_on_debug()
#########MODEL SELECTION#########
#MODEL = "llama3-groq-tool-use:8b-q8_0"  # Change this to the desired model name
#MODEL = "aliafshar/gemma3-it-qat-tools"
#MODEL = "qwen3:14b-q4_K_M"
MODEL = "granite3.3"

root_agent = LlmAgent(
    #model = "gemini-2.0-flash-lite",
    #model="gemini-2.5-flash",
    model=LiteLlm(model=f"ollama_chat/{MODEL}"),
    name='contextual_web_navigator_agent',
    instruction=(
        "You are an expert at navigating the web by leveraging contextual clues and information on web pages to achieve the end objective. "
        "You excel at interpreting ambiguous instructions, deducing next steps, and adapting your approach to reach the user's goal efficiently. "
        "Use all available browser tools to gather information, make decisions, and execute actions that move you closer to the desired outcome. "
        "If you encounter uncertainty, use contextual hints from the page or search for additional information as needed."
        "if you require to read the content of the page, use the 'browser_snapshot' tool after navigating to the page. "
    ),
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                args=[
                    "-y",
                    "@playwright/mcp@latest",
                ],
                ),
                timeout=30
            ),
             #tool_filter=['browser_navigate', 'browser_screenshot', 'browser_fill', 'browser_click','browser_press_key','browser_take_screenshot','browser_hover','browser_select_option','browser_wait_for']
        )
    ],
)