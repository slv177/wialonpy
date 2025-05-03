import requests
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_WIALON_URL = "https://hst-api.wialon.com/wialon/ajax.html"

class WialonAuthError(Exception):
    """Raised when Wialon authentication fails."""
    pass

def wialon_get_session_eid(w_token: str, wialon_url: str = DEFAULT_WIALON_URL) -> Optional[str]:
    """
    Authenticate with Wialon API using a token and return the session ID (eid).

    Args:
        w_token (str): Wialon API token.
        wialon_url (str): URL to Wialon API. Defaults to production endpoint.

    Returns:
        Optional[str]: Session ID (eid) if successful, otherwise None.

    Raises:
        WialonAuthError: If the authentication fails.
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        params = {
            "svc": "token/login",
            "params": json.dumps({"token": w_token}),
        }
        response = requests.post(wialon_url, params=params)
        response.raise_for_status()

        data = response.json()
        eid = data.get("eid")

        if not eid:
            logger.warning("Wialon returned no session ID: %s", data)
            raise WialonAuthError("No session ID returned by Wialon")

        return eid

    except requests.RequestException as e:
        logger.error("Wialon request failed: %s", e)
        raise
    except json.JSONDecodeError as e:
        logger.error("Failed to parse Wialon response: %s", e)
        raise WialonAuthError("Invalid JSON response from Wialon")
