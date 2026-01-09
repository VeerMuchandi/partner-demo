
"""Agent for vetting and validating the case data."""

from google.adk.agents import LlmAgent
from dmv_case_triage_agent.tools import judicial_system, mvs_database, ndr_api

validation_agent = LlmAgent(
    name="CaseValidationAgent",
    description="Verifies the case against internal and external systems and gathers all necessary records.",
    tools=[
        judicial_system.verify_case,
        mvs_database.get_driver_history,
        ndr_api.check_national_register,
    ],
    instruction="""You are a data validation and retrieval specialist.

Your task is to use the provided tools to validate the case and gather all necessary records. Follow these steps precisely:

1.  **Get Inputs from State**: The initial user request contains the `driver_id` and `case_number`. The `classification_result` from the previous agent is also in the state.

2.  **Verify Court Case**: Use the `verify_case` tool with the `case_number`.

3.  **Get Driver History**: Use the `get_driver_history` tool with the `driver_id`.

4.  **Check National Register (Conditional)**: Look at the `classification_result` in the session state. If `requires_ndr_check` is True, you MUST use the `check_national_register` tool with the `driver_id`.

5.  **Handle Results**:
    *   **If any tool call returns a status of 'error'**, you MUST stop immediately. Your final output should be ONLY the error message from the tool.
    *   **If all tool calls are successful**, provide a brief, one-sentence summary of your findings. For example: "Successfully validated the case and retrieved the driver's history."
""",
    output_key="validation_summary",
)
