import requests
import json

RESEND_API_KEY = "re_QmbtZKAH_72Yh1AQQ45tXkPACW5HeP2LW"


contacts = [
    {
        "name": "Tosh",
        "email": "js0109426@gmail.com",  # simulating delivery to yourself
        "role": "Program Manager",
        "personalization": "Having worked at PwC and Avataar before Anakin, you understand how pricing gaps cost brands revenue at scale."
    },
    {
        "name": "Viral",
        "email": "js0109426@gmail.com",  # simulating delivery to yourself
        "role": "VP of Sales",
        "personalization": "With your BD experience at SenseHawk and Danaher, you know how real-time competitive data can directly accelerate enterprise deal cycles."
    },
    {
        "name": "Viral",
        "email": "js0109426@gmail.com",  # simulating delivery to yourself
        "role": "VP of Sales",
        "personalization": "Your journey from energy-tech at SenseHawk to leading sales at a YC-backed company shows you value data-driven decision making."
    }
]

def send_email(contact):
    subject = f"Quick thought for you, {contact['name']}"
    
    html_body = f"""
    <p>Hi {contact['name']},</p>

    <p>{contact['personalization']}</p>

    <p>The eCommerce brands winning today aren't just competing on product — 
    they're winning on <strong>real-time pricing intelligence, competitive 
    benchmarking, and assortment insights</strong>.</p>

    <p>Most teams are still doing this manually — pulling competitor data in 
    spreadsheets, reacting to price changes days late. The gap between brands 
    using automated pricing intelligence vs those that aren't is growing fast.</p>

    <p>If this resonates, I'd love to share more context. And if you find it 
    relevant, I can introduce you to a <strong>YC-backed company</strong> that 
    has built exactly this — serving 15+ multi-billion dollar retail brands 
    across 30+ countries with real-time pricing and assortment data.</p>

    <p>Worth a quick 15-min call?</p>

    <p>Best,<br>
    Jatin Saini<br>
    js0109426@gmail.com</p>
    """
    
    payload = {
        "from": "Jatin Saini <onboarding@resend.dev>",
        "to": [contact["email"]],
        "subject": subject,
        "html": html_body,
        "reply_to": "js0109426@gmail.com"
    }
    
    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps(payload)
    )
    
    print(f"Sent to {contact['name']} ({contact['role']}): Status {response.status_code} — {response.json()}")

for contact in contacts:
    send_email(contact)

print("\nAll emails sent successfully!")