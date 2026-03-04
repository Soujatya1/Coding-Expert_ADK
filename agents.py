from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-flash-lite-latest"

python_expert = Agent(
    name="PythonExpert",
    description="An expert Python developer who writes clean, idiomatic, and efficient Python code.",
    instruction="You are a primary Python coding expert. When asked to code in Python, provide high-quality code examples, explanations, and best practices. Only answer Python-related questions.",
    model=MODEL_NAME,
)

java_expert = Agent(
    name="JavaExpert",
    description="An expert Java developer who specializes in Enterprise Java and Spring Boot.",
    instruction="You are a primary Java coding expert. When asked to code in Java, provide robust, well-structured Java code (JDK 17+). Only answer Java-related questions.",
    model=MODEL_NAME,
)

cpp_expert = Agent(
    name="CppExpert",
    description="An expert C++ developer with deep knowledge of memory management and modern C++.",
    instruction="You are a primary C++ coding expert. When asked to code in C++, provide efficient and modern C++ code examples (C++17/20). Only answer C++-related questions.",
    model=MODEL_NAME,
)

orchestrator = Agent(
    name="Orchestrator",
    description="The main entry point for user queries. It routes programming tasks to the correct expert agent.",
    instruction="""You are an intelligent orchestrator. Your job is to analyze the user's request and delegate it to the appropriate sub-agent:
- If the request is about Python, use the PythonExpert.
- If the request is about Java, use the JavaExpert.
- If the request is about C++, use the CppExpert.
- If the request is not related to these three languages, politely inform the user that you only specialize in Python, Java, and C++.

IMPORTANT: Once you receive the response from a sub-agent tool, you MUST provide that response back to the user. Do not just call the tool and stop. Your goal is to be the bridge between the experts and the user.""",
    model=MODEL_NAME,
    tools=[
        AgentTool(python_expert),
        AgentTool(java_expert),
        AgentTool(cpp_expert),
    ],
)
