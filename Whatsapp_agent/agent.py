from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters
from google.adk.models.lite_llm import LiteLlm
import litellm
litellm._turn_on_debug()


root_agent = LlmAgent(
    model="gemini-2.5-flash",
    #model=LiteLlm(model="ollama_chat/gemma3:12b-it-qat"),
    name='contextual_web_navigator_agent',
    instruction=(
        "You are an expert at navigating the web by leveraging contextual clues and information on web pages to achieve the end objective. "
        "You excel at interpreting ambiguous instructions, deducing next steps, and adapting your approach to reach the user's goal efficiently. "
        "Use all available browser tools to gather information, make decisions, and execute actions that move you closer to the desired outcome. "
        "If you encounter uncertainty, use contextual hints from the page or search for additional information as needed."
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
            # tool_filter=['browser_navigate', 'browser_screenshot', 'browser_fill', 'browser_click']
        )
    ],
)