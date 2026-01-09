
"""Mock for the State Judicial System API."""

import datetime

# Mock database of court cases
_mock_cases = {
    "CA-2024-1038A": {"status": "active", "jurisdiction": "CA", "requires_history": True},
    "NY-2023-9927B": {"status": "active", "jurisdiction": "NY", "requires_history": False},
    "TX-2024-4551C": {"status": "closed", "jurisdiction": "TX", "requires_history": False},
    "FL-2022-7811D": {"status": "active", "jurisdiction": "FL", "requires_history": True},
    "IL-2024-3329E": {"status": "pending", "jurisdiction": "IL", "requires_history": False},
    "PA-2023-5432F": {"status": "active", "jurisdiction": "PA", "requires_history": True},
    "OH-2024-8876G": {"status": "dismissed", "jurisdiction": "OH", "requires_history": False},
    "GA-2021-9123H": {"status": "active", "jurisdiction": "GA", "requires_history": True},
    "NC-2024-7765I": {"status": "active", "jurisdiction": "NC", "requires_history": False},
    "MI-2023-2345J": {"status": "closed", "jurisdiction": "MI", "requires_history": False},
    "WA-2024-6789K": {"status": "active", "jurisdiction": "WA", "requires_history": True},
}

def verify_case(case_number: str) -> dict:
    """
    Verifies the authenticity and status of a court order against the
    official judicial database.

    Args:
        case_number: The unique identifier for the court case.

    Returns:
        A dictionary containing the case status and details, or an error
        if the case is not found.
    """
    if case_number in _mock_cases:
        return {
            "status": "success",
            "case_details": {
                "case_number": case_number,
                "is_valid": True,
                "case_status": _mock_cases[case_number]["status"],
                "jurisdiction": _mock_cases[case_number]["jurisdiction"],
                "requires_driver_history": _mock_cases[case_number]["requires_history"],
                "verified_at": datetime.datetime.now().isoformat(),
            },
        }
    else:
        return {
            "status": "error",
            "message": f"Case number '{case_number}' not found in judicial records.",
            "case_details": {
                "case_number": case_number,
                "is_valid": False,
            },
        }
