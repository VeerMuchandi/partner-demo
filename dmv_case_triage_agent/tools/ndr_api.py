
"""Mock for the National Driver Register (NDR) API."""

# Mock database of NDR records, indicating issues in other states.
_mock_ndr = {
    # This driver has a clean record nationally
    "D12345678": {"has_record": False, "summary": None},
    # This driver has a suspension in another state
    "D87654321": {
        "has_record": True,
        "summary": "License suspension on record in state of Arizona (AZ) as of 2022-09-10.",
    },
    "D11223344": {"has_record": False, "summary": None},
    # This driver has a revocation in another state
    "D55667788": {
        "has_record": True,
        "summary": "License revocation on record in state of Nevada (NV) as of 2020-07-22.",
    },
    "D99887766": {"has_record": False, "summary": None},
    "D23456789": {"has_record": False, "summary": None},
    "D34567890": {"has_record": False, "summary": None},
    # This driver has a major violation in another state
    "D45678901": {
        "has_record": True,
        "summary": "Major violation (reckless driving) on record in Oregon (OR) as of 2021-11-05.",
    },
    "D56789012": {"has_record": False, "summary": None},
    "D67890123": {"has_record": False, "summary": None},
    "D78901234": {"has_record": False, "summary": None},
    # Add a new one for testing
    "D10293847": {
        "has_record": True,
        "summary": "Multiple unresolved speeding citations in Texas (TX).",
    },
}

def check_national_register(driver_id: str) -> dict:
    """
    Performs a multi-state check to get a national picture of the driver's record.

    Args:
        driver_id: The driver's license number.

    Returns:
        A dictionary with a summary of any national records found.
    """
    if driver_id in _mock_ndr:
        record = _mock_ndr[driver_id]
        return {
            "status": "success",
            "has_national_record": record["has_record"],
            "national_summary": record["summary"],
        }
    else:
        # Default to a clean record if not explicitly mocked
        return {
            "status": "success",
            "has_national_record": False,
            "national_summary": None,
            "message": f"Driver ID '{driver_id}' not explicitly found in NDR mock; assuming clean.",
        }
