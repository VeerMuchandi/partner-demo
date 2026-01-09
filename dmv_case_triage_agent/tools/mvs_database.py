
"""Mock for the Motor Vehicle/Driver Licensing (MVS/DL) Database."""

# Mock database of driver records
_mock_drivers = {
    "D12345678": {
        "full_name": "John A. Smith",
        "license_status": "valid",
        "class": "C",
        "violations": [{"date": "2023-05-20", "code": "VC22350", "description": "Speeding"}],
        "points": 1,
        "vehicles": [{"vin": "VIN123", "make": "Honda", "model": "Civic"}],
    },
    "D87654321": {
        "full_name": "Jane M. Doe",
        "license_status": "suspended",
        "class": "C",
        "violations": [
            {"date": "2022-11-15", "code": "VC23152", "description": "DUI"},
            {"date": "2023-08-01", "code": "VC12500", "description": "Driving without a license"},
        ],
        "points": 4,
        "vehicles": [],
    },
    "D11223344": {
        "full_name": "Robert B. Johnson",
        "license_status": "valid",
        "class": "A",
        "endorsements": ["H"], # Hazmat
        "violations": [],
        "points": 0,
        "vehicles": [{"vin": "VIN456", "make": "Peterbilt", "model": "379"}],
    },
    "D55667788": {
        "full_name": "Emily K. Williams",
        "license_status": "revoked",
        "class": "C",
        "violations": [{"date": "2021-01-10", "code": "VC23103", "description": "Reckless driving"}],
        "points": 8,
        "vehicles": [{"vin": "VIN789", "make": "Toyota", "model": "Camry"}],
    },
    "D99887766": {
        "full_name": "Michael T. Brown",
        "license_status": "valid",
        "class": "M1",
        "violations": [],
        "points": 0,
        "vehicles": [{"vin": "VIN101", "make": "Harley-Davidson", "model": "Sportster"}],
    },
    "D23456789": {
        "full_name": "Jessica L. Jones",
        "license_status": "valid",
        "class": "C",
        "violations": [],
        "points": 0,
        "vehicles": [],
    },
    "D34567890": {
        "full_name": "David G. Garcia",
        "license_status": "expired",
        "class": "C",
        "violations": [{"date": "2020-03-12", "code": "VC4000", "description": "Expired registration"}],
        "points": 1,
        "vehicles": [{"vin": "VIN112", "make": "Ford", "model": "F-150"}],
    },
    "D45678901": {
        "full_name": "Sarah P. Miller",
        "license_status": "valid",
        "class": "B",
        "endorsements": ["P", "S"], # Passenger, School Bus
        "violations": [],
        "points": 0,
        "vehicles": [],
    },
    "D56789012": {
        "full_name": "Christopher H. Davis",
        "license_status": "valid",
        "class": "C",
        "violations": [{"date": "2023-11-30", "code": "VC21453", "description": "Red light violation"}],
        "points": 1,
        "vehicles": [{"vin": "VIN113", "make": "Chevrolet", "model": "Malibu"}],
    },
    "D67890123": {
        "full_name": "Amanda R. Rodriguez",
        "license_status": "valid",
        "class": "C",
        "violations": [],
        "points": 0,
        "vehicles": [{"vin": "VIN114", "make": "Nissan", "model": "Altima"}],
    },
     "D78901234": {
        "full_name": "James F. Wilson",
        "license_status": "valid",
        "class": "A",
        "violations": [{"date": "2022-09-18", "code": "VC22406", "description": "Speeding (Truck)"}],
        "points": 2,
        "vehicles": [{"vin": "VIN115", "make": "Kenworth", "model": "W900"}],
    },
}

def get_driver_history(driver_id: str) -> dict:
    """
    Retrieves the complete, official record of a driver's license status,
    vehicles, points, and violation history from the MVS database.

    Args:
        driver_id: The driver's license number.

    Returns:
        A dictionary containing the driver's full record, or an error if not found.
    """
    if driver_id in _mock_drivers:
        return {"status": "success", "driver_record": _mock_drivers[driver_id]}
    else:
        return {
            "status": "error",
            "message": f"Driver ID '{driver_id}' not found in MVS database.",
        }
