import json
import os

import urllib3


def email_validation(email: str) -> bool:
    http = urllib3.PoolManager()
    api_key = os.environ['HUNT_API_KEY']
    response = http.request(
        'GET',
        f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"
    )

    if response.status == 200 and json.loads(response.data.decode('utf-8'))['data']['result'] == "deliverable":
        return True
    else:
        return False
