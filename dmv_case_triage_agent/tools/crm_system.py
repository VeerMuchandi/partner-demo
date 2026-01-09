
"""Mock for the Case Management/CRM System."""

import datetime
import random

def create_and_assign_case(case_details: dict, assignee_email: str) -> dict:
    """
    Autonomously creates a new case file in the CRM, logs the initial request,
    attaches all gathered data, and finalizes the assignment to the selected
    human specialist.

    Args:
        case_details: A dictionary containing all gathered information about the case.
        assignee_email: The email of the specialist to whom the case is assigned.

    Returns:
        A dictionary confirming the case creation and assignment.
    """
    if not case_details or not assignee_email:
        return {
            "status": "error",
            "message": "Case details and assignee email are required.",
        }

    # Simulate case creation
    new_case_id = f"CRM-{datetime.date.today().year}-{random.randint(10000, 99999)}"

    print(
        f"--- CRM ACTION ---"
        f"Creating new case: {new_case_id}"
        f"Assigning to: {assignee_email}"
        f"Attaching {len(case_details.keys())} data points."
        f"------------------"
    )

    return {
        "status": "success",
        "message": f"Successfully created and assigned case {new_case_id} to {assignee_email}.",
        "case_id": new_case_id,
        "assigned_to": assignee_email,
        "created_at": datetime.datetime.now().isoformat(),
    }
