
"""Agent for classifying the nature of the incoming request."""

from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field
from typing import List


class ClassificationResult(BaseModel):
    """A structured representation of the case classification."""

    case_type: str = Field(
        description="A specific category for the request, e.g., 'Lifetime_History_Audit', 'CDL_Revocation', 'Vehicle_Forfeiture', 'Interstate_Record_Check'."
    )
    required_skills: List[str] = Field(
        description="A list of specific skills required to handle this case, e.g., ['CDL_audit', 'vehicle_title_law']."
    )
    compliance_level: str = Field(
        description="The required security and compliance level, e.g., 'Standard', 'FOIA_Exempt_C2', 'Federal_Mandate'."
    )
    requires_ndr_check: bool = Field(
        description="Set to True if the request implies or requires a multi-state or national driver history check."
    )


classification_agent = LlmAgent(
    name="RequestClassificationAgent",
    description="Analyzes an unstructured request to determine its precise legal nature, complexity, and required skills.",
    instruction="""Your sole job is to analyze the user's request and classify it.

Read the user's input, which includes the initial request details.

Determine the specific type of case (e.g., 'Lifetime_History_Audit', 'CDL_Revocation', 'Vehicle_Forfeiture', 'Interstate_Record_Check').

Identify the skills an expert would need to handle it. Prioritize skills like 'Driving_History_Audit', 'Legal_Compliance', 'lifetime_history_audit', 'CDL_audit', 'vehicle_title_law', 'fraud_investigation', 'FOIA_compliance', 'interstate_records', 'hazmat_endorsement', 'federal_motor_carrier_regs', 'vehicle_forfeiture', 'asset_seizure_law', 'data_privacy', 'NDR_specialist'.

Determine the compliance level (e.g., 'Standard', 'FOIA_Exempt_C2', 'Federal_Mandate').

Decide whether a National Driver Register (NDR) check is necessary based on the request's complexity or wording (e.g., mentions of other states or national records).

Output a single, raw JSON object that validates against the 'ClassificationResult' schema. Do not add any other text, explanation, or conversational filler.
""",
    output_schema=ClassificationResult,
    output_key="classification_result",  # Save the JSON output to session state
)
