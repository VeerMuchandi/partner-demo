
from typing import Optional

def get_mock_visual_analysis():
    """
    Returns a dictionary of mock visual analysis data for 10 images.
    """
    return {
        "image_1.jpg": {
            "text": "Brand A",
            "backgroundColor": "blue",
            "objects": ["Adult", "Work attire", "Digital dashboards"]
        },
        "image_2.png": {
            "text": "Brand B",
            "backgroundColor": "red",
            "objects": ["Couple", "Holding hands", "Wedding cake"]
        },
        "image_3.jpg": {
            "text": "",
            "backgroundColor": "white",
            "objects": ["Child", "Toy", "Crib"]
        },
        "image_4.png": {
            "text": "Get a new credit card",
            "backgroundColor": "green",
            "objects": ["Adult", "Credit Card", "Online shopping"]
        },
        "image_5.jpg": {
            "text": "Plan for your future",
            "backgroundColor": "grey",
            "objects": ["Adult", "Age indicators", "401k documents"]
        },
        "image_6.png": {
            "text": "Brand A",
            "backgroundColor": "red", # Conflicting background
            "objects": ["Adult", "Work attire"]
        },
        "image_7.jpg": {
            "text": "Brand C", # Unknown brand
            "backgroundColor": "yellow",
            "objects": ["Adult", "House", "For Sale sign"]
        },
        "image_8.png": {
            "text": "",
            "backgroundColor": "purple",
            "objects": ["Newborn", "Stroller"]
        },
        "image_9.jpg": {
            "text": "Grow your wealth",
            "backgroundColor": "blue",
            "objects": ["Adult", "Online investment graphs", "Retirement calculators"]
        },
        "image_10.png": {
            "text": "Brand B",
            "backgroundColor": "red",
            "objects": ["Couple", "Divorce papers"] # Avoid when cue
        },
        "person_with_computer.jpg": {
            "text": "Banking from home",
            "backgroundColor": "blue",
            "objects": ["Adult", "Computer", "Mobile banking UI"]
        }
    }
