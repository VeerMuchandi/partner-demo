
"""Main agent file defining the root agent and orchestrator."""

from google.adk.agents import LlmAgent, SequentialAgent

# Import the specialized agents
from .classification_agent.agent import classification_agent
from .validation_agent.agent import validation_agent
from .assignment_agent.agent import assignment_agent

# 2. The Sequential Orchestrator Agent
# This agent runs the main business logic pipeline in a fixed order.
case_triage_orchestrator = SequentialAgent(
    name="CaseTriageOrchestratorAgent",
    description="""A sequential pipeline that classifies a request, validates all data, 
                 and assigns the fully-vetted case to a specialist. Use this tool 
                 once you have collected all initial inputs from the user.""",
    sub_agents=[
        classification_agent,
        validation_agent,
        assignment_agent,
    ],

)

# 1. The User-Facing Root Agent
# This is the entry point agent that interacts with the user.
root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="DMVTriageAssistantAgent",
    description="A helpful assistant for DMV staff to triage and route complex cases.",
    sub_agents=[
        case_triage_orchestrator, # The orchestrator is a sub-agent (tool) for the root
    ],
    instruction="""You are a helpful assistant for DMV staff.

Your primary function is to triage and route complex cases from external government agencies.

**Your workflow is as follows:**

1.  **Greet the user** and introduce yourself.
2.  **Collect Inputs**: You MUST collect the following three pieces of information from the user:
    *   The driver's ID (e.g., D12345678).
    *   The court case number (e.g., CA-2024-1038A).
    *   The unstructured text of the official request (e.g., "Request for full lifetime driving history for court proceedings.").
    Keep asking until you have all three.

3.  **Delegate to the Orchestrator**: Once you have collected all three inputs, you MUST call the `CaseTriageOrchestratorAgent` tool to start the automated triage and assignment process. Do not try to answer questions or perform the triage yourself.

4.  **Confirm and Loop**: After the `CaseTriageOrchestratorAgent` finishes, check the session state for `assignment_confirmation`. If it exists, relay its value to the user. Then, ask the user if they would like to triage another case. If they say yes, start the process over from step 2. If they say no, end the conversation politely.
"""
)
