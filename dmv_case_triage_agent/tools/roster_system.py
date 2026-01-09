
"""Mock for the Internal Roster and Workload System."""

# Mock database of DMV specialists, their skills, and current workload
_mock_roster = [
    {
        "email": "alice.c@dmv.gov",
        "name": "Alice Chen",
        "skills": ["CDL_audit", "vehicle_title_law", "fraud_investigation", "Driving_History_Audit"],
        "workload": 3, # Number of active complex cases
    },
    {
        "email": "bob.d@dmv.gov",
        "name": "Bob Davis",
        "skills": ["lifetime_history_audit", "FOIA_compliance", "interstate_records", "Legal_Compliance"],
        "workload": 5,
    },
    {
        "email": "charlie.e@dmv.gov",
        "name": "Charlie Edwards",
        "skills": ["CDL_audit", "hazmat_endorsement", "federal_motor_carrier_regs", "lifetime_history_audit"],
        "workload": 2,
    },
    {
        "email": "diana.f@dmv.gov",
        "name": "Diana Foster",
        "skills": ["vehicle_forfeiture", "asset_seizure_law"],
        "workload": 4,
    },
    {
        "email": "edward.g@dmv.gov",
        "name": "Edward Garcia",
        "skills": ["lifetime_history_audit", "FOIA_compliance", "data_privacy", "Driving_History_Audit", "Legal_Compliance", "interstate_records"],
        "workload": 1, # Low workload, ideal for assignment
    },
    {
        "email": "fiona.h@dmv.gov",
        "name": "Fiona Harris",
        "skills": ["CDL_revocation", "CDL_audit"],
        "workload": 6, # High workload
    },
    {
        "email": "george.i@dmv.gov",
        "name": "George Ito",
        "skills": ["vehicle_forfeiture", "fraud_investigation"],
        "workload": 1,
    },
    {
        "email": "hannah.j@dmv.gov",
        "name": "Hannah Jones",
        "skills": ["interstate_records", "NDR_specialist"],
        "workload": 4,
    },
    {
        "email": "ivan.k@dmv.gov",
        "name": "Ivan Kuznetsov",
        "skills": ["lifetime_history_audit", "data_privacy"],
        "workload": 2,
    },
    {
        "email": "judy.l@dmv.gov",
        "name": "Judy Lee",
        "skills": ["CDL_audit", "vehicle_title_law"],
        "workload": 5,
    },
]

def find_specialists(required_skills: list[str]) -> dict:
    """
    Finds certified specialists from the internal roster who match a set of
    required skills and checks their current workload. It returns a list of
    candidates, prioritizing those with more matching skills.

    Args:
        required_skills: A list of skills needed to handle the case.

    Returns:
        A dictionary containing a list of qualified specialists, including the
        number of skills they matched.
    """
    if not required_skills:
        return {"status": "error", "message": "Required skills cannot be empty."}

    candidate_specialists = []
    for specialist in _mock_roster:
        matched_skills = [skill for skill in required_skills if skill in specialist["skills"]]
        if matched_skills:
            candidate_specialists.append(
                {
                    "name": specialist["name"],
                    "email": specialist["email"],
                    "workload": specialist["workload"],
                    "matched_skills_count": len(matched_skills),
                    "matched_skills_list": matched_skills,
                }
            )

    if not candidate_specialists:
        return {
            "status": "error",
            "message": f"No specialists found with any of the required skills: {required_skills}",
        }

    # Sort candidates by the number of matched skills (descending), then by workload (ascending)
    sorted_candidates = sorted(
        candidate_specialists, key=lambda x: (-x["matched_skills_count"], x["workload"])
    )

    return {"status": "success", "specialists": sorted_candidates}
