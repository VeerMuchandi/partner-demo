
"""Mock for the Internal Email/Notification Service."""

import datetime

def send_notification(email: str, subject: str, body: str) -> dict:
    """
    Sends a direct, contextual notification to a specialist to confirm a handoff.

    Args:
        email: The recipient's email address.
        subject: The subject line of the notification.
        body: The main content of the notification.

    Returns:
        A dictionary confirming that the notification was sent.
    """
    if not all([email, subject, body]):
        return {"status": "error", "message": "Email, subject, and body are required."}

    # In a real system, this would integrate with an email API like SendGrid or SMTP.
    # Here, we just print to the console to simulate the action.
    print(
        f"--- NOTIFICATION SENT ---"
        f"To: {email}"
        f"Subject: {subject}"
        f"Body: {body[:150]}..."
        f"-------------------------"
    )

    return {
        "status": "success",
        "message": f"Notification successfully sent to {email}.",
        "sent_at": datetime.datetime.now().isoformat(),
    }
